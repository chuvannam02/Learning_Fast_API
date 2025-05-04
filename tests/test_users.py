# unit test

from httpx import AsyncClient
from app.main import app
import pytest
# Snowflake là một dịch vụ lưu trữ dữ liệu đám mây

@pytest.mark.asyncio
async def test_create_user():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/users/", json={
            "username": "johndoe",
            "email": "john@example.com",
            "password": "123456"
        })
    assert response.status_code == 200
    assert "User 'johndoe'" in response.json()["message"]
