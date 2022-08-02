import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# def check_mentions(api, keywords, since_id):
    # logger.info("Retrieving mentions")
    # new_since_id = since_id
    # for tweet in tweepy.Cursor(api.get_users_mentions,
    #     since_id=since_id).items():
    #     new_since_id = max(tweet.id, new_since_id)
    #     if tweet.in_reply_to_status_id is not None:
    #         continue
    #     if any(keyword in tweet.text.lower() for keyword in keywords):
    #         logger.info(f"Answering to {tweet.user.name}")

    #         if not tweet.user.following:
    #             tweet.user.follow()

    #         api.update_status(
    #             status="Please reach us via DM",
    #             in_reply_to_status_id=tweet.id,
    #         )
    # return new_since_id
# def check_mentions(api, keywords, since_id):
    # logger.info("Retrieving mentions")
    # mentions =api.get_users_mentions
    # mentions.
    # print(api.get_users_mentions)
    

def main():
    api = create_api()
    user=api.get_user
    
    print(user.__str__)
    since_id = 1
    while True:
        since_id = check_mentions(api, ["help", "support"], since_id)
        logger.info("Waiting...")
        time.sleep(60)
    mentions = api.get_users_mentions("@itsuv")
    print(mentions)
if __name__ == "__main__":
    main()