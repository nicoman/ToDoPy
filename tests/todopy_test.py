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
        task1_test = Task("Test", "Test")
        task2_test = Task("Test", "Test")
        task_list = TaskList(task1_test, task2_test)

if __name__ == '__main__':
    unittest.main()
