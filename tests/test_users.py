from tests.conftest import client


def test_me_unauthorized():
    response = client.get(
        "/users/me"
    )

    assert response.status_code == 401


def test_me_wrong_token():
    response = client.get(
        "/users/me",
        headers={
            "Authorization": "Bearer fake_token"
        }
    )

    assert response.status_code == 401
       