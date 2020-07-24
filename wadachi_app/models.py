from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    # postを作った人
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # 資料のtitle
    title = models.CharField(max_length=200)
    # 資料のurl
    url = models.URLField(max_length=200, default='', null=True)

    # text = models.TextField()

    # データが作成された時刻
    created_date = models.DateTimeField(default=timezone.now)

    # published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title