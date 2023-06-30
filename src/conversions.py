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
    files = os.listdir("../decay_data/")
    files = [file for file in files if file.startswith(prefix)] 
    
    # Keep the first file in the list
    filename = files[0]
    # Split the filename into a list of strings separated by "_"
    filename = filename.split("_")
    # Keep the second string of the list
    element = filename[1]

    # return the concatenation of the string, prefixed by dec- and suffixed by .endf
    return "dec-" + atomic_number + "_" + element + "_" + atomic_mass + energy_state + ".endf"

#create a main for that function
if __name__ == "__main__":
    # get number from command line arguments
    import sys
    atomic_number = int(sys.argv[1])
    atomic_mass = int(sys.argv[2])
    energy_state = int(sys.argv[3])

    print(filename_from_nuclear_data(atomic_number, atomic_mass, energy_state))