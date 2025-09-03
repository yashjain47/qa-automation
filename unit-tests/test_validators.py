from utils.validators import is_valid_email

def test_valid_emails():
    assert is_valid_email("test@example.com") is True
    assert is_valid_email("user.name@domain.co") is True

def test_invalid_emails():
    assert is_valid_email("plainaddress") is False
    assert is_valid_email("missing@domain") is False
    assert is_valid_email("") is False  
    assert is_valid_email(None) is False

