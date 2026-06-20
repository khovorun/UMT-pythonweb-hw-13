from tests.conftest import client


def test_root():
    response = client.get("/")
    assert response.status_code == 200
      