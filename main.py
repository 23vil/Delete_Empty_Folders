#Delete empty folders

from os import listdir
from os.path import isfile, join, isdir
import shutil

def main(path):
    """
    Parameters
    ----------
    path : str
        Path where to look for image files.
    """
   
    onlyfolders = [join(path, f) for f in listdir(path) if isdir(join(path, f, "model"))]
    for direc in onlyfolders:
        if not listdir(join(direc, "model")):
            shutil.rmtree(direc)

if __name__ == '__main__':
    main(path='/home/ps815691/git/TTSR/train/IMM/TTSR')
