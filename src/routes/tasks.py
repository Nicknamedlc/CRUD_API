from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_session
from src.models import Task, User
from src.security import get_current_user

router = APIRouter(prefix='/tasks', tags=['Tarefas'])
Session = Annotated[Session, Depends(get_session)]
CurrentUser = Annotated[User, Depends(get_current_user)]


@router.post('/', response_model=Task)
def crate_task(
    user: CurrentUser,
    session: Session,
): ...
