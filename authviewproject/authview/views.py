from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from authview.forms import Loginform
# Create your views here.

class MyloginView(LoginView):
    template_name='authview/login.html'
    authentication_form=Loginform

class MylogoutView(LogoutView):
    template_name='authview/logout.html'

class MyPasswordChangeView(PasswordChangeView):
    template_name='authview/changePassword.html'
    success_url='/changePassworddone/'

class MyPasswordChangeDoneView(PasswordChangeDoneView):
    template_name='authview/changepassdone.html'