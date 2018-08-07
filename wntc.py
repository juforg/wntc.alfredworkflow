# -*- coding: utf-8 -*-
from clipboard import get_paste_img_file
from util import *
import os
import subprocess
import sys
import time
try:
    import oss2
except:
    oss2 = install_and_load('oss2')



"""
oss 阿里云配置
"""
AccessKeyId = os.getenv('oss.AccessKeyId')
AccessKeySecret = os.getenv('oss.AccessKeySecret')
bucket_name = os.getenv('oss.bucket_name')
endpoint = os.getenv('oss.endpoint')



favor_yun = os.getenv('favor_yun') ##优先云代码
vardate = time.strftime('%Y/%-m/%-d',time.localtime(time.time()))
yuncode = ''  #指定云代码
upload_name='' #上传文件名
yuncodelist = [] #有效云code
if len(sys.argv) > 1:
    yuncode = sys.argv[1]
    if(checkConfig(yuncode)):
        yuncodelist.append(yuncode)
else:
    yuncodelist = getAllConfiged()
if(yuncodelist.__len__() == 0 ):
     notice("未正确配置图床信息！")
else:
    img_file, need_format, format = get_paste_img_file()
    if img_file is not None:
        upload_name = "%s.%s" % (int(time.time() * 1000), format)
    sys.stdout.write(upload_name)
