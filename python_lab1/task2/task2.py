import os


def getListOfChosenFiles(dir_path, needed_files: list = None):
    required_files = []
    other_files = []
    number_of_files = 0
    size_sum = 0
    if dir_path is None:
        dir_path = "."
    if needed_files is not None:
        for filename in os.listdir(dir_path):
            if filename in needed_files:
                required_files.append(filename)

            else:
                other_files.append(filename)

        with open("required_files.txt", "w") as required:
            for name in required_files:
                required.write(name+"\n")
        with open("other_files.txt", "w") as other:
            for name in other_files:
                other.write(name+"\n")

        return print("Найденные переданные файлы: ", required_files, "\nОстальные файлы: ", other_files)
    else:
        dir_path = "."
        for filename in os.listdir(dir_path):
            filepath = os.path.join(dir_path, filename)
            if os.path.isfile(filepath):
                number_of_files += 1
                if os.path.isfile(filepath):
                    size_sum += os.path.getsize(filepath)
        return print("Количество файлов: ", number_of_files, "\nОбщий размер файлов: ", size_sum)

getListOfChosenFiles(r"C:\Users\Rodion\Documents\python_course\python_lab1\task1\directory_of_files", )