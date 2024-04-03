import os

def list_directories(path):
    directories = []
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            directories.append(item)
    return directories



def main():
    desktop_path = os.path.expanduser("~/Desktop")
    directories = list_directories(desktop_path)
    if directories:
        print("Directories on Desktop:")
        for directory in directories:
            print(directory)
            print(" ------- ")
    else:
        print("No directories found on Desktop.")

if __name__ == "__main__":
    main()
