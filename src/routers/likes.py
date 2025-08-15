from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, deps

router = APIRouter(prefix="/api/posts", tags=["Likes"])

@router.post("/{blog_id}/like")
def like_post(blog_id: int, db: Session = Depends(deps.get_db), current_user=Depends(deps.get_current_user)):
    post = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    # Check if user already liked
    if db.query(models.Like).filter(models.Like.blog_id == blog_id, models.Like.user_id == current_user.id).first():
        raise HTTPException(status_code=400, detail="You already liked this post")

    like = models.Like(blog_id=blog_id, user_id=current_user.id)
    db.add(like)
    db.commit()
    return {"message": "Post liked"}
