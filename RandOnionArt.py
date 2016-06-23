#!/usr/bin/python3

import feedparser
import random

onion_url = 'http://www.theonion.com/feeds/rss'

feed = feedparser.parse( onion_url )

items = feed['items']

random_article = random.randint(0, len(items)-1)

print(items[random_article]["title"])

