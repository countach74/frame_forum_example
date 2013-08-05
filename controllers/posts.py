import frame
from models import Post, Topic, Forum, ForumGroup


class Posts(frame.Controller):
  def create(self, forum_group_slug, forum_slug, topic_slug, **data):
    print 'Posts.create()'
    
    topic = self.db.query(Topic).join('forum', 'forum_group').filter(
      ForumGroup.slug==forum_group_slug,
      Forum.slug==forum_slug,
      Topic.slug==topic_slug).first()
    
    if not topic:
      raise frame.Error404
    
    post = Post(
      content=data['content'],
      author_id=self.session['user']['id'],
      topic_id=topic.id)
    
    self.db.add(post)
    self.db.commit()
    
    self.redirect('/forumgroups/%s/forums/%s/topics/%s' % (
      forum_group_slug, forum_slug, topic_slug))