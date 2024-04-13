from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import SignupForm, UserProfileForm, AdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.

# Signup View Function
def sign_up(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully!!!')
            fm.save()
            return HttpResponseRedirect('/login/')
    else:
        fm = SignupForm()
    return render(request, 'authapp/signup.html', {'form': fm})

# Login View Function
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully!!!')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'authapp/userlogin.html', {'form': fm})
    else:
        return HttpResponseRedirect('/profile/')


# Profile
def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = AdminProfileForm(request.POST, instance= request.user)
            else:
                fm = UserProfileForm(request.POST, instance= request.user)
            if fm.is_valid():
                messages.success(request, 'Profile Updated Successfully!!!')
                fm.save()
        else:    
            if request.user.is_superuser == True:
                fm = AdminProfileForm(instance=request.user)
            else:
                fm = UserProfileForm(instance=request.user)
        return render(request, 'authapp/profile.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')


# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

# Change Password with Old Password
def user_changePassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password Changed Successfully!!!')
                return HttpResponseRedirect('/profile/')
                # return HttpResponseRedirect('/login/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'authapp/changePassword.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')
    
# Change Password without Old Password
def user_forgetPassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password Reset Successfully!!!')
                return HttpResponseRedirect('/profile/')
                # return HttpResponseRedirect('/login/')
        else:
            fm = SetPasswordForm(user=request.user)
        return render(request, 'authapp/forgetPassword.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')
    