# FastAPI Sync Version - User API

This project demonstrates a **synchronous** FastAPI implementation for a simple User API. The application performs synchronous database operations using **SQLAlchemy** and the **psycopg2** driver for PostgreSQL.

## Features
- FastAPI-based User API.
- Synchronous database queries using SQLAlchemy and psycopg2.
- Basic user lookup by ID.

## Project Structure
```bash
sync_version/
│
├── database.py     # SQLAlchemy setup for sync engine
├── main.py         # FastAPI routes and endpoints
├── README.md       # Project documentation
└── requirements.txt # Project dependencies
```


## Requirements
- Python 3.9+
- FastAPI
- SQLAlchemy
- psycopg2-binary (PostgreSQL driver)


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/d-k-patel/fastapi-practices.git
    cd fastapi-practices/blocking_event_loop/sync_version
    ```
2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  
    # On Windows use `venv\Scripts\activate`
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Setup PostgreSQL Database: Make sure you have PostgreSQL running and create a database for the project:
    ```bash
      CREATE DATABASE user_db;
    ```
5. Update database connection in database.py: Replace the database URL in database.py with your own credentials:

    ```python
    DATABASE_URL = "postgresql://<username>:<password>@localhost/user_db"
    ```
6. Run the application:
    ```bash
    uvicorn main:app --reload
    ```
    or
    ```bash
    uvicorn sync_version.main:app --reload
    ```
7. Access the API: Visit `http://127.0.0.1:8000/docs` to access the FastAPI Swagger UI and interact with the API.

## Endpoints

GET `/users/{user_id}`

## Example Request
```bash
curl -X 'GET' 'http://127.0.0.1:8000/users/1' -H 'accept: application/json'
```

## Benchmarking using Apache Benchmark
```bash
ab -n 1000 -c 100 http://127.0.0.1:8000/users/1
```

## Additional Information

- You will also find a `initial_users.sql` file that can be used to seed the database with 10 random users. 
- **Make sure to change the directory to the relevant location before running the command**.

### Seed Database
```bash
psql -d user_db -f initial_users.sql
```