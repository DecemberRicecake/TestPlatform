# -*- coding: utf-8 -*-
import datetime
import schedule
import threading
import time
from api.models import Task


def job(task_id):
    print('task: '+str(task_id), datetime.datetime.now())


def job_task(task_id):
    threading.Thread(target=job, args=(task_id,)).start()


def get_task_curr_info():
    task_curr_info = {}
    task_curr_list = []
    results = Task.objects.filter(status=1, taskType=1).values('id', 'taskType', 'standardTime', 'status')
    for r in results:
        task_curr_info[str(r['id'])] = r
        task_curr_list.append(r['id'])
    return task_curr_info, task_curr_list

if __name__ == '__main__':
        task_dict = {}
        task_info, task_list = {}, []
        while True:
            task_info_new, task_list_new = get_task_curr_info()
            ''' 任务的交集'''
            both_list = list(set(task_list_new) & set(task_list))
            add_list = list(set(task_list_new) - set(task_list))
            reduce_list = list(set(task_list) - set(task_list_new))

            ''' 处理任务时间有变化的场景'''
            if both_list:
                for both in both_list:
                    if task_info_new[str(both)]['standardTime'] != task_info[str(both)]['standardTime']:
                        add_list.append(both)
                        reduce_list.append(both)

            ''' 循环减任务(因为有重复的任务id，必须先减任务，后加任务，达到更新的目的)'''
            if reduce_list:
                for q in reduce_list:
                    schedule.cancel_job(task_dict[str(q)])
                    task_dict.pop(str(q))

            ''' 循环加任务'''
            if add_list:
                for p in add_list:
                    act_time = task_info_new[str(p)]['standardTime'][:5]
                    job_tmp = schedule.every().day.at(act_time).do(job_task, p)
                    # job_tmp = schedule.every(0).seconds.do(job_task, p)
                    task_dict[str(p)] = job_tmp

            print(add_list, reduce_list, both_list, datetime.datetime.now())
            schedule.run_pending()
            ''' 下个循环用，重新赋值'''
            task_info, task_list = task_info_new, task_list_new
            time.sleep(60)























