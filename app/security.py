from argon2 import PasswordHasher
from argon2.exceptions import VerificationError, VerifyMismatchError, InvalidHashError

# Creating an Argon2id hasher object
password_haser = PasswordHasher()

def hash_password(plain_password: str) -> str:
    return password_haser.hash(plain_password) # from  plain-text password to returns an Argon2 hash.


def verify_password(plain_password: str, password_hash: str) -> bool:
    try:
        return password_haser.verify(password_hash, plain_password)
    
    except (VerifyMismatchError, VerifyMismatchError, InvalidHashError):
        return False

    """
    Compares the plain password with the stored hash.
    Returns True if they match; returns False if the password is incorrect or the hash is invalid.
    """




"""
#  fro Verification . Hit Terminal
python -c "from app.security import hash_password, verify_password; h = hash_password('Secret@123'); print('Hash:', h[:20] + '...'); print('Correct:', verify_password('Secret@123', h)); print('Wrong:', verify_password('WrongPass', h))"
"""
"""
result:
    Correct: True
    Wrong: False
"""