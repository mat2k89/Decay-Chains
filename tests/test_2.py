import unittest
import src.test_interfaces as interface

class Test_2(unittest.TestCase):
    '''
    Tests the code produced for Activity 2
    '''
    places = 2

    def compare_results(self, code_result, reference_result, output_times):
        '''
        Used to compare the results of the code being tested and the corresponding sample results
        '''

        # Check all reference isomer names are in the code results
        for reference_isomer_name in reference_result:
            self.assertIn(reference_isomer_name, code_result.keys(), msg="The isomer name {} should have been in the results, but it wasn't".format(reference_isomer_name))

        # Check all code isomer names are in the code results
        for code_isomer_name in code_result:
            self.assertIn(code_isomer_name, reference_result.keys(), msg="The isomer name {} appeared in the results, but it shouldn't be there".format(code_isomer_name))

        # Now we know the same isomer names are in each, tests the results of each isomer
        for isomer_name in code_result:
            for code_value, reference_value, time in zip(code_result[isomer_name], reference_result[isomer_name], output_times):
                self.assertAlmostEqual(code_value, reference_value, self.places, msg="When compared the population of the isomer {} at t={}s, the code had a value of {} but the reference value was {}".format(isomer_name, time, code_value, reference_value))

    def test_stable(self):
        '''
        Tests the correct answer is returned when a stable isomer is provided
        '''

        initial_isomer_name = "H1"
        initial_isomer_population = 1
        output_times = [i * 0.1 for i in range(100)]

        code_results = interface.task_2_isomer_chain_from_initial_population(initial_isomer_name, initial_isomer_population, output_times)

        reference_results = {"H1":[1.0] * 100}

        self.compare_results(code_results, reference_results, output_times)

    def test_short_chain(self):
        '''
        Tests the correct answer is returned when an isomer which decays to a stable isomer is provided
        '''

        initial_isomer_name = "Ni65"
        initial_isomer_population = 10
        output_times = [i * 1000 for i in range(50)]

        code_results = interface.task_2_isomer_chain_from_initial_population(initial_isomer_name, initial_isomer_population, output_times)

        reference_results = {"H1":[1.0] * 100}

        self.compare_results(code_results, reference_results, output_times)



        