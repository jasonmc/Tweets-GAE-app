from google.appengine.ext.webapp.util import run_wsgi_app
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'libs'))
from tweets import app

run_wsgi_app(app)
