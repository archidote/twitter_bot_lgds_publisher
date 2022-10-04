import time
from unittest import result 
from assets.articles import select_random_article
from assets.controller import * 
from assets.meme_publisher import * 
from assets.quote_publisher import * 


def bot_retweet () : 
    
   
    search = '#cybersecurity'
    
    maxNumberOfTweets = 1
    
    for tweet in tweepy.Cursor(api.search_tweets, search,  result_type='recent').items(maxNumberOfTweets) :
        try:
            logging.info("I have a tweet from "+tweet.user.screen_name+" with the following"+search+"")

            #Publishing retweet
            tweet.retweet()
            logging.info("I have retweeted a tweet from "+tweet.user.screen_name+"")

        except tweepy.TweepError as e:
            print('Error: ' + e.args[0][0]['message'])
