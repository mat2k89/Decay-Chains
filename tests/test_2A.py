import unittest
import src.test_interfaces as interface
import math


class Test_2A(unittest.TestCase):
    '''
    Tests the code produced for Activity 2A
    '''
    places = 2

    def compare_results(self, code_result, reference_result, output_times, initial_isomer_name, initial_isomer_population):
        '''
        Used to compare the results of the code being tested and the corresponding sample results
        '''

        test_description = "In this test, there were initially {} moles of {} at t=0.".format(initial_isomer_population, initial_isomer_name)

        # Check all reference isomer names are in the code results
        for reference_isomer_name in reference_result:
            self.assertIn(reference_isomer_name, code_result.keys(), msg="{} The isomer name {} should have been in the results, but it wasn't".format(test_description, reference_isomer_name))

        # Check all code isomer names are in the code results
        for code_isomer_name in code_result:
            self.assertIn(code_isomer_name, reference_result.keys(), msg="{} The isomer name {} appeared in the results, but it shouldn't be there".format(test_description, code_isomer_name))

        # Now we know the same isomer names are in each, tests the results of each isomer
        for isomer_name in code_result:
            for code_value, reference_value, time in zip(code_result[isomer_name], reference_result[isomer_name], output_times):
                self.assertAlmostEqual(code_value, reference_value, self.places, msg="{} When comparing the population of the isomer {} at t={}s, the code had a value of {} but the reference value was {}".format(test_description, isomer_name, time, code_value, reference_value))

    def test_stable(self):
        '''
        Tests the correct answer is returned when a stable isomer is provided
        '''

        initial_isomer_name = "H1"
        initial_isomer_population = 1
        output_times = [i * 0.1 for i in range(100)]

        code_results = interface.task_2_isomer_chain_from_initial_population(initial_isomer_name, initial_isomer_population, output_times)

        reference_results = {"H1": [1.0] * 100}

        self.compare_results(code_results, reference_results, output_times, initial_isomer_name, initial_isomer_population)

    def test_short_chain(self):
        '''
        Tests the correct answer is returned when an isomer which decays to a stable isomer is provided
        '''

        initial_isomer_name = "Ni65"
        initial_isomer_population = 10
        output_times = [i * 1000 for i in range(50)]
        decay_rate = 7.649040536823748e-05

        code_results = interface.task_2_isomer_chain_from_initial_population(initial_isomer_name, initial_isomer_population, output_times)

        # Calculate the reference results
        reference_results = {}
        reference_results["Ni65"] = list(map(lambda t: initial_isomer_population * math.exp(-t * decay_rate), output_times))
        reference_results["Cu65"] = list(map(lambda pop1: initial_isomer_population - pop1, reference_results["Ni65"]))

        print(reference_results)
        print(code_results)

        self.compare_results(code_results, reference_results, output_times, initial_isomer_name, initial_isomer_population)

    def test_long_chain(self):
        '''
        Tests the correct answer is returned when an isomer which decays twice before becoming a stable isomer is provided
        '''

        initial_isomer_name = "Pd98"
        initial_isomer_population = 100
        output_times = list(range(0, 1000, 100))

        code_results = interface.task_2_isomer_chain_from_initial_population(initial_isomer_name, initial_isomer_population, output_times)

        print(code_results)

        # Calculate the reference results using Analytic Results
        reference_results = {}
        decay_rate_Pd = math.log(2) / (17.7 * 60)
        decay_rate_Rh = math.log(2) / (8.72 * 60)
        reference_results["Pd98"] = list(map(lambda t: initial_isomer_population * math.exp(-t * decay_rate_Pd), output_times))

        reference_results["Rh98"] = list(map(lambda t: initial_isomer_population * decay_rate_Pd * (math.exp(-decay_rate_Pd * t) - math.exp(-decay_rate_Rh * t)) / (decay_rate_Rh - decay_rate_Pd), output_times))

        reference_results["Ru98"] = list(map(lambda pops_Pd_Rh: initial_isomer_population - pops_Pd_Rh[0] - pops_Pd_Rh[1], zip(reference_results["Pd98"], reference_results["Rh98"])))

        print(reference_results)
        print(code_results)

        self.compare_results(code_results, reference_results, output_times, initial_isomer_name, initial_isomer_population)
