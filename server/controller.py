from fastapi import FastAPI, Form, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends
from view import user_register, user_login, read_messages, new_message, get_users
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
    return await user_register(username=username, password=password, db=db)


@app.post("/login")
async def login_check(username: str = Form(...), password: str = Form(...), db=Depends(get_db)):
    return await user_login(username=username, password=password, db=db)


@app.get("/messages")
async def get_messages(user_id: int, skip: int = 0, limit: int = 10, db=Depends(get_db)):
    return await read_messages(db=db, user_id=user_id, skip=skip, limit=limit)


@app.post("/messages")
async def send_messages(user_id: int, text: str, to: int, db=Depends(get_db)):
    return await new_message(user_id=user_id, text=text, to=to, db=db)


@app.get("/getUsers")
async def user_list(db=Depends(get_db)):
    return await get_users(db=db)


@app.websocket("/ws")
async def sockChat(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    while True:
        data = await websocket.receive_text()
        for sock in clients:
            await sock.send_text(data)
