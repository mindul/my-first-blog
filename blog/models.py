
# Create your models here.
from django.db import models
from django.utils import timezone

# 이미지 처리
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail

class Post(models.Model):
     author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
     title = models.CharField(max_length=200)
     text = models.TextField()
     created_date = models.DateTimeField(default=timezone.now)
     published_date = models.DateTimeField(blank=True, null=True)
     photo = models.ImageField()
     photo_thumbnail = ImageSpecField(
	     source = 'photo', 		   # 원본 ImageField 명
	     processors = [Thumbnail(100, 100)], # 처리할 작업목록
	     format = 'JPEG',		   # 최종 저장 포맷
	     options = {'quality': 60}) # 저장 옵션
	
     def publish(self):
         self.published_date = timezone.now()
         self.save()

     def __str__(self):
         return self.title