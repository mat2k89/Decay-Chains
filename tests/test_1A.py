import unittest
import src.test_interfaces as interface
import math

class Test_1A(unittest.TestCase):
    '''
    Tests the code produced for exercise 1B
    '''
    # The comparison tolerance to be used for these tests
    # It is deliberately loose, to keep the focus off technicalities of numerical accuracy of ivp solvers
    places = 2

    def test_non_decaying_parent(self):
        '''
        Tests if the correct answer is returned when the parent isomer doesn't decay at all
        '''
        # Calculate the result from the supplied program
        output_times = list(range(0, 100, 1))
        program_result = interface.task_1a_simple_decay_chain_populations(output_times, 1, 0)

        # Calculate the reference result
        reference_result1 = [1.0] * 100
        reference_result2 = [0.0] * 100

        # Compare the results
        for time, reference_value1, reference_value2, program_value1, program_value2 in zip(output_times, reference_result1, reference_result2, program_result[0], program_result[1]):
            self.assertAlmostEqual(reference_value1, program_value1, msg="There was a difference between the reference population ({}) and your population ({}) of  Isomer 1 at t={}s when Isomer 1 was a stable isomer".format(reference_value1, program_value1, time), places=self.places)
            self.assertAlmostEqual(reference_value2, program_value2, msg="There was a difference between the reference population ({}) and your population ({}) of  Isomer 2 at t={}s when Isomer 1 was a stable isomer".format(reference_value2, program_value2, time), places=self.places)

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
        for time, reference_value1, reference_value2, program_value1, program_value2 in zip(output_times, reference_result1, reference_result2, program_result[0], program_result[1]):
            self.assertAlmostEqual(reference_value1, program_value1, msg="There was a difference between the reference population ({}) and your population ({}) of  Isomer 1 at t={}s when Isomer 1 decays slowly".format(reference_value1, program_value1, time), places=self.places)
            self.assertAlmostEqual(reference_value2, program_value2, msg="There was a difference between the reference population ({}) and your population ({}) of  Isomer 2 at t={}s when Isomer 1 decays slowly".format(reference_value2, program_value2, time), places=self.places)

    def test_decaying_parent_fast_decay(self):
        '''
        Tests if the correct answer is returned when the parent isomer decays relatively slowly
        '''
        # Calculate test parameters
        output_times = [5 * i for i in range(0, 10)]
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
        for time, reference_value1, reference_value2, program_value1, program_value2 in zip(output_times, reference_result1, reference_result2, program_result[0], program_result[1]):
            self.assertAlmostEqual(reference_value1, program_value1, msg="There was a difference between the reference population ({}) and your population ({}) of  Isomer 1 at t={}s when Isomer 1 decays quickly".format(reference_value1, program_value1, time), places=self.places)
            self.assertAlmostEqual(reference_value2, program_value2, msg="There was a difference between the reference population ({}) and your population ({}) of  Isomer 2 at t={}s when Isomer 1 decays quickly".format(reference_value2, program_value2, time), places=self.places)