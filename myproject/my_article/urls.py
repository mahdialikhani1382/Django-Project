from django.urls import path, include
from rest_framework.routers import DefaultRouter
from my_article import views

router = DefaultRouter()
router.register('articles',views.ArticleViewSetApiView)
router.register('comments',views.CommentViewSetApiView)
urlpatterns = [
    path('',include(router.urls))

]