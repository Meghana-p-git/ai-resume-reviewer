
# AI Resume Reviewer

A web application built with Python and Flask to help develop an understanding of resume review, skill identification, and job-description matching. The project is being developed incrementally, starting with backend fundamentals and form handling.

## Project Status

🚧 In Progress

The current version demonstrates Flask routing, form handling, input validation, Jinja templates, and a basic JSON API. Resume parsing and automated resume analysis are planned future features.

## Features Implemented

- **Flask web application:** Routes for the home page, form submission, and skill search.
- **Form handling:** Accepts user input through HTML forms using GET and POST requests.
- **Input validation:** Handles empty and whitespace-only input.
- **Dynamic HTML pages:** Uses Jinja templates to display submitted data.
- **Template inheritance:** Reuses a common layout across pages.
- **Skill descriptions:** Displays predefined descriptions for Python, React, and SQL.
- **JSON API:** Provides a project status endpoint at `/api/status`.

## Tech Stack

- **Language:** Python
- **Backend:** Flask
- **Frontend:** HTML, Jinja2
- **Data format:** JSON
- **Version Control:** Git and GitHub

## Project Structure

```text
ai-resume-reviewer/
├── app.py
├── requirements.txt
├── README.md
└── templates/
    ├── base.html
    ├── index.html
    ├── review.html
    └── search.html
```

## Getting Started

### Prerequisites

- Python 3.10 or later
- pip
- Git

### Installation

1. Clone the repository:

   ```bash
   git clone <YOUR_GITHUB_REPOSITORY_URL>
   cd ai-resume-reviewer
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

3. Activate the environment:

   ```bash
   source venv/bin/activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:

   ```bash
   python app.py
   ```

6. Open `http://127.0.0.1:5000/` in your browser.

## API Endpoint

### GET `/api/status`

Returns a JSON response describing the application status.

Example response:

```json
{
  "project": "AI Resume Reviewer",
  "status": "running"
}
```

## Planned Improvements

- Resume file upload functionality
- PDF text extraction
- Skill identification from resume content
- Job-description and resume skill matching
- Resume feedback and improvement suggestions
- Automated resume scoring
- Testing and deployment

## Learning Objectives

This project is also a hands-on exercise in backend development, HTTP methods, REST API fundamentals, input validation, template rendering, and frontend-backend integration.

## Development Approach

This project is being developed incrementally, starting with Flask
routes, HTTP methods, form handling, input validation, and template
rendering. Future improvements will build on this foundation.