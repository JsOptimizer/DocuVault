import datetime
import uuid

from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from flaskr.extension.core import db


class User(db.Model):
    id: Mapped[str] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str]
    password_hash: Mapped[str]
    create_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now)
