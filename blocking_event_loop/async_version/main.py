from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .database import get_async_db, User, initialize_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Initialize the database
    await initialize_database()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/users/{user_id}")
async def get_user(user_id: int, db: AsyncSession = Depends(get_async_db)):
    result = await db.execute(select(User).where(User.c.id == user_id))
    user = result.fetchone()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user.id, "name": user.name, "email": user.email}
