from fastapi import APIRouter, UploadFile, File, Depends
from fastapi_limiter.depends import RateLimiter
from sqlalchemy.orm import Session
import cloudinary
import cloudinary.uploader

from src.settings.config import settings, get_db
from src.auth.dependencies import get_current_user
from src.database.models import User
from src.schemas.user import UserResponse

router = APIRouter(prefix="/users", tags=["users"])

# Cloudinary config
cloudinary.config(
    cloud_name=settings.CLOUDINARY_NAME,
    api_key=settings.CLOUDINARY_API_KEY,
    api_secret=settings.CLOUDINARY_API_SECRET
)

# GET /me with rate limit
@router.get("/me", response_model=UserResponse, dependencies=[Depends(RateLimiter(times=5, seconds=60))])
def get_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.put("/users/avatar")
async def upload_avatar(file: UploadFile = File(...), current_user: User = Depends(get_current_user)):
    # приклад простої логіки (можна замінити на збереження в базу/хмару)
    filename = f"{current_user.email}_avatar.png"
    contents = await file.read()
    with open(f"avatars/{filename}", "wb") as f:
        f.write(contents)

    return {"message": "Avatar uploaded", "filename": filename}