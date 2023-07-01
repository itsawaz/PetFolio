import pytz
import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

import pytz
from django.utils import timezone

import pytz
import datetime
from django.db import models
from django.contrib.auth.models import User
from signup.models import Peto
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_type = models.CharField(max_length=50, default='')
    def __str__(self):
        return self.title
