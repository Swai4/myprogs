from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    author = models.CharField(max_length=50, null=False, blank=False)
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        return self.published_date

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs ={'pk': self.pk})

    def p_text(self):
        return self.text   


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postcomments')
    author = models.CharField(max_length=50, null=False, blank=False)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text