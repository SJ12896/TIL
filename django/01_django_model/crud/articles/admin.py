from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    # 부모 클래스에 정의된 변수를 덮어쓰는 거라서 정해진 변수를 사용해야한다.
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at', )

# admin site에 register하겠다.
admin.site.register(Article, ArticleAdmin)
