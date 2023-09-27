def delete_h_atoms_xyz(input_file, output_file):
    with open(input_file, 'r') as f_in:
        lines = f_in.readlines()

    num_lines_per_iteration = 1428  # Number of lines per iteration (including the header)

    with open(output_file, 'w') as f_out:
        for i in range(len(lines) // num_lines_per_iteration):
            iteration_start = i * num_lines_per_iteration
            iteration_end = (i + 1) * num_lines_per_iteration

            header_lines = lines[iteration_start:iteration_start + 2]
            atom_lines = lines[iteration_start + 2:iteration_end]

            filtered_atoms = [line for line in atom_lines if not (line.split()[0] == "Pb" and 28.5 <= float(line.split()[3]) <= 50)]

            f_out.writelines(header_lines)
            f_out.writelines(filtered_atoms)

    print("H atoms successfully deleted and file saved.")

# Usage example
input_filename = 'BA_I_term-pos-1.xyz'
output_filename = 'BA_I_surface.xyz'

delete_h_atoms_xyz(input_filename, output_filename)
