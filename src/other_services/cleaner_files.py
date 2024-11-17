import os


def deletes_files() -> None:
    all_files = os.listdir("src/static/files")
    for file in all_files:
        file_path = os.path.join("src/static/files", file)
        if os.path.isdir(file_path):
            for file2 in os.listdir(file_path):
                os.remove(os.path.join("src/static/files/compress", file2))
        else:
            os.remove("src/static/files/{}".format(file))
