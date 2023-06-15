import unittest
import src.test_interfaces as interface
import math
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Test_1A(unittest.TestCase):
    '''
    Tests the code produced for exercise 1B
    '''
    # The comparison tolerances to be used for these tests
    # They are deliberately quite loose, to keep the focus off technicalities of numerical accuracy of ivp solvers
    relative_tolerance = 1e-2
    absolute_tolerance = 1e-2

    def test_non_decaying_parent(self):
        '''
        Tests if the correct answer is returned when the parent isomer doesn't decay at all
        '''
        # Calculate the result from the supplied program
        program_result = interface.task_1a_simple_decay_chain_populations(list(range(0, 100, 1)), 1, 0)

        # Calculate the reference result
        reference_result1 = [1] * 100
        reference_result2 = [0] * 100

        # Compare the results
        self.assertListEqual(reference_result1, list(program_result[0]))
        self.assertListEqual(reference_result2, list(program_result[1]))

    def test_decaying_parent_slow_decay(self):
        '''
        Tests if the correct answer is returned when the parent isomer decays relatively slowly
        '''
        # Calculate test parameters
        output_times = [0.1 * i for i in range(0, 200)]
        decay_rate = 1e-3
        initial_value = 10

        # Calculate the result from the supplied program
        program_result = interface.task_1a_simple_decay_chain_populations(output_times, initial_value, decay_rate)

        # Calculate the reference results
        reference_result1 = list(map(lambda t : initial_value * math.exp(-t * decay_rate), output_times))
        reference_result2 = list(map(lambda pop1 : initial_value - pop1, reference_result1))

        # Compare the results
        for i in range(len(output_times)):
            self.assertAlmostEqual(reference_result1[i], program_result[0][i])
            self.assertAlmostEqual(reference_result2[i], program_result[1][i])

    def test_decaying_parent_fast_decay(self):
        '''
        Tests if the correct answer is returned when the parent isomer decays relatively slowly
        '''
        # Calculate test parameters
        output_times = np.arange(0, 50, 5)
        decay_rate = 1
        initial_value = 100

        # Calculate the result from the supplied program
        program_result = interface.task_1a_simple_decay_chain_populations(output_times, initial_value, decay_rate)

        # Calculate the result from the supplied program
        program_result = interface.task_1a_simple_decay_chain_populations(output_times, initial_value, decay_rate)

        # Calculate the reference results
        reference_result1 = list(map(lambda t : initial_value * math.exp(-t * decay_rate), output_times))
        reference_result2 = list(map(lambda pop1 : initial_value - pop1, reference_result1))

        # Compare the results
        for i in range(len(output_times)):
            self.assertAlmostEqual(reference_result1[i], program_result[0][i])
            self.assertAlmostEqual(reference_result2[i], program_result[1][i])