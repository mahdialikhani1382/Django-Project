from django.urls import path
from setuptools.extern import names

from pages.views import HomePageView, AboutPageView, ArticleDetailView, ArticleListView, ContactFormView, \
    ThanksPageView, ArticleCreateView

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('about/',AboutPageView.as_view(),name='about'),
    path('article/<int:pk>',ArticleDetailView.as_view(),name='article_detail'),
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('contact/',ContactFormView.as_view(),name='contact'),
    path('thanks/',ThanksPageView.as_view(),name='thanks'),
    path('article/new/',ArticleCreateView.as_view(),name='article_create'),
]