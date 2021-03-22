from django.contrib.auth.forms import UserChangeForm
# user 직접 참조 권장 x. 앞으로 커스텀 유저 모델을 메인으로 사용할꺼라서. 
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# 보통 커스텀은 상속받는 거 앞에 custom표시
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', )