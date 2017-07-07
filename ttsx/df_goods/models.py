from django.db import models

# Create your models here.
class GoodsType(models.Model):
    Gsorts = models.CharField(default='',max_length=20)
    Isdelete = models.BooleanField(default = False)

class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    gimg = models.ImageField(max_length=40)
    gprice = models.DecimalField(max_digits=5, decimal_places=2)
    gunit= models.CharField(max_length=10)
    gclick = models.IntegerField()
    gsub = models.CharField(max_length=40)
    gcontent = models.CharField(max_length=20)
    grelation = models.ForeignKey('GoodsType')
    Isdelete = models.BooleanField(default=False)

    class TypeInfo(models.Model):
        ttitle = models.CharField(max_length=20)
        isDelete = models.BooleanField(default=False)

        def __str__(self):
            return self.ttitle.encode('utf-8')

    class GoodsInfo(models.Model):
        gtitle = models.CharField(max_length=50)
        gpic = models.ImageField(upload_to='goods')
        gprice = models.DecimalField(max_digits=5, decimal_places=2)  # 999.99
        gclick = models.IntegerField(default=0)
        gunit = models.CharField(max_length=20)
        isDelete = models.BooleanField(default=False)
        gsubtitle = models.CharField(max_length=200)
        gkucun = models.IntegerField(default=100)
        gcontent = HTMLField()
        gtype = models.ForeignKey('TypeInfo')
