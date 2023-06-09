import unittest
import src.test_interfaces as interface

class Test_0(unittest.TestCase):
    def test_always_return_0(self):
        '''This test checks 0 is always returned from the correct function'''
        self.assertEqual(interface.task_0_always_return_0(), 0)

    def test_addition_integers(self):
        '''This test checks addition always completes successfully when integers are provided'''
        self.assertEqual(interface.task_0_addition(1, 2), 3)

    def test_addition_floats(self):
        '''This test checks addition always completes successfully when integers are provided'''
        self.assertAlmostEqual(interface.task_0_addition(1.1, 2.2), 3.3)