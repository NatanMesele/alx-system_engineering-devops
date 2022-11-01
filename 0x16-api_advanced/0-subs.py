#!/usr/bin/python3
"""
script that queries Reddit API and returns
number of subscribers for a given subreddit.
if invalid, return 0
"""
import json
import requests
import sys

headers = {'User-Agent': 'My User Agent 1.0'}


def number_of_subscribers(subreddit):
    """
    function that returns
    the number of subscribers
    """
    response = requests.get('https://www.reddit.com/r/{}/about.json'.format(
        sys.argv[1]), allow_redirects=False, headers=headers)

    if response.status_code == 200:
        return (response.json()['data']['subscribers'])
    else:
        return 0
