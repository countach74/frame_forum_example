import frame
from models import ForumGroup, Forum


class Root(frame.Controller):
  def index(self):
    forum_groups = self.db.query(ForumGroup).outerjoin(Forum).all()
    
    return {'forum_groups': forum_groups}