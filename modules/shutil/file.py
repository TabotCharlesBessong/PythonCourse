
from copy import copy
from importlib.metadata import files, metadata
from msilib.schema import Directory
from shutil import copy2, copyfile
import shutil
from statistics import mode


# copyfile() = copies contents of a file 
# copy() = copyfile() + permission mode + destination can be Directory 
# copy2() = copy() + copies metadata (files creation and modification times)


shutil.copyfile('test.txt','copy.txt')
shutil.copyfile('test.txt','C:\\Users\\CHARLES\\Documents\\copy.txt')