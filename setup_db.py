#!/usr/bin/env python

from models import *
from db import Base, Session, engine


def drop():
  Base.metadata.drop_all(engine)


def setup():
  Base.metadata.create_all(engine)

def make_test_data():
  s = Session()

  admin_group = Group(name='admin')
  users_group = Group(name='users')

  admin = User(
    username='countach74',
    password='12thfret',
    email='countach74@gmail.com',
    firstname='Tim',
    lastname='Radke')

  admin.groups.extend([admin_group, users_group])

  s.add(admin)

  groups = []

  for i in xrange(1,6):
    fg = ForumGroup(name='Forum Group %s' % i, position=i)
    s.add(fg)
    groups.append(fg)

  first_group = groups[0]

  for i in xrange(1, 6):
    f = Forum(name='Test Forum %s' % i, position=i)
    f.forum_group = first_group
    s.add(f)

  s.commit()
