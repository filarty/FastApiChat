from sqlalchemy.orm import Session
from . import models


def create_user(db: Session, username: str, password: bytes):
    db_user = models.User(username=username, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def create_message(db: Session, user_id: int, text: str, to: int):
    message = models.Messages(user_id=user_id, message_text=text, to_user_id=to)
    db.add(message)
    db.commit()
    db.refresh(message)
    return message
