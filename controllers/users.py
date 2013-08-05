import frame
from models import User


class Users(frame.Controller):
  def index(self):
    users = self.db.query(User).all()
    return {'users': users}
    
  def new(self):
    pass

  def show(self, slug):
    user = self.db.query(User).filter_by(username=slug).first()

    if not user:
      raise frame.Error404

    return {'user': user}

  def create(self, **kwargs):
    data = dict(kwargs)

    user = User(**data)

    self.db.add(user)
    self.db.commit()

    return {'user': user}

  def edit(self, slug):
    user = self.db.query(User).filter_by(username=slug).first()

    if not user:
      raise frame.Error404

    return {'user': user}

  def update(self, slug, **data):
    self.db.query(User).filter_by(username=slug).update(data)
    self.db.commit()
    self.redirect('/users/' + slug)