from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.LoginPage, name='login'),
    path('signup/', views.User_Signup, name='signup'),
    path('adminpage/', views.Adminpage, name='admin'),
    path('dashboard/', views.DashboardPage, name='dashboard'),
    path('managecomplaint/', views. ManageComplaint, name='managecomplaint'),
    path('manageuser/', views.ManageUser, name='manageuser'),
    path('DeleteUser/<int:id>/', views.DeleteUser, name='DeleteUser'),
    path('addcategory/', views.AddCategory, name='addcategory'),
    path('addsubcategory/', views.AddSubCategory, name='addsubcategory'),
    path('addstate/', views.AddState, name='addstate'),
    path('userloginlog/', views.UserLoginLog, name='userloginlog'),
    path('logoutpage/', views.AdminLogout, name='logoutpage')

]






