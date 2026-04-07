import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app
from data import inventory


def setup_function():
    inventory.clear()


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_add_item():
    client = app.test_client()
    response = client.post("/inventory", json={
        "name": "Milk",
        "price": 100,
        "stock": 5
    })
    assert response.status_code == 201


def test_get_items():
    client = app.test_client()
    client.post("/inventory", json={
        "name": "Bread",
        "price": 50,
        "stock": 2
    })
    response = client.get("/inventory")
    assert response.status_code == 200


def test_update_item():
    client = app.test_client()
    client.post("/inventory", json={
        "name": "Sugar",
        "price": 80,
        "stock": 4
    })
    response = client.patch("/inventory/1", json={
        "name": "Brown Sugar"
    })
    assert response.status_code == 200


def test_delete_item():
    client = app.test_client()
    client.post("/inventory", json={
        "name": "Tea",
        "price": 30,
        "stock": 3
    })
    response = client.delete("/inventory/1")
    assert response.status_code == 200