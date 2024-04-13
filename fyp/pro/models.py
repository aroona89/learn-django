from django.db import models

# Create your models here.

class Category(models.Model):
    CategoryName = models.CharField(max_length=100)
    CategoryDesc = models.CharField(max_length=100)
    CategoryDateTime = models.DateTimeField(auto_now_add=True)
    DateTimeUpdate= models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.CategoryName

class SubCategory(models.Model):
    InheritCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    SubCategoryName = models.CharField(max_length=100)
    SubCategoryDateTime = models.DateTimeField(auto_now_add=True)
    UpdateDateTime = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.SubCategoryName

class State(models.Model):
    StateName = models.CharField(max_length=100)
    StateDesc = models.CharField(max_length=100)
    StateDate = models.DateTimeField(auto_now_add=True)
    StateDateTime = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.StateName


