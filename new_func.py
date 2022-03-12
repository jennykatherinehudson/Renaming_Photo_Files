import glob
import os

path = r'E:\Python\python_my_projekt1_renaming_photos\Library'
print(os.listdir(path))

file_extension = '*.jpeg'
path_with_extention = os.path.join(path, file_extension)

glob_len_items = len(glob.glob(path_with_extention))