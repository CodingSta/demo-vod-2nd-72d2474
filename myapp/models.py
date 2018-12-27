from django.db import models
from django.core.validators import MinLengthValidator


class Post(models.Model):
    title = models.CharField(max_length=100, validators=[MinLengthValidator(3)],
                             help_text='글 제목입니다. 100자 이내로 입력해주세요.')
    content = models.TextField(help_text='글 내용')
    user_agent = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    message = models.TextField()
    ip = models.CharField(max_length=15)
