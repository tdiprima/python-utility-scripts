import random

def scramble_lines(file_path):
    # Read lines from the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Shuffle the lines
    random.shuffle(lines)

    # Print the shuffled lines
    for line in lines:
        print(line.strip())

# Replace 'your_file.txt' with the actual file path you want to process
file_path = 'your_file.txt'
scramble_lines(file_path)
