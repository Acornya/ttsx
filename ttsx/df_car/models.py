from django.db import models
from df_goods.models import GoodsInfo
from df_user.models import UserInfo

# Create your models here.
class CarInfo(models.Model):
    cgoods = models.ForeignKey(GoodsInfo)
    cuser = models.ForeignKey(UserInfo)
    count = models.IntegerField()

