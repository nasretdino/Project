from fastapi import APIRouter, HTTPException, Response
from pydantic import BaseModel, Field
import datetime


router = APIRouter(prefix="/posts", tags=["posts"])


class Item(BaseModel):
    id: int = None
    title: str
    content: str
    autor: str | None = None
    published: bool = True
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)


POSTS: list[Item] = []


@router.post("/")
async def create_item(item: Item):
    item.id = len(POSTS)
    POSTS.append(item)
    return item

@router.get("/")
async def get_posts():
    return POSTS

@router.get("/{id}")
async def get_post(id: int):
    p = [i for i in POSTS if i.id == id]
    if not p: raise HTTPException(status_code=404, detail="Post not found")
    else: return p

@router.put("/{id}")
async def update_post(id: int, item: Item):
    for i, p in enumerate(POSTS):
        if p.id == id:
            item.id = id
            POSTS[i] = item
            return item
    raise HTTPException(status_code=404, detail="Post not found")

@router.delete("/{id}")
async def delete_post(id: int):
    for i, p in enumerate(POSTS):
        if p.id == id:
            del POSTS[i]
            return Response(status_code=200, content="Post deleted")
    raise HTTPException(status_code=404, detail="Post not found")
