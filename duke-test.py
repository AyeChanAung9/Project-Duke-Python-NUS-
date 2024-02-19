import unittest
from typing import Any
from logic_model import logic


class TestTaskFunctions(unittest.TestCase):

    def setUp(self):
        self.task_list :list[dict[str,Any]]= []         # Set up initial tasks for testing

    def test_add_task_todo(self):
        # Add task todo
        logic.add_task(self.task_list,0, 'todo', 'unit_test')
        self.assertEqual(len(self.task_list), 1)
        self.assertEqual(self.task_list[0]['type'], 'todo')

    def test_add_task_deadline(self):
        # Add task deadline
        logic.add_task(self.task_list,0, 'deadline', 'submission', due_time= 'Oct 8')
        self.assertEqual(len(self.task_list), 1)
        self.assertEqual(self.task_list[0]['type'], 'deadline')

    def test_add_task_event(self):
        # Add task event
        logic.add_task(self.task_list,0, 'event', 'meeting', start_time= '11 am', end_time= '3 pm')
        self.assertEqual(len(self.task_list), 1)
        self.assertEqual(self.task_list[0]['type'], 'event')

    def test_add_task_appointment(self):
        # Add task appointment
        logic.add_task(self.task_list,0, 'appointment', 'meeting', start_time= '11 am', end_time= '3 pm',location= 'MICT')
        self.assertEqual(len(self.task_list), 1)
        self.assertEqual(self.task_list[0]['type'], 'appointment')

    def test_delete(self):
        # Add tasks to the list for testing
        logic.add_task(self.task_list,0, 'todo', 'unit_test')
        logic.add_task(self.task_list,1, 'deadline', 'submission', due_time='2023-10-10')
        logic.add_task(self.task_list,2, 'todo', 'work_out')

        # Delete the first task
        logic.delete(self.task_list,0)
        self.assertEqual(len(self.task_list), 2)
        self.assertEqual(self.task_list[0]['id'], 0)
        self.assertEqual(self.task_list[0]['type'], 'deadline')

    def test_mark(self):
        # Add a task and mark it
        logic.add_task(self.task_list,0, 'todo', 'unit_test')
        logic.mark(self.task_list,0)
        self.assertTrue(self.task_list[0]['done'])

    def test_unmark(self):
        # Add a task, mark it, then unmark it
        logic.add_task(self.task_list,0, 'todo', 'unit_test')
        logic.mark(self.task_list,0)
        logic.unmark(self.task_list,0)
        self.assertFalse(self.task_list[0]['done'])

    def test_convert(self):
        # Add a task and convert it from todo to Event
        logic.add_task(self.task_list,0, 'todo', 'unit_test')
        logic.convert(self.task_list,0, 'event')
        self.assertEqual(self.task_list[0]['type'], 'event')
        self.assertTrue('start_time' in self.task_list[0])
        self.assertTrue('end_time' in self.task_list[0])


if __name__ == '__main__':
    unittest.main()
