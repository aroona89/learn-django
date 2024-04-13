from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import ChangeUserPassForm, UserEditForm, ProfileForm, AdminProfileForm
from pro.models import Category, SubCategory, State
from .models import ComplaintLodge
from .forms import fileform, UserLodgeComplaintForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ProfileImage

# Create your views here.

@login_required
def UserDashboard(request):
    return render(request, 'UserDashboard.html', {'name':request.user})

@login_required
def UserProfile(request):
    if request.user.is_authenticated:
       if request.method == 'POST':
            fm = UserEditForm(request.POST, instance= request.user)
            if fm.is_valid():
                messages.success(request, 'Profile Updated Successfully!!!')
                fm.save()
       else:    
           fm = UserEditForm(instance=request.user)
       return render(request, 'UserProfile.html', {'form':fm})
    else:
        return redirect("login")
    
    #     form = UserEditForm(request.POST, instance=request.user)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('UserProfile')
    # else:
    #     form = UserEditForm(instance=request.user)

    # if request.method == 'POST':
    #     photo = ProfileForm(request.POST, request.FILES)
    #     if photo.is_valid():
    #         photo.save()
    # else:
    #     photo = ProfileForm()
    # return render(request, 'UserProfile.html', {'form':form, 'name':request.user,
    #                                             'photo':photo})

@login_required
def UserCanChangePassword(request):
    if request.method == 'POST':
        form = ChangeUserPassForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ChangeUserPassForm(user=request.user)
    return render(request, 'UserCanChangePassword.html', {'form':form, 'name':request.user})


# def UserLodgeComplain(request):
#
#         return render(request, 'UserLodgeComplain.html')

@login_required
def UserLodgeComplaint(request):
    if request.method == 'POST':
        form = UserLodgeComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = UserLodgeComplaintForm()
    else:
        form = UserLodgeComplaintForm()

    # Fetch available choices for select fields and pass them to the template context
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    departments = State.objects.all()
    return render(request, 'UserLodgeComplaint.html', {'form':form, 'name':request.user, 
                                                       'categories': categories, 
                                                       'subcategories': subcategories,
                                                        'departments' : departments})

@login_required
def UserComplaintHistory(request):
    return render(request, 'UserComplaintHistory.html')

@login_required
def update_image(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
          form.save()
    else:
       form = ProfileForm()
    img = ProfileImage.objects.all()
    return render(request, 'update-image.html', {'img':img, 'form':form})
