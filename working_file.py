import glob
import os
from FileDiscovery import FileDiscovery

path = r'E:\Python\python_my_projekt1_renaming_photos\Library'

photo_files_test = FileDiscovery(path)
print(photo_files_test.amount_of_all_files_in_dir())


print(os.listdir(path))

file_extension = '*.jpeg'
path_with_extention = os.path.join(path, file_extension)

glob_len_items = len(glob.glob(path_with_extention))
