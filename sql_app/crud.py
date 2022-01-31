from sqlalchemy.orm import Session

from valid_for_pass import Password

from . import models


def create_user(db: Session, username: str, password: str):
    hash_pass = Password.crypt_pass(password)
    db_user = models.User(username=username, password=hash_pass)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()
