from django.db import models


# Create your models here.
class SocialNetwork(models.Model):
    user_name = models.CharField(max_length=30)
    social_network_link = models.CharField(max_length=30)
