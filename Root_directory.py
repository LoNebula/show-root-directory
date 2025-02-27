import os

def print_directory_tree(root_dir, padding=""):
    print(padding[:-1] + "+--" + os.path.basename(root_dir) + "/")
    padding = padding + "   "
    files = []
    dirs = []
    for item in os.listdir(root_dir):
        if os.path.isfile(os.path.join(root_dir, item)):
            files.append(item)
        else:
            dirs.append(item)
    for file in files:
        print(padding + "+--" + file)
    for dir in dirs:
        print_directory_tree(os.path.join(root_dir, dir), padding + "|  ")

root_directory = os.getcwd()
print_directory_tree(root_directory)