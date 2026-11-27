# To use EmailStr, run { pip install email-validator }

from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"



"""
Verification
python -c "from app.schemas.auth import LoginRequest, TokenResponse; req = LoginRequest(email='hr@example.com', password='DemoPassword@123'); res = TokenResponse(access_token='sample.jwt.token'); print(req.email, res.token_type)"
"""