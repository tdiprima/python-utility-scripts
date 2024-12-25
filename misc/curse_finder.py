# Searches for and prints occurrences of certain profanities in the files of all subdirectories of a specified base directory.
import os
import subprocess

home_directory = os.environ["HOME"]
# home_directory = os.path.expanduser("~")

# Define the base directory to search
base_directory = home_directory + "/trabajo/parallel-lines"

# Define the bash command pattern
ack_command = r'ack -iw --ignore-dir=node_modules --ignore-dir=.git --ignore-dir=data --ignore-dir=venv --ignore-dir=examples "wtf|wth|fxck|f#ck|fuck|sh!t|sh1t|shit|ass|@ss|crap|suck|stupid"'

def run_ack_on_directories(directory):
    for root, dirs, _ in os.walk(directory):
        for sub_dir in dirs:
            sub_dir_path = os.path.join(root, sub_dir)
            try:
                # Run the ack command on the current sub-directory
                print(f"\nRunning command on: {sub_dir_path}")
                completed_process = subprocess.run(
                    f'{ack_command} "{sub_dir_path}"',
                    shell=True,
                    text=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                # Print the output if matches are found
                if completed_process.stdout:
                    print(f"Matches in {sub_dir_path}:\n{completed_process.stdout}")
                if completed_process.stderr:
                    print(f"Errors in {sub_dir_path}:\n{completed_process.stderr}")
            except Exception as e:
                print(f"Error processing {sub_dir_path}: {e}")

if __name__ == "__main__":
    run_ack_on_directories(base_directory)
