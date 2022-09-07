from typing import List
from fastapi import (
    APIRouter, Depends, HTTPException, Path, status
)
from app.api.dependencies import get_db
from app.api import crud
from app.api.schemas import (
    ProgrammerListItem, ProgrammerDetail
)


rooter = APIRouter()


@rooter.get("/", response_model=List[ProgrammerListItem])
def list_programmers(db=Depends(get_db)):
    return crud.get_programmers(db)


@rooter.get(
    "/{name}",
    response_model=ProgrammerDetail,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "programmer not found",
        }
    }
)
def detail_programmer(
    name: str = Path(max_length=100),
    db=Depends(get_db)
):
    if not crud.exists_programmer(db, name):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="programmer not found",
        )
    return crud.get_programmer_detail_by_name(db, name)


@rooter.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_400_BAD_REQUEST: {  # 注
            "description": "programmer already exists",
        }
    })
def add_programmer(programmer: ProgrammerDetail, db=Depends(get_db)):
    crud.add_programmer(db, programmer)
    return {"result": "OK"}


@rooter.put(
    "/{name}",
    status_code=status.HTTP_201_CREATED
)
def update_programmer(
        *,
        name: str = Path(max_length=100),
        programmer: ProgrammerDetail,
        db=Depends(get_db)
):
    crud.update_programmer(db, name, programmer)
    return {"result": "OK"}


@rooter.delete(
    "/{name}",
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "programmer not found",
        }
    }
)
def delete_programmer(name: str, db=Depends(get_db)):
    if not crud.exists_programmer(db, name):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="programmer not found",
        )
    crud.delete_programmer(db, name)
    return {"result": "OK"}
