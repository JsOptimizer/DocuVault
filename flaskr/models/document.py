from flaskr.extension.core import db
from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column


class Document(db.Model):
    id: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey('user.id'))
    title: Mapped[str] = mapped_column(String(256))
    file_name: Mapped[str] = mapped_column(Text)
    file_path: Mapped[str] = mapped_column(Text)
