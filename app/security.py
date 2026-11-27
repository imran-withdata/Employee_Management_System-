# ......................Part_1: Password Hashing & Verification...................


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
#  for Verification . Hit Terminal
python -c "from app.security import hash_password, verify_password; h = hash_password('Secret@123'); print('Hash:', h[:20] + '...'); print('Correct:', verify_password('Secret@123', h)); print('Wrong:', verify_password('WrongPass', h))"
    """
"""
result:
    Correct: True
    Wrong: False
"""




#.................... Part-2: Create_JWT_Access_Token.......

from datetime import datetime, timedelta, timezone
import uuid

import jwt
from app.config import settings

def create_access_token(user_id : int | str) -> str:
    # It takes a `user_id` and returns a `str` (JWT token).
    now = datetime.now(timezone.utc) # Take real time
    expire = now + timedelta(minutes=settings.access_token_expire_minutes)

    payload= {
        "sub" : str(user_id), # The user id is kept as a string as the subject.
        "exp" : expire, # Token expiration time
        "jti" : str(uuid.uuid4()), # A unique random ID for each token.D।
    }

    return jwt.encode(
        payload,
        settings.jwt_secret_key,
        algorithm=settings.jwt_algorithm,
    ) # Returns the final token string signed with the payload, settings.jwt_secret_key and settings.jwt_algorithm.

"""
# Verification of JWT token
python -c "import jwt; from app.config import settings; from app.security import create_access_token; tok = create_access_token(1); print('Token:', tok[:30] + '...'); decoded = jwt.decode(tok, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm]); print('Payload:', decoded)"
"""





# .......................Part-3: decode_access_token..........
def decode_access_token(token: str) -> dict:
    return jwt.decode(
        token,
        settings.jwt_secret_key,
        algorithms=[settings.jwt_algorithm],
    )


