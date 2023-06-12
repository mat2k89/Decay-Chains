import os
from src.element_info import ElementInfo

class IsomerData:
    @classmethod
    def filename_from_nuclear_data(cls, atomic_number, atomic_mass, energy_state=0):
        filename = "dec-{}_{}_{}".format(str(atomic_number).zfill(3), ElementInfo.get_element_symbol_from_atomic_number(atomic_number), str(atomic_mass).zfill(3))

        if energy_state:
            filename += "m{}".format(energy_state)

        filename += ".endf"

        return(filename)
    
    @classmethod
    def isomer_name_from_nuclear_data(cls, atomic_number, atomic_mass, energy_state=0):
        element_name = "{}{}".format(ElementInfo.get_element_symbol_from_atomic_number(atomic_number), atomic_mass)

        if energy_state:
            element_name += "m{}".format(energy_state)

        return(element_name)
    
    @classmethod
    def get_nuclear_data_from_name(cls, element_name):
        for i, char in enumerate(element_name):
            if char.isnumeric():
                n_char_symbol = i
                break

        symbol = element_name[:n_char_symbol]

        atomic_number = ElementInfo.get_atomic_number_from_element_symbol(symbol)

        non_zero_group = "m" in element_name[i:]

        if non_zero_group:
            for j, char in enumerate(element_name[n_char_symbol:]):
                if char.isalpha():
                    n_char_atomic_mass = j - n_char_symbol
                    break
            atomic_mass = int(element_name[n_char_symbol:n_char_symbol + n_char_atomic_mass])

            energy_group = int(element_name[n_char_symbol + n_char_symbol + 1])
        else:
            atomic_mass = int(element_name[n_char_symbol:])
            energy_group = 0

        return(atomic_number, atomic_mass, energy_group)


