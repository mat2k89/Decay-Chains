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
        isomer_name = "{}{}".format(ElementInfo.get_element_symbol_from_atomic_number(atomic_number), atomic_mass)

        if energy_state:
            isomer_name += "m{}".format(energy_state)

        return(isomer_name)
    
    @classmethod
    def get_nuclear_data_from_name(cls, isomer_name):
        for i, char in enumerate(isomer_name):
            if char.isnumeric():
                n_char_symbol = i
                break

        symbol = isomer_name[:n_char_symbol]

        atomic_number = ElementInfo.get_atomic_number_from_element_symbol(symbol)

        mass_and_group = isomer_name[n_char_symbol:].split("m")

        atomic_mass = int(mass_and_group[0])

        try:
            energy_state = int(mass_and_group[1])
        except IndexError:
            energy_state = 0

        return(atomic_number, atomic_mass, energy_state)
