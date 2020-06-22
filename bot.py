#Shitty Twitter Lyric Bot
#By Napuc

import tweepy
import random
import time

#For Timestamping actions
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

# Authenticate to Twitter
auth = tweepy.OAuthHandler("[API KEY]",
    "[SECRET API KEY]")
auth.set_access_token("[ACCESS TOKEN]",
    "[ACCESS TOKEN SECRET]")

#Authentication status messages
api = tweepy.API(auth)
try:
    api.verify_credentials()
    print(f"{current_time}: Authentication Sucess!")
except:
    print(f"{current_time}: Something fucked up during authentication!")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

#Find phrase from .txt file and tweet it
with open("tweets.txt", "r") as f:
            data = f.readlines()
            while True:
                line = random.choice(data)
                line = line.replace("~", "\n")
                api.update_status(line)
                for tweet in tweepy.Cursor(api.home_timeline).items(1):
                    print(f"At {current_time}: {tweet.user.name} tweeted: {tweet.text}")
                time.sleep(30*60)