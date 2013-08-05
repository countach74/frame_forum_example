from sqlalchemy import text, Column, Table, ForeignKey, UniqueConstraint
from sqlalchemy.types import String, Integer, LargeBinary, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.event import listen
from db import Base
from hashlib import sha1
from random import getrandbits
from hashlib import sha1
from tim.orm import regex_validator, BulkUpdate


users_groups = Table('users_groups', Base.metadata,
  Column('user_id', Integer, ForeignKey('users.id')),
  Column('group_id', Integer, ForeignKey('groups.id')),
  UniqueConstraint('user_id', 'group_id'),
  mysql_engine='InnoDB')


class User(Base, BulkUpdate):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True)
  username = Column(String(50), nullable=False, unique=True)
  firstname = Column(String(50), nullable=False)
  lastname = Column(String(50), nullable=False)
  email = Column(String(100), nullable=False)
  password = Column(String(100), nullable=False)
  confirmation_code = Column(String(100), nullable=True)

  # Relationships
  groups = relationship('Group', secondary=users_groups, backref='users')
  topics = relationship('Topic', backref='author')
  posts = relationship('Post', backref='author')

  def __init__(self, data={}, create_confirmation=True, **kwargs):
    if create_confirmation:
      self.confirmation_code = self.make_confirmation()
    BulkUpdate.__init__(self, data, **kwargs)

  @staticmethod
  def hash_password(target, value, oldvalue, initiator):
    return sha1(value).hexdigest()

  @staticmethod
  def make_confirmation(num_bits=256):
    return '%02x' % getrandbits(num_bits)


listen(User.password, 'set', User.hash_password, retval=True)
listen(User.username, 'set', regex_validator('a-zA-Z0-9\-\._'))
