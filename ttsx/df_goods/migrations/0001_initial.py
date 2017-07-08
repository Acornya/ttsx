# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gtitle', models.CharField(max_length=50)),
                ('gimg', models.ImageField(upload_to=b'df_goods/')),
                ('gprice', models.DecimalField(max_digits=5, decimal_places=2)),
                ('gclick', models.IntegerField(default=0)),
                ('gunit', models.CharField(max_length=20)),
                ('Isdelete', models.BooleanField(default=False)),
                ('gsub', models.CharField(max_length=200)),
                ('gkucun', models.IntegerField(default=100)),
                ('gcontent', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Gsorts', models.CharField(default=b'', max_length=20)),
                ('Isdelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='grelation',
            field=models.ForeignKey(to='df_goods.GoodsType'),
        ),
    ]
