from django.urls import include, path
from api import views
from rest_framework.routers import SimpleRouter, DefaultRouter
router = DefaultRouter()

router.register(r'environment', views.EnvironmentSet)
router.register(r'project', views.ProjectSet)
router.register(r'customparameters', views.CustomParametersSet)
router.register(r'api', views.ApiSet)
router.register(r'testcase', views.TestCaseSet)
router.register(r'task', views.TaskSet)

app_name = 'api'


from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view),
    path('api/get_index/', views.api_get_index, name='api_get_index'),


    path('api/add_api/', views.api_add_api, name='api_add_api'),
    path('api/del_api/', views.api_del_api, name='api_del_api'),
    path('api/get_api/', views.api_get_api, name='api_get_api'),

    path('api/add_case/', views.api_add_case, name='api_add_case'),
    path('api/del_case/', views.api_del_case, name='api_del_case'),
    path('api/get_case/', views.api_get_case, name='api_get_case'),

    path('api/add_task/', views.api_add_task, name='api_add_task'),
    path('api/del_task/', views.api_del_task, name='api_del_task'),
    path('api/get_task/', views.api_get_task, name='api_get_task'),

    path('api/run_task/', views.api_run_task, name='api_run_task'),

    path('api/get_report/', views.api_get_report, name='api_get_report'),

]
