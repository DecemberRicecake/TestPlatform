import json

from django.contrib import auth
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response

from api.models import Api, TestCase, Environment, CustomParameters, Project, Task
from django.core.exceptions import ValidationError
from rest_framework import viewsets
from api.serializers import EnvironmentSerializer, ProjectSerializer, CustomParametersSerializer, ApiSerializer, \
    ApiSerializerNodepth
from api.viewsCommon import api_do_chart
from service.taskService import run_task


# Create your views here.


def api_get_index(request):
    if request.method == 'POST':
        status, all_data = api_do_chart()
        if status:
            data = {
                'num': {
                    'api_num': all_data['api_api'][-1],
                    'case_num': all_data['api_testcase'][-1],
                    'task_num': all_data['api_task'][-1],
                    'project_num': Project.objects.count()
                },
                'detail': {
                    'date_detail': all_data['date'],
                    'api_detail': all_data['api_api'],
                    'case_detail': all_data['api_testcase'],
                    'task_detail': all_data['api_task'],
                }
            }
            print(data)
            return JsonResponse({'status': 200, 'data': data})
        else:
            return JsonResponse({'status': 10021, 'message': 'data error'})


class EnvironmentSet(viewsets.ModelViewSet):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer


class ProjectSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CustomParametersSet(viewsets.ModelViewSet):
    queryset = CustomParameters.objects.all()
    serializer_class = CustomParametersSerializer


class ApiSet(viewsets.ModelViewSet):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('apiName',)

    def create(self, request):
        print(request.data)
        serialized = ApiSerializerNodepth(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_200_OK)
        else:
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        case = self.get_object()
        serialized = ApiSerializerNodepth(case, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_200_OK)
        else:
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class TestCaseSet(viewsets.ModelViewSet):
    queryset = CustomParameters.objects.all()
    serializer_class = CustomParametersSerializer


class TaskSet(viewsets.ModelViewSet):
    queryset = CustomParameters.objects.all()
    serializer_class = CustomParametersSerializer


# def api_add_api(request):
#     if request.method == 'POST':
#         received_data = json.loads(request.body.decode('utf-8'))
#         print(received_data)
#         apiName = received_data['apiName']
#         projectId = received_data['projectID']
#         envId = received_data['proxyID']
#         url = received_data['apiUrl']
#         method = received_data['method']
#         questData = received_data['questData']
#         validators = received_data['validators']
#         extractFlag = received_data['extractFlag']
#         extracts = received_data['extracts']
#         if apiName == '' or projectId == '' or envId == '' or url == '' or method == '' or questData == '' or extractFlag == '':
#             return JsonResponse({'status': 10021, 'message': 'parameter error'})
#         try:
#             Api.objects.create(apiName=apiName, project_id=projectId, env_id=envId, url=url, questData=questData,
#                                method=method, validators=validators, extractFlag=extractFlag, extracts=extracts)
#         except ValidationError:
#             return JsonResponse({'status': 10022, 'message': 'DB Error'})
#         else:
#             return JsonResponse({'status': 200, 'message': 'add api success'})
#
#
# def api_del_api(request):
#     if request.method == 'POST':
#         received_data = json.loads(request.body.decode('utf-8'))
#         print(received_data)
#         id = received_data['api_id']
#         if id == '':
#             return JsonResponse({'status': 10021, 'message': 'parameter error'})
#         try:
#             Api.objects.filter(id=id).delete()
#         except ValidationError:
#             return JsonResponse({'status': 10022, 'message': 'DB Error'})
#         else:
#             return JsonResponse({'status': 200, 'message': 'delete api success'})
#
#
# def api_get_api(request):
#     if request.method == 'POST':
#         received_data = json.loads(request.body.decode('utf-8'))
#         apiName = received_data['search_txt']
#         print(apiName)
#         datas = []
#         if apiName == '':
#             results = Api.objects.all().values('id', 'apiName', 'url', 'method', 'env__Name', 'project__projectName', 'createTime')
#         else:
#             results = Api.objects.filter(apiName__contains=apiName).values('id', 'apiName', 'url', 'method', 'env__Name', 'project__projectName', 'createTime')
#         if results:
#             for r in results:
#                 datas.append(r)
#         return JsonResponse({'status': 200, 'message': 'success', 'datas': datas})


def api_add_case(request):
    if request.method == 'POST':
        received_data = json.loads(request.body.decode('utf-8'))
        caseName = received_data['caseName']
        apiIds = received_data['apiIds']
        caseDesc = received_data['caseDesc']
        if caseName == '' or apiIds == '':
            return JsonResponse({'status': 10021, 'message': 'parameter error'})
        try:
            TestCase.objects.create(caseName=caseName, apiIds=apiIds, caseDesc=caseDesc)
        except ValidationError:
            return JsonResponse({'status': 10022, 'message': 'DB Error'})
        else:
            return JsonResponse({'status': 200, 'message': 'add case success'})


def api_del_case(request):
    if request.method == 'POST':
        received_data = json.loads(request.body.decode('utf-8'))
        print(received_data)
        id = received_data['case_id']
        if id == '':
            return JsonResponse({'status': 10021, 'message': 'parameter error'})
        try:
            TestCase.objects.filter(id=id).delete()
        except ValidationError:
            return JsonResponse({'status': 10022, 'message': 'DB Error'})
        else:
            return JsonResponse({'status': 200, 'message': 'delete case success'})


def api_get_case(request):
    if request.method == 'POST':
        received_data = json.loads(request.body.decode('utf-8'))
        caseName = received_data['search_txt']
        print(caseName)
        datas = []
        if caseName == '':
            results = TestCase.objects.all().values('id', 'caseName', 'apiIds', 'caseDesc', 'createTime')
        else:
            results = TestCase.objects.filter(caseName__contains=caseName).values('id', 'caseName', 'apiIds', 'caseDesc', 'createTime')
        if results:
            for r in results:
                datas.append(r)
        return JsonResponse({'status': 200, 'message': 'success', 'datas': datas})


def api_add_task(request):
    if request.method == 'POST':
        received_data = json.loads(request.body.decode('utf-8'))
        print(received_data)
        taskName = received_data['taskName']
        caseIds = received_data['caseIds']
        taskType = int(received_data['taskType'])
        standardTime = received_data['standardTime']
        if taskName == '':
            return JsonResponse({'status': 10021, 'message': 'parameter error'})
        try:
            Task.objects.create(taskName=taskName, caseIds=caseIds, taskType=taskType, standardTime=standardTime)
        except ValidationError:
            return JsonResponse({'status': 10022, 'message': 'DB Error'})
        else:
            return JsonResponse({'status': 200, 'message': 'add task success'})


def api_del_task(request):
    if request.method == 'POST':
        received_data = json.loads(request.body.decode('utf-8'))
        print(received_data)
        id = received_data['task_id']
        if id == '':
            return JsonResponse({'status': 10021, 'message': 'parameter error'})
        try:
            Task.objects.filter(id=id).delete()
        except ValidationError:
            return JsonResponse({'status': 10022, 'message': 'DB Error'})
        else:
            return JsonResponse({'status': 200, 'message': 'delete task success'})


def api_get_task(request):
    if request.method == 'POST':
        received_data = json.loads(request.body.decode('utf-8'))
        taskName = received_data['search_txt']
        print(taskName)
        datas = []
        taskType_dict = {0: '手动执行', 1: '每天定时'}
        if taskName == '':
            results = Task.objects.all().values('id', 'taskName', 'caseIds', 'taskType', 'standardTime', 'createTime', 'hasReport')
        else:
            results = Task.objects.filter(taskName__contains=taskName).values('id', 'taskName', 'caseIds', 'taskType', 'standardTime', 'createTime', 'hasReport')
        if results:
            for r in results:
                r['taskType'] = taskType_dict[r['taskType']]
                datas.append(r)
        return JsonResponse({'status': 200, 'message': 'success', 'datas': datas})


def api_run_task(request):
    if request.method == 'POST':
        received_data = json.loads(request.body.decode('utf-8'))
        taskid = received_data['taskid']
        if taskid == '':
            return JsonResponse({'status': 10021, 'message': 'task id is null'})
        if taskid != '':
            taskResults = Task.objects.get(id=taskid)
            pre_data = {}
            pre_data['taskname'] = taskResults.taskName  # 任务名字
            pre_data['caseids'] = [int(p) for p in taskResults.caseIds.split(',') if p]  # 任务中case的顺序列表
            caseResults = TestCase.objects.filter(id__in=pre_data['caseids'])
            if len(caseResults) != len(pre_data['caseids']):
                return JsonResponse({'status': 10022, 'message': 'case id is not exist'})
            else:
                queue = {}  # case中接口id的字典
                caseallids = []  # case中接口id列表的总集合
                casenamedic = {}  # case名字的字典
                for caseResult in caseResults:
                    casetmpid = []
                    for p in caseResult.apiIds.split(','):
                        if p:
                            caseallids.append(int(p))
                            casetmpid.append(int(p))
                    queue[str(caseResult.id)] = casetmpid
                    casenamedic[str(caseResult.id)] = caseResult.caseName
                pre_data['queue'] = queue
                pre_data['casenamedic'] = casenamedic
                caseonlyids = list(set(caseallids))  # 去除重复的id
                ApiResults = Api.objects.filter(id__in=caseonlyids)
                if len(ApiResults) != len(caseonlyids):
                    return JsonResponse({'status': 10023, 'message': 'api id is not exist'})
                else:
                    apidata = {}  # case中接口id的字典
                    for ApiResult in ApiResults:
                        apidata[str(ApiResult.id)] = {
                            'name': ApiResult.apiName,
                            'request': {
                                'url': ApiResult.url,
                                'proxies': {'http': ApiResult.env.ip + ':' + ApiResult.env.port},
                                'method': ApiResult.method,
                                'headers': {'content-type': 'application/json'},
                                'json': ApiResult.questData
                            },
                            'response': eval(ApiResult.validators),
                            'extractFlag': ApiResult.extractFlag,
                            'extracts': eval(ApiResult.extracts)
                        }
                    pre_data['apidata'] = apidata
                    status, baogao = run_task(pre_data)
                    if status:
                        Task.objects.filter(id=taskid).update(report=baogao, hasReport=True)
                        return JsonResponse({'status': 200, 'message': 'success'})
                    else:
                        return JsonResponse({'status': 10024, 'message': 'data format error'})


def api_get_report(request):
    if request.method == 'POST':
        received_data = json.loads(request.body.decode('utf-8'))
        taskid = received_data['taskid']
        if taskid == '':
            return JsonResponse({'status': 10021, 'message': 'task id is null'})
        if taskid != '':
            results = Task.objects.get(id=taskid).report
            return JsonResponse({'status': 200, 'message': 'success', 'datas': eval(results)})




