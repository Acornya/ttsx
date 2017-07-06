from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(default='', max_length=20)
    upwd = models.CharField(default='', max_length=40)   #mi ma
    uphone = models.CharField(default='', max_length=11)
    ucode = models.CharField(default='', max_length=6)
    uaddr_detail = models.CharField(default='', max_length=80)
    urcv = models.CharField(default='', max_length=20)
    uemail = models.CharField(default='', max_length=20)




