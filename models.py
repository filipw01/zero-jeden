__author__ = 'Filip Wachowiak'

from sqlalchemy import Column
from sqlalchemy.types import Integer
from sqlalchemy.types import String

from __init__ import db


class Like(db.Model):
    """
    Komentarze
    """
    __tablename__ = 'likes'
    id = Column(Integer, autoincrement=True, primary_key=True)
    post = Column(String(100))
    username = Column(String(20), unique=True)