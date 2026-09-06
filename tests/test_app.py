from src.app import add, subtract, app


def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 7) == -2

def test_home_route():
    client=app.test_client()
    response=client.get("/")
    assert response.status_code==200
    assert response.data== b"Hello, this is my sample app for pipeline testing"