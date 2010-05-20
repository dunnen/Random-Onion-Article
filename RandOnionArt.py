#!/usr/bin/python

import feedparser
import random

onion_url = "http://feeds.theonion.com/onionnewsnetwork"

feed = feedparser.parse( onion_url )

entries = []
entries.extend(feed["items"])

random_article = random.randint(0, len(entries)-1)

print entries[random_article]["title"]
