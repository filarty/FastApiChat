from fastapi import FastAPI, Request, Form, Depends, HTTPException, status
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from valid_for_pass import Password
from sql_app.crud import get_user, create_user
from sql_app.database import engine, SessionLocal, Base
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
templates = Jinja2Templates(directory="templates")
Base.metadata.create_all(bind=engine)

origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/register")
async def register(username: str = Form(...), password: str = Form(..., min_length=6), db=Depends(get_db)):
    if get_user(db, username):
        raise HTTPException(status_code=404, detail="user has registered!")
    if Password.valid_pass(password):
        create_user(db, username, password)
        return RedirectResponse("/", status_code=status.HTTP_302_FOUND)
    return JSONResponse({"password": "not valid"})


@app.get("/", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login")
async def login_check(username: str = Form(...), password: str = Form(...), db=Depends(get_db)):
    check_pass = password
    db_user = get_user(db, username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="user not registered!")
    if not Password.check_pass(check_pass, db_user.password):
        raise HTTPException(status_code=404, detail="wrong password!")
    return JSONResponse({"name": username, "pass": check_pass})
