from fastapi import APIRouter, Depends, HTTPException, status

from app.database import get_db
from app.security import create_access_token
from app.schemas.auth import LoginRequest, TokenResponse
from app.services.auth_service import authenticate_user

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=TokenResponse )
def login(payload: LoginRequest, db: Session = Depends(get_db)) -> TokenResponse: