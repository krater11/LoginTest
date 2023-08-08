from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserInfo


class SignView(APIView):

    def post(self, request, *args, **kwargs):

        s = request.data
        print(s["name"])
        username = UserInfo.objects.filter(UserName=s["name"])
        if not username.exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        User = UserInfo.objects.create(UserName=s["name"], PassWord=s["password"], PhoneNumber=s["phone"], )
        return Response(data=request.data, status=status.HTTP_200_OK)

