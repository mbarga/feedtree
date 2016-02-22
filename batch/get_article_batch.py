# -*- coding: UTF-8 -*-

from content_provider import ContentProvider

from settings import db
from collections import Counter
import json
import sys
import time

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DAYS = 7


# get keyword counts from database
def count_keywords(start, end, db):
    keywords_count = Counter()
    for a in db.find({"published": {"$gt": start, "$lt": end}}):
        try:
            if 'keywords' in a:
                for keyword in a['keywords']:
                    keywords_count[keyword] += 1
        except Exception as e:
            logger.error("Could not fetch keyword counts from database: %s" % e.message)
            return None

    return keywords_count

# dump to json file on disk
#dump_json(dict(counter.most_common(20)), "flare.json")
def dump_json(counter, filename):
    my_json = {}
    children = []
    for key in counter:
        item = {}
        item["name"] = key
        item["size"] = counter[key]
        children.append(item)
    my_json["name"] = "News"
    my_json["children"] = children
    with open(filename, 'w') as outfile:
        json.dump(my_json, outfile)


if __name__ == "__main__":
    now = int(time.time())
    start = long(1000 * (now - (DAYS*86400)))
    end = long(1000 * now)
    # print datetime.datetime.fromtimestamp(d/1000).strftime("%Y-%m-%d %H:%M:%S")

    fetcher = ContentProvider()

    # get updated feed subscription categories
    try:
        subscriptions = fetcher.fetch_feeds()
        if "errorMessage" in subscriptions and "token expired" in subscriptions["errorMessage"]:
           fetcher.refresh_token()
           subscriptions = fetcher.fetch_feeds()
        categories = fetcher.fetch_categories()
        categoriesdb = db.categories
        # for category in categories:
            # category_id = categoriesdb.update(key, category, {upsert:true})
            # category_id = categoriesdb.insert_one(category).inserted_id
            # key = {'key':'va`lue'}
            # data = {'key2':'value2', 'key3':'value3'};
            # coll.update(key, data, {upsert:true});

        stream_ids = [s['id'] for s in categories]
    except Exception as e:
        logger.error("Could not fetch content: " + e.message)
        exit(1)

    for category in categories:
        stream_id = category['id']
        continuation_id = None
        article_count = 0
        try:
            while True and article_count < 100:
                chunk = fetcher.fetch_articles(stream_id, start, continuation_id)
                # logger.info("Chunk of %s items" % str(len(chunk)))
                articles = list(chunk['items'])

                # insert articles fetched into database
                if articles:
                    logger.debug("Articles: " + str(articles))
                    articlesdb = db.articles
                    #TODO: hash the ID
                    for article in articles:
                        article['parent_id'] = category['id']
                        article_id = articlesdb.insert_one(article).inserted_id
                        article_count+=1

                if 'continuation' in chunk:
                    continuation_id = chunk['continuation']
                else:
                    break

                logger.info("Pushed %s articles to database" % article_count)

        except Exception as e:
            logger.error("Couldnt fetch articles: %s" % e.message)
            sys.exit()

