import json
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.db import connection
from django.contrib import auth
from django.http import HttpResponseRedirect
from datetime import datetime, timedelta

# Create your views here.


def api_do_chart():
    sql_lists = ['api_api', 'api_testcase', 'api_task']
    date_list = []  # 7天时间列表
    for i in range(7):
        date_list.append((datetime.now() + timedelta(days=(i - 6))).strftime("%Y-%m-%d"))
    # print(date_list)
    all_data = {}
    status = 1  #  处理数据状态是否正常

    try:
        cursor = connection.cursor()
        for sql_list in sql_lists:
            sql = "select date(createTime) as newTime , count(*) as num from " + sql_list + " group by day(createTime)"
            cursor.execute(sql)
            results = cursor.fetchall()
            date_num = []
            for i in range(len(date_list)):
                num_tmp = 0
                for row in results:
                    if str(row[0]) <= date_list[i]:
                        num_tmp += row[1]
                    else:
                        break
                date_num.append(num_tmp)
            all_data[sql_list] = date_num
        all_data['date'] = date_list
        cursor.close()
    except ValidationError:
        status = 0
        return status, all_data
    else:
        return status, all_data









