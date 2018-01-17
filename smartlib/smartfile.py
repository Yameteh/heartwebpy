import os


def make_dirs(dirs):
    exist = os.path.exists(dirs)
    if not exist:
        os.makedirs(dirs)