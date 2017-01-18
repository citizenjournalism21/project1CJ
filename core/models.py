from __future__ import unicode_literals

from django.db import models

# Create your models here.
from mongoengine import *


class Poll(Document):
    question = StringField(max_length=200)
    pub_date = DateTimeField(help_text='date published')
    #choices = ListField(EmbeddedDocumentField(Choice))

