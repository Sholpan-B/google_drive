from fastapi import HTTPException, Depends
from app.models import User, Token

from fastapi import APIRouter

router = APIRouter()


@router.post("/token", response_model=Token)
async def login_for_access_token(user: User):
    is_authenticated = await authenticate_user(user)
    if not is_authenticated:
        raise HTTPException(status_code=401, detail="Неправильные учетные данные")
    return {"access_token": "dummy_access_token", "token_type": "bearer"}


async def get_current_user(token: str = Depends(login_for_access_token)):
    user = {"username": "user123"}
    return user


async def authenticate_user(user: User) -> bool:
    if user.username == "test_user" and user.password == "test_password":
        return True
    return False
