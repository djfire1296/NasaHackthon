#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 14:29:06 2017

@author: moon
"""

from api_key import *    
from twython import Twython

#print TWITTER_APP_KEY

t = Twython(app_key=TWITTER_APP_KEY, 
            app_secret=TWITTER_APP_KEY_SECRET, 
            oauth_token=TWITTER_ACCESS_TOKEN, 
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

search = t.search(q = '#wtf', count = 10)

tweets = search['statuses']

for tweet in tweets:
    print tweet['id_str'],'\n', tweet['text'], '\n\n'