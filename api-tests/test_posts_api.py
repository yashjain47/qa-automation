import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
ID = 12

def test_get_posts():
    r = requests.get(f"{BASE_URL}/posts")
    assert r.status_code == 200
    assert len(r.json()) == 100

def test_create_post():
    payload = {"title": "foo", "body": "bar", "userId": 1}
    r = requests.post(f"{BASE_URL}/posts", json=payload)
    assert r.status_code == 201
    assert r.json()["title"] == "foo"

def test_get_post_by_id():
    r = requests.get(f"{BASE_URL}/posts/{ID}")
    assert r.status_code == 200
    assert len(r.json()) == 100 