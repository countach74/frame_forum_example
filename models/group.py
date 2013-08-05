from sqlalchemy import text, Column, Table, ForeignKey, UniqueConstraint
from sqlalchemy.types import String, Integer, LargeBinary, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.event import listen
from db import Base
from hashlib import sha1
from random import getrandbits
from hashlib import sha1
from tim.orm import regex_validator, BulkUpdate


class Group(Base):
  __tablename__ = 'groups'

  id = Column(Integer, primary_key=True)
  name = Column(String(20), nullable=False, unique=True)

  def __str__(self):
    return self.name

  def __eq__(self, other):
    if (isinstance(other, Group)):
      return self.name == other.name
    else:
      return self.name == other


listen(Group.name, 'set', regex_validator('a-zA-Z0-9\_\-\.'))
