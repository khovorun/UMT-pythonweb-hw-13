from unittest.mock import patch

from services.cloudinary_service import (
    upload_avatar
)


@patch("cloudinary.uploader.upload")
def test_upload_avatar(mock_upload):
    mock_upload.return_value = {
        "secure_url": "https://test.com/avatar.jpg"
    }

    result = upload_avatar(
        "fake_file"
    )

    assert result == (
        "https://test.com/avatar.jpg"
    )
       