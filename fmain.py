
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'libs'))
from tweets import app


if __name__ == '__main__':
    app.run()
