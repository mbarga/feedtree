# -*- coding: UTF-8 -*-
"""
This file connects to feedly through feedly_client.py to fetch feed and article data
"""

from content import feedly_client

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ContentProvider(object):

    def __init__(self):
        self.feedly = feedly_client

    def refresh_token(self):
        feedly_client.refresh_token()

    def fetch_categories(self):
        '''
        get user's categories
        '''
        try:
            user_categories = self.feedly.get_user_categories(self.feedly.token)
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
            user_subscriptions = self.feedly.get_user_subscriptions(self.feedly.token)
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
                self.feedly.token,
                stream_id,
                newerThan,
                continuation
            )
            return content
        except Exception as e:
            logger.error("Exception fetching articles from stream: " + e.message)
            raise
