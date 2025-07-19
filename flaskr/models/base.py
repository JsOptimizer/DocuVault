from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import TIMESTAMP
import datetime


class Base(DeclarativeBase):
    type_annotation_map = {datetime.datetime: TIMESTAMP(timezone=True)}
    pass
