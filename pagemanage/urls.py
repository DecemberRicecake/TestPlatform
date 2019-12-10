from django.urls import path
from pagemanage import views

app_name = 'pagemanage'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('env_manage/', views.env_manage, name='env_manage'),
    path('project_manage/', views.project_manage, name='project_manage'),
    path('parameters/', views.parameters, name='parameters'),
    path('api_list/', views.api_list, name='api_list'),
    path('add_api/', views.add_api, name='add_api'),
    path('case_list/', views.case_list, name='case_list'),
    path('task_list/', views.task_list, name='task_list'),
    path('task/<int:task_id>/report/', views.report, name='report'),
]
