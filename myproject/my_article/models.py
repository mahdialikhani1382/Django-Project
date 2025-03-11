from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments')
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text