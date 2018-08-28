from werkzeug.wsgi import DispatcherMiddleware
from forum_app import application as forum
from hina_app import application as front_main

application = DispatcherMiddleware(front_main, {
    '/forum':     forum
})