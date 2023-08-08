from django.db import models


class UserInfo(models.Model):
    UserName = models.CharField(verbose_name="用户名", max_length=255)
    PassWord = models.CharField(verbose_name="密码", max_length=20)
    PhoneNumber = models.IntegerField(verbose_name="电话号码", max_length=11)
    CreateTime = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)