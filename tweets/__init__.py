from flask import Flask
import settings

app = Flask('tweets')
app.config.from_object('tweets.settings')

import views
