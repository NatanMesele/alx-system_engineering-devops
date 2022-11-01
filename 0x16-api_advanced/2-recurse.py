#!/usr/bin/python3
"""
script that returns list of all hot articles
for a given subreddit, returns None if invalid
"""
import json
import requests
import sys

headers = {
  'User-Agent': 'My User Agent 1.0'
}
after = None


def recurse(subreddit, hot_list=[]):
    """
    returns hot articles from subreddit
    """
    try:
        url = 'https://www.reddit.com/r/'
        global after
        if after:
            response = requests.get(url + subreddit + "/hot.json?after=" +
                                    after, headers=headers,
                                    allow_redirects=False)
        else:
            response = requests.get(url + subreddit + "/hot.json",
                                    headers=headers, allow_redirects=False)
        after = response.json()['data']['after']
        hot_list += [element['data']['title'] for element in response.
                     json()['data']['children']]
        if after:
            return recurse(subreddit, hot_list)
        return hot_list
    except:
        return None
