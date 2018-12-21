import tweepy
import numpy as np

from secrets import *
from GarfieldChain2 import *

#initialize Markov library
tabby = open('garfield.txt', encoding='utf8').read()
corpus = tabby.split()

#create OAuthHandle instance
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

#Shows bot is running
print("running...")
    
def tweet_nonsense(username,status_id):
    #generates a comic, then tweets a replay and the same comic on the bot's profile
    nonsense = stripGen(3,corpus)
    api.update_status(status="@{}{}".format(username,nonsense), in_reply_to_status_id=status_id)
    api.update_status(status=nonsense)
    
#create class inheriting from tweepy StreamListener
class BotStreamer(tweepy.StreamListener):
    #Called when a new status arrives which is passed down from the on_data method of StreamListener
    def on_status(self, status):
        username = status.user.screen_name
        status_id = status.id
        tweet_nonsense(username,status_id)
        print("tweet sent!")
        
#stream initializing  
myStreamListener = BotStreamer()
myStream = tweepy.Stream(auth, myStreamListener)
myStream.filter(track=['@GarfieldMarkov'])