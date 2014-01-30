import unittest
import sys
sys.path.append("../")
from todopy import Task, TaskList


class TestTask(unittest.TestCase):

    def test_create_task(self):
        task_test = Task("Test_Title", "Test_Description")
        self.assertEqual(task_test.title, "Test_Title")
        self.assertEqual(task_test.description, "Test_Description")

    def test_create_tasklist(self):
        task_list = TaskList("My List")
        self.assertEqual(task_list.name, "My List")
        self.assertEqual(task_list.tasks, [])

    def test_add_tasks_to_tasklist(self):
        task1_test = Task("Test1_title", "Test1_description")
        task2_test = Task("Test2_title", "Test2_description")
        task_list = TaskList("My List")
        task_list.add(task1_test)
        task_list.add(task2_test)
        self.assertEqual(len(task_list), 2)

if __name__ == '__main__':
    unittest.main()
