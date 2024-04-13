from django.urls import path
# from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
# from authview.forms import Loginform
from authview import views as myauth_views

urlpatterns = [
    path('', TemplateView.as_view(template_name='authview/home.html'), name='home'),
    path('dashboard/', TemplateView.as_view(template_name='authview/dashboard.html'), name='dashboard'),
    path('login/', myauth_views.MyloginView.as_view(), name='login'),
    path('logout/', myauth_views.MylogoutView.as_view(), name='logout'),
    path('changePassword/', myauth_views.MyPasswordChangeView.as_view(), name='changePassword'),
    path('changePassworddone/', myauth_views.MyPasswordChangeDoneView.as_view(), name='changepassdone'),
]

    # path('login/', auth_views.LoginView.as_view(template_name='authview/login.html', authentication_form=Loginform), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='authview/logout.html'), name='logout'),
    # path('changePassword/', auth_views.PasswordChangeView.as_view(template_name='authview/changePassword.html', success_url='/changePassworddone/'), name='changePassword'),
    # path('changePassworddone/', auth_views.PasswordChangeDoneView.as_view(template_name='authview/changepassdone.html'), name='changepassdone'),
