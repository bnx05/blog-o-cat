from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from tinymce.models import HTMLField


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    text = HTMLField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
