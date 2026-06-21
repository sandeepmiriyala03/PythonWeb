from fastapi import APIRouter

from models.user import user
from services.user_service import userService   

router = APIRouter(
    prefix="/users",
    tags=["user"]
)

@router.get("/users")
def get_users():
    return userService.get_users()


@router.post("")
def create_user(
    user: user
):
    return userService.create_user(
        user
    )