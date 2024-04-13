from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/', views.UserDashboard, name='UserDashboard'),
    path('profile/', views.UserProfile, name='UserProfile'),
    path('changepassword/', views.UserCanChangePassword, name='UserCanChangePassword'),
    path('lodgecomplaint/', views.UserLodgeComplaint, name='UserLodgeComplaint'),
    path('complainthistory/', views.UserComplaintHistory, name='UserComplaintHistory'),
    path('update-image', views.update_image, name='update-image'),
]