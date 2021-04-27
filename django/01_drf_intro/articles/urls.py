from django.urls import path
from .import views

urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>', views.article_detail),
    path('comment/', views.comment_list),
    path('comment/<int:comment_pk>', views.comment_detail),
    path('<int:article_pk>/comments/', views.comment_create),
]
