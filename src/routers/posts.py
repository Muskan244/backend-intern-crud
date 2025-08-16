from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from .. import models, deps
from ..schemas import BlogResponse, BlogCreate, BlogUpdate

bearer_scheme = HTTPBearer()

router = APIRouter(prefix="/api/posts", tags=["Posts"])

@router.post("/", response_model=BlogResponse)
def create_post(
    post: BlogCreate,
    db: Session = Depends(deps.get_db),
    current_user=Depends(deps.get_current_user),
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)
):
    new_post = models.Blog(
        title=post.title,
        content=post.content,
        author_id=current_user.id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return BlogResponse.model_validate(new_post)


@router.get("/", response_model=list[BlogResponse])
def get_all_posts(db: Session = Depends(deps.get_db)):
    return [BlogResponse.model_validate(post) for post in db.query(models.Blog).all()]


@router.get("/{post_id}", response_model=BlogResponse)
def get_post(post_id: int, db: Session = Depends(deps.get_db)):
    post = db.query(models.Blog).filter(models.Blog.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return BlogResponse.model_validate(post)


@router.put("/{post_id}")
def update_post(post_id: int, post_data: BlogUpdate, db: Session = Depends(deps.get_db), current_user=Depends(deps.get_current_user), credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    post = db.query(models.Blog).filter(models.Blog.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    post.title = post_data.title
    post.content = post_data.content
    db.commit()
    db.refresh(post)
    return BlogResponse.model_validate(post)


@router.delete("/{post_id}", response_model=dict)
def delete_post(
    post_id: int,
    db: Session = Depends(deps.get_db),
    current_user=Depends(deps.get_current_user),
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)
):
    post = db.query(models.Blog).filter(models.Blog.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    db.delete(post)
    db.commit()
    return {"message": "Post deleted"}
