# -*- coding: utf-8 -*-
from clipboard import get_paste_img_file
from util import *
import os
import sys
import time

debug = os.getenv('debug')=="true" and True or False
favor_yun = os.getenv('favor_yun') ##优先云代码
vardate = time.strftime('%Y/%-m/%-d',time.localtime(time.time()))
yuncode = ''  #指定云代码
upload_name='' #上传文件名
yuncodelist = [] #有效云code 都会上传
markdown_url = '' # 最终在剪贴板中的url
url_dict = {}

if len(sys.argv) > 1 and sys.argv[1]:
    yuncode = sys.argv[1]
    if yuncode:
        if checkConfig(yuncode) :
            yuncodelist.append(yuncode)
        else:
            notice("占不支持该云！%s" % yuncode)
else:
    if debug: notice("获取所有有用配置")
    yuncodelist = getAllConfiged()
    if debug : notice("有效配置 %s 个 " % (yuncodelist.__len__()),'debug')

if(yuncodelist.__len__() == 0 ):
     notice("未正确配置图床信息！请在Alfred workflow 配置！")
else:
    img_file, need_format, format = get_paste_img_file()
    if img_file is not None:
        upload_name = "%s/%s.%s" % (vardate,int(time.time() * 1000), format)
        if debug: notice("文件名：%s" % upload_name,'debug')
        for i in yuncodelist:
            if 'oss' == i:
                uploadOssObj('localfile',upload_name,img_file.name)
                url_dict['oss'] = getOssMKurl(upload_name)
            elif 'cos' ==i:
                uploadCosObj('localfile',upload_name,img_file.name)
                url_dict['cos'] = getCosMKurl(upload_name)
            elif 'imgur' == i:
                url_dict['imgur'] = uploadImgurObj('localfile',upload_name,img_file.name)
            else:
                if debug: notice("该云尚未实现！%s" % i)
        if url_dict:
            if favor_yun and url_dict.has_key(favor_yun):
                markdown_url = url_dict[favor_yun]
            else:
                markdown_url = url_dict.values()[0]

        if markdown_url:
            os.system("echo '%s' | pbcopy" % markdown_url)
            sys.stdout.write(markdown_url)
    else:
        notice("剪贴板无图片！")
    sys.stdout.write(yuncode)
