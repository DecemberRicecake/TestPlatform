from django.db import models

# Create your models here.


# 环境表
class Environment(models.Model):
    Name = models.CharField(max_length=200)                     # 环境代理自定义名称
    ip = models.CharField(max_length=200)                       # 代理IP地址
    port = models.CharField(max_length=200)                     # 代理端口号
    createTime = models.DateTimeField(auto_now=True)            # 创建时间（自动获取当前时间）


# 项目表
class Project(models.Model):
    projectName = models.CharField(max_length=200)              # 项目名字
    people = models.CharField(max_length=200, null=True)        # 项目负责人
    description = models.CharField(max_length=200, null=True)   # 备注
    createTime = models.DateTimeField(auto_now=True)            # 创建时间（自动获取当前时间）


# 全局变量管理
class CustomParameters(models.Model):
    name = models.CharField(max_length=200)                     # 名称
    value = models.CharField(max_length=200)                    # 值
    description = models.CharField(max_length=200, null=True)   # 备注
    createTime = models.DateTimeField(auto_now=True)            # 创建时间（自动获取当前时间）


# 接口模板表
class Api(models.Model):
    apiName = models.CharField(max_length=200)                  # 接口名字
    url = models.CharField(max_length=200)                      # 接口url
    method = models.CharField(max_length=20)                    # 请求方式为POST
    # headers = models.CharField(max_length=200, null=True)             # 请求头
    project = models.ForeignKey(Project, on_delete=models.CASCADE)      # 项目ID
    env = models.ForeignKey(Environment, on_delete=models.CASCADE)      # 代理id
    questData = models.CharField(max_length=3000, null=True)    # 入参
    validators = models.CharField(max_length=3000, null=True)   # 校验内容
    extractFlag = models.BooleanField(default=False)            # 是否提取变量
    extracts = models.CharField(max_length=3000, null=True)     # 提取变量
    createTime = models.DateTimeField(auto_now=True)            # 创建时间（自动获取当前时间）


# 用例表
class TestCase(models.Model):
    caseName = models.CharField(max_length=200)                 # 用例名字
    apiIds = models.CharField(max_length=300, null=True)        # 接口id集合
    caseDesc = models.CharField(max_length=500, null=True)      # 描述
    createTime = models.DateTimeField(auto_now=True)            # 创建时间（自动获取当前时间）


# 任务表
class Task(models.Model):
    taskName = models.CharField(max_length=200)                 # 任务名字
    caseIds = models.CharField(max_length=300, null=True)       # 用例id集合
    taskType = models.IntegerField(default=0)                   # 任务类型（0手动、1每天定时）
    standardTime = models.CharField(max_length=200, null=True)  # 定时执行（每天执行的时间）
    status = models.IntegerField(default=0)                     # 任务状态（0:停止、1:运行中）
    hasReport = models.BooleanField(default=False)              # 是否已生成测试报告
    report = models.CharField(max_length=20000, null=True)      # 报告
    createTime = models.DateTimeField(auto_now=True)            # 创建时间（自动获取当前时间）


# 历史记录表
class ApiHistory(models.Model):
    taskId = models.IntegerField()                              # 任务id
    caseId = models.IntegerField()                              # 用例id
    apiId = models.IntegerField()                               # 接口id
    taskName = models.CharField(max_length=200)                 # 任务名字
    caseName = models.CharField(max_length=200)                 # 接口名字
    apiName = models.CharField(max_length=200)                  # 接口名字
    url = models.CharField(max_length=200)                      # 接口url
    questData = models.CharField(max_length=3000)               # 入参
    responseData = models.CharField(max_length=10000)           # 出参
    result = models.CharField(max_length=20, null=True)         # 测试结果
    startTime = models.DateTimeField(null=True)                 # 开始时间
    endTime = models.DateTimeField(null=True)                   # 结束时间
    createTime = models.DateTimeField(auto_now=True)            # 创建时间（自动获取当前时间）


