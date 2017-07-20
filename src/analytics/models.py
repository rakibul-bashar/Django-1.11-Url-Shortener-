# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from shortener.models import RakibbUrl
# Create your models here.
class ClickEventManager(models.Manager):
    def create_event(self,Rakibbinstance):
        if isinstance(Rakibbinstance,RakibbUrl):
            obj,created=self.get_or_create(rakibb_url=Rakibbinstance)
            obj.count+=1
            obj.save()
            return obj.count
        return None
class ClickEvent(models.Model):
    rakibb_url=models.OneToOneField(RakibbUrl)
    count=models.IntegerField(default=0)
    updated=models.DateTimeField(auto_now=True)#everytime the model is saved
    timestamp=models.DateTimeField(auto_now_add=True)#when model is created
    objects=ClickEventManager()
    def __str__(self):
        return "{i}".format(i=self.count)
