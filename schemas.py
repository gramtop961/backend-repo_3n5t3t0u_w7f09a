from pydantic import BaseModel, Field, EmailStr
from typing import Optional

# Collections
class Authuser(BaseModel):
    """
    Authentication users collection
    Collection name: "authuser" (lowercase of class name)
    """
    email: EmailStr = Field(..., description="Unique email address")
    name: str = Field(..., description="Display name")
    password_hash: str = Field(..., description="BCrypt password hash")
    is_active: bool = Field(True, description="Active account flag")

# Request/Response models (not collections)
class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    name: str
    email: EmailStr
