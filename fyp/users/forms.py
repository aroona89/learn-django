from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,\
    UsernameField, SetPasswordForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User
from .models import ProfileImage, ComplaintLodge


class ChangeUserPassForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password:',
                                    widget=forms.PasswordInput(attrs=
                                    {'placeholder':'Old Password',
                                     'class':'form-control'})
                                   )
    new_password1 = forms.CharField(label='New Password:',
                                   widget=forms.PasswordInput(attrs=
                                    {'placeholder':'New Password',
                                     'class':'form-control'})
                                    )
    new_password2 = forms.CharField(label='Confirm Password:',
                                    widget=forms.PasswordInput(attrs=
                                    {'placeholder':'confirm New Password',
                                     'class':'form-control'})
                                    )

class UserEditForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email'}

class AdminProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'
        labels = {'email': 'Email'}


class ProfileForm(forms.ModelForm):
    class Meta:
        model= ProfileImage
        fields = '__all__'
        labels = {'image':''}
        exclude = ['user', 'date']



class fileform(forms.Form):
    file = forms.FileField()


class UserLodgeComplaintForm(forms.ModelForm):
    class Meta:
        model = ComplaintLodge
        fields = '__all__'
        labels = {'category':'Select Category', 'subcategory':'Select SubCategory',
                  'state':'Select Department', 'Desc':'Document Details',
                  'Doc':'Upload Doc (if any)'}
        widgets = {'category':forms.Select(attrs={'class':'form-control'}),
                   'subcategory':forms.Select(attrs={'class':'form-control'}),
                   'state':forms.Select(attrs={'class':'form-control'}),
                   'Type':forms.TextInput(attrs={'class':'form-control'}),
                   'Desc':forms.Textarea(attrs={'class':'form-control'}),
                   'Doc':forms.FileInput(attrs={'class':'form-control'}),}







