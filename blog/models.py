from pyexpat import model
from re import M
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    # author: 추후 작성 예정

    def __ster__(self):
        return f'[{self.pk}]{self.title}'