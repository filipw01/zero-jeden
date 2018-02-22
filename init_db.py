__author__ = 'Filip Wachowiak'

from sqlalchemy import create_engine
from __init__ import db
from passlib.hash import sha256_crypt


def db_start():
    engine = create_engine('sqlite:///tmp/likes.db', convert_unicode=True)
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    db_start()