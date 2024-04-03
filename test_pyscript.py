import os

"""
Test Python Script - Used for testing sphinx auto doc generation
"""

__version__ = "0.1.0"

def list_directories_v2(path_2):
    """
    Return a list of names of the directories.

    :param path_2: path to the directories that will be printed 
    :type path_2: str
    :return: The directories list.
    :rtype: list[str]
    """
    directories = []
    for item in os.listdir(path_2):
        full_path = os.path.join(path_2, item)
        if os.path.isdir(full_path):
            directories.append(item)
    return directories

def list_directories(path):
    """
    Return a list of names of the directories.

    :param path: path to the directories that will be printed 
    :type path: str
    :return: The directories list.
    :rtype: list[str]
    """
    directories = []
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            directories.append(item)
    return directories



def main():
    """Main function to list directories on the desktop."""
    desktop_path = os.path.expanduser("~/Desktop")
    directories = list_directories(desktop_path)
    if directories:
        print("Directories on Desktop:")
        for directory in directories:
            print(directory)
            print("--------")
    else:
        print("No directories found on Desktop.")

if __name__ == "__main__":
    main()
