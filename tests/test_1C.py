import unittest
import src.test_interfaces as interface
import numpy as np
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Test_1C(unittest.TestCase):
    '''
    Tests the code produced for Activity 1C
    '''

    def test_short_numbers_zero_energy(self):
        '''
        Tests if the correct answer is returned when both the atomic number and atomic mass are one-digit numbers and the energy state is zero
        '''

        filename = interface.task_1c_endf_file_names_from_nuclear_data(1, 1, 0)

        self.assertEqual(filename, "dec-001_H_001.endf")

    def test_medium_numbers_zero_energy(self):
        '''
        Tests if the correct answer is returned when both the atomic number and atomic mass are two digit numbers and the energy state is zero
        '''

        filename = interface.task_1c_endf_file_names_from_nuclear_data(18, 40, 0)

        self.assertEqual(filename, "dec-018_Ar_040.endf")

    def test_long_numbers_zero_energy(self):
        '''
        Tests if the correct answer is returned when both the atomic number and atomic mass are three digit numbers and the energy state is zero
        '''

        filename = interface.task_1c_endf_file_names_from_nuclear_data(101, 247, 0)

        self.assertEqual(filename, "dec-101_Md_247.endf")

    def test_non_zero_energy(self):
        '''
        Tests if the correct answer is returned when the energy state is non-zero
        '''

        filename = interface.task_1c_endf_file_names_from_nuclear_data(92, 235, 1)

        self.assertEqual(filename, "dec-092_U_235m1.endf")