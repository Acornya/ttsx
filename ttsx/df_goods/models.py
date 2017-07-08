#coding=utf-8
from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class GoodsType(models.Model):
    Gsorts = models.CharField(default='',max_length=20)
    Isdelete = models.BooleanField(default = False)
    def __str__(self):
        return self.Gsorts.encode('utf-8')

class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=50)
    gimg = models.ImageField(upload_to= 'df_goods/')
    gprice = models.DecimalField(max_digits=5, decimal_places=2)#999.99
    gclick = models.IntegerField(default=0)
    gunit= models.CharField(max_length=20)#单位
    Isdelete = models.BooleanField(default=False)
    gsub = models.CharField(max_length=200) # 副标题
    gkucun = models.IntegerField(default=100) #库存
    gcontent = HTMLField()
    grelation = models.ForeignKey('GoodsType')


