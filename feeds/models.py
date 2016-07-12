from __future__ import unicode_literals
import datetime
from django.db import models
from django.contrib.auth.models import User
from markdown import markdown
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=500,help_text='Maximum 250 characters')
    description = models.TextField()
    slug = models.SlugField(unique=True,help_text="Suggested value automatically generated from title.Must be unique")

    def get_absolute_url(self):
        return "/categories/%s/" %self.slug

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural='Categories'
        ordering=['title']

class Entry(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = ((LIVE_STATUS, 'Live'),(DRAFT_STATUS, 'Draft'),(HIDDEN_STATUS, 'Hidden'),)
    #core fields
    title=models.CharField(max_length=250)
    excerpt=models.TextField(blank=True,help_text="A short summary of the Entry. Optional.")
    body=models.TextField()
    pub_date=models.DateTimeField(default=datetime.datetime.now)


    #metadata
    author=models.ForeignKey(User)
    enable_comments=models.BooleanField(default=True)
    featured=models.BooleanField(default=False)
    slug=models.SlugField(unique_for_date='pub_date', help_text="Suggested value automatically generated from title.Must be unique.")
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS,help_text="Only entries with live status will be publicly displayed")

    # Categorization.
    category = models.ManyToManyField(Category)


   #to store generated hmtl
    excerpt_html = models.TextField(editable=False, blank=True)
    body_html = models.TextField(editable=False, blank=True)

    class Meta:
        verbose_name_plural="Entries"
        ordering=['-pub_date']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/weblog/%s/%s/" %(self.pub_date.strftime("%Y/%b/%d").lower(),self.slug)

    def save(self, force_insert=False, force_update=False):
        self.body_html = markdown(self.body)
        if self.excerpt:
            self.excerpt_html = markdown(self.excerpt)
            super(Entry, self).save(force_insert, force_update)
















