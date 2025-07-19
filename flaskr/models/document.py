from ..extension.core import db
from typing import List, Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class document(db.Model):
    id: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey('user.id'))
    title: Mapped[str]
    file_name: Mapped[str]
    file_path: Mapped[str]
