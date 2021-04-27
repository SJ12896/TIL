from rest_framework import serializers
from .models import Article, Comment


# 모델에서 들고와서 바로 설정
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id','title',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)


class ArticleSerializer(serializers.ModelSerializer):
    # 이름은 comment_set으로 정해짐. 바꾸고싶으면 model
    # Comment에서 article 외래키의 related_name을 바꿔준다.
    #comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # 근데 comment_serializer가 더 아래 있어서 오류 발생 순서를 바꿔야함
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    comment_first = CommentSerializer(source='comment_set.first', read_only=True)
    comment_filter = serializers.SerializerMethodField('greater_10')

    def greater_10(serlf, article):
        qs = Comment.objects.filter(pk__gte=10, article=article)
        serializer = CommentSerializer(instance=qs, many=True)
        return serializer.data

    class Meta:
        model = Article
        fields = '__all__'
