# Implements several functions to interact with Twitter API through Tweepy, including reading home timeline, posting a status update, getting follower count of a user, and fetching a user's tweets along with their ID.
# https://sites.psu.edu/bigdataebook/chapter3-tutorials/tutorial1/
import tweepy

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def test1():
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)


def test2():
    api.update_status("Sending this via Tweepy :cool:")


def test3():
    abc = api.get_user('abc')
    print(abc.followers_count)


def test4():
    timeline = api.user_timeline('abc')
    for tweet in timeline:
        print('Tweet ID:', tweet.id)
        print('Tweet:', tweet.text)
        print()
