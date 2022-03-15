from django.db import models
from djange.utils import timezone
from django.contrib.auth.models import user
# Create your models here.
class Post (models.model) : 
    STATUS_CHOICES - (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    Recipe = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
    unique_for_date="publish")
    author = models.ForeignKey(User,
    on_delete=models.CASCADE,
    related_name="blog_Posts")

    img = models.ImageField(null=True, blank=True)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
    choices=STATUS_CHOICES,
    default='draft')

    class Meta:
    ordering = ('-publish',)

    def __str__(self):
    return self.Recipe
