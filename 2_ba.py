def delete_lines_xyz(input_file, output_file, start_line, line_sum, repeat_interval):
    with open(input_file, 'r') as f_in:
        lines = f_in.readlines()

    num_lines = len(lines)
    num_iterations = num_lines // repeat_interval

    with open(output_file, 'w') as f_out:
        for i in range(num_iterations):
            iteration_start = i * repeat_interval
            iteration_end = (i + 1) * repeat_interval

            if iteration_end > num_lines:
                iteration_end = num_lines

            lines_to_keep = []
            for j in range(iteration_start, iteration_end):
                if j < iteration_start + start_line or j >= iteration_start + start_line + line_sum:
                    lines_to_keep.append(lines[j])

            f_out.writelines(lines_to_keep)

    print("Lines successfully deleted and file saved.")

# Usage example
input_filename = 'input.xyz'
output_filename = 'output1.xyz'
start_line = 505
line_sum = 240
repeat_interval = 1044

delete_lines_xyz(input_filename, output_filename, start_line, line_sum, repeat_interval)
