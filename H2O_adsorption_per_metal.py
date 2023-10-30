import numpy as np

# Function to calculate the distance between two atoms
def calculate_distance(atom1, atom2):
    return np.linalg.norm(np.array(atom1) - np.array(atom2))

# Open a .dat file for writing the results
with open('PbO_bonds.dat', 'w') as output_file:
    # Loop through frames from i = 0 to 9999
    for i in range(10000):
        # Initialize variables to keep track of Pb and O coordinates
        pb_coords = []
        o_coords = []

        # Load the contents of the traj.xyz file for the current frame
        with open('traj.xyz', 'r') as file:
            lines = file.readlines()

        # Find the starting line for the current frame (each frame has 1002 rows)
        start_line = 2 + i * 1002
        end_line = start_line + 1002

        # Extract Pb and O coordinates for the current frame
        for line in lines[start_line:end_line]:
            tokens = line.split()
            if tokens[0] == 'Pb':
                pb_coords.append(list(map(float, tokens[1:])))
            elif tokens[0] == 'O':
                o_coords.append(list(map(float, tokens[1:])))

        # Calculate Pb-O distances and count the bonds
        num_pbo_bonds = 0
        for pb_atom in pb_coords:
            for o_atom in o_coords:
                distance = calculate_distance(pb_atom, o_atom)
                if distance <= 3.0:
                    num_pbo_bonds += 1

        # Write the frame number and the number of Pb-O bonds to the .dat file
        output_file.write(f"Frame {i}: {num_pbo_bonds}\n")

print("Calculation completed. Results saved in PbO_bonds.dat.")
