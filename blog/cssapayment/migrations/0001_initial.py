# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u59d3\u540d')),
                ('uid', models.CharField(max_length=10, verbose_name='\u5b78\u865f')),
                ('gender', models.CharField(choices=[('M', '\u7537'), ('F', '\u5973')], max_length=1, verbose_name='\u751f\u7406\u6027\u5225')),
                ('paymentway', models.CharField(choices=[('0131', '\u570b\u6cf0\u4e16\u83ef\u5546\u696d\u9280\u884cCUCB \u8f49\u5e33'), ('0132', '\u570b\u6cf0\u4e16\u83ef\u5546\u696d\u9280\u884cCUCB \u7121\u647a\u5b58\u6b3e'), ('8221', '\u4e2d\u570b\u4fe1\u8a17CTBC \u8f49\u5e33'), ('8222', '\u4e2d\u570b\u4fe1\u8a17CTBC \u7121\u647a\u5b58\u6b3e'), ('7001', '\u4e2d\u83ef\u90f5\u653fChunghwa Post \u8f49\u5e33'), ('7002', '\u4e2d\u83ef\u90f5\u653fChunghwa Post \u7121\u647a\u5b58\u6b3e'), ('9999', '\u89aa\u81ea\u6536\u6b3e')], max_length=4, verbose_name='\u4ed8\u6b3e\u65b9\u5f0f')),
                ('choicecamp', models.CharField(choices=[('Y', '\u53c3\u52a0\u5bbf\u71df'), ('N', '\u4e0d\u53c3\u52a0\u5bbf\u71df')], max_length=1, verbose_name='\u5bbf\u71df\u610f\u9858')),
                ('money', models.CharField(max_length=10, verbose_name='\u7e73\u4ea4\u91d1\u984d')),
            ],
        ),
    ]