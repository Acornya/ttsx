from django.contrib import admin

# Register your models here.
from models import *
class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id','gtitle','gimg','gprice','gclick','gunit',
                    'Isdelete','gsub','gkucun','gcontent','grelation',]

admin.site.register(GoodsInfo,GoodsInfoAdmin)

class GoodsTypeAdmin(admin.ModelAdmin):
    list_display = ['id','Isdelete','Gsorts']

admin.site.register(GoodsType,GoodsTypeAdmin)