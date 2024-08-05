from django.shortcuts import render
from .models import Project

# Create your views here.
from rest_framework import viewsets
from .models import Project, TestCase, TestRun, TestResult
from .serializers import ProjectSerializer, TestCaseSerializer, TestRunSerializer, TestResultSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TestCaseViewSet(viewsets.ModelViewSet):
    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializer

class TestRunViewSet(viewsets.ModelViewSet):
    queryset = TestRun.objects.all()
    serializer_class = TestRunSerializer

class TestResultViewSet(viewsets.ModelViewSet):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'testcases/templates/project_list.html', {'projects': projects})
