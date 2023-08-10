from rest_framework import serializers
from datetime import datetime
from rest_framework import serializers

from LoginTest.models import UserInfo


class RegistSerializer(serializers.ModelSerializer):
    PassWord = serializers.CharField(write_only=True)

    class Meta:
        model = UserInfo
        fields = ['UserName', 'PassWord', 'PhoneNumber']

    def create(self, validated_data):
        userinfo = UserInfo.objects.create_user(
            UserName=validated_data['UserName'],
            PassWord=validated_data['PassWord'],
            PhoneNumber=validated_data['PhoneNumber']
        )

        return userinfo
