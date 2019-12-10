import json
import re
from api.models import CustomParameters
from service import apiService


def run_task(pre_data):
    status = 1
    baogao = {}
    baogao['task_name'] = pre_data['taskname']
    baogao['results'] = []
    baogao['case_detail'] = []
    baogao['api_detail'] = {}
    casecount = 0
    caseids = pre_data['caseids']
    for caseid in caseids:
        apiids = pre_data['queue'][str(caseid)]
        casecount += 1
        baogao['api_detail']['case' + str(casecount)] = []
        local_params = {}  # 用例级别的局部变量,初始化
        caseflag = True
        apicount = 0
        for apiid in apiids:
            apicount += 1
            testdata = pre_data['apidata'][str(apiid)]
            if caseflag:
                newjson = replace(testdata["request"]["json"], local_params)  # 替换所有变量
                try:
                    testdata["request"]["json"] = eval(newjson)  # 刷新json数据
                except:
                    status = 0
                    return status, baogao
                success, diff_content, resp_body = apiService.run_testcase(testdata)
                caseflag = success
                if success:
                    apiflag = 1
                    if testdata["extractFlag"]:
                        local_params.update(save_local_params(json.dumps(resp_body, separators=(',', ':'), ensure_ascii=False), testdata["extracts"]))  # 存局部变量
                else:
                    apiflag = 0
            else:
                apiflag = 2
                resp_body = {}
            baogao['results'].append(apiflag)
            baogao['api_detail']['case'+str(casecount)].append({'apiNO': apicount, 'apiName': testdata['name'], 'result': apiflag, 'request': testdata['request']['json'], 'response': resp_body})
        if caseflag:
            caseflag = 1
        else:
            caseflag = 0
        baogao['case_detail'].append({'caseNO': casecount, 'name': pre_data['casenamedic'][str(caseid)], 'result': caseflag})
    baogao = result_count(baogao)  # 统计结果数量
    return status, baogao


def result_count(baogao):
    baogao['num'] = {}
    baogao['num']['Total'] = len(baogao['results'])
    baogao['num']['Failed'] = baogao['results'].count(0)
    baogao['num']['Passed'] = baogao['results'].count(1)
    baogao['num']['Skipped'] = baogao['results'].count(2)
    return baogao


def load_global_params():
    global_params = {}
    results = CustomParameters.objects.all()
    if results:
        for r in results:
            global_params[r.name] = r.value
    return global_params


def replace(data, local_params):
    data_g = replace_g(data)
    data_l = replace_l(data_g, local_params)
    return data_l


def replace_g(data):  # 替换json中的的全局变量
    global_params = load_global_params()  # 加载全局变量
    if global_params:
        variable_regexp = "\$\{([\w]+)\}"
        pattern = re.compile(variable_regexp)
        params_list = pattern.findall(data)
        if params_list:
            for param in params_list:
                if param in global_params.keys():
                    data = re.sub('\$\{' + param + '\}', global_params[param], data)
    return data


def save_local_params(resp_body, extracts):
    local_params_dict = {}
    for key, value in extracts.items():
        variable_regexp = value
        pattern = re.compile(variable_regexp)
        params_list = pattern.findall(resp_body)
        if params_list:
            local_params_dict[key] = params_list
    return local_params_dict


def replace_l(data, local_params):  # 替换局部变量
    if local_params:
        variable_regexp = "\#\{(\w+)\[(\d+)\]\}"
        pattern = re.compile(variable_regexp)
        params_list = pattern.findall(data)
        if params_list:
            for param in params_list:
                if param[0] in local_params.keys():
                    data = re.sub('#\{' + param[0] + '\[' + param[1] + '\]\}', local_params[param[0]][int(param[1])], data)
    return data






