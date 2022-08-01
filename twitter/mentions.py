import tweepy
import logging
from config import create_api
import time
import json

def main():
    api = create_api()
    # Replace user ID
    id = "891498964607844352"

    tweets = api.get_users_mentions(id=id, tweet_fields=['context_annotations','created_at','geo','conversation_id'],expansions=['referenced_tweets.id'])
    for tweet in tweets.includes['tweets']:
        print(tweet['text'])
if __name__ == "__main__":
    main()

