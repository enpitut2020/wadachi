from django.conf import settings
from django.db import models
from django.utils import timezone




# 資料をまとめたもの
class Bridge(models.Model):
    # postを作った人
    contributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 橋のtitle
    topic = models.CharField(max_length=200)
    # 投稿者の状態・context (必須)
    context = models.TextField()
    # 投稿者の目的 (必須)
    goal = models.TextField()
    # データが作成された時刻
    created_date = models.DateTimeField(default=timezone.now)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.topic


# 個別資料のデータ
class Brick(models.Model):
    # 資料のtitle (Brickの名前)   例："入門Haskell"
    title = models.CharField(max_length=200)
    # 資料の著者                  例："John Smith"
    author = models.CharField(max_length=200)
    # 資料のurl                   例：https://amazon.com/入門Haskell
    url = models.URLField(max_length=200, default='', null=True)
    # データが作成された時刻
    created_date = models.DateTimeField(default=timezone.now)
    # 所属するbridge
    bridge = models.ForeignKey(Bridge, on_delete=models.CASCADE)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
