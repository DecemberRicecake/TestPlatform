from rest_framework import serializers
from api.models import Environment, Project, CustomParameters, Api


class EnvironmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Environment
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class CustomParametersSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomParameters
        fields = '__all__'


class ApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Api
        fields = '__all__'
        depth = 1


class ApiSerializerNodepth(serializers.ModelSerializer):

    class Meta:
        model = Api
        fields = '__all__'




