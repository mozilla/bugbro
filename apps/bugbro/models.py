from django.db import models
from django.contrib.auth.models import User


class ReviewJob(models.Model):
    name = models.CharField(max_length=30)
    reviewer = models.ForeignKey(User, related_name='reviewer')
    reviewee = models.ForeignKey(User, related_name='reviewee')
    url = models.URLField()
    description = models.TextField()
    comment = models.TextField()



