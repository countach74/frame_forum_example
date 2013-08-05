from sqlalchemy import text, Column, Table, ForeignKey, UniqueConstraint
from sqlalchemy.types import String, Integer, LargeBinary, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.event import listen
from db import Base
from hashlib import sha1
from random import getrandbits
from hashlib import sha1
from tim.orm import regex_validator, BulkUpdate, make_slug


class ForumGroup(Base):
  __tablename__ = 'forumgroups'

  id = Column(Integer, primary_key=True)
  name = Column(String(255), unique=True)
  slug = Column(String(255), unique=True)
  position = Column(Integer, unique=True)

  # Relationships
  forums = relationship('Forum', backref='forum_group')


listen(ForumGroup.name, 'set', regex_validator('a-zA-Z0-9_\-\., '))
listen(ForumGroup.name, 'set', make_slug())