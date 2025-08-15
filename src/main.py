from fastapi import FastAPI
from .database import Base, engine
from .routers import users, posts, likes, comments

# Create all tables (for development mode)
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="Blog Management API", version="1.0.0")

# Include routers
app.include_router(users.router)
app.include_router(posts.router)
app.include_router(likes.router)
app.include_router(comments.router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to Blog Management API"}
