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


def get_users_list(db: Session):
    return db.query(models.User.username).all()


def create_message(db: Session, user_id: int, text: str, to: int):
    message = models.Messages(user_id=user_id, message_text=text, to_user_id=to)
    db.add(message)
    db.commit()
    db.refresh(message)
    return message


def get_user_friends(db: Session, user_id: int):
    user = db.query(models.User.friends).filter(models.User.id == user_id).all()
    return user


def add_user_friend(db: Session, user_id: int, friend_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user.friends is None:
        user.friends = [friend_id]
    if friend_id in user.friends:
        return False
    else:
        array_friends = user.friends[:]
        array_friends.append(friend_id)
        user.friends = array_friends
    db.add(user)
    db.commit()
    db.refresh(user)
    return user.friends


def get_messages(db: Session, user_id: int, skip: int, limit: int):
    return db.query(models.Messages).filter(models.Messages.user_id == user_id).offset(skip).limit(limit).all()
