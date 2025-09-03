from unit_tests.utils.validators import is_valid_email

def test_valid_emails():
    assert is_valid_email("test@example.com")
    assert is_valid_email("user.name@domain.co")

def test_invalid_emails():
    assert not is_valid_email("plainaddress")
    assert not is_valid_email("missing@domain")
