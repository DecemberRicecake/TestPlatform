import re
from datetime import datetime, timedelta

test1 = """{
   "name": "融管家是否取消金币",
   "request": {
       "url": "https://mi.rongzi.com/mi/home/GetIsCancelPayByGoldCoin",
       "method": "POST",
       "headers": {
           "content-type": "application/json"
       },
       "json": {
           "Head": {
                "Version": "4.0.0",
                "Token": "",
                "AppType": 1,
                "Build": ${nihao}
            },
            "Content": {
                "UserId": ""
            }
       }
   },
   "response": {
       "status_code": "#{code_3}",
       "Content": "False33",
       "Msg": "调用接口成功"
   }
}"""
#
# test2 = 'http://10.51.0.129:3002/task/15/report/'
#
#
#
# #variable_regexp = r"\$\{([\w]+)\}"
# variable_regexp = r"\#\{([\w]+)\}"
# pattern = re.compile(variable_regexp)
# result1 = pattern.findall(test1)
#
# # variable_regexp = r"\/([0-9]+)\/"
# # pattern = re.compile(variable_regexp)
# # result1 = pattern.findall(test2)
#
# print(result1)


import time

def dateRange(bgn, end):
    fmt = '%Y-%m-%d'
    bgn = int(time.mktime(time.strptime(bgn, fmt)))
    end = int(time.mktime(time.strptime(end, fmt)))
    return [time.strftime(fmt,time.localtime(i)) for i in range(bgn, end+1, 3600*24)]


list = []
for i in range(7):
    dddd = (datetime.now() + timedelta(days=(i-6))).strftime("%Y-%m-%d")
    list.append(dddd)
print(list)

