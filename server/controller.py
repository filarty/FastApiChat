from fastapi import FastAPI, Form, WebSocket, Depends, Response, Cookie
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from sql_app.Schemas import AddFriend

from view import user_register, user_login, read_messages, new_message, get_users, get_friends, add_friend
from sql_app.database import SessionLocal, engine, Base

app = FastAPI()
Base.metadata.create_all(bind=engine)
clients = []


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/register")
async def register(username: str = Form(...), password: str = Form(..., min_length=6), db=Depends(get_db)):
    """Registration for user"""
    return await user_register(username=username, password=password, db=db)


@app.post("/login")
async def login_check(username: str = Form(...), password: str = Form(...), db=Depends(get_db)):
    """login users and set cookies without username"""
    response = await user_login(username=username, password=password, db=db)
    response.set_cookie(key="login", value=username)
    return response


@app.get("/messages")
async def get_messages(user_id: int, skip: int = 0, limit: int = 10, db=Depends(get_db)):
    """:return messages for user_id"""
    return await read_messages(db=db, user_id=user_id, skip=skip, limit=limit)


@app.post("/messages")
async def send_messages(user_id: int, text: str, to_user: int, db=Depends(get_db)):
    """:return send messages user_id -> to_user"""
    return await new_message(user_id=user_id, text=text, to=to_user, db=db)


@app.get("/getUsers")
async def user_list(db=Depends(get_db)):
    """:return list without all users in database"""
    return await get_users(db=db)


@app.get("/getFriends")
async def get_user_friends(user_id: int, db=Depends(get_db)):
    """:return all friends in user_id"""
    return await get_friends(db, user_id)


@app.put("/addFriends")
async def add_user(user: AddFriend, db=Depends(get_db)) -> JSONResponse:
    return await add_friend(db=db, user_id=user.user_id, friend_id=user.friend_id)


@app.websocket("/ws")
async def sockChat(websocket: WebSocket):
    """TEST future!!"""
    await websocket.accept()
    clients.append(websocket)
    while True:
        data = await websocket.receive_text()
        for sock in clients:
            await sock.send_text(data)
