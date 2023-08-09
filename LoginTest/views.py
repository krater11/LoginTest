from django.contrib.auth import authenticate
from django.db.models.signals import post_save
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from Serializer.UserSerializer import UserSerializer
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.conf import settings


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def generate_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)


class UserRegistrationView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        # 验证密码强度
        try:
            validate_password(password, user=User)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            # 创建用户
        user = User.objects.create_user(username=username, password=password)
        return Response({'message': '注册成功'}, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # 使用Django的身份验证函数进行用户认证
        user = authenticate(username=username, password=password)

        if user is not None:
            # 认证成功，生成或获取现有令牌
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            # 认证失败
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)