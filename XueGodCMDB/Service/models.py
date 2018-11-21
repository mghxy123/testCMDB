#coding:utf-8
from django.db import models

class Service(models.Model):
    """
    服务器基本信息
    """
    ip = models.CharField(max_length = 32,verbose_name = "服务器ip")
    mac = models.CharField(max_length = 32,verbose_name = "服务器物理地址")
    cpu = models.CharField(max_length = 32,verbose_name = "服务器CPU")
    memory = models.CharField(max_length = 32,verbose_name = "服务器内存")
    hostname = models.CharField(max_length=32, verbose_name="服务器主机")
    isalive = models.CharField(max_length = 32,verbose_name = "服务器状态")


class CMDBUser(models.Model):
    """
    cmdb系统用户信息
    一个用户可以对应多台服务器，一台服务器可以对应多个用户
    所以他两之间是多对多关系
    """
    username = models.CharField(max_length = 32,verbose_name = "用户账号")
    password = models.CharField(max_length = 32,verbose_name = "用户密码")
    nickname = models.CharField(max_length = 32,verbose_name = "用户姓名")
    phone = models.CharField(max_length = 32,verbose_name = "用户手机号")
    email = models.EmailField(verbose_name = "用户邮箱")
    photo = models.ImageField(verbose_name = "用户头像",upload_to = "images")
    service = models.ManyToManyField(Service) #通过这个字段创建关联

class Service_Cpu(models.Model):
    """
    服务器CPU关联
    """
    service_id = models.IntegerField()
    cpu_id = models.IntegerField()

class Service_Memory(models.Model):
    """
    服务器内存关联
    """
    service_id = models.IntegerField()
    Memory_id = models.IntegerField()

from ckeditor_uploader.fields import RichTextUploadingField
class Api(models.Model):
    """
    	CMDB接口数据模型
   	 """
    name = models.CharField(max_length = 32,verbose_name = "接口名称")
    description = RichTextUploadingField(verbose_name = "接口描述") #采用富文本编辑器编写的接口描述字段
    doc = models.CharField(max_length = 64,verbose_name = "接口文档")

class LoginUser(models.Model):
    """
    登录用户
    """
    username = models.CharField(max_length = 32,verbose_name = "用户名")
    password = models.CharField(max_length=32, verbose_name="密码")

    def __str__(self):
        return self.username

class APIToken(models.Model):
    """
    服务器信息
    """
    value = models.CharField(max_length=32, verbose_name="token值")
    time = models.DateTimeField(verbose_name="生成时间")
    #这里一定要注意Django settings默认设置的时区
    user_id = models.CharField(max_length=32, verbose_name="token用户")


    def __str__(self):
        return self.value