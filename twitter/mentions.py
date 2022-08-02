import tweepy
from config import create_api
import time
import json

def main():
    api = create_api()
    since_id=1
    # Replace user ID
    id = "891498964607844352"
    while True:
        # print(since_id)
        since_id = check_mentions(api,id,since_id)
        time.sleep(20)

def find_duplicates():
    pass

def reply_to_mention():
    pass

def check_mentions(api,id,sinceid):
    new_since_id = sinceid
    
    tweets = api.get_users_mentions(id=id,expansions=['referenced_tweets.id'],since_id=sinceid)
    if(len(tweets.includes)>0):
        for tweet in tweets.includes['tweets']:
            root_tweet_text=tweet['text']
            root_tweet_id = tweet['id'] 
        # print(str(root_tweet_id) +"::"+root_tweet_text)
        new_since_ids = []
        for tweet in tweets.data:
            new_since_ids.append(tweet.id)
        new_since_id = max(new_since_ids)
    print(new_since_id)
    return new_since_id
    


if __name__ == "__main__":
    main()

