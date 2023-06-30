import os

def filename_from_nuclear_data(atomic_number: int, atomic_mass: int, energy_state: int):
    # convert int into string with 3 characters and leading zeroes, e.g., 001
    atomic_number = str(atomic_number).zfill(3)
    atomic_mass = str(atomic_mass).zfill(3)

    # prefix the energy state with m if it is not zero
    if energy_state == 0:
        energy_state = ""
    else:
        energy_state = "m" + str(energy_state)

    # concatenate atomic_number prefixed by "dec-"
    # e.g., dec-001_001
    prefix = "dec-" + atomic_number + "_" 
       
    # List the files in the ../decay_data/ directory that start with the prefix
    files = os.listdir("decay_data/")
    files = [file for file in files if file.startswith(prefix)] 
    
    # Keep the first file in the list
    filename = files[0]
    # Split the filename into a list of strings separated by "_"
    filename = filename.split("_")
    # Keep the second string of the list
    element = filename[1]

    # return the concatenation of the string, prefixed by dec- and suffixed by .endf
    return "dec-" + atomic_number + "_" + element + "_" + atomic_mass + energy_state + ".endf"

def isomer_name_from_nuclear_data(atomic_number: int, atomic_mass: int, energy_state: int):
    filename = filename_from_nuclear_data(atomic_number, atomic_mass, energy_state)

    # Split the filename into a list of strings separated by "_"
    filename = filename.split("_")
    # Keep the second and third strings of the list
    element = filename[1]
    mass = filename[2]

    # Remove trailing 0s
    mass = mass.lstrip("0")

    # Remove the .endf suffix
    mass = mass.split(".")
    mass = mass[0]
    
    return element + mass

def isomer_nuclear_data_from_name(isomer_name: str):
    # Get the first non digit character
    element = ""
    for char in isomer_name:
        if not char.isdigit():
            element += char
        else:
            break

    # Get all the following digits up to 'm' if it is present
    mass = ""
    for char in isomer_name:
        if char.isdigit():
            mass += char
        elif char == "m":
            break

    # Find the position of the 'm' character in the string if it is present
    try:
        m = isomer_name.index('m')
    except ValueError:
        m = -1

    # Get the last digit character if the character befors is 'm'
    energy_state = "0"
    if m != -1:
        energy_state = isomer_name[m+1]

    mass = str(mass).zfill(3)

    suffix = element + "_" + mass + ".endf"
    print(suffix)

    files = os.listdir("decay_data/")
    files = [file for file in files if file.endswith(suffix)] 
    # Keep the first file in the list
    filename = files[0]

    # Get the characters between the fifth and heighth
    atomic_number = filename[4:7]

    # Return a tuple of the three strings converted to integers
    return (int(atomic_number), int(mass), int(energy_state))

# Add main function to test the functions
if __name__ == "__main__":
    isomer_nuclear_data_from_name('Au197')
    isomer_nuclear_data_from_name('Cu70m2')