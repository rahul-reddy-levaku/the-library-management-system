Library Management System API

This is a Flask-based RESTful API for managing the books and members of a library. The API allows users to perform CRUD (Create, Read, Update, Delete) operations for both books and members.

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

Python 3.7 or greater installed on your computer

Step

Install Flask:

pip install flask

 Run the application

python app.py

Access API at:

 Base URL: http://127.0.0.1:5000

API End-points

Books

GET /books: Get All Books

POST /books: Add a New Book (the request body requires id, title, and author).

GET /books/<book_id>: Get particular book details.

PUT /books/<book_id>: Update information of a book.

DELETE /books/<book_id>: Deletes a particular book.

Members

GET /members: Get All members

POST /members: Adds a new member. This should include id and name in the request body

GET /members/<member_id>: Returns details of a given member

PUT /members/<member_id>: Updates details of a given member

DELETE /members/<member_id>: Deletes a given member

Design Decisions

Framework: Flask is selected because it is lightweight and easy to use. Therefore, this would be good for small projects and APIs.

In-memory Storage: For simplicity and fast prototyping. Data will always reset on the server restart, though.

Every book and member have an id uniquely assigned to it.

The API is accessed locally for testing and development purposes.

Limitations

No database is used; the data is held in memory and hence not appropriate for production usage.

No authentication or user access control is in place.

Future Improvements

Implement a database for persistent storage of data.

Add user authentication and role-based access control.

Implement pagination when the dataset size is large.

Add more complex error handling.
