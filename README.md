Library Management System API

This project is a Flask-based RESTful API for managing a library's books and members. The API allows users to perform CRUD (Create, Read, Update, Delete) operations for both books and members.

Features

Manage books:

Add a new book

View all books

Get details of a specific book

Update book details

Delete a book

Manage members:

Add a new member

View all members

Get details of a specific member

Update member details

Delete a member

How to Run the Project

Prerequisites

Python 3.7 or later installed on your machine

Steps


Install Flask:

pip install flask

Run the application:

python app.py

Access the API at:

Base URL: http://127.0.0.1:5000

API Endpoints

Books

GET /books: Retrieve all books

POST /books: Add a new book (requires id, title, and author in the request body)

GET /books/<book_id>: Retrieve details of a specific book

PUT /books/<book_id>: Update details of a specific book

DELETE /books/<book_id>: Delete a specific book

Members

GET /members: Retrieve all members

POST /members: Add a new member (requires id and name in the request body)

GET /members/<member_id>: Retrieve details of a specific member

PUT /members/<member_id>: Update details of a specific member

DELETE /members/<member_id>: Delete a specific member

Design Choices

Framework: Flask was chosen for its simplicity and lightweight nature, making it ideal for small projects and APIs.

In-memory Storage: Used for simplicity and quick prototyping. Note that the data will reset whenever the server restarts.

Assumptions

Each book and member has a unique id.

The API is accessed locally for testing and development purposes.

Limitations

No database is used; data is stored in memory, making it unsuitable for production use.

No authentication or user access control is implemented.

Future Improvements

Integrate a database for persistent data storage.

Add user authentication and role-based access control.

Implement pagination for large datasets.

Add more advanced error handling.

