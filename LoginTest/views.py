from django.contrib.auth import authenticate
from django.db.models.signals import post_save
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from Serializer.UserSerializer import UserSerializer
from Serializer.RegistSerializer import RegistSerializer
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.conf import settings
from .models import UserInfo, FileFolder
from datetime import datetime
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from utils.token.generatetoken import generate_token
from Serializer.ImageSerializer import ImageSerializer
from django.core import serializers


class login(APIView):

    def post(self, request, *args, **kwargs):
        UserName = request.data.get("UserName")
        PassWord = request.data.get("PassWord")

        username = UserInfo.objects.get(UserName=UserName)
        match = check_password(PassWord, username.PassWord)

        if not match:
            return Response({"error":"密码错误"}, status=status.HTTP_401_UNAUTHORIZED)

        token = username.UserToken
        if len(token) == 0:
            usertoken = generate_token()
            print(usertoken)
            username.UserToken = usertoken
            username.save()

        return Response(status=status.HTTP_200_OK)


class regist(APIView):

    def post(self, request, *args, **kwargs):
        print(request.data)
        Regist_Serializer = RegistSerializer(data=request.data)
        print(Regist_Serializer.is_valid())
        if not Regist_Serializer.is_valid():
            return Response(Regist_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        UserName = Regist_Serializer.validated_data["UserName"]
        PassWord = make_password(Regist_Serializer.validated_data['PassWord'])
        PhoneNumber = Regist_Serializer.validated_data['PhoneNumber']
        CreateTime = datetime.now()

        try:
            validate_password(PassWord, user=UserName)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        userinfo = UserInfo.objects.create(UserName=UserName,PassWord=PassWord, PhoneNumber=PhoneNumber, CreateTime=CreateTime)
        return Response(status=status.HTTP_200_OK)


class ImagePostView(APIView):

    def post(self, request, *args, **kwargs):

        file_data = request.FILES['JPG']
        data = {'image':file_data}
        serializer = ImageSerializer(data=data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        Image = serializer.validated_data['image']
        FileFolder.objects.create(image=Image)
        return Response(status=status.HTTP_200_OK)


class ImageListView(APIView):

    def get(self, request, *args, **kwargs):

        queryset = FileFolder.objects.all()

        data = serializers.serialize('json', queryset)
        d_data = serializers.deserialize('json', data)
        for i in d_data:
            print(i.object.image.url)
        s = ImageSerializer(instance=queryset, many=True)
        return Response(s.data, status=status.HTTP_200_OK)
