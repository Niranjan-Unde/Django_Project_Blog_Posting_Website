from django.db import models
from django.contrib.auth.models import User
# from datetime import date

import django.utils


# Create your models here.

class Post(models.Model):

    title=models.CharField(max_length=50)
    sdetail=models.CharField(max_length=70)
    detail=models.CharField(max_length=500)
    cat=models.IntegerField()
    status=models.IntegerField()
    created_on=models.DateField(default=django.utils.timezone.now)      #date.today()
    uid=models.IntegerField()