from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/")
def users_test():
    return {
        "message": "Users API is working"
    }