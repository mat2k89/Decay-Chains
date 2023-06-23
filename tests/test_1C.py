import unittest
import src.test_interfaces as interface


class Test_1C_Filename_Generation(unittest.TestCase):
    '''
    Tests the code produced for Activity 1C
    Tests the generation of filenames
    '''

    def test_filename_short_numbers_zero_energy(self):
        '''
        Tests if the correct endf filename is returned when both the atomic number and atomic mass are one-digit numbers and the energy state is zero
        '''

        atomic_number = 1
        atomic_mass = 1
        energy_state = 0
        filename = interface.task_1c_endf_filename_from_nuclear_data(atomic_number, atomic_mass, energy_state)

        reference_filename = "dec-001_H_001.endf"

        self.assertEqual(filename, reference_filename, msg="When asked for the filename relating to an isomer with atomic number {}, atomic mass {}, and energy state {} your code returned {} when it should have returned {}".format(atomic_number, atomic_mass, energy_state, filename, reference_filename))

    def test_filename_medium_numbers_zero_energy(self):
        '''
        Tests if the correct endf filename is returned when both the atomic number and atomic mass are two digit numbers and the energy state is zero
        '''

        atomic_number = 18
        atomic_mass = 40
        energy_state = 0
        filename = interface.task_1c_endf_filename_from_nuclear_data(atomic_number, atomic_mass, energy_state)

        reference_filename = "dec-018_Ar_040.endf"

        self.assertEqual(filename, reference_filename, msg="When asked for the filename relating to an isomer with atomic number {}, atomic mass {}, and energy state {} your code returned {} when it should have returned {}".format(atomic_number, atomic_mass, energy_state, filename, reference_filename))

    def test_filename_long_numbers_zero_energy(self):
        '''
        Tests if the correct endf filename is returned when both the atomic number and atomic mass are three digit numbers and the energy state is zero
        '''
        atomic_number = 101
        atomic_mass = 247
        energy_state = 0
        filename = interface.task_1c_endf_filename_from_nuclear_data(atomic_number, atomic_mass, energy_state)

        reference_filename = "dec-101_Md_247.endf"

        self.assertEqual(filename, reference_filename, msg="When asked for the filename relating to an isomer with atomic number {}, atomic mass {}, and energy state {} your code returned {} when it should have returned {}".format(atomic_number, atomic_mass, energy_state, filename, reference_filename))

    def test_filename_non_zero_energy(self):
        '''
        Tests if the correct endf filename is returned when the energy state is non-zero
        '''
        atomic_number = 92
        atomic_mass = 235
        energy_state = 1
        filename = interface.task_1c_endf_filename_from_nuclear_data(atomic_number, atomic_mass, energy_state)

        reference_filename = "dec-092_U_235m1.endf"

        self.assertEqual(filename, reference_filename, msg="When asked for the filename relating to an isomer with atomic number {}, atomic mass {}, and energy state {} your code returned {} when it should have returned {}".format(atomic_number, atomic_mass, energy_state, filename, reference_filename))


class Test_1C_Isomer_Name_Generation(unittest.TestCase):
    '''
    Tests the code produced for Activity 1C
    Tests the generation of isomer names
    '''
    def test_isomer_name_short_numbers_zero_energy(self):
        '''
        Tests if the correct endf isomer name is returned when both the atomic number and atomic mass are one-digit numbers and the energy state is zero
        '''

        atomic_number = 1
        atomic_mass = 1
        energy_state = 0
        isomer_name = interface.task_1c_isomer_name_from_nuclear_data(atomic_number, atomic_mass, energy_state)

        reference_name = "H1"

        self.assertEqual(isomer_name, reference_name, msg="When asked for the isomer name relating to an isomer with atomic number {}, atomic mass {}, and energy state {} your code returned {} when it should have returned {}".format(atomic_number, atomic_mass, energy_state, isomer_name, reference_name))

    def test_isomer_name_medium_numbers_zero_energy(self):
        '''
        Tests if the correct endf isomer name is returned when both the atomic number and atomic mass are two digit numbers and the energy state is zero
        '''
        atomic_number = 18
        atomic_mass = 40
        energy_state = 0
        isomer_name = interface.task_1c_isomer_name_from_nuclear_data(atomic_number, atomic_mass, energy_state)

        reference_name = "Ar40"

        self.assertEqual(isomer_name, reference_name, msg="When asked for the isomer name relating to an isomer with atomic number {}, atomic mass {}, and energy state {} your code returned {} when it should have returned {}".format(atomic_number, atomic_mass, energy_state, isomer_name, reference_name))

    def test_isomer_name_long_numbers_zero_energy(self):
        '''
        Tests if the correct endf isomer name is returned when both the atomic number and atomic mass are three digit numbers and the energy state is zero
        '''
        atomic_number = 101
        atomic_mass = 247
        energy_state = 0
        isomer_name = interface.task_1c_isomer_name_from_nuclear_data(atomic_number, atomic_mass, energy_state)

        reference_name = "Md247"

        self.assertEqual(isomer_name, reference_name, msg="When asked for the isomer name relating to an isomer with atomic number {}, atomic mass {}, and energy state {} your code returned {} when it should have returned {}".format(atomic_number, atomic_mass, energy_state, isomer_name, reference_name))

    def test_isomer_name_non_zero_energy(self):
        '''
        Tests if the correct endf isomer name is returned when the energy state is non-zero
        '''

        atomic_number = 92
        atomic_mass = 235
        energy_state = 1
        isomer_name = interface.task_1c_isomer_name_from_nuclear_data(atomic_number, atomic_mass, energy_state)

        reference_name = "U235m1"

        self.assertEqual(isomer_name, reference_name, msg="When asked for the isomer name relating to an isomer with atomic number {}, atomic mass {}, and energy state {} your code returned {} when it should have returned {}".format(atomic_number, atomic_mass, energy_state, isomer_name, reference_name))


class Test_1C_Nuclear_Data_Generation(unittest.TestCase):
    '''
    Tests the code produced for Activity 1C
    Tests the generation of  nuclear data
    '''
    def test_nuclear_data_from_isomer_name_short(self):
        '''
        Tests if the correct nuclear data is returned when a short isomer name is provided
        '''

        isomer_name = "H1"
        nuclear_data = interface.task_1c_isomer_nuclear_data_from_name(isomer_name)

        reference_data = (1, 1, 0)

        self.assertTupleEqual(nuclear_data, reference_data, msg="When asked for the (atomic number, atomic mass, energy state) of the isomer {}, your code returned {} when it should have returned {}".format(isomer_name, nuclear_data, reference_data))

    def test_nuclear_data_from_isomer_name_long(self):
        '''
        Tests if the correct nuclear data is returned when a short isomer name is provided
        '''

        isomer_name = "Th232"
        nuclear_data = interface.task_1c_isomer_nuclear_data_from_name(isomer_name)

        reference_data = (90, 232, 0)

        self.assertTupleEqual(nuclear_data, reference_data, msg="When asked for the (atomic number, atomic mass, energy state) of the isomer {}, your code returned {} when it should have returned {}".format(isomer_name, nuclear_data, reference_data))

    def test_nuclear_data_from_isomer_name_non_zero_energy_state(self):
        '''
        Tests if the correct nuclear data is returned when a short isomer name is provided
        '''

        isomer_name = "In98m1"
        nuclear_data = interface.task_1c_isomer_nuclear_data_from_name(isomer_name)

        reference_data = (49, 98, 1)

        self.assertTupleEqual(nuclear_data, reference_data, msg="When asked for the (atomic number, atomic mass, energy state) of the isomer {}, your code returned {} when it should have returned {}".format(isomer_name, nuclear_data, reference_data))
