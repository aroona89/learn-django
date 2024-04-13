from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm,\
    PasswordChangeForm,  AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Category, SubCategory, State
from .forms import SignupForm, LoginForm, ChangePassForm, ChangeAdminPassForm,\
    CategoryForm, SubCategoryForm, StateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User

# Create your views here.

def Home(request):
    return render(request, 'home.html')

def User_Signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if  form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully!!!")
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form':form})

def LoginPage(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/user/dashboard/')
    else:
        form = LoginForm()
    #change password
    if request.method == 'POST':
        fm = ChangePassForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = ChangePassForm(user=request.user)
    return render(request, 'login.html', {'form': form, 'fm':fm})


#Adminpage
def Adminpage(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/log/managecomplaint/')
    else:
        form = LoginForm()
    return render(request, 'adminpage.html', {'form':form})


def DashboardPage(request):
    if request.user.is_superuser == False:
        return render(request, 'dashboard.html')
    else:
        return HttpResponseRedirect('/log/login/')

def  ManageComplaint(request):
    if request.user.is_superuser == True:
        if request.method == 'POST':
            form = ChangeAdminPassForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
        else:
            form = ChangeAdminPassForm(user=request.user)
        return render(request, 'admin1.html', {'form':form})
    else:
        return HttpResponseRedirect('/log/login/')

def ManageUser(request):
    users = User.objects.all()
    form = UserChangeForm(instance=request.user)
    return render(request, 'manageuser.html', {'form':form, 'users':users})

def DeleteUser(request, id):
    if request.method == 'POST':
        obj = User.objects.get(pk=id)
        obj.delete()
    return HttpResponseRedirect('/log/manageuser/')

def AddCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            form = CategoryForm()
    else:
        form = CategoryForm()
    model = Category.objects.all()
    return render(request, 'addcategory.html', {'form':form, 'model':model})

def AddSubCategory(request):
    if request.method == 'POST':
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            form = SubCategoryForm()
    else:
        form = SubCategoryForm()
    model = SubCategory.objects.all()
    return render(request, 'addsubcategory.html', {'form':form, 'subcategory':model})


def AddState(request):
    if request.method == 'POST':
        form = StateForm(request.POST)
        if form.is_valid():
            form.save()
            form = StateForm()
    else:
        form = StateForm()
    model = State.objects.all()
    return render(request, 'addstate.html', {'form':form, 'model':model})

def UserLoginLog(request):
    return render(request, 'userloginlog.html')


def AdminLogout(request):
    logout(request)
    return HttpResponseRedirect('/log/adminpage/')




