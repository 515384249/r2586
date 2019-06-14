import json
import os
from django.shortcuts import reverse, redirect
from . import models
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django.db.models import Q


# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt

def youxiangchaxun(request):
    context = {}
    if request.method == 'GET':
        case_name = request.GET.get('name')
        case_page = request.GET.get('page')
    elif request.method == 'POST':
        case_name = request.POST.get('name')
        case_page = request.POST.get('page')
    if case_name:
        contact_list = models.tongxunlu.objects.filter(
            Q(xingming__contains=case_name) | Q(yuan__contains=case_name) | Q(xi__contains=case_name) | Q(
                zhuanye__contains=case_name) | Q(zhiwu__contains=case_name) | Q(dianhua__contains=case_name) | Q(
                dizhi__contains=case_name)
        ).values('yuan', 'xi', 'zhuanye', 'xingming', 'zhiwu', 'dianhua', 'dizhi').order_by('id')
    else:
        contact_list = models.tongxunlu.objects.all().values('yuan', 'xi', 'zhuanye', 'xingming', 'zhiwu',
                                                             'dianhua',
                                                             'dizhi').order_by('id')

    paginator = Paginator(contact_list, 2200)  # 每页显示25条
    yuanxi = models.yuan.objects.all().values('name', 'father_name')
    try:
        contacts = paginator.page(case_page)
    except PageNotAnInteger:
        # 如果请求的页数不是整数，返回第一页。
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(1)
    context = {'contacts': contacts,
               'case_name': yuanxi,
               'search_name': case_name,
               }
    return render(request,'youxiangchaxun.html',context)






def fileupload(request):
    if request.method == "POST":  # 请求方法为POST时，进行处理
        myFile = request.FILES.get("myfile", None)  # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("no files for upload!")
        destination = open(os.path.join("E:\\upload", myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        return HttpResponse("upload over!")



def showtable(request):
    if request.method == "GET":
        search = request.GET.get('search')  # how many items per page
        print(search)
        if search:  # 判断是否有搜索字
            print(search)
            all_records = models.tongxunlu.objects.filter(
                Q(xingming__contains=search) | Q(yuan__contains=search) | Q(xi__contains=search) | Q(
                    zhuanye__contains=search) | Q(zhiwu__contains=search) | Q(dianhua__contains=search) | Q(
                    dizhi__contains=search)
            ).values('id', 'yuan', 'xi', 'zhuanye', 'xingming', 'zhiwu', 'dianhua', 'dizhi').order_by('id')
        else:
            all_records = models.tongxunlu.objects.all().values('id', 'yuan', 'xi', 'zhuanye', 'xingming', 'zhiwu',
                                                                'dianhua',
                                                                'dizhi')
        ppp = json.dumps(list(all_records))
        print(ppp)
    return HttpResponse(ppp)


def ceshi(request):
    context = {}
    return render(request, 'ceshi.html', context)


@login_required
@require_GET
def mylogout(request):
    print("logout")
    try:
        logout(request)
    except:
        pass
    return render(request, 'mylogin.html')


def mylogin(request):
    context = {}
    if request.method == 'POST':
        print("post")
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        print(username)
        print(pwd)
        user = authenticate(request, username=username, password=pwd)
        if user:
            print("zhuce")
            login(request, user)
            return redirect(reverse('ceshi'))
        else:
            return HttpResponse("<h1>密码错误</h1>")
    elif request.method == 'GET':
        return render(request, 'mylogin.html', context)


def kjfs_search(request):
    if request.method == 'POST':
        print("收到post")
        type = request.POST.get('type')  # 测试是否能够接收到前端发来的name字段
        print(type)
        a = request.POST.get('data')  # 测试是否能够接收到前端发来的name字段
        b = a.strip(" ")
        if (type == "kjjs"):
            data = models.tongxunlu.objects.filter(yuan=b).values('id', 'yuan', 'xi', 'zhuanye', 'xingming', 'zhiwu',
                                                                  'dianhua', 'dizhi')
            print("ccccc")
            print(data)
            print("ccccc")
            json_data = json.dumps(list(data))
            print(json_data)
            return HttpResponse(json_data)
    else:
        return HttpResponse("<h1>test</h1>")


def kjfs_edit(request):
    if request.method == 'POST':

        type = request.POST.get('type')  # 测试是否能够接收到前端发来的name字段
        print(type)

        a = request.POST.get('data')  # 测试是否能够接收到前端发来的name字段
        c = json.loads(a)
        # print(c[0].zhiwu)
        if (type == 'save'):
            for i in c:
                if (models.tongxunlu.objects.filter(id=i['id']).exists()):
                    print("updata")
                    b = i['id']
                    del i['id']
                    del i['state']
                    models.tongxunlu.objects.filter(id=b).update(**i)
                else:
                    print("new")
                    del i['id']
                    del i['state']
                    models.tongxunlu.objects.create(**i)
        elif (type == 'del'):
            for i in c:
                models.tongxunlu.objects.filter(id=i['id']).delete()

        return HttpResponse("success")
    else:
        return HttpResponse("<h1>test</h1>")


def comments_upload(request):
    context = {}
    if request.method == 'POST':
        print("收到post")
        type = request.POST.get('type')  # 测试是否能够接收到前端发来的name字段
        print(type)
        a = request.POST.get('data')  # 测试是否能够接收到前端发来的name字段
        b = a.replace('/', '')
        c = b.split(',')
        if (type == "del"):
            print("删除开始")
            for i in c:
                models.tongxunlu.objects.filter(id=int(i)).delete()
            # print(b)
            ret = {"删除成功"}

            return HttpResponse(ret)  # 最后返会给前端的数据，如果能在前端弹出框中显示我们就成功了
        elif (type == "new"):
            print("新建始")
            return HttpResponse("/tianxie/")

        elif (type == "edit"):
            data = models.tongxunlu.objects.filter(id=c[0])
            # t1 = loader.get_template('tianxie.html')
            # context = RequestContext(request, {'data': data})
            # return HttpResponse(t1.render(context))

            json_data = serializers.serialize('json', data)

            return HttpResponse(json_data)
    else:
        return HttpResponse("<h1>test</h1>")


@login_required
def xdh(request):
    context = {}
    if request.method == 'GET':
        case_name = request.GET.get('name')
        case_yuanxi = request.GET.get('yuanxi')
        case_dianhua = request.GET.get('dianhua')
        case_page = request.GET.get('page')
        print(case_name)
        print(case_page)
    elif request.method == 'POST':
        case_name = request.POST.get('name')
        case_yuanxi = request.POST.get('yuanxi')
        case_dianhua = request.POST.get('dianhua')
        case_page = request.POST.get('page')

    search_dict = dict()
    # 如果有这个值 就写入到字典中去

    if case_name:
        search_dict['xingming__contains'] = case_name

    if case_yuanxi:
        search_dict['yuan__contains'] = case_yuanxi
        # search_dict['xi__contains'] = case_yuanxi

    if case_dianhua:
        search_dict['dianhua__contains'] = case_dianhua

    contact_list = models.tongxunlu.objects.filter(**search_dict).values('id', 'yuan', 'xi', 'zhuanye', 'xingming',
                                                                         'zhiwu', 'dianhua', 'dizhi').order_by('id')

    paginator = Paginator(contact_list, 50)  # 每页显示25条
    try:
        contacts = paginator.page(case_page)
    except PageNotAnInteger:
        # 如果请求的页数不是整数，返回第一页。
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(1)
    context = {'contacts': contacts,
               'case_name': case_name,
               'case_yuanxi': case_yuanxi,
               'case_dianhua': case_dianhua,
               }
    return render(request, 'xdh2.html', context)


def tianxie(request, id=None):
    context = {}
    print("start")
    if request.method == 'GET':
        print("GET")
        case_id = request.GET.get('id')
        print(case_id)
        if case_id:
            print("case_id")
            print(case_id)
            data = models.tongxunlu.objects.filter(id=case_id).order_by('id')
            context = {'data': data}
            print(data)
        return render(request, 'tianxie.html', context)

    if request.method == 'POST':
        print("POST")
        case_yuan = request.POST.get('yuan')
        case_xi = request.POST.get('xi')
        case_zhuanye = request.POST.get('zhuanye')
        case_erjizhuanye = request.POST.get('erjizhuanye')
        case_xingming = request.POST.get('xingming')
        case_zhiwu = request.POST.get('zhiwu')
        case_zhize = request.POST.get('zhize')
        case_dianhua = request.POST.get('dianhua')
        case_dizhi = request.POST.get('dizhi')
        case_id = request.GET.get('id')
        case_youxiang = request.POST.get('youxiang')
        search_dict = dict()
        # 如果有这个值 就写入到字典中去
        if case_yuan:
            search_dict['yuan'] = case_yuan
        if case_xi:
            search_dict['xi'] = case_xi
        if case_xingming:
            search_dict['xingming'] = case_xingming
        if case_zhuanye:
            search_dict['zhuanye'] = case_zhuanye
        if case_erjizhuanye:
            search_dict['erjizhuanye'] = case_erjizhuanye
        if case_zhiwu:
            search_dict['zhiwu'] = case_zhiwu
        if case_zhize:
            search_dict['zhize'] = case_zhize
        if case_dianhua:
            search_dict['dianhua'] = case_dianhua
        if case_dizhi:
            search_dict['dizhi'] = case_dizhi
        if case_youxiang:
            search_dict['youxiang'] = case_youxiang
        if case_id:
            print("updata")
            models.tongxunlu.objects.filter(id=int(case_id)).update(**search_dict)
        else:
            print("new")
            models.tongxunlu.objects.create(**search_dict)
        context = {
            "msg": "succ",

        }
        messages.success(request, "保存成功")
        return render(request, 'tianxie.html', context)


def cdh(request):
    context = {}
    if request.method == 'GET':
        case_name = request.GET.get('name')
        case_page = request.GET.get('page')
    elif request.method == 'POST':
        case_name = request.POST.get('name')
        case_page = request.POST.get('page')
    if case_name:
        contact_list = models.tongxunlu.objects.filter(
            Q(xingming__contains=case_name) | Q(yuan__contains=case_name) | Q(xi__contains=case_name) | Q(
                zhuanye__contains=case_name) | Q(zhiwu__contains=case_name) | Q(dianhua__contains=case_name) | Q(
                dizhi__contains=case_name)
        ).values('yuan', 'xi', 'zhuanye', 'xingming', 'zhiwu', 'dianhua', 'dizhi').order_by('id')
    else:
        contact_list = models.tongxunlu.objects.all().values('yuan', 'xi', 'zhuanye', 'xingming', 'zhiwu', 'dianhua',
                                                             'dizhi').order_by('id')

    paginator = Paginator(contact_list, 2200)  # 每页显示25条
    yuanxi = models.yuan.objects.all().values('name', 'father_name')
    try:
        contacts = paginator.page(case_page)
    except PageNotAnInteger:
        # 如果请求的页数不是整数，返回第一页。
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(1)
    context = {'contacts': contacts,
               'case_name': yuanxi,
               'search_name': case_name,
               }
    return render(request, 'mylogin.html', context)
