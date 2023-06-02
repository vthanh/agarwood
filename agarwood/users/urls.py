from django.urls import path, include, re_path
from agarwood.users.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    re_path(r'^settings/$', UserProfile.as_view(), name='profile'),
    re_path(r'^reviews/$', UserReviews.as_view(), name='user_reviews'),
    re_path(r'^favorites/$', UserFavorites.as_view(), name='user_favorites'),
    re_path(r'^change_password/$', auth_views.PasswordChangeView.as_view(template_name='users/change_password.html',
                                                                     success_url='/'), name='change_password'),

    # Forget Password
    re_path(r'^password-reset/$', UserPasswordResetView.as_view(), name='user_password_reset'),
    re_path(r'^password-reset/done/$', UserPasswordResetDoneView.as_view(), name='user_password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(),
        name='user_password_reset_confirm'),
    re_path(r'^password-reset-complete/$', UserPasswordResetCompleteView.as_view(), name='user_password_reset_complete'),
]
