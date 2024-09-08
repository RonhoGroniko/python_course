import os
import shutil


def getListOfSmallFiles(directory_path=None):
        list_of_files = []
        if directory_path is None:
            directory_path = "."

        for filename in os.listdir(directory_path):
            filepath = os.path.join(directory_path, filename)
            if os.path.isfile(filepath) and os.path.getsize(filepath) <= 2000:
                list_of_files.append(filename)
        if len(list_of_files) == 0:
            print("No files with weight less than 2K")
        else:
            print("List of small files:", list_of_files)

        return list_of_files


def copySmallFiles(start_pass, finish_path):
    list_of_files = getListOfSmallFiles(start_pass)
    if len(list_of_files) == 0:
        return
    else:
        os.makedirs(finish_path, exist_ok=True)
        for filename in list_of_files:
            start_filepath = os.path.join(start_pass, filename)
            finish_filepath = os.path.join(finish_path, filename)
            shutil.copy(start_filepath, finish_filepath)


source_path = r"C:\Users\Rodion\Documents\python_course\python_lab1\task1\directory_of_files"
destination_path = r"C:\Users\Rodion\Documents\python_course\python_lab1\task1\small"

copySmallFiles(source_path, destination_path)
