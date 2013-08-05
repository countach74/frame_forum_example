from setup_db import *
from controllers import *
import _routes
from tim.orm import make_db_hook
import frame


make_db_hook(Session)

frame.config.templates.environment.update({
  'extensions': ['pyjade.ext.jinja.PyJadeExtension', 'jinja2.ext.do']
})

frame.config.static_map.update({
  '/styles': 'styles',
  '/scripts': 'scripts',
  '/images': 'images'
})

frame.config.templates.extension = '.jade'