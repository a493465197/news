import code
from django.shortcuts import render
from requests import delete
from scrapy import cmdline
import random
import os
# Create your views here.

from django.http import HttpResponse
from newsWeb import models
import json

def getInfo(request):
    if request.COOKIES.get('username') == None:
        return HttpResponse(json.dumps({}))

    ret = models.user.objects(username = request.COOKIES.get('username')).as_pymongo()

    for i in ret:
        i['_id'] = ''
    ret = list(ret)
    return HttpResponse(json.dumps({
        'code': 0,
        'value': ret[0]
    }))

def reg(request):
    models.user(**json.loads(request.body)).save()
    return HttpResponse(json.dumps({'code': 0, 'msg': '注册成功'}))

def login(request):
    body = json.loads(request.body)
    if models.user.objects(username = body.get('username'), password = body.get('password')).count() > 0:
        h = HttpResponse(json.dumps({'code': 0, 'msg': '登录成功'}))
    else:
        h = HttpResponse(json.dumps({'code': -1, 'msg': '登录失败'}))
    h.set_cookie('username', body.get('username'))
    return h

    


def docList(request):
    ret = models.newsina.objects().limit(300).order_by('-ctime').as_pymongo()
    for i in ret:
        i['_id'] = ''
    ret = list(ret)
    return HttpResponse(json.dumps({
        'code': 0,
        'value': ret
    }))


def updateDoc(request):
    body = json.loads(request.body)

    h = models.newsina.objects.get(**{'id1': body.get('id1')})
    h.update(**{'content': body.get('content')})
    h.save()

    return HttpResponse(json.dumps({
        'code': 0,
        'value': 'ok'
    }))
def setInfo(request):
    body = json.loads(request.body)

    h = models.user.objects.get(**{'username': body.get('currUser') or body.get('username')})
    if body.get('currUser'):
        body.pop('currUser')
    h.update(**body)
    h.save()

    return HttpResponse(json.dumps({
        'code': 0,
        'value': 'ok'
    }))

def hendleGet(request):
    body = json.loads(request.body)
    id1 = str(random.random())[2:10]
    # cmdline.execute('scrapy crawl newsina_spider'.split())
    if body.get('value') == 'xl':
        models.run(**{'type': '新浪网', 'username': request.COOKIES.get('username'), 'id1': id1}).save()
        os.system('scrapy crawl newsina_spider -a id1=' + id1)
    if body.get('value') == 'tx':
        models.run(**{'type': '腾讯网', 'username': request.COOKIES.get('username'), 'id1': id1}).save()
        os.system('scrapy crawl qq_spider -a id1=' + id1)
    if body.get('value') == 'rm':
        models.run(**{'type': '人民网', 'username': request.COOKIES.get('username'), 'id1': id1}).save()
        os.system('scrapy crawl newsina_spider -a id1=' + id1)
    return HttpResponse(json.dumps({
        'code': 0,
        'value': 'ok'
    }))


def runList(request):
    ret = models.run.objects().as_pymongo().limit(200).order_by('-time')
    for i in ret:
        i['_id'] = ''
    ret = list(ret)
    return HttpResponse(json.dumps({
        'code': 0,
        'value': ret
    }))

def logout(request):
    h = HttpResponse(json.dumps({'code': 0, 'msg': '登出成功'}))
    h.delete_cookie('username')
    return h

def userList(request):
    ret = models.user.objects().as_pymongo().limit(200)
    for i in ret:
        i['_id'] = ''
    ret = list(ret)
    return HttpResponse(json.dumps({
        'code': 0,
        'value': ret
    }))

def delUser(request):
    body = json.loads(request.body)
    ret = models.user.objects.get(**{'username': body.get('username')})
    ret.delete()
    ret.save()
    return HttpResponse(json.dumps({
        'code': 0,
    }))

def delDoc(request):
    body = json.loads(request.body)
    ret = models.newsina.objects.get(**{'id1': body.get('id1')})
    ret.delete()
    ret.save()
    return HttpResponse(json.dumps({
        'code': 0,
    }))

def addTag(request):
    body = json.loads(request.body)
    ret = models.newsina.objects().as_pymongo().limit(200)
    flag = False
    for i in ret:
        i['_id'] = ''
        if i.get('content').find(body.get('value')) >= 0:
            flag = True
            findItem = models.newsina.objects.get(**{'id1': i['id1']})
            findItem.update(**{'keywords': findItem['keywords'] + ',' + body.get('value')})
            findItem.update(**{'lids': findItem['lids'] + ',' + body.get('value')})
            findItem.save()
    ret = list(ret)
    if flag:
        return HttpResponse(json.dumps({
            'code': 0,
        }))
    else:
        return HttpResponse(json.dumps({
            'code': -1,
            'msg': '没有找到相关新闻'
        }))
