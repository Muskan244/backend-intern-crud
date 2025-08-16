from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .database import Base, engine
from .routers import users, posts, likes, comments

# Create all tables (for development mode)
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="Blog Management API", version="1.0.0")

bearer_scheme = HTTPBearer()

# Include routers
app.include_router(users.router)
app.include_router(posts.router)
app.include_router(likes.router)
app.include_router(comments.router)

@app.get("/api/users/me")
def read_users_me(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = credentials.credentials
    return {"token_received": token}

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to Blog Management API"}
