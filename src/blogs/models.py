from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    # auto_now=True, auto_now_add=False means everytime it get updated or edited it saves the time
    postupdate = models.DateTimeField(auto_now=True, auto_now_add=False)
    # auto_now=False, auto_now_add=True means it only saves time when it was added to the database
    posttime = models.DateTimeField(auto_now=False, auto_now_add=True)

    # For python2
    def __unicode__(self):
        return self.title

    # For python3
    def __str__(self):
        return self.title
