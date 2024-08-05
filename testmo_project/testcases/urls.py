from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TestCaseViewSet, TestRunViewSet, TestResultViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'testcases', TestCaseViewSet)
router.register(r'testruns', TestRunViewSet)
router.register(r'testresults', TestResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.project_list, name='project_list'),
]
