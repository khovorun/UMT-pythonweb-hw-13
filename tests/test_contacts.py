from tests.conftest import client


def test_contacts_unauthorized():
    response = client.get("/contacts/")
    assert response.status_code == 401


def test_birthdays_unauthorized():
    response = client.get("/contacts/birthdays/")
    assert response.status_code == 401
        