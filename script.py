#Made by MinoDab492

import os
import sys
import subprocess
from git import Repo

# Helper functions
def run_command(command):
    """ Run a system command and handle errors. """
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        raise Exception(f"Command failed: {command}")

def download_repo(repo_url, dest_dir):
    """ Clone a GitHub repo """
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    Repo.clone_from(repo_url, dest_dir)

def list_files(startpath):
    """ List all files in the directory tree """
    with open("file_list.txt", "w") as f:
        for root, dirs, files in os.walk(startpath):
            for name in files:
                f.write(os.path.join(root, name) + '\n')

def main():
    if len(sys.argv) != 2 or sys.argv[1] != "-download":
        print("Usage: script.py -download")
        return

    # Download SatisfactoryModdingLoader repository
    repo_url = "https://github.com/satisfactorymodding/SatisfactoryModLoader.git"
    download_repo(repo_url, "SatisfactoryModLoader")

    # List all files in the repository
    list_files("SatisfactoryModLoader")

    print("Repository downloaded and file list created in file_list.txt")

if __name__ == "__main__":
    main()
