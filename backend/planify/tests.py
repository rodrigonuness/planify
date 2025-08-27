from django.test import TestCase, Client
from .models import Task, Upload
from django.core.files.uploadedfile import SimpleUploadedFile

class SmokeTest(TestCase):
    def test_basic(self):
        print("SmokeTest is running!")
        self.assertEqual(1, 1)

class TaskModelTest(TestCase):
    def test_create_task(self):
        task = Task.objects.create(
            day_of_week='Monday',
            time='08:00',
            description='Test task',
            completed=False
        )
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(task.description, 'Test task')

class UploadModelTest(TestCase):
    def test_create_upload(self):
        file = SimpleUploadedFile("test.xlsx", b"file_content")
        upload = Upload.objects.create(file=file)
        self.assertEqual(Upload.objects.count(), 1)

class APITest(TestCase):
    def setUp(self):
        self.client = Client()
        Task.objects.create(
            day_of_week='Monday',
            time='08:00',
            description='API task',
            completed=False
        )

    def test_get_today_tasks(self):
        response = self.client.get('/api/tasks/today/')
        print("GET /api/tasks/today/ status:", response.status_code)
        print("Response data:", response.json() if response.status_code == 200 else response.content)
        self.assertIn(response.status_code, [200, 404])

    def test_get_all_tasks(self):
        response = self.client.get('/api/tasks/')
        print("GET /api/tasks/ status:", response.status_code)
        print("Response data:", response.json() if response.status_code == 200 else response.content)
        self.assertEqual(response.status_code, 200)

    def test_patch_complete_task(self):
        task = Task.objects.first()
        response = self.client.patch(f'/api/tasks/{task.id}/complete/', data={'completed': True}, content_type='application/json')
        print(f"PATCH /api/tasks/{task.id}/complete/ status:", response.status_code)
        print("Response data:", response.json() if response.status_code == 200 else response.content)
        self.assertEqual(response.status_code, 200)
