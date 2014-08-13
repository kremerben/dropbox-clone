from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Media(models.Model):
    owner = models.ForeignKey(User, related_name='owner')
    filename = models.CharField(max_length=120)
    file = models.FileField(upload_to='uploads')
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.filename

