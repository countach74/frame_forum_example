from sqlalchemy import text, Column, Table, ForeignKey, UniqueConstraint
from sqlalchemy.types import String, Integer, LargeBinary, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.event import listen
from db import Base
from hashlib import sha1
from random import getrandbits
from hashlib import sha1
from tim.orm import regex_validator, BulkUpdate, make_slug


moderators = Table('moderators', Base.metadata,
  Column('user_id', Integer, ForeignKey('users.id')),
  Column('forum_id', Integer, ForeignKey('forums.id')),
  UniqueConstraint('user_id', 'forum_id'),
  mysql_engine = 'InnoDB')


class Forum(Base, BulkUpdate):
  __tablename__ = 'forums'
  __table_args__ = (
    UniqueConstraint('forum_group_id', 'position'),
    dict(Base.__table_args__)
  )

  id = Column(Integer, primary_key=True)
  name = Column(String(255), unique=True)
  slug = Column(String(255), unique=True)
  forum_group_id = Column(Integer, ForeignKey('forumgroups.id'))
  position = Column(Integer)

  # Relationships
  topics = relationship('Topic', backref='forum')
  moderators = relationship('User', secondary=moderators, backref='forums_moderating')


listen(Forum.name, 'set', regex_validator('a-zA-Z0-9_\-\. '))
listen(Forum.name, 'set', make_slug())
