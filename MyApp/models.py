# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class Commodity(models.Model):
    name = models.TextField(blank=True, null=True, verbose_name="商品名称")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name
        db_table = 'commodity'


class Comment(models.Model):
    id_Commodity = models.ForeignKey(Commodity, models.DO_NOTHING, db_column='id_Commodity', blank=True, null=True,
                                     verbose_name='商品')
    content = models.TextField(blank=True, null=True, verbose_name='内容')

    datetime = models.DateTimeField(blank=True, null=True, verbose_name='时间', auto_now_add=True)
    sentiment = models.FloatField(blank=True, null=True, verbose_name='情感值')

    def __unicode__(self):
        return self.content

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        db_table = 'comment'


class KeywordsStatistics(models.Model):
    id_Commodity = models.ForeignKey(Commodity, models.DO_NOTHING, db_column='id_Commodity', blank=True, null=True,
                                     verbose_name='商品')
    keywords = models.CharField(blank=True, null=True, max_length=30, verbose_name='关键字')
    amount = models.IntegerField(blank=True, null=True, verbose_name='数量')

    def __unicode__(self):
        return self.keywords

    class Meta:
        verbose_name = '关键字'
        verbose_name_plural = verbose_name
        db_table = 'keywords'




