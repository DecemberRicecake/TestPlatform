import re
import json
from requests import Session


def get_paras():
    pass


def post_paras(v):
    try:
        return v['parameters'][0]['schema']
    except:
        return {}


def do_defs(definitions):

    for k in definitions:
        str_defs = json.dumps(definitions, ensure_ascii=False)
        regexp = r'\{\"\$ref\W*\/definitions\/' + k + '\"\}'
        str_defs = re.sub(regexp, json.dumps(definitions[k]['properties'], ensure_ascii=False), str_defs)
        definitions = json.loads(str_defs)
    return str_defs


def auto_gen_cases(swagger_url):
    res = Session().request('get', swagger_url).json()      # 获取数据
    data = res.get('paths')
    defs = res.get('definitions')
    res = {}
    for k, v in data.items():               # k是api url地址，也是接口名字
        for _k, _v in v.items():            # _k是请求方式
            if _k == 'get':
                pass
                paras = {}           # 后面再实现，get的入参
            elif _k == 'post':
                paras = post_paras(_v)       # 获取post的入参body data
            else:
                paras = {}

        res[k] = {
            'method': _k,
            'paras': paras,
        }


    # print(do_defs(defs))
    # ssss = do_defs(defs)
    # print(json.loads(ssss))


    # print(res)
    j_res = json.dumps(res)
    regexp = r'\{\"\$ref\W*\/definitions\/\w+\"\}'
    regular_result = re.findall(regexp, j_res)
    print(regular_result)
    for item in regular_result:
        step = re.findall(r'(\{\"\$ref\W*\/definitions\/)(\w+)(\"\})', item)[0][1]
        j_res = j_res.replace(item, json.dumps(defs[step]['properties'], ensure_ascii=False))
    print(j_res)



#     if p_para.find('#/definitions/') >= 0:
#         final_para = lookfor(p_para, defs)
#     return final_para
#
#
# def lookfor(v, defs):
#     v_list = re.split(r'[/]+', v)
#     if v_list[-1] in defs:
#         para_tmp = defs[v_list[-1]]['properties']
#         return para_tmp



if __name__ == '__main__':
    swagger_url1 = 'http://10.40.3.8:8111/swagger/docs/v1'
    auto_gen_cases(swagger_url1)
