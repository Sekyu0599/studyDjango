# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.http import HttpResponse
from django.core import serializers
import MySQLdb;
import simplejson as json

# Create your models here.
def DBTest():
    a_list=[];
    try:
        # 连接数据库
        conn = MySQLdb.connect('localhost','root', '1Qaz2Wsx', 'studyDjango')
        cursor = conn.cursor()  # 创建数据游标

        # 执行查询
        query = ("SELECT uid, upwd, uname FROM userinfo ")
        cursor.execute(query)

        # 使用 fetchone() 方法获取一条数据库。
        data = cursor.fetchone()
        print data

        a_list = cursor.fetchall()  # fetchone获取一个元组
        # count = int(cursor.rowcount) # 获取元组个数

        response_data = {}
        response_data['result'] = 'failed'
        response_data['message'] = 'You messed up'
        return HttpResponse(json.dumps(response_data), content_type="application/json")

        # return a_list

    except MySQLdb.Error as err:
        print("Something went wrong: {}".format(err))
        exit()

    finally:
        conn.commit()  # 提交修改
        cursor.close()  # 关闭数据库
        conn.close()
    return;

DBTest()