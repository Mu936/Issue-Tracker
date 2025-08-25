A minimal, clean, and effective issue tracking application built with Python Flask and SQLite.

## Features

- Create new issues with title, description, and priority
- List all issues with filtering by status (Open, In Progress, Closed)
- Update issue status with a single click
- Responsive design that works on all devices
- Clean and intuitive user interface

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. Navigate to the project directory:
   ```bash
   cd /path/to/issue-tracker
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the Flask development server:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Using the Application

- **Create a new issue**: Fill out the form on the left and click "Create Issue"
- **Update status**: Use the action buttons on each issue to change its status
- **Filter issues**: Click the filter buttons at the top of the issues list to filter by status

## Project Structure

```
issue-tracker/
├── app.py               # Main application file
├── requirements.txt     # Python dependencies
├── render.yaml          # Render.com deployment configuration
├── Procfile             # Production process file
├── .gitignore          # Git ignore file
├── instance/
│   └── issues.db       # SQLite database (created on first run)
└── templates/
    └── index.html      # Frontend HTML template
```

## Deployment

### Deploy to Render.com (Recommended)

1. **Push your code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   ```

2. **Sign up/Log in to Render**
   - Go to [Render.com](https://render.com/)
   - Sign up or log in with your GitHub account

3. **Create a new Web Service**
   - Click "New +" and select "Web Service"
   - Connect your GitHub account and select the repository
   - Configure the service:
     - **Name**: issue-tracker (or your preferred name)
     - **Region**: Choose the one closest to you
     - **Branch**: main (or your main branch)
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
   - Click "Create Web Service"

4. **Wait for deployment**
   - Render will automatically deploy your application
   - Once complete, you'll get a URL like `https://your-app-name.onrender.com`

### Alternative: Deploy to Heroku

1. **Install Heroku CLI**
   ```bash
   # On macOS
   brew tap heroku/brew && brew install heroku
   
   # Or visit https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create a new Heroku app**
   ```bash
   heroku create your-app-name
   ```

4. **Deploy your code**
   ```bash
   git push heroku main
   ```

5. **Open your app**
   ```bash
   heroku open
   ```

## API Endpoints

- `GET /api/issues` - Get all issues
- `POST /api/issues` - Create a new issue
- `PUT /api/issues/<id>` - Update an existing issue

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
# Issue-Tracker
A small app to keep track of tasks or problems.
