from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib import messages, auth

from home.common.views import TitleMixin
from .forms import UserSignupForm, UserLoginForm, UserUpdateForm, ProfileImageForm, PassResetForm, PassResetConfirmForm


class UserSignupView(TitleMixin, CreateView):
    model = User
    form_class = UserSignupForm
    title = 'Регистрация'
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')


# def signup(request):
#     if request.method == 'POST':
#         form = UserSignupForm(request.POST)
#         if form.is_valid():
#             # form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Пользователь {username} успешно создан')
#             return redirect('home')
#     else:
#         form = UserSignupForm()
#     return render(request,
#                   'users/signup.html',
#                   {
#                       'title': 'Регистрация',
#                       'form': form
#                   }
#                   )

class UserLoginView(TitleMixin, LoginView):
    title = 'Авторизация'
    template_name = 'users/login.html'
    form_class = UserLoginForm


# class UserLogoutView(LogoutView):
#     template_name = 'users/exit.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         ctx = super(UserLogoutView, self).get_context_data(**kwargs)
#         ctx['title'] = 'Выход'
#         ctx['text'] = 'Вы успешно вышли из аккаунта'
#
#         return ctx

def exit(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def profile(request):
    if request.method == 'POST':
        profileImageForm = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)

        if profileImageForm.is_valid() and updateUserForm.is_valid():
            updateUserForm.save()
            profileImageForm.save()
            messages.success(request, f'Ваш аккаунта был успешно обновлен')
            return redirect('profile')
    else:
        profileImageForm = ProfileImageForm(instance=request.user.profile)
        updateUserForm = UserUpdateForm(instance=request.user)

    data = {
        'title': 'Профиль',
        'profileImageForm': profileImageForm,
        'updateUserForm': updateUserForm,
    }
    return render(request, 'users/profile.html', data)


class PassResetView(PasswordResetView):
    title = 'Восстановить пароль'
    template_name = 'users/pass-reset.html'
    form_class = PassResetForm


class PassResetConfirmView(TitleMixin, PasswordResetConfirmView):
    title = 'Новый пароль'
    template_name = 'users/password-reset-confirm.html'
    form_class = PassResetConfirmForm

