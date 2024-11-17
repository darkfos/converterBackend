import os


def deletes_files() -> None:
    all_files = os.listdir("src/static/files")
    for file in all_files:
        os.remove("src/static/files/{}".format(file))
