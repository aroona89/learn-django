from django.contrib.auth.models import User
from django.db import models
from pro.models import Category, SubCategory, State
from datetime import datetime

# Create your models here.

class ProfileImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="images")
    date = models.DateTimeField(default=datetime.now)

class ComplaintLodge(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    Type = models.CharField(max_length=100)
    Desc = models.TextField()
    Doc = models.FileField(upload_to="Files")


