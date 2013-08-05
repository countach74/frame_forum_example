from sqlalchemy import text, Column, Table, ForeignKey, UniqueConstraint
from sqlalchemy.types import String, Integer, LargeBinary, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.event import listen
from db import Base
from hashlib import sha1
from random import getrandbits
from hashlib import sha1
from tim.orm import regex_validator, BulkUpdate, make_slug


class Topic(Base):
  __tablename__ = 'topics'

  id = Column(Integer, primary_key=True)
  forum_id = Column(Integer, ForeignKey('forums.id'))
  title = Column(String(255), nullable=False)
  slug = Column(String(255), unique=True, nullable=False)
  author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
  views = Column(Integer, default=0)

  # Relationships
  posts = relationship('Post', backref='topic')
  

listen(Topic.title, 'set', regex_validator('a-zA-Z0-9_\-\., '))
listen(Topic.title, 'set', make_slug())