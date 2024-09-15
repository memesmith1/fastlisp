#this is some sample code that expresses how a proper fastlisp compiler should look when integrated into python
#obviosuly this current fastlisp compiler is composed shittly of gpt code
#also it is not intended to depend on tunney's blc compiler

#to make this work you have to change the path to the blc compiler to the path that you have the blc interpreter installed at
#in addition you have to change the path to the github folder where you did a git clone of the fastlisp repo

import subprocess

def run_compiler(input_string):
    # Define the local variables for the paths
    path_to_blc_compiler = "/path/to/blc/compiler"  # Adjust this to the actual BLC compiler path
    path_to_fastlisp_folder = "/path/to/fastlisp/folder/from/github"  # Adjust this to the actual Fastlisp folder path

    # Build the command string using the input string and paths
    fastlisp_command = f"bash {path_to_fastlisp_folder}/fastlisp-compiler-2.bash"
    full_command = f"{fastlisp_command} | {path_to_blc_compiler}"

    try:
        # Run the command and capture the output
        result = subprocess.run(
            full_command,
            input=input_string.encode(),  # Pipe the input_string to the command
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,  # Use shell=True to allow piping
            check=True  # Raise an error if the command fails
        )

        # Return stdout as a string
        return result.stdout.decode().strip()

    except subprocess.CalledProcessError as e:
        # Handle errors, return stderr if there's a problem
        return f"An error occurred: {e.stderr.decode().strip()}"

print(run_compiler("(lambda x x)(lambda x x)"))
