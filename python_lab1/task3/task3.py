import os


package_path = r"C:\Users\Rodion\Documents\python_course\python_lab1\task3\files_dir"

with open(r"C:\Users\Rodion\Documents\python_course\python_lab1\task2\other_files.txt", "r") as file:
    list_of_files = [line.strip() for line in file]


def createFiles(files = None):
    if files is None:
        return print("No files to create")

    else:
        os.makedirs(package_path, exist_ok=True)
        for filename in files:
            filepath = os.path.join(package_path, filename)
            with open(filepath, "w") as f:
                f.write(filename+" was created")

createFiles(list_of_files)