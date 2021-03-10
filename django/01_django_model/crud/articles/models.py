from django.db import models

# Create your models here.
class Article(models.Model):
    # 컬럼-데이터 입장(모델 필드 - 장고입장) = 로우(데이터 형식)
    title = models.CharField(max_length=100) # CharField는 길이에 제한을 두기 때문에 필수인자인 max_length가 필요하다.
    content = models.TextField()
    # 자동으로 작성되는 시간을 넣기 위한 인자
    created_at = models.DateTimeField(auto_now_add=True)
    # 자동으로 수정되는 시간을 넣기 위한 인자. 두 개 헷갈리지 말기
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title