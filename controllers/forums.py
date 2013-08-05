import frame
from models import ForumGroup, Forum


class Forums(frame.Controller):
  def index(self, forum_group_slug):
    forum_groups = self.db.query(ForumGroup).filter_by(
      slug=forum_group_slug).outerjoin("forums").all()
      
    return {'forum_groups': forum_groups}

  def show(self, forum_group_slug, slug):
    forum = self.db.query(Forum).filter_by(slug=slug).outerjoin(
      'forum_group').filter_by(slug=forum_group_slug).outerjoin('topics')
      
    print forum
    forum = forum.first()
      
    print forum_group_slug, slug
    
    if not forum:
      raise frame.Error404

    return {'forum': forum}
    
  def new(self, forum_group_slug):
    forum_group = self.db.query(ForumGroup).filter_by(slug=forum_group_slug).first()
    
    if not forum_group:
      raise frame.Error404
    
    return {'forum_group': forum_group}

  def create(self, forum_group_slug, **data):
    forum_group = self.db.query(ForumGroup).filter_by(slug=forum_group_slug).first()
    
    if not forum_group:
      raise frame.Error404
    
    forum = Forum(**data)
    forum.forum_group = forum_group
    
    self.db.add(forum)
    self.db.commit()
    
    self.redirect('/')