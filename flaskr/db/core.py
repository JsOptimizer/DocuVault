from flask_sqlalchemy import SQLAlchemy
from flask import current_app, g
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

db = SQLAlchemy()


class Base(DeclarativeBase):
    pass


def get_db():
    if 'db' not in g:
        db.init_app(current_app)
        g.db = db
        pass
    return g.db


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]
    pass
