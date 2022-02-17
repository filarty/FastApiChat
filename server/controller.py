from fastapi import FastAPI, Form, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends
from view import user_register, user_login
from sql_app.database import SessionLocal, engine, Base

app = FastAPI()
Base.metadata.create_all(bind=engine)


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


@app.websocket("/ws")
async def sockChat(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(data)
