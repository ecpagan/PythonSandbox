import tweepy
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)
user = api.get_user(screen_name='ecpagan')
client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret,
                       access_token=access_token, access_token_secret=access_token_secret)


def limit_handle(cursor):
    try:
        while True:
            try:
                yield cursor.next()
            except StopIteration:
                return
    except tweepy.errors.TooManyRequests:
        time.sleep(1)  # wait 1 second


for follower in limit_handle(tweepy.Cursor(api.get_followers).items()):
    print(follower.name)
    if follower.screen_name == 'ZaichaB':
        client.follow_user(target_user_id=follower.id, user_auth=True)
        follower.following = True
        print(f'\tnow following {follower.name}')
