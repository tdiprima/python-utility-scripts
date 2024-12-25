# Logs the paths of directories with spaces in their names, starting from the current directory, into a text file.
import os

# Define the log file for directories with spaces
spaces_log_file = "directories_with_spaces.txt"

# Clear the log file at the start
with open(spaces_log_file, "w") as log_file:
    log_file.write("")

def find_directories_with_spaces(root_dir):
    """
    Recursively check all directories for spaces in their names.
    Log directories with spaces to a file.
    """
    for subdir, dirs, _ in os.walk(root_dir):
        for directory in dirs:
            if " " in directory:
                dir_path = os.path.join(subdir, directory)
                # Log the directory with spaces to the log file
                with open(spaces_log_file, "a") as log_file:
                    log_file.write(f"Directory with space: {dir_path}\n")

if __name__ == "__main__":
    # Get the current directory
    current_directory = os.getcwd()
    find_directories_with_spaces(current_directory)
