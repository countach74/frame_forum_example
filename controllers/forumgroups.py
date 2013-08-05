import frame
from models import ForumGroup


class ForumGroups(frame.Controller):
  def new(self):
    pass

  def create(self, **kwargs):
    data = dict(kwargs)

    forum_group = ForumGroup(**data)

    self.db.add(forum_group)
    self.db.commit()

    self.redirect('/')