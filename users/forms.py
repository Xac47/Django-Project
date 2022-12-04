from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm

from users.models import Profile


class UserSignupForm(UserCreationForm):
    username = forms.CharField(
        label='',
        min_length=6,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Придумайте логин'})
    )
    first_name = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'})
    )
    email = forms.EmailField(
        label='',
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите E-mail'})
    )
    password1 = forms.CharField(
        label='',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Придумайте пароль'})
    )
    password2 = forms.CharField(
        label='',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Придумайте пароль'})
    )


    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Введите имя'})
    )
    password = forms.CharField(
        label='',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Введите пароль'})
    )

    class Meta:
        model = User
        fields = ['username', 'password']

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите новый логин'})
    )

    email = forms.EmailField(
        label='',
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите новый email'})
    )

    first_name = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите новое имя'})
    )


    class Meta:
        model = User
        fields = ['first_name', 'username', 'email']



class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label='Загрузить фото',
        required=False,
        widget=forms.FileInput
    )

    class Meta:
        model = Profile
        fields = ['img']


class PassResetForm(PasswordResetForm):
    email = forms.EmailField(
        label='',
        required=True,
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder': 'Введите свой E-mail', "autocomplete": "email"})
    )

    class Meta:
        model = User
        fields = 'email'


class PassResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='',
        required=True,
        strip=False,
        widget=forms.PasswordInput(attrs={'class':' form-control', 'placeholder': 'Придумайте пароль', "autocomplete": "new-password"})
    )

    new_password2 = forms.CharField(
        label='',
        required=True,
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Подтвердите пароль', "autocomplete": "new-password"})
    )