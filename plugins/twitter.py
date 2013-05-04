import oauth2
import json
import urllib

import plugins.constants as plugins_constants

def get_oauth_client():
    consumer = oauth2.Consumer(plugins_constants.TWITTER_CONSUMER_KEY, plugins_constants.TWITTER_CONSUMER_SECRET)
    token = oauth2.Token(plugins_constants.TWITTER_TOKEN, plugins_constants.TWITTER_TOKEN_SECRET)

    return oauth2.Client(consumer, token)

"""
Given a term to search on, return the most recent tweets based on that term.
"""
def get_tweets_by_term(term):
    endpoint = 'https://api.twitter.com/1.1/search/tweets.json?q=%s' % urllib.quote(term)

    client = get_oauth_client()
    
    headers, content = client.request(endpoint)

    return json.loads(content)

""" 
Given a twitter handle, returns the most recent tweets by that user.  
""" 
def get_tweets_by_user(handle):
    endpoint = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=%s' % urllib.quote(handle)

    client = get_oauth_client()

    headers, content = client.request(endpoint)

    return json.loads(content)

def main():
    return 1

if __name__ == '__main__':
    main()
