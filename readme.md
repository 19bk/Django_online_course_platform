# Online Course Platform

## Overview

This is a Django-based REST API for an online course platform. It allows users to browse available courses, purchase them using a credit system, and be automatically assigned to study groups. The platform supports course creation, lesson management, and student group assignments.

## Features

- Course listing and detail views
- Lesson management within courses
- User balance management
- Course purchase functionality
- Automatic group assignment upon course purchase
- API documentation with Swagger UI and ReDoc

## Technology Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- drf-spectacular for API documentation

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/online_course_platform.git
   cd online_course_platform
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

## Running the Application

1. Start the Django development server:
   ```
   python manage.py runserver
   ```

2. Access the application at `http://127.0.0.1:8000/`

## API Documentation

- Swagger UI: `http://127.0.0.1:8000/api/schema/swagger-ui/`
- ReDoc: `http://127.0.0.1:8000/api/schema/redoc/`

## Usage

1. Admin Interface:
   - Access the admin interface at `http://127.0.0.1:8000/admin/`
   - Log in with your superuser credentials
   - Add courses, lessons, and manage user balances

2. API Endpoints:
   - List all courses: GET `/api/products/`
   - Course details: GET `/api/products/{id}/`
   - Purchase a course: POST `/api/products/{id}/pay/`
   - List all groups: GET `/api/groups/`
   - Group details: GET `/api/groups/{id}/`
   - List students in a group: GET `/api/groups/{id}/students/`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
