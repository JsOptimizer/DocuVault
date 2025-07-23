import datetime

from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from flaskr.extension.core import db


class User(db.Model):
    id: Mapped[str] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str]
    password_hash: Mapped[str]
    create_at: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP(timezone=True), default=TIMESTAMP
    )
