# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
# from django.urls import reverse
# from django.views.generic import DetailView, ListView, RedirectView, UpdateView
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

# from .models import User
from .forms import SignUpForm, UserForm, ProfileForm
from django.contrib.auth.models import User


class UserSignUp(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            if User.objects.filter(email=email) or User.objects.filter(username=username):
                messages.error(request, f"The email/username fields was duplicated.")
            else:
                form.save()
                user = authenticate(username=username, email=email, password=password1)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, f'Register {username} successfully!!')
                return redirect('login')
        return render(request, 'registration/signup.html', {'form': form})


class UserLogin(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form, 'title': 'log in'})

    def post(self, request):
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            if 'remember_me' in request.POST:
                request.session.set_expiry(1209600)  # 2 weeks
            messages.success(request, f' welcome {username} !!')
            return redirect('home')
        else:
            messages.error(request, f'Wrong email/username or password')
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form, 'title': 'log in'})


class UserLogout(LoginRequiredMixin, View):
    login_required = True

    def get(self, request):
        logout(request)
        return redirect('home')


class UserProfile(View):
    def get(self, request):
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        return render(request, 'users/account_settings.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })

    def post(self, request):
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')

        return render(request, 'users/account_settings.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })


class UserReviews(View):
    def get(self, request):
        form = None
        return render(request, 'users/reviews.html', {'form': form})

    def post(self, request):
        pass


class UserFavorites(View):
    def get(self, request):
        form = None
        number_favorites = 0
        return render(request, 'users/favorites.html', {'form': form, 'number_favorites': number_favorites})

    def post(self, request):
        pass


class UserPasswordResetView(auth_views.PasswordResetView):
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject.txt'
    success_url = reverse_lazy('user_password_reset_done')
    template_name = 'users/password_reset.html'
    title = _('Password reset')


class UserPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'
    title = _('Password reset sent')


class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    success_url = reverse_lazy('user_password_reset_complete')
    template_name = 'users/password_reset_confirm.html'
    title = _('Enter new password')


class UserPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'
    title = _('Password reset complete')

# class UserDetailView(LoginRequiredMixin, DetailView):
#     model = User
#     # These next two lines tell the view to index lookups by username
#     slug_field = 'username'
#     slug_url_kwarg = 'username'
#
#
# class UserRedirectView(LoginRequiredMixin, RedirectView):
#     permanent = False
#
#     def get_redirect_url(self):
#         return reverse('users:detail',
#                        kwargs={'username': self.request.user.username})
#
#
# class UserUpdateView(LoginRequiredMixin, UpdateView):
#
#     fields = ['name', ]
#
#     # we already imported User in the view code above, remember?
#     model = User
#
#     # send the user back to their own page after a successful update
#     def get_success_url(self):
#         return reverse('users:detail',
#                        kwargs={'username': self.request.user.username})
#
#     def get_object(self):
#         # Only get the User record for the user making the request
#         return User.objects.get(username=self.request.user.username)
#
#
# class UserListView(LoginRequiredMixin, ListView):
#     model = User
#     # These next two lines tell the view to index lookups by username
#     slug_field = 'username'
#     slug_url_kwarg = 'username'
