from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

# User Schemas
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime

    class Config:
        from_attributes = True

class TokenData(BaseModel):
    access_token: str
    token_type: str

class LoginResponse(BaseModel):
    user: UserResponse
    token: TokenData

# Blog Schemas
class BlogBase(BaseModel):
    title: str
    content: str

class BlogCreate(BlogBase):
    title: str
    content: str

class BlogUpdate(BaseModel):
    title: str
    content: str

class BlogResponse(BlogBase):
    id: int
    created_at: datetime
    author: UserResponse

    class Config:
        from_attributes = True

# Like Schemas
class LikeBase(BaseModel):
    blog_id: int


class LikeResponse(BaseModel):
    id: int
    user: UserResponse

    class Config:
        from_attributes = True

# Comment Schemas
class CommentBase(BaseModel):
    content: str


class CommentCreate(CommentBase):
    blog_id: int


class CommentResponse(CommentBase):
    id: int
    created_at: datetime
    user: UserResponse

    class Config:
        from_attributes = True

# Combined Blog Detail Schema
class BlogDetail(BlogResponse):
    likes: List[LikeResponse] = []
    comments: List[CommentResponse] = []
