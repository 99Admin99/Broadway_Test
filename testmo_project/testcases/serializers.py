from rest_framework import serializers
from .models import Project, TestCase, TestRun, TestResult

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = '__all__'

class TestRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestRun
        fields = '__all__'

class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = '__all__'
