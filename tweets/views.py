from tweets import app
#from models import Post
from flask import render_template
from flask import session, url_for, request, redirect, flash



from flaskext.oauth import OAuth



#app.secret_key = SECRET_KEY
oauth = OAuth()

# Use Twitter as example remote application
twitter = oauth.remote_app('twitter',
    # unless absolute urls are used to make requests, this will be added
    # before all URLs. This is also true for request_token_url and others.
    base_url='http://api.twitter.com/1/',
    # where flask should look for new request tokens
    request_token_url='http://api.twitter.com/oauth/request_token',
    # where flask should exchange the token with the remote application
    access_token_url='http://api.twitter.com/oauth/access_token',
    # twitter knows two authorizatiom URLs. /authorize and /authenticate.
    # they mostly work the same, but for sign on /authenticate is
    # expected because this will give the user a slightly different
    # user interface on the twitter side.
    authorize_url='http://api.twitter.com/oauth/authenticate',
    # the consumer keys from the twitter application registry.
    consumer_key='F2Nw0Y0UiDuZyycYdfht9w',
    consumer_secret='6HKS7GBCmM21l28OmdStRryiO4ATkQYvP8bdFj0s'
)





@app.route('/posts')
def list_posts():
    #posts = Post.all()
    class Tmp:
        pass
    t = Tmp()
    a = Tmp()
    a.nickname = lambda :"jas"
    t.author = a
    t.title = "wat"
    t.content = "nothing"
    
    return render_template('list_posts.html', posts=[t])


# @app.route('/')
# def hello_world():
#     #oauth = oauth.OAuth()
#     return 'Hello World from flask'




@twitter.tokengetter
def get_twitter_token():
    if 'twitter_user' in session and session['twitter_user'] is not None:
        return session.get('twitter_token')




@app.route('/')
def index():
    # tweets = None
    # if g.user is not None:
    #     resp = twitter.get('statuses/home_timeline.json')
    #     if resp.status == 200:
    #         tweets = resp.data
    #     else:
    #         flash('Unable to load tweets from Twitter. Maybe out of '
    #               'API calls or Twitter is overloaded.')
    # return render_template('index.html', tweets=tweets)
    return redirect(url_for('timeline'))



@app.route('/login')
def login():
    return twitter.authorize(callback=url_for('oauth_authorized',
        next=request.args.get('next') or request.referrer or None))


@app.route('/logout')
def logout():
    session.pop('twitter_user', None)
    flash('You were signed out')
    return redirect(request.referrer or url_for('index'))


@app.route('/twitter_back')
@twitter.authorized_handler
def oauth_authorized(resp):
    next_url = request.args.get('next') or url_for('index')
    if resp is None:
        flash(u'You denied the request to sign in.')
        return redirect(next_url)

    session['twitter_token'] = (
        resp['oauth_token'],
        resp['oauth_token_secret']
    )
    session['twitter_user'] = resp['screen_name']

    flash('You were signed in as %s' % resp['screen_name'])
    return redirect(next_url)



@app.route('/timeline')
def timeline():

    tweets = None
    if 'twitter_user' in session and session['twitter_user'] is not None:

        resp = twitter.get('statuses/home_timeline.json')
        if resp.status == 200:
            tweets = resp.data

        else:
            tweets = None
            flash('Unable to load tweets from Twitter. Maybe out of '
                  'API calls or Twitter is overloaded.')
            #return 'failure %d' % resp.status


    return render_template('timeline.html', tweets=tweets)

