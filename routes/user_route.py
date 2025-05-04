from fastapi import APIRouter, Depends, HTTPException
from schemas.user_schema import UserCreate

router = APIRouter()

@router.post("/")
def create_user(user: UserCreate):
    if user.username == "admin":
        raise HTTPException(status_code=400, detail="Username 'admin' is not allowed.")
    
    return {"message": f"User {user.username} created successfully!"}