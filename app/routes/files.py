from typing import List

from fastapi import APIRouter, Depends
from app.models import File
from .auth import get_current_user

router = APIRouter()


@router.get("/files", response_model=List[File])
async def get_files(user: dict = Depends(get_current_user)):
    files = [
        {"name": "file1.txt", "owner": "user123"},
        {"name": "file2.txt", "owner": "user123"},
    ]
    return files
