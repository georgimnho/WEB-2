from django.test import TestCase
from .models import Task, Category, Priority

class TaskModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Work')
        self.priority = Priority.objects.create(level='High')
        self.task = Task.objects.create(
            title='Test Task',
            description='Test description',
            completed=False,
            category=self.category,
            priority=self.priority
        )

    def test_task_str(self):
        self.assertEqual(str(self.task), 'Test Task')

    def test_task_category(self):
        self.assertEqual(self.task.category.name, 'Work')

    def test_task_priority(self):
        self.assertEqual(self.task.priority.level, 'High')

        #usar:  python manage.py test
