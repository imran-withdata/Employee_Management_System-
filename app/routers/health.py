from fastapi import APIRouter



router = APIRouter(tags = ["Health"])



@router.get("/health")
def Health_check():
    return { "status": "Ok"}
