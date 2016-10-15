# -*- coding: utf-8 -*-

import tweepy  # https://github.com/tweepy/tweepy
import json
import sys
import config as config

# Twitter API credentials
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_key = config.access_token
access_secret = config.access_secret

audience_set = set()


def write_tweet(tweet, account):
    with open('tweets_' + account + '.json', 'a') as f:
        t = tweet._json
        if not t["text"].startswith("RT @"):
            f.write(json.dumps(t) + "\n")


def write_audience(audience_set, account):
    with open('audience_' + account + '.json', 'a') as f:
        for user in audience_set:
            f.write(str(user) + "\n")


def get_all_tweets(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    for result in tweepy.Cursor(api.user_timeline, screen_name=screen_name, count=200).items():
        write_tweet(result, screen_name)

    # new_tweets = api.user_timeline(screen_name=screen_name, count=200, wait_on_rate_limit=True, wait_on_rate_limit_notify= True)

    # write_tweets(new_tweets, screen_name)

    # oldest = new_tweets[-1].id - 1
    # no_of_tweets = len(new_tweets)

    # while len(new_tweets) > 0:
    #     print("\t getting tweets before %s" % oldest)
    #     new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest, wait_on_rate_limit=True, wait_on_rate_limit_notify= True)
    #     if new_tweets is None or len(new_tweets) == 0:
    #         continue
    #     oldest = new_tweets[-1].id - 1
    #     no_of_tweets += len(new_tweets)
    #     write_tweets(new_tweets, screen_name)
    #     print("\t ...%s tweets downloaded so far" % no_of_tweets)


def get_audience(tweet_id, screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)


    for result in tweepy.Cursor(api.retweeters, id=tweet_id).items():
        audience_set.add(result)
    

    # oldest = new_tweets[-1].id - 1
    # no_of_tweets = len(new_tweets)

    # while len(new_tweets) > 0:
    #     print("\t getting tweets before %s" % oldest)
    #     new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)
    #     if new_tweets is None or len(new_tweets) == 0:
    #         continue
    #     oldest = new_tweets[-1].id - 1
    #     no_of_tweets += len(new_tweets)
    #     write_tweets(new_tweets, screen_name)
    #     print("\t ...%s tweets downloaded so far" % no_of_tweets)


def usage():
    print("Usage :")
    print("""\t python %s @twitter_handle""" % sys.argv[0])

if __name__ == '__main__':
    if len(sys.argv) == 1:
        usage()
        sys.exit()

    account = sys.argv[1]
    account = account.replace("@", "")
    print("Downloading Tweets of %s" % account)
    get_all_tweets(account)
    print("Done")

    with open('tweets_' + account + '.json') as f:
        for line in f:
            tweet = json.loads(line)
            if tweet["retweet_count"] > 0:
                tweet_id = tweet["id"]
                get_audience(tweet_id, account)

    write_audience(audience_set, screen_name)


    # tweet = sys.argv[1]
    # get_audience(tweet, "realmadriden")

        
