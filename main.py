import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'libs'))
from tweets import app


try:
    from google.appengine.ext.webapp.util import run_wsgi_app
except:
    if __name__ == '__main__':
        app.run()
else:
    run_wsgi_app(app)
