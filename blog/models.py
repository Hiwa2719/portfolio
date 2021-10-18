from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=256)
    image = models.ImageField()
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.pk})

    def summery(self):
        return self.content[:50]
