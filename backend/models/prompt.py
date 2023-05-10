from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy_json import mutable_json_type

from models.base import Base


class Prompt(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    template = Column(String)
    examples = Column(mutable_json_type(dbtype=JSONB, nested=True))
