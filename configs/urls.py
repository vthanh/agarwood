"""cleaner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.urls import include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views import defaults as default_views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from agarwood.apps.views import *
from agarwood.users.views import *

admin.site.site_header = 'GRASSLIST ADMIN'
admin.site.site_title = 'GRASS LIST'

urlpatterns = [
    # Admin site
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    re_path(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
    path('admin/password_reset/', auth_views.PasswordResetView.as_view(), name='admin_password_reset',),
    path('admin/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done',),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm',),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete',),


    path('logout/', UserLogout.as_view(), name='logout'),
    path('login/', UserLogin.as_view(), name='login'),
    # path('logout/', auth.LogoutView.as_view(template_name ='user / index.html'), name ='logout'),
    path('signup/', UserSignUp.as_view(), name='signup'),
    path('oauth/', include('social_django.urls', namespace='social')),

    # User management
    # path('accounts/', include('django.contrib.auth.urls')),
    path('user/', include('agarwood.users.urls')),
    path(r'', include('agarwood.apps.urls')),

    # dispensaries
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        re_path(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        re_path(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        re_path(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        re_path(r'^500/$', default_views.server_error),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            re_path(r'^__debug__/', include(debug_toolbar.urls)),
        ]
