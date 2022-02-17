from sqlalchemy import Column, Integer, String, LargeBinary, ForeignKey, TEXT
from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))
    password = Column(LargeBinary(length=60))


class Messages(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    to_user_id = Column(Integer, ForeignKey('users.id'))
    message_text = Column(TEXT)
