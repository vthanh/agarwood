from django.urls import include, re_path, path
from agarwood.apps.views import *
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^$', HomeView.as_view(), name='home'),
    re_path(r'about', AboutView.as_view(), name='about'),
    re_path(r'contact', ContactView.as_view(), name='contact'),
    re_path(r'products/$', ProductListView.as_view(), name='products'),
    path(r'products/<int:pk>/', ProductDetailView.as_view(), name='products-detail'),
    re_path(r'news/$', NewsListView.as_view(), name='news'),
    path(r'news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    re_path(r'services', ServiceView.as_view(), name='services'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
