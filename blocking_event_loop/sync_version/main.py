from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException

from .database import User, get_db


app = FastAPI()


@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    # Synchronous and blocking
    user = db.query(User).filter(User.c.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"name": user.name, "email": user.email}
