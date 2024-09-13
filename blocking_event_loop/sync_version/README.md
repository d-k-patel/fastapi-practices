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
├── main.py         # FastAPI routes and endpoints
├── database.py     # SQLAlchemy setup for sync engine
├── requirements.txt # Project dependencies
└── README.md       # Project documentation
```


## Requirements
- Python 3.9+
- FastAPI
- SQLAlchemy
- psycopg2-binary (PostgreSQL driver)


## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/fastapi-sync-version.git
cd fastapi-sync-version/sync_version