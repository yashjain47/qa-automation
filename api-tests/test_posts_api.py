import re
import pytest
import requests
from jsonschema import validate

BASE_URL = "https://jsonplaceholder.typicode.com"


'------------------------ Schemas ------------------------' 

post_schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    },
    "required": ["userId", "id", "title", "body"]
}

user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "username": {"type": "string"},
        "email": {"type": "string"},

        "address": {
            "type": "object",
            "properties": {
                "street": {"type": "string"},
                "suite": {"type": "string"},
                "city": {"type": "string"},
                "zipcode": {"type": "string"},    

                "geo": {
                "type": "object",
                "properties": {
                    "lat": {"type": "string"},
                    "lng": {"type": "string"},    
                },
                "required": ["lat", "lng"]
            },
            },
            "required": ["street", "suite", "city", "zipcode","geo"]
        },

        "phone": {"type": "string"},
        "website": {"type": "string"},

        "company": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "catchPhrase": {"type": "string"},
                "bs": {"type": "string"},
            },
            "required": ["name", "catchPhrase", "bs"]
        },

    },
    "required": ["id", "name", "username", "email", "address","phone","website","company"]
}


'------------------------ Tests ------------------------'

def test_get_posts():
    """API Test 1 — GET /posts"""
    resp = requests.get(f"{BASE_URL}/posts")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) == 100
    # validate first post against schema
    validate(instance=data[0], schema=post_schema)


def test_get_user_by_id():
    """API Test 2 — GET /users/{id}"""
    resp = requests.get(f"{BASE_URL}/users/1")
    assert resp.status_code == 200
    user = resp.json()
    validate(instance=user, schema=user_schema)
    # check email format
    assert re.match(r"[^@]+@[^@]+\\.[^@]+", user["email"])
    # no null fields
    assert all(v is not None for v in user.values())


def test_create_post():
    """API Test 3 — POST /posts"""
    payload = {"title": "foo", "body": "bar", "userId": 1}
    resp = requests.post(f"{BASE_URL}/posts", json=payload)
    assert resp.status_code == 201
    response = resp.json()
    for key in payload:
        assert response[key] == payload[key]
    assert "id" in response


def test_update_post_put_and_patch():
    """API Test 4 — PUT & PATCH /posts/{id}"""
    put_payload = {"id": 1, "title": "updated", "body": "new body", "userId": 1}
    resp_put = requests.put(f"{BASE_URL}/posts/1", json=put_payload)
    assert resp_put.status_code == 200
    assert resp_put.json()["title"] == "updated"

    patch_payload = {"title": "patched title"}
    resp_patch = requests.patch(f"{BASE_URL}/posts/1", json=patch_payload)
    assert resp_patch.status_code == 200
    assert resp_patch.json()["title"] == "patched title"


def test_delete_post():
    """API Test 5 — DELETE /posts/{id}"""
    resp = requests.delete(f"{BASE_URL}/posts/1")
    assert resp.status_code in [200, 204]


# -------- Negative Tests -------- #

def test_get_invalid_user():
    resp = requests.get(f"{BASE_URL}/users/9999")
    # should return empty object
    assert resp.status_code == 200
    assert resp.json() == {}


def test_create_post_missing_fields():
    resp = requests.post(f"{BASE_URL}/posts", json={"title": "foo"})
    assert resp.status_code == 201
    # JSONPlaceholder accepts incomplete data but returns it
    data = resp.json()
    assert data["title"] == "foo"
    assert "id" in data


def test_wrong_header_type():
    headers = {"Content-Type": "text/plain"}
    resp = requests.post(f"{BASE_URL}/posts", headers=headers, data="raw text")
    # Fake API still returns 201, but ensure it responds
    assert resp.status_code in [201, 415]