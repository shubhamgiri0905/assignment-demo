# assignment-demo
This is my first Git repository
<br>
# Python Flask REST API with MongoDB

This project is a REST API server built using Python, Flask, and MongoDB. It allows users to Create, Read, Update, and Delete (CRUD) books from a MongoDB database.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Server](#running-the-server)
- [API Endpoints](#api-endpoints)
  - [Create a Book](#create-a-book)
  - [Get All Books](#get-all-books)
  - [Get a Single Book](#get-a-single-book)
  - [Update a Book](#update-a-book)
  - [Delete a Book](#delete-a-book)
- [Seeding the Database](#seeding-the-database)
- [License](#license)

## Features

- Create a new book entry
- Retrieve all book entries
- Retrieve a single book by ID
- Update an existing book by ID
- Delete a book by ID

## Requirements

- Python 3.12.3 or later
- MongoDB

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/python-flask-mongodb-api.git
    cd python-flask-mongodb-api
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

3. **Install dependencies:**

    ```bash
    pip install Flask Flask-PyMongo
    ```

4. **Install and set up MongoDB:**

    - Download and install MongoDB from [mongodb.com](https://www.mongodb.com/try/download/community).
    - Start the MongoDB server.
    - Ensure MongoDB is running on `mongodb://localhost:27017/`.

## Running the Server

1. **Run the Flask server:**

    ```bash
    python src/app.py
    ```

    The server will start on `http://localhost:5000`.

## API Endpoints

### Create a Book

- **URL:** `/api/books`
- **Method:** `POST`
- **Request Body:**

    ```json
    {
        "name": "Book Name",
        "img": "https://example.com/image.jpg",
        "summary": "Book summary"
    }
    ```

- **Success Response:**

    ```json
    {
        "id": "book_id",
        "name": "Book Name",
        "img": "https://example.com/image.jpg",
        "summary": "Book summary"
    }
    ```

### Get All Books

- **URL:** `/api/books`
- **Method:** `GET`
- **Success Response:**

    ```json
    [
        {
            "id": "book_id",
            "name": "Book Name",
            "img": "https://example.com/image.jpg",
            "summary": "Book summary"
        },
        ...
    ]
    ```

### Get a Single Book

- **URL:** `/api/books/<id>`
- **Method:** `GET`
- **Success Response:**

    ```json
    {
        "id": "book_id",
        "name": "Book Name",
        "img": "https://example.com/image.jpg",
        "summary": "Book summary"
    }
    ```

### Update a Book

- **URL:** `/api/books/<id>`
- **Method:** `PUT`
- **Request Body:**

    ```json
    {
        "name": "Updated Book Name",
        "img": "https://example.com/updated-image.jpg",
        "summary": "Updated book summary"
    }
    ```

- **Success Response:**

    ```json
    {
        "id": "book_id",
        "name": "Updated Book Name",
        "img": "https://example.com/updated-image.jpg",
        "summary": "Updated book summary"
    }
    ```

### Delete a Book

- **URL:** `/api/books/<id>`
- **Method:** `DELETE`
- **Success Response:**

    ```json
    {
        "message": "Book deleted successfully"
    }
    ```

## Seeding the Database

1. **Create and run the seed script to populate the database with initial data:**

    ```python
    # seed.py

    from pymongo import MongoClient

    client = MongoClient('mongodb://localhost:27017/')
    db = client.bookdb

    books = [
        {
            "name": "Harry Potter and the Order of the Phoenix",
            "img": "https://bit.ly/2IcnSwz",
            "summary": "Harry Potter and Dumbledore's warning about the return of Lord Voldemort is not heeded by the wizard authorities who, in turn, look to undermine Dumbledore's authority at Hogwarts and discredit Harry."
        },
        {
            "name": "The Lord of the Rings: The Fellowship of the Ring",
            "img": "https://bit.ly/2tC1Lcg",
            "summary": "A young hobbit, Frodo, who has found the One Ring that belongs to the Dark Lord Sauron, begins his journey with eight companions to Mount Doom, the only place where it can be destroyed."
        },
        {
            "name": "Avengers: Endgame",
            "img": "https://bit.ly/2Pzczlb",
            "summary": "Adrift in space with no food or water, Tony Stark sends a message to Pepper Potts as his oxygen supply starts to dwindle. Meanwhile, the remaining Avengers -- Thor, Black Widow, Captain America, and Bruce Banner -- must figure out a way to bring back their vanquished allies for an epic showdown with Thanos -- the evil demigod who decimated the planet and the universe."
        }
    ]

    db.books.insert_many(books)
    print("Data inserted successfully")
    client.close()
    ```

2. **Run the seed script:**

    ```bash
    python src/seed.py
    ```

## License

This project is licensed under the MIT License.

<br>
author name- Shubham Giri 
