from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, deps, schemas
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

bearer_scheme = HTTPBearer()

router = APIRouter(prefix="/api/posts", tags=["Comments"])

@router.post("/{blog_id}/comment", response_model=schemas.CommentResponse)
def add_comment(
    blog_id: int,
    comment_data: schemas.CommentBase,  # Expect content from body
    db: Session = Depends(deps.get_db),
    current_user=Depends(deps.get_current_user),
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)
):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    comment = models.Comment(
        content=comment_data.content,  # match schema name
        blog_id=blog_id,
        user_id=current_user.id
    )
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment


@router.get("/{blog_id}/comments", response_model=list[schemas.CommentResponse])
def get_comments(blog_id: int, db: Session = Depends(deps.get_db)):
    return db.query(models.Comment).filter(models.Comment.blog_id == blog_id).all()
