from __future__ import unicode_literals

from django.db import models

from mongoengine import connect, Document, StringField, DateTimeField

# Create your models here.
from blongo.settings import DBNAME

connect(DBNAME)

class Post(Document):
    title = StringField(max_length=120, required=True)
    content = StringField(max_length=500, required=True)
    last_update = DateTimeField(required=True)
