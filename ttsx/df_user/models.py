from django.db import models

# Create your models here.

class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=20)
    uphone = models.IntegerField()
    uemail = models.CharField(max_length=20)

    def __str__(self):
        return "%d" % self.pk


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=100)
    hBook = models.ForeignKey('BookInfo')
    def __str__(self):
        return "%d" % self.pk