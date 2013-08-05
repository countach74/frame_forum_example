import frame
from models import Forum, ForumGroup, Topic, Post


class Topics(frame.Controller):
  def create(self, forum_group_slug, forum_slug, **data):
    # Make a copy of data and use that instead
    
    data = dict(data)
    if 'content' in data:
      content = data['content']
      del(data['content'])
    else:
      raise frame.Error400("Expected 'content' data")
    
    forum = self.db.query(Forum).filter_by(slug=forum_slug).join(
      'forum_group').filter_by(slug=forum_group_slug).first()
    
    if not forum:
      raise frame.Error404
    
    # Inject user_id into data
    data['author_id'] = self.session['user']['id']
    
    topic = Topic(**data)
    topic.forum = forum
    
    post = Post(
      author_id=self.session['user']['id'],
      content=content,
      topic=topic
    )
    
    self.db.add(post)
    self.db.commit()
    
    self.redirect('/forumgroups/%s/forums/%s/topics/%s' % (
      forum.forum_group.slug,
      forum.slug,
      topic.slug)
    )
  
  def show(self, forum_group_slug, forum_slug, slug):
    topic = self.db.query(Topic).filter_by(slug=slug).join('author').join(
      'forum', 'forum_group').filter(Forum.slug==forum_slug,
      ForumGroup.slug==forum_group_slug).first()
    
    if not topic:
      raise frame.Error404
  
    return {'topic': topic, 'author': topic.author}