from email.policy import default
from mongoengine import *
from datetime import datetime
import random


class newsina(Document):
    content = StringField(max_length=200, required=False)
    ctime = StringField(max_length=200, required=False)
    url = StringField(max_length=200, required=False)
    wapurl = StringField(max_length=200, required=False)
    title = StringField(max_length=200, required=False)
    media_name = StringField(max_length=200, required=False)
    keywords = StringField(max_length=200, required=False)
    lids = StringField(max_length=200, required=False)
    content = StringField(max_length=200000, required=False)
    runId1 = StringField(max_length=200, required=False)
    id1 = StringField(max_length=200, required=False,default=str(random.random())[2:10])

class user(Document):
    username = StringField(max_length=200, required=False, unique=True)
    name = StringField(max_length=200, required=False)
    keywords = StringField(max_length=200, required=False)
    password = StringField(max_length=200, required=False)
    isAdmin = BooleanField(max_length=200, required=False, default=False)
    time = StringField(max_length=200, required=False, default=str(datetime.now()))
    id1 = StringField(max_length=200, required=False,default=str(random.random())[2:10])

class run(Document):
    username = StringField(max_length=200, required=False)
    type = StringField(max_length=200, required=False)
    count = StringField(max_length=200, required=False)
    time = StringField(max_length=200, required=False, default=str(datetime.now()))
    id1 = StringField(max_length=200, required=False,default=str(random.random())[2:10])
