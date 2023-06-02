import json, logging
from pytz import timezone
from enum import Enum

from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from django.views.generic.list import ListView

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse

from .models import *
from .business import *


# Number of star which is reviewing score of the store (dispensary)
NUM_START = 5


class MenuBar(Enum):
    HOME = "HOME"
    ABOUT_US = "ABOUT US"
    PRODUCTS = "PRODUCTS"
    SERVICES = "SERVICES"
    NEWS = "NEWS"
    CONTACT_US = "CONTACT US"


class HomeView(View):
    def get(self, request, *args, **kwargs):
        products = Products.objects.all().order_by('-id')[:3]
        news_list = News.objects.all().order_by('-id')[:3]
        product_caterory_list = ProductCategory.objects.filter(is_parent_category=True).order_by('name')
        context = {
            "products": products,
            "news_list": news_list,
            "product_caterory_list": product_caterory_list,
            "page_name": MenuBar.HOME.value
        }
        return render(request, './apps/home.html', context)
    

class AboutView(View):
    def get(self, request, *args, **kwargs):
        employee_list = EmployeeProfile.objects.all().order_by('name')
        context = {
            "employee_list": employee_list,
            "page_name": MenuBar.ABOUT_US.value
        }
        return render(request, './apps/about.html', context)
    

class ContactView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "page_name": MenuBar.CONTACT_US.value
        }
        return render(request, './apps/contact-us.html', context)

    def post(self, request, *args, **kwargs):
        return JsonResponse({})


class ProductListView(ListView):
    model = Products
    context_object_name = 'products'
    paginate_by = 25  # if pagination is desired
    template_name = './apps/products.html'
    
    def get_queryset(self):
        object_list = Products.objects.all().order_by('-id')
        product_category = self.request.GET.get('product_category', None)
        if product_category:
            object_list = Products.objects.filter(product_category__name=product_category).order_by('-id')
        return object_list
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_caterory_list = ProductCategory.objects.filter(is_parent_category=True).order_by('name')
        context["product_caterory_list"] = product_caterory_list
        context["page_name"] = MenuBar.PRODUCTS.value
        context["product_category"] = self.request.GET.get('product_category', '')
        return context
    

class ProductDetailView(DetailView):
    model = Products
    context_object_name = 'product'
    template_name = './apps/product_detail.html'

    def get_context_data(self, **kwargs):
        current_product = self.get_object()
        context = super().get_context_data(**kwargs)
        products = Products.objects.all().order_by('-id')[:25]
        product_reviews = ProductReviews.objects.filter(product_id=current_product.id)
        context["products"] = products
        context["product_reviews"] = product_reviews
        context['meta'] = self.get_object().as_meta(self.request)
        context["page_name"] = MenuBar.PRODUCTS.value
        return context
    

class NewsListView(ListView):
    model = News
    context_object_name = 'news_list'
    paginate_by = 25  # if pagination is desired
    template_name = './apps/news.html'
    
    
    def get_queryset(self):
        object_list = News.objects.all().order_by('-id')
        news_category = self.request.GET.get('news_category', None)
        # if news_category:
        #     object_list = News.objects.filter(news_category__name=news_category).order_by('-id')
        return object_list
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news_category_list = NewsCategory.objects.all().order_by('name')
        context["news_category_list"] = news_category_list
        context["page_name"] = MenuBar.NEWS.value
        context["current_category"] = self.request.GET.get('news_category', '')
        return context
    

class NewsDetailView(DetailView):
    model = News
    context_object_name = 'news'
    template_name = './apps/news_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news_list = News.objects.all().order_by('-id')[:25]
        news_category_list = NewsCategory.objects.all().order_by('name')
        context["news_list"] = news_list
        context["news_category_list"] = news_category_list
        context['meta'] = self.get_object().as_meta(self.request)
        context["page_name"] = MenuBar.NEWS.value
        return context


class ServiceView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "page_name": MenuBar.SERVICES.value
        }
        return render(request, './apps/services.html', context)


