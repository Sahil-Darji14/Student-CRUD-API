# Student CRUD API

A simple REST API built using **FastAPI** to manage university student records.

This project was created as part of a FastAPI CRUD assignment.

## Features

* Create a student
* Get all students
* Get a student by ID
* Update a student
* Delete a student
* Pydantic validation
* HTTP status codes
* Swagger API documentation
* In-memory data storage
* No database used

## Technologies Used

* Python
* FastAPI
* Uvicorn
* Pydantic

## Project Structure

```text
student-crud/
│
├── main.py
├── requirements.txt
├── README.md
│
├── models/
│   └── student_model.py
│
├── routes/
│   └── student_routes.py
│
└── controllers/
    └── student_controller.py
```

## API Endpoints

| Method | Endpoint         | Description       |
| ------ | ---------------- | ----------------- |
| POST   | `/students`      | Create a student  |
| GET    | `/students`      | Get all students  |
| GET    | `/students/{id}` | Get student by ID |
| PUT    | `/students/{id}` | Update a student  |
| DELETE | `/students/{id}` | Delete a student  |

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Go to the project folder:

```bash
cd student-crud
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

The application will run at:

```text
http://127.0.0.1:8000
```

## Swagger Documentation

Open the following URL in your browser:

```text
http://127.0.0.1:8000/docs
```

Swagger UI can be used to test all five CRUD APIs.

## Storage

This project uses **local in-memory storage** using a Python list.

No database such as MySQL, PostgreSQL, MongoDB, or SQLite is used.

## Status Codes

* `200 OK` — Successful GET or PUT request
* `201 Created` — Student successfully created
* `204 No Content` — Student successfully deleted
* `404 Not Found` — Student ID does not exist
* `422 Unprocessable Entity` — Invalid input validation
