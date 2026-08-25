from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_
from fastapi import HTTPException, status
from typing import Optional, List

from app.models import Item, User
from app.schemas import ItemCreate, ItemUpdate

class ItemService:    
    @staticmethod
    async def get_by_id(db: AsyncSession, item_id: int) -> Optional[Item]:
        result = await db.execute(select(Item).where(Item.id == item_id))
        return result.scalar_one_or_none()
    
    @staticmethod
    async def get_user_items(
        db: AsyncSession, 
        user_id: int, 
        skip: int = 0, 
        limit: int = 100,
        search: Optional[str] = None
    ) -> List[Item]:
        query = select(Item).where(Item.owner_id == user_id)
        
        if search:
            query = query.where(
                or_(
                    Item.title.ilike(f"%{search}%"),
                    Item.description.ilike(f"%{search}%")
                )
            )
        
        query = query.offset(skip).limit(limit)
        result = await db.execute(query)
        return result.scalars().all()
    
    @staticmethod
    async def create_item(
        db: AsyncSession, 
        item_data: ItemCreate, 
        user_id: int
    ) -> Item:
        db_item = Item(
            **item_data.model_dump(),
            owner_id=user_id
        )
        
        db.add(db_item)
        await db.commit()
        await db.refresh(db_item)
        
        return db_item
    
    @staticmethod
    async def update_item(
        db: AsyncSession, 
        item_id: int, 
        item_data: ItemUpdate,
        user_id: int
    ) -> Item:
        db_item = await ItemService.get_by_id(db, item_id)
        
        if not db_item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Item not found"
            )
        
        if db_item.owner_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions"
            )
        
        update_data = item_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_item, key, value)
        
        await db.commit()
        await db.refresh(db_item)
        
        return db_item
    
    @staticmethod
    async def delete_item(db: AsyncSession, item_id: int, user_id: int) -> None:
        db_item = await ItemService.get_by_id(db, item_id)
        
        if not db_item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Item not found"
            )
        
        if db_item.owner_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions"
            )
        
        await db.delete(db_item)
        await db.commit()
    
    @staticmethod
    async def get_items_count(db: AsyncSession, user_id: int) -> int:
        from sqlalchemy import func
        result = await db.execute(
            select(func.count()).select_from(Item).where(Item.owner_id == user_id)
        )
        return result.scalar() or 0