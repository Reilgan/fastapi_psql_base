
from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.crud.base import CRUDBase
from app.models.post import Post
from app.schemas.post import PostCreate, PostUpdate


class CRUDPost(CRUDBase[Post, PostCreate, PostUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: PostCreate, owner_id: int
    ) -> Post:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[Post]:
        return db.execute(
                select(self.model)
                .filter(Post.owner_id == owner_id)
                .offset(skip)
                .limit(limit)
            ).all()


post = CRUDPost(Post)
