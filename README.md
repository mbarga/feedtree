This is the beginning of a project to bring visualization to streams from the Feedly news aggregator. I'm a fan of the site newstree.jp which applies a visual tree structure to trending google news articles. I wanted to accomplish the same thing on my personal news feed to gain insights into what I am reading.

The initial goal is to setup a visual tree of trending articles/topics on my feed, and additionally have a basic sentiment analysis feature for each feed category.

To get this software running locally:
- set environment variables PYTHONPATH and FEEDLY_CLIENT_SECRET (check for the most recent secret at https://groups.google.com/forum/#!forum/feedly-cloud)
- default setting looks for mongodb to be installed and running on localhost:27017 (runserver.py will not start if mongodb not running)
- start feely_connect.py
- access localhost:8080/auth and sign in to have the token stored

NOTE: 
feedly has currently announced a version 2.0 of there API which will release soon. The feedly wrapper will most likely break after this release.

