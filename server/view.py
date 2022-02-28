from fastapi.responses import JSONResponse, Response
from fastapi import HTTPException

from sqlalchemy.orm import Session
from sql_app.crud import get_user, create_user, get_messages, create_message, get_users_list

from valid_for_pass import Password


async def user_register(username: str, password: str, db: Session) -> Response:
    if get_user(db, username):
        raise HTTPException(status_code=404, detail="user has registered!")
    if Password.valid_pass(password):
        hash_pass = Password.crypt_pass(password)
        create_user(db, username, password=hash_pass)
        return JSONResponse({"detail": username})
    return JSONResponse({"password": "not valid"})


async def user_login(username: str, password: str, db: Session) -> Response:
    check_pass = password
    db_user = get_user(db, username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="user not registered!")
    if not Password.check_pass(check_pass, db_user.password):
        raise HTTPException(status_code=404, detail="wrong password!")
    return JSONResponse({"login": "success"})


async def get_users(db: Session) -> JSONResponse:
    response = []
    for user in get_users_list(db=db):
        response.append(user['username'])
    return JSONResponse({'users': response})


async def new_message(db: Session, user_id: int, text: str, to: int):
    return create_message(db=db, user_id=user_id, text=text, to=to)


async def read_messages(db: Session, user_id: int, skip: int, limit: int):
    return get_messages(db=db, user_id=user_id, skip=skip, limit=limit)
