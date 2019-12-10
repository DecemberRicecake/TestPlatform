from rest_framework import serializers
from usermanage.models import User, Token


class UserSerializer(serializers.ModelSerializer):
    """
    用户信息序列化
    """
    class Meta:
        model = User
        fields = '__all__'
