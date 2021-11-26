from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    STATUS = (
        ('draft','Draft'),
        ('published','Published'),
    )

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=250, blank=False)
    slug = models.SlugField(max_length=250, unique_for_date='publish_date')
    author = models.ForeignKey(User, on_delete=models.CASCADE, 
                                    related_name='blog_posts')
    content = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default='draft')

    class Meta:
        ordering = ['-publish_date'] 

    def __str__(self):
        return self.title




