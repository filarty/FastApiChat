from sqlalchemy import Column, Integer, String, LargeBinary
from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))
    password = Column(LargeBinary(length=60))
