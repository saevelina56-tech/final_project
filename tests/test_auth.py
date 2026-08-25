import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_register_user():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(
            "/users/register",
            json={
                "username": "tester",
                "email": "tester@example.com",
                "password": "securepass123"  
            }
        )
        assert response.status_code == 201
        data = response.json()
        assert data["username"] == "tester" 
        assert data["email"] == "tester@example.com"  
        assert "id" in data

@pytest.mark.asyncio
async def test_register_duplicate_user():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        await ac.post(
            "/users/register",
            json={
                "username": "tester2",
                "email": "test2@example.com",
                "password": "securepass456"
            }
        )
        response = await ac.post(
            "/users/register",
            json={
                "username": "tester2",  
                "email": "test3@example.com",  
                "password": "securepass789"
            }
        )
        assert response.status_code == 400
        assert "Username already registered" in response.json()["detail"]

@pytest.mark.asyncio
async def test_login():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        await ac.post(
            "/users/register",
            json={
                "username": "testuser",  
                "email": "testlogin@example.com",  
                "password": "securepass123"
            }
        )
        response = await ac.post(
            "/users/token",
            data={
                "username": "testuser",  
                "password": "securepass123"  
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"

@pytest.mark.asyncio
async def test_login_invalid_credentials():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(
            "/users/token",
            data={
                "username": "nonexistent_user",  
                "password": "wrongpassword"
            }
        )
        assert response.status_code == 401
        assert "Incorrect username or password" in response.json()["detail"]

@pytest.mark.asyncio
async def test_login_with_email():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        await ac.post(
            "/users/register",
            json={
                "username": "emailuser",
                "email": "emaillogin@example.com",
                "password": "securepass123"
            }
        )
        response = await ac.post(
            "/users/token",
            data={
                "username": "emaillogin@example.com",  
                "password": "securepass123"
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"

@pytest.mark.asyncio
async def test_get_current_user():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        await ac.post(
            "/users/register",
            json={
                "username": "currentuser",
                "email": "current@example.com",
                "password": "securepass123"
            }
        )
        login_response = await ac.post(
            "/users/token",
            data={
                "username": "currentuser",
                "password": "securepass123"
            }
        )
        token = login_response.json()["access_token"]
        
        response = await ac.get(
            "/users/me",
            headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["username"] == "currentuser"
        assert data["email"] == "current@example.com"

@pytest.mark.asyncio
async def test_register_invalid_password():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(
            "/users/register",
            json={
                "username": "shortpass",
                "email": "short@example.com",
                "password": "123"  
            }
        )
        assert response.status_code == 422  