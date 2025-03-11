from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from my_article.models import Article, Comment
from my_article.serializers import ArticleSerializer, CommentSerializer
from rest_framework import mixins,generics
from rest_framework import viewsets

class CustomPagination(PageNumberPagination):
    page_size = 5
    max_page_size = 50
    page_query_param = 'pagination_page'

    def get_paginated_response(self, data):
        return Response({
            'total_items_count' : self.page.paginator.count,
            'total_pages_count' : self.page.paginator.num_pages,
            'current_page' : self.page.number,
            'items' : data
        })

class ArticleViewSetApiView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

class CommentViewSetApiView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = CustomPagination
