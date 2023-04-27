import praw
import requests
import shutil
import os
from instagrapi import Client
from instagrapi.types import Usertag , Location
import bot_config

#praw , instagrapi must be installed by running pip install -U "either"

#config file must be created berfore executing this code the config.py should contain the following code:
#username = "your_username"
#password = "your_password"
#Secret = 'Your_Secret'
#Agent = 'Agent_Name'
#can be aquired by singing in as a developer on reddit

 
reddit = praw.Reddit(client_id =  bot_config.ID, 
                     client_secret= bot_config.Secret ,
                     user_agent= bot_config.Agent)

usr = Client()
usr.login(bot_config.username , bot_config.password)

subreddit_name = 'animemes'
subreddit = reddit.subreddit(subreddit_name)
top_post = subreddit.new(limit=1)

for post in top_post:
    image_url = post.url
    image_request = request = requests.get(image_url , stream=True)

    with open(f'{post.id}.jpg' , 'wb') as f:
        shutil.copyfileobj(image_request.raw , f)
        print(post.id)
        p = post.id
        ThePath = "/home/zatch/Bots/" + p + ".jpg"
        print(ThePath)
        media = usr.photo_upload(path=ThePath, caption="#yanime #animemes #funnyanimememes#dankanimememes #animememes4u#memesanime#animeme #anime_kawaii #anime #animetattoo #animeinstagram #animescenes#animejapan#animefanart #animepage #anime4life#weebmemes #weeboo #megumin #otakuart#otakuanime \n #otaku_crew #animekawai#animequote #animefunny #funnyanime #chikafujiwara")

        os.remove(post.id)