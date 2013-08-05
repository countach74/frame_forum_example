from sqlalchemy import text, Column, Table, ForeignKey, UniqueConstraint
from sqlalchemy.types import String, Integer, LargeBinary, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.event import listen
from db import Base
from hashlib import sha1
from random import getrandbits
from hashlib import sha1
from tim.orm import regex_validator, BulkUpdate


class Post(Base, BulkUpdate):
  __tablename__ = 'posts'

  id = Column(Integer, primary_key=True)
  topic_id = Column(Integer, ForeignKey('topics.id'))
  author_id = Column(Integer, ForeignKey('users.id'))
  content = Column(String(pow(2,16)), nullable=False)
  votes = Column(Integer, default=0)
