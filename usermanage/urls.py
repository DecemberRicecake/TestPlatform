from django.urls import include, path
from usermanage import views
from rest_framework_jwt.views import obtain_jwt_token

app_name = 'usermanage'

urlpatterns = [
    path('jwt-auth/', obtain_jwt_token),
    path('info/', views.userinfoView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('login/', views.LoginView.as_view())
]


