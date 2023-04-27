import praw
import requests
import os
import shutil
import bot_config

#praw must be installed by running pip install -U praw

#config file must be created berfore executing this code the config.py should contain the following code:
#ID = 'Your_ID'
#Secret = 'Your_Secret'
#Agent = 'Agent_Name'
#can be aquired by singing in as a developer on reddit

reddit = praw.Reddit(client_id =  bot_config.ID, 
                     client_secret= bot_config.Secret ,
                     user_agent= bot_config.Agent)

subreddit_name = 'animemes'
subreddit = reddit.subreddit(subreddit_name)
top_post = subreddit.new(limit = 1)

for post in top_post:
    image_url = post.url
    image_request = request = requests.get(image_url , stream=True)

    with open(f'{post.id}.jpg' , 'wb') as f:
        shutil.copyfileobj(image_request.raw , f)
        print(post.id)