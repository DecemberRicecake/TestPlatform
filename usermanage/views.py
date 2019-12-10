import json
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.viewsets import ViewSet
from rest_framework_jwt.views import obtain_jwt_token

from usermanage.models import User

# Create your views here.
from usermanage.serializers import UserSerializer


class RegisterView(APIView):
    pass


class LoginView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        received_data = json.loads(request.body.decode('utf-8'))
        print(received_data)
        username = received_data['username']
        password = received_data['password']
        user = User.objects.filter(username=username).first()
        if user:
            # check_password(password, user.password)
            pass
        else:
            return JsonResponse({'status': 10021, 'message': 'username or password error!'})
        # user = auth.authenticate(username=username, password=password)


class userinfoView(APIView):
    def get(self, request):
        query_set = User.objects.all()
        user_ser = UserSerializer(query_set, many=True)
        return Response(user_ser.data)

