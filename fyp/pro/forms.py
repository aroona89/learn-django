from django import forms
from .models import Category, SubCategory, State
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,\
    UsernameField, SetPasswordForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _

#signup form
class SignupForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=
                        {'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=
                     {'class':'form-control', 'placeholder':'Confirm Password'}))
    class Meta:
        model = User

        fields = ['username','email']
        widgets = {'username':forms.TextInput(attrs={'class':'form-control',
                                                     'placeholder':'Username'}),
                   'email':forms.EmailInput(attrs={'class':'form-control',
                                                       'placeholder':'Email'}),
                   }


#loginform
class LoginForm(AuthenticationForm):

    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control',
                             'autofocus':True, 'placeholder':'Username'})
                             )
    password = forms.CharField(label= _('Password'), strip=False,
                             widget=forms.PasswordInput(attrs=
                     {'autocomplete':'current-password', 'class':'form-control',
                           'placeholder':'Password'})
                               )

#Change the Password(form) without old password
class ChangePassForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs=
                                    {'placeholder':'New Password',
                                     'class':'form-control'})
                                    )
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs=
                                    {'placeholder':'confirm New Password',
                                     'class':'form-control'})
                                    )

class ChangeAdminPassForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs=
                                    {'placeholder':'Old Password',
                                     'class':'form-control'})
                                   )
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs=
                                    {'placeholder':'New Password',
                                     'class':'form-control'})
                                    )
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs=
                                    {'placeholder':'confirm New Password',
                                     'class':'form-control'})
                                    )




class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['CategoryName', 'CategoryDesc']
        labels  = {'CategoryName':'Category Name', 'CategoryDesc':'Description'}
        widgets = {'CategoryName':forms.TextInput(attrs={'class':'form-control'}),
                   'CategoryDesc': forms.Textarea(attrs={'class': 'form-control'}),
                   }


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = '__all__'
        labels  = {'InheritCategory':'Category', 'SubCategoryName':'SubCategory'}
        widgets = {'InheritCategory':forms.Select(attrs={'class':'form-control'}),
                   'SubCategoryName': forms.TextInput(attrs={'class': 'form-control'}),
                   }


class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ['StateName', 'StateDesc']
        widgets = {'SateName':forms.TextInput(attrs={'class':'form-control'}),
                   'StateDesc':forms.Textarea(attrs={'class':'form-control'}),
                   }


