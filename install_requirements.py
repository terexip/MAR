# install_requirements.py

import subprocess

def install_libraries(requirements_file):
    try:
        with open(requirements_file, 'r') as file:
            libraries = file.readlines()
        for library in libraries:
            library = library.strip()
            if library:
                print(f"Installing {library}...")
                try:
                    subprocess.check_call([f"pip install {library}"], shell=True)
                except subprocess.CalledProcessError:
                    print(f"Error installing {library}. Skipping to next.")
    except FileNotFoundError:
        print(f"Error: {requirements_file} not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    install_libraries("requirements.txt")
