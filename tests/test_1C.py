import unittest
import src.test_interfaces as interface

class Test_1C(unittest.TestCase):
    '''
    Tests the code produced for Activity 1C
    '''

    def test_filename_short_numbers_zero_energy(self):
        '''
        Tests if the correct endf filename is returned when both the atomic number and atomic mass are one-digit numbers and the energy state is zero
        '''

        filename = interface.task_1c_endf_filename_from_nuclear_data(1, 1, 0)

        self.assertEqual(filename, "dec-001_H_001.endf")

    def test_filename_medium_numbers_zero_energy(self):
        '''
        Tests if the correct endf filename is returned when both the atomic number and atomic mass are two digit numbers and the energy state is zero
        '''

        filename = interface.task_1c_endf_filename_from_nuclear_data(18, 40, 0)

        self.assertEqual(filename, "dec-018_Ar_040.endf")

    def test_filename_long_numbers_zero_energy(self):
        '''
        Tests if the correct endf filename is returned when both the atomic number and atomic mass are three digit numbers and the energy state is zero
        '''

        filename = interface.task_1c_endf_filename_from_nuclear_data(101, 247, 0)

        self.assertEqual(filename, "dec-101_Md_247.endf")

    def test_filename_non_zero_energy(self):
        '''
        Tests if the correct endf filename is returned when the energy state is non-zero
        '''

        filename = interface.task_1c_endf_filename_from_nuclear_data(92, 235, 1)

        self.assertEqual(filename, "dec-092_U_235m1.endf")

    def test_isomer_name_short_numbers_zero_energy(self):
        '''
        Tests if the correct endf isomer name is returned when both the atomic number and atomic mass are one-digit numbers and the energy state is zero
        '''

        isomer_name = interface.task_1c_isomer_name_from_nuclear_data(1, 1, 0)

        self.assertEqual(isomer_name, "H1")

    def test_isomer_name_medium_numbers_zero_energy(self):
        '''
        Tests if the correct endf isomer name is returned when both the atomic number and atomic mass are two digit numbers and the energy state is zero
        '''

        isomer_name = interface.task_1c_isomer_name_from_nuclear_data(18, 40, 0)

        self.assertEqual(isomer_name, "Ar40")

    def test_isomer_name_long_numbers_zero_energy(self):
        '''
        Tests if the correct endf isomer name is returned when both the atomic number and atomic mass are three digit numbers and the energy state is zero
        '''

        isomer_name = interface.task_1c_isomer_name_from_nuclear_data(101, 247, 0)

        self.assertEqual(isomer_name, "Md247")

    def test_isomer_name_non_zero_energy(self):
        '''
        Tests if the correct endf isomer name is returned when the energy state is non-zero
        '''

        isomer_name = interface.task_1c_isomer_name_from_nuclear_data(92, 235, 1)

        self.assertEqual(isomer_name, "U235m1")

    def test_nuclear_data_from_isomer_name_short(self):
        '''
        Tests if the correct nuclear data is returned when a short isomer name is provided
        '''

        nuclear_data = interface.task_1c_isomer_nuclear_data_from_name("H1")

        self.assertTupleEqual(nuclear_data, (1, 1, 0))

    def test_nuclear_data_from_isomer_name_long(self):
        '''
        Tests if the correct nuclear data is returned when a short isomer name is provided
        '''

        nuclear_data = interface.task_1c_isomer_nuclear_data_from_name("Th232")

        self.assertTupleEqual(nuclear_data, (90, 232, 0))

    def test_nuclear_data_from_isomer_name_non_zero_energy_state(self):
        '''
        Tests if the correct nuclear data is returned when a short isomer name is provided
        '''

        nuclear_data = interface.task_1c_isomer_nuclear_data_from_name("In98m1")

        self.assertTupleEqual(nuclear_data, (49, 98, 1))