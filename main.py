from google.appengine.ext.webapp.util import run_wsgi_app
from tweets import app

run_wsgi_app(app)
