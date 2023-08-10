from django.db import models


class UserInfo(models.Model):
    UserName = models.CharField(verbose_name="用户名", max_length=255)
    PassWord = models.CharField(verbose_name="密码", max_length=15)
    PhoneNumber = models.IntegerField(verbose_name="电话号码")
    CreateTime = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    UserToken = models.CharField(verbose_name="Token", max_length=255, default="")


class FileFolder(models.Model):
    image = models.FileField(verbose_name="图片")