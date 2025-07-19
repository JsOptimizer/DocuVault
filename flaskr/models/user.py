from ..extension.core import db
from typing import List, Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class user(db.Model):
    id: Mapped[str] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str]
    password_hash: Mapped[str]
