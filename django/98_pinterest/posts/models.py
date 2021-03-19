from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    image = ProcessedImageField(upload_to='images/%Y/%m/%d',
                                           processors=[ResizeToFill(500, 500)],
                                           format='JPEG',
                                           options={'quality': 60})
    # image_thumbnail = ImageSpecField(source='image', # 썸네일 만들 기준 이미지
    #                                   processors=[ResizeToFill(200, 200)], # 필요없는 부분 잘라내고 영역 맞추기
    #                                   format='JPEG',
    #                                   options={'quality': 60})
    created_at = models.DateTimeField(auto_now_add=True)