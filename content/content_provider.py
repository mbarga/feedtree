# -*- coding: UTF-8 -*-
"""
This file connects to feedly through feedly_client.py to fetch feed and article data
"""

from content import feedly_client, token

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


#def _load_token():
    # get from disk
    # if os.path.isfile(settings.ACCESS_TOKEN_FILE):
    #     with open(settings.ACCESS_TOKEN_FILE) as f:
    #         lines = f.readlines()
    #     access_token = lines[0].strip()
    #     return access_token


class ContentProvider(object):

    def __init__(self):

        self.feedly = feedly_client
        self.access_token = token

    def fetch_categories(self):
        '''
        get user's categories
        '''
        try:
            user_categories = self.feedly.get_user_categories(self.access_token)
            logger.info("Found %s categories: " % str(len(user_categories)))
            return user_categories
        except Exception as e:
            logger.error("Exception fetching user categories: " + e.message)
            raise

    def fetch_feeds(self):
        '''
        get user's subscription list to check for category names
        '''
        try:
            user_subscriptions = self.feedly.get_user_subscriptions(self.access_token)
            logger.info("Subscriptions: %s" % str(len(user_subscriptions)))
            return user_subscriptions
        except Exception as e:
            logger.error("Exception fetching user subscriptions: " + e.message)
            raise

    def fetch_articles(self, stream_id, newerThan, continuation):
        '''
        get content stream for a specific category
        '''
        try:
            content = self.feedly.get_feed_content(
                self.access_token,
                stream_id,
                newerThan,
                continuation
            )
            return content
        except Exception as e:
            logger.error("Exception fetching articles from stream: " + e.message)
            raise
