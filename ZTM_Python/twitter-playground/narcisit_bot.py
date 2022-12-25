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


search_string = 'Eddy Pagan'
numbers_of_tweets = 1


for tweet in tweepy.Cursor(api.search_tweets, search_string).items(numbers_of_tweets):
    try:
        url = f'https://twitter.com/{tweet.author.screen_name}/status/{tweet.id}'
        api.create_favorite(tweet.id)
        print(f'I liked that tweet: {url}')
        api.retweet(tweet.id)
        print(f'I retweeted: {url}')
    except tweepy.TweepyException as e:
        print(e.reason)
    except StopIteration:
        break

print(f'confirm the likes here: https://twitter.com/{user.screen_name}/likes')
print(f'confirm the retweets here: https://twitter.com/{user.screen_name}')
