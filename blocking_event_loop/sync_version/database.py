from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker

# Replace with your actual database URL
DATABASE_URL = "postgresql://user:password@localhost/db_name"

# Create a synchronous SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a session maker for synchronous queries
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Define metadata and user table
metadata = MetaData()

User = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("email", String),
)

# create all tables
metadata.create_all(engine)


# Dependency to get a synchronous DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
