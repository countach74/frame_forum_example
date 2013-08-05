import frame
from models import User
from hashlib import sha1


class Login(frame.Controller):
  def get(self):
    pass

  def post(self, **data):
    pwd_hash = sha1(data['password']).hexdigest()

    user = self.db.query(User).filter_by(
      username=data['username'],
      password=pwd_hash).first()

    if user:
      self.make_session(user)
      self.redirect('/')
    else:
      return self.get_template('login/fail.html').render()

  def make_session(self, user):
    self.session['user'] = {
      'id': user.id,
      'username': user.username,
      'firstname': user.firstname,
      'lastname': user.lastname,
      'email': user.email,
      'groups': map(str, user.groups)
    }
