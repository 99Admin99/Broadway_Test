from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Project, TestCase as TestCaseModel, TestRun, TestResult
from django.contrib.auth.models import User

class TestCaseManagementTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.project = Project.objects.create(name='Test Project', description='Test Description')
        self.test_case = TestCaseModel.objects.create(
            title='Test Case 1',
            description='Test Description',
            project=self.project,
            created_by=self.user
        )
        self.test_run = TestRun.objects.create(
            name='Test Run 1',
            project=self.project,
            created_by=self.user
        )
        self.test_result = TestResult.objects.create(
            test_case=self.test_case,
            test_run=self.test_run,
            status='Passed',
            executed_by=self.user
        )

    def test_project_creation(self):
        self.assertEqual(self.project.name, 'Test Project')

    def test_testcase_creation(self):
        self.assertEqual(self.test_case.title, 'Test Case 1')

    def test_testrun_creation(self):
        self.assertEqual(self.test_run.name, 'Test Run 1')

    def test_testresult_creation(self):
        self.assertEqual(self.test_result.status, 'Passed')
