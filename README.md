# 万能图床

这是一个方便的剪贴板图片上传实用工具，且同时可上传至多个云（已实现同时上传至腾讯云和阿里云）
图片上传到图床之后，会自动把上传返回的链接放置到系统剪切版上，整个过程只需要两步：

1. 截图/复制本地图片/复制网络图片链接
2. 快捷键 `cmd + opt + p` 进行上传 (或者用调用alfred  输入关键字wn 或 tc 或你自定义的关键字 )


上传完成之后，返回的图片链接自动放入到系统剪切版中，可以直接使用`cmd + V` 使用。
![](http://wntc-1251220317.cossh.myqcloud.com/2019/4/4/1554350660039.gif)

----
## 支持列表
- [X] 阿里云oss
- [x] 腾讯云cos
- [x] imgur
- [ ] 七牛云
- [ ] 坚果云


## 运行环境

- macOs 10.13.6
- alfred v3.6.2 开通PowerPack
- python 2.7  mac系统默认
- python依赖库
    - PyObjC
    - cos-python-sdk-v5
    - oss2
    - requests


## 配置说明
![](http://wntc.oss-cn-shanghai.aliyuncs.com/2018/8/8/1533723079124.png)

|name|说明|
|--|--|
|debug|是否开启debug模式（会弹出多余信息）|
|keyword|自定义关键字启动万能图床|
|favor_yun|如果配置了多个云，配置该项会将该项的url拷贝到剪贴板里|
|cos_bucket_name|腾讯云存储桶名称|
|cos_is_cdn|是否使用cdn链接，前提是你开通了cdn|
|cos_cdn_domain|开通了cdn的域名 如cossh.myqcloud.com|
|cos_region|域名中的地域信息。枚举值参见 可用地域 文档，如：ap-beijing, ap-hongkong, eu-frankfurt 等|
|cos_secret_id|开发者拥有的项目身份识别 ID，用以身份认证|
|cos_secret_key|开发者拥有的项目身份密钥|
|oss.AccessKeyId|开发者拥有的项目身份识别 ID，用以身份认证|
|oss.AccessKeySecret|开发者拥有的项目身份密钥|
|oss.bucket_name||
|oss.endpoint||
|imgur_use|是否使用imgur（可选）因为需要翻墙速度慢大部分人默认可关闭  true/false|
|imgur_client_id||
|imgur_client_secret||
|imgur_access_token||
|imgur_refresh_token||
|imgur_album|可选|
|porxyconf|如：http://127.0.0.1:58555 代理设置 imgur可能需要翻墙|

#### 腾讯云
![](http://wntc-1251220317.cossh.myqcloud.com/2018/8/9/1533800822447.png)
https://cloud.tencent.com/document/product/436/7751
#### 阿里云
![](http://wntc-1251220317.cossh.myqcloud.com/2018/8/9/1533800963677.png)
https://help.aliyun.com/document_detail/52834.html?spm=a2c4g.11186623.6.677.84qFxY

---


##  特性
. 极速截图转图片链接
2. 极速本地图片转图片链接
3. 极速网络图片转自定义图片链接
- 直接将图片粘贴为markdown支持的图片链接
- 自动图片上传，失败通知栏通知
- 方便的图片上传工具 

## 使用

首先请确认依赖库安装成功；然后导入Alfred工作流；

#### 通过截图上传

使用任意截图工具截图之后，，按下 `cmd + opt + p` ，再在任意编辑器里面你需要插入markdown格式图片的地方，按下cmd + V即可！

#### 通过本地图片上传

如果你已经有一张图片了，希望上传到图床得到一个链接；
直接复制本地图片，然后按下 `cmd + opt + p`就能得到图床的链接！

## TODO
- 选中任何文件即可上传到云上
- 增加 七牛云、坚果云等

## 版本
###v1.1
- 增加imgur支持
- 增加cos的cdn域名自定义
###v1.0
- 增加腾讯云cos
###v0.1
-  可以使用阿里云oss

## 鸣谢
 - https://github.com/Imgur/imgurpython