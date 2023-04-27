from instagrapi import Client
from instagrapi.types import Usertag , Location
import bot_config

#instagrapi must be installed by running pip install -U instagrapi

#config file must be created berfore executing this code the config.py should contain the following code:
#username = "your_username"
#password = "your_password"

usr = Client()
usr.login(bot_config.username , bot_config.password)
#give it the path for the photo
media = usr.photo_upload(path="/home/zatch/Bots/130clif.jpg" , caption="Hello There")