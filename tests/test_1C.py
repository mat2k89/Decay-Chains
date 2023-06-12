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
        Tests if the correct answer is returned when both the atomic number and atomic mass is a one-digit number and the energy group is zero
        '''


