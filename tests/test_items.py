import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_item():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        await ac.post(
            "/users/register",
            json={
                "username": "itemuser",
                "email": "item@example.com",
                "password": "securepass123"
            }
        )
        login_response = await ac.post(
            "/users/token",
            data={
                "username": "itemuser",
                "password": "securepass123"
            }
        )
        token = login_response.json()["access_token"]
        
        response = await ac.post(
            "/items/",
            json={
                "title": "Test Item",
                "description": "Test Description",
                "price": 99.99
            },
            headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "Test Item"
        assert data["price"] == 99.99
        assert "id" in data
        assert data["owner_id"] is not None

@pytest.mark.asyncio
async def test_get_items():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        await ac.post(
            "/users/register",
            json={
                "username": "getitemsuser",
                "email": "getitems@example.com",
                "password": "securepass123"
            }
        )
        login_response = await ac.post(
            "/users/token",
            data={
                "username": "getitemsuser",
                "password": "securepass123"
            }
        )
        token = login_response.json()["access_token"]
        
        for i in range(3):
            await ac.post(
                "/items/",
                json={
                    "title": f"Item {i}",
                    "description": f"Description {i}",
                    "price": 10.0 * (i + 1)
                },
                headers={"Authorization": f"Bearer {token}"}
            )
        
        response = await ac.get(
            "/items/",
            headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 3

@pytest.mark.asyncio
async def test_get_items_with_pagination():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        await ac.post(
            "/users/register",
            json={
                "username": "paginationuser",
                "email": "pagination@example.com",
                "password": "securepass123"
            }
        )
        login_response = await ac.post(
            "/users/token",
            data={
                "username": "paginationuser",
                "password": "securepass123"
            }
        )
        token = login_response.json()["access_token"]
        
        for i in range(5):
            await ac.post(
                "/items/",
                json={
                    "title": f"Pagination Item {i}",
                    "price": 10.0 * (i + 1)
                },
                headers={"Authorization": f"Bearer {token}"}
            )
        
        response = await ac.get(
            "/items/?skip=0&limit=2",
            headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2

@pytest.mark.asyncio
async def test_update_item():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        await ac.post(
            "/users/register",
            json={
                "username": "updateuser",
                "email": "update@example.com",
                "password": "securepass123"
            }
        )
        login_response = await ac.post(
            "/users/token",
            data={
                "username": "updateuser",
                "password": "securepass123"
            }
        )
        token = login_response.json()["access_token"]
        
        create_response = await ac.post(
            "/items/",
            json={
                "title": "Original Title",
                "description": "Original Description",
                "price": 50.0
            },
            headers={"Authorization": f"Bearer {token}"}
        )
        item_id = create_response.json()["id"]
        
        response = await ac.put(
            f"/items/{item_id}",
            json={
                "title": "Updated Title",
                "price": 75.0
            },
            headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Updated Title"
        assert data["price"] == 75.0
        assert data["description"] == "Original Description"  

@pytest.mark.asyncio
async def test_delete_item():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        await ac.post(
            "/users/register",
            json={
                "username": "deleteuser",
                "email": "delete@example.com",
                "password": "securepass123"
            }
        )
        login_response = await ac.post(
            "/users/token",
            data={
                "username": "deleteuser",
                "password": "securepass123"
            }
        )
        token = login_response.json()["access_token"]
        
        create_response = await ac.post(
            "/items/",
            json={
                "title": "To Delete",
                "description": "Will be deleted",
                "price": 10.0
            },
            headers={"Authorization": f"Bearer {token}"}
        )
        item_id = create_response.json()["id"]
        
        response = await ac.delete(
            f"/items/{item_id}",
            headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 204
        
        get_response = await ac.get(
            f"/items/{item_id}",
            headers={"Authorization": f"Bearer {token}"}
        )
        assert get_response.status_code == 404

@pytest.mark.asyncio
async def test_item_not_found():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        await ac.post(
            "/users/register",
            json={
                "username": "notfounduser",
                "email": "notfound@example.com",
                "password": "securepass123"
            }
        )
        login_response = await ac.post(
            "/users/token",
            data={
                "username": "notfounduser",
                "password": "securepass123"
            }
        )
        token = login_response.json()["access_token"]
        
        response = await ac.get(
            "/items/99999",
            headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 404