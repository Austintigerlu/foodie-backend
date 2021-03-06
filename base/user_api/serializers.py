from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
    
class UserSerializerWithToken(serializers.ModelSerializer):
    token =serializers.SerializerMethodField(read_only=True)
    isAdmin =serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'token', 'isAdmin']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token)
    
    def get_isAdmin(self, obj):
        return obj.is_staff