from django.contrib import admin
from .models import Category, SubCategory, State

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'CategoryName', 'CategoryDesc', 'CategoryDateTime', 'DateTimeUpdate']

@admin.register(SubCategory)
class SubCategoryModel(admin.ModelAdmin):
    list_display = ['id','InheritCategory', 'SubCategoryName', 'SubCategoryDateTime', 'UpdateDateTime']

@admin.register(State)
class StateModel(admin.ModelAdmin):
    list_display = ['id', 'StateName', 'StateDesc', 'StateDate', 'StateDateTime']
