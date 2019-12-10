from django.shortcuts import render
# Create your views here.


def login(request):
    return render(request, "login.html")


def index(request):
    return render(request, "index.html")


def env_manage(request):
    return render(request, 'env_manage.html')


def project_manage(request):
    return render(request, 'project_manage.html')


def parameters(request):
    return render(request, 'parameters.html')


def api_list(request):
    return render(request, "api_list.html")


def add_api(request):
    return render(request, "add_api.html")


def case_list(request):
    return render(request, "case_list.html")


def task_list(request):
    return render(request, "task_list.html")


def report(request, task_id):
    return render(request, "report.html")





