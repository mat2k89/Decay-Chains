'''Edit the functions in this file as you complete the associated tasks.
Each test should utilise aspects of your code to complete the specified task.
These functions will be called by tests in the test suite to ensure you code is working properly.
'''

def task_0_always_return_0():
    '''This function should always return the value zero'''
    return(0)


def task_0_addition(a, b):
    '''This function should return the sum of the parameters a and b'''
    return(a + b)

def task_1a_simple_decay_chain_populations(output_times, initial_number_of_moles, decay_rate):
    '''
    Edit this function as part of Activity 1A
    This function should return the populations of two isomers at a number of output times as one decays into the other
    :param output_times: 1-D Numpy array of floats containing the times at which the populations of the isomers should be returned. The first time will always be 0. 
    :param initial_number_of_moles: The initial number of moles of Isomer 1 (the decaying isomer). Isomer 2 (the produced isomer) should have an initial population of 0.
    :param decay_rate: The decay rate of the decaying isomer in units of 1/s.
    :returns: Should return two sequences (e.g. lists, Tuples, 1D Numpy arrays) of length n where n is the number of output times. The first sequence contains the populations of Isomer 1 as a function of time, the second contains he populations of Isomer 1 as a function of time. Ine ach sequence, the value with index [0] in each array is the population the isomer at t=0 and the value with index [n] is the number of moles of the isomer at the end of the simulation.
    '''
    import src.system_pre_defined

    system = src.system_pre_defined.SystemPreDefined([initial_number_of_moles, 0], [decay_rate, 0])

    system.solve_system(output_times)

    return(system.y[0,:], system.y[1,:])

def task_1b_decay_data_from_filename(filepath):
    '''
    Edit this function as part of Activity 1B
    This function should accept the a filename of a file in the endf dataset and return its decay rate and decay mode
    :param filename: str containing the filename to be read from, with no path prefix (such as "dec-019_K_040.endf") 
    :returns: Should be a tuple containing the decay rate as a float units of 1/s, and the change to the atomic number and atomic mass caused by the decay as ints (e.g. (1.0, -2, 4) for alpha decay with a decay rate of 1.0/s)
    '''

    import src.isomer_data
    import os

    isomer_data = src.isomer_data.IsomerData(os.path.join("decay_data", filepath))

    return(isomer_data.decay_rate, isomer_data.decay_atomic_number_change, isomer_data.decay_atomic_mass_change)

def task_1c_endf_filename_from_nuclear_data(atomic_number, atomic_mass, energy_state):
    '''
    Edit this function as part of Activity 1C
    This function should accept the nuclear data of a isomer and return the corresponding endf file name (without any preceding path)
    Note, you do not need to check if the file actually exists
    :param atomic_number: int providing the atomic number 
    :param atomic_mass: int providing the atomic mass
    :param energy state: int providing the energy_state_number 
    :returns: Should be a string containing the endf filename  corresponding to the nuclear data (without any preceding path), e.g. dec-006_C_016
    '''

    import src.isomer_data

    return(src.isomer_data.IsomerData.filename_from_nuclear_data(atomic_number, atomic_mass, energy_state))

def task_1c_isomer_name_from_nuclear_data(atomic_number, atomic_mass, energy_state):
    '''
    Edit this function as part of Activity 1C
    This function should accept the nuclear data of a isomer and return the corresponding isomer name
    :param atomic_number: int providing the atomic number 
    :param atomic_mass: int providing the atomic mass
    :param energy state: int providing the energy_state_number 
    :returns: Should be a string containing the isomer name  corresponding to the nuclear data, e.g. C16m1
    '''

    import src.isomer_data

    return(src.isomer_data.IsomerData.isomer_name_from_nuclear_data(atomic_number, atomic_mass, energy_state))

def task_1c_isomer_nuclear_data_from_name(isomer_name):
    '''
    Edit this function as part of Activity 1C
    This function should accept the name of an isomer and return its nuclear data
    :param isomer_name: str containing the name of the nucleus (e.g. "Na24m1") 
    :returns: Should be a tuple containing the atomic number, atomic mass and energy state number as ints
    '''

    import src.isomer_data

    return(src.isomer_data.IsomerData.get_nuclear_data_from_name(isomer_name))