from frame import routes


routes.connect('/', 'root#index')

routes.resource('forumgroups')
routes.resource('forums', '/forumgroups/{forum_group_slug}/forums')
routes.resource('users')
routes.resource('topics', '/forumgroups/{forum_group_slug}/forums/{forum_slug}/topics')

routes.connect('/login', 'login#get', conditions={'method': ['GET']})
routes.connect('/login', 'login#post', conditions={'method': ['POST']})

routes.connect('/forumgroups/{slug}/new_forum', 'forumgroups#new_forum')