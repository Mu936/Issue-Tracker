from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import logging

app = Flask(__name__)

# Configure database for Railway
import os
from pathlib import Path

# Create data directory if it doesn't exist
data_dir = Path('data')
data_dir.mkdir(exist_ok=True)

# Use Railway's DATABASE_URL if available, otherwise use SQLite in data directory
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', f'sqlite:///{data_dir}/issues.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

db = SQLAlchemy(app)

class Issue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), default='Open')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    priority = db.Column(db.String(10), default='Medium')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'priority': self.priority
        }

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    try:
        # Test database connection
        db.session.execute('SELECT 1')
        return render_template('index.html')
    except Exception as e:
        logger.error(f"Database connection failed: {str(e)}")
        return "Error connecting to the database. Please check the logs.", 500

@app.route('/api/issues', methods=['GET'])
def get_issues():
    issues = Issue.query.order_by(Issue.created_at.desc()).all()
    return jsonify([issue.to_dict() for issue in issues])

@app.route('/api/issues', methods=['POST'])
def create_issue():
    data = request.json
    issue = Issue(
        title=data.get('title'),
        description=data.get('description', ''),
        status='Open',
        priority=data.get('priority', 'Medium')
    )
    db.session.add(issue)
    db.session.commit()
    return jsonify(issue.to_dict()), 201

@app.route('/api/issues/<int:issue_id>', methods=['PUT'])
def update_issue(issue_id):
    issue = Issue.query.get_or_404(issue_id)
    data = request.json
    
    if 'status' in data:
        issue.status = data['status']
    if 'priority' in data:
        issue.priority = data['priority']
    
    db.session.commit()
    return jsonify(issue.to_dict())

# Create database tables if they don't exist
with app.app_context():
    try:
        db.create_all()
        logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Error creating database tables: {str(e)}")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    os.makedirs('instance', exist_ok=True)
    app.run(host='0.0.0.0', port=port, debug=port == 5001)
