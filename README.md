# 万能图床

这是一个方便的图片上传实用工具，可以**方便**, **快速**地把一张图片上传然后得到一个图片链接：

1. 极速截图转图片链接
2. 极速本地图片转图片链接
3. 极速网络图片转自定义图片链接

图片上传到图床之后，会自动把上传返回的链接放置到系统剪切版上，同时它对markdown格式有特殊的支持；整个过程只需要两步：

1. 截图/复制本地图片/复制网络图片链接
2. 快捷键 `cmd + opt + p` 进行上传

上传完成之后，返回的图片链接自动放入到系统剪切版中，可以直接使用`cmd + V` 使用。

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
|cos_is_cdn||
|cos_region||
|cos_secret_id||
|cos_secret_key||
|oss.AccessKeyId||
|oss.AccessKeySecret||
|oss.bucket_name||
|oss.endpoint||

## 预览

1. 极速截图转图片链接


2. 极速本地图片转图片链接


##  特性

- 直接将图片粘贴为markdown支持的图片链接
- 自动图片上传，失败通知栏通知
- 方便的图片上传工具 

## 使用

### 依赖


### 使用

首先请确认`request`库安装成功；然后导入Alfred工作流；记得**设置触发热键！**，保证不要与其他软件的热键冲突。

#### 通过截图上传

使用任意截图工具截图之后，在任意编辑器里面你需要插入markdown格式图片的地方，按下cmd + ctrl + V即可！

另外，markdwon里面的图片链接不是标准的markdown格式，而是html的img标签；这是因为在retina屏幕下截图的话，

#### 通过本地图片上传

如果你已经有一张图片了，希望上传到图床得到一个链接；通常的方式需要图床客户端或者浏览器插件，通过这个alfred插件：

直接复制本地图片，然后按下 就能得到图床的链接！

## TODO

