from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm
from typing import List

from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserResponse, Token, ItemResponse
from app.auth import (
    create_access_token,
    get_current_user,
    authenticate_user,
    ACCESS_TOKEN_EXPIRE_MINUTES
)
from app.services import UserService, ItemService
from app.html_pages import get_register_page, get_login_page

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return HTMLResponse(content=get_register_page())

@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return HTMLResponse(content=get_login_page())

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(
    user: UserCreate, 
    db: AsyncSession = Depends(get_db)
):
    return await UserService.create_user(db, user)

@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    user = await authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(
        data={"sub": user.email},
        expires_delta=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserResponse)
async def read_users_me(
    current_user: User = Depends(get_current_user)
):
    return current_user

@router.get("/me/items", response_model=List[ItemResponse])
async def read_user_items(
    skip: int = 0,
    limit: int = 100,
    search: str = None,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    items = await ItemService.get_user_items(
        db, 
        current_user.id, 
        skip=skip, 
        limit=limit,
        search=search
    )
    return items