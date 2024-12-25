# Executes all Python scripts in a directory (and its subdirectories) and logs the paths of any scripts that fail.
import os
import subprocess

# Define the log file for errors
error_log_file = "error_log.txt"

# Clear the log file at the start
with open(error_log_file, "w") as log_file:
    log_file.write("")


def execute_scripts_in_directory(root_dir):
    """
    Recursively go through all subdirectories and run each Python script.
    If a script fails, log its path to the error log file.
    """
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".py"):
                script_path = os.path.join(subdir, file)
                try:
                    # Run the script and suppress its output
                    subprocess.run(
                        ["python3", script_path],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                        check=True,
                    )
                except subprocess.CalledProcessError:
                    # Log the error to the log file
                    with open(error_log_file, "a") as log_file:
                        log_file.write(f"Error in script: {script_path}\n")


if __name__ == "__main__":
    # Get the current directory
    current_directory = os.getcwd()
    execute_scripts_in_directory(current_directory)
