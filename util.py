# -*- coding: utf-8
import os
import pip
import imp

def notice(msg, title="万能图床",subtitle=''):
    ''' notoce message in notification center'''
    os.system('osascript -e \'display notification "%s" with title "%s" subtitle “%s”\'' % (msg, title,subtitle))

def install_and_load(package):
    pip.main(['install', package])

    f, fname, desc = imp.find_module(package)
    return imp.load_module(package, f, fname, desc)

"""
检查指定云是否配置正确
"""
def checkConfig(yuncode):
    if('oss' == yuncode):
        return checkOssConfig()
    elif('cos'== yuncode):
        return checkCosConfig()

"""
获取所以配置正确的云code
"""
def getAllConfiged():
    list = []
    if(checkOssConfig()):
        list.append('oss')
    if(checkCosConfig()):
        list.append('cos')
    return list


def checkOssConfig():
    AccessKeyId = os.getenv('oss.AccessKeyId')
    AccessKeySecret = os.getenv('oss.AccessKeySecret')
    bucket_name = os.getenv('oss.bucket_name')
    endpoint = os.getenv('oss.endpoint')
    if(AccessKeyId is not None
            and AccessKeySecret is not None
            and bucket_name is not None
            and endpoint is not None
    ):
        return True
    else:
        return False

def checkCosConfig():
    cos_bucket_name = os.getenv('cos_bucket_name')
    cos_is_cdn = os.getenv('cos_is_cdn')
    cos_region = os.getenv('cos_region')
    cos_secret_id = os.getenv('cos_secret_id')
    cos_secret_key = os.getenv('cos_secret_key')
    if(cos_bucket_name is not None
            and cos_is_cdn is not None
            and cos_region is not None
            and cos_secret_id is not None
            and cos_secret_key is not None
    ):
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        import oss2
    except:
        print("err p")