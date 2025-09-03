import re

def is_valid_email(email):
    if not isinstance(email, str) or not email:
        return False
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))
