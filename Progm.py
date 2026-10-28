input_file_path = 'input.txt'
output_file_path = 'output.txt'

try:
    with open(input_file_path, 'r') as file:
        lines = file.readlines()
        
    total_lines = len(lines)
    print(f"Total number of lines in '{input_file_path}': {total_lines}")
    
    extracted_lines = lines[:2]
    
    with open(output_file_path, 'w') as file:
        file.writelines(extracted_lines)
        
    print(f"Successfully extracted the first two lines and wrote them to '{output_file_path}'.")

except FileNotFoundError:
    print(f"Error: The file '{input_file_path}' does not exist.")