from services.auth import (
    get_password_hash,
    verify_password,
    create_access_token,
    create_email_token,
    verify_email_token,
    create_reset_token,
    verify_reset_token,
)


def test_password_hash():
    password = "12345678"

    hashed = get_password_hash(password)

    assert hashed != password
    assert verify_password(password, hashed) is True


def test_verify_password_wrong():
    password = "12345678"

    hashed = get_password_hash(password)

    assert verify_password(
        "wrong_password",
        hashed
    ) is False


def test_create_access_token():
    token = create_access_token(
        {"sub": "test@gmail.com"}
    )

    assert isinstance(token, str)
    assert len(token) > 0


def test_create_email_token():
    token = create_email_token(
        "test@gmail.com"
    )

    assert isinstance(token, str)
    assert len(token) > 0


def test_verify_email_token():
    token = create_email_token(
        "test@gmail.com"
    )

    email = verify_email_token(token)

    assert email == "test@gmail.com"


def test_verify_email_token_invalid():
    email = verify_email_token(
        "invalid_token"
    )

    assert email is None


def test_create_reset_token():
    token = create_reset_token(
        "test@gmail.com"
    )

    assert isinstance(token, str)
    assert len(token) > 0


def test_verify_reset_token():
    token = create_reset_token(
        "test@gmail.com"
    )

    email = verify_reset_token(token)

    assert email == "test@gmail.com"


def test_verify_reset_token_invalid():
    email = verify_reset_token(
        "invalid_token"
    )

    assert email is None
    