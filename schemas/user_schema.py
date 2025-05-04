from pydantic import BaseModel, Field, EmailStr

# BaseModel là lớp cơ sở cho tất cả các mô hình Pydantic
# Field là một hàm để định nghĩa các trường trong mô hình
# EmailStr là kiểu dữ liệu để xác thực địa chỉ email
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr
    age: int = Field(..., ge=18, le=100)