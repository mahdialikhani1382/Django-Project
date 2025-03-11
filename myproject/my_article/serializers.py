from rest_framework import serializers
from my_article.models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','text','article']

class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True,read_only=True)
    class Meta:
        model = Article
        fields = ['id','title','content','comments']