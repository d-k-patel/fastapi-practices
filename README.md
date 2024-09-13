## FastAPI Sync & Async Versions - User API
This repository contains both synchronous and asynchronous implementations of a FastAPI-based User API. It demonstrates how to handle database operations using SQLAlchemy and PostgreSQL, providing two distinct approaches for handling I/O-bound tasks:

- Sync Version: Utilizes synchronous database queries with psycopg2.
- Async Version: Utilizes asynchronous database queries with asyncpg.

Each version is located in its respective directory:
- sync_version/
- async_version/

For setup instructions, details on database connection, and usage, refer to the individual README.md files located inside the sync_version and async_version directories.