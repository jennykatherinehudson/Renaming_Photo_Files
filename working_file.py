import glob
import os
from FileDiscovery import FileDiscovery

path = r'E:\Python\python_my_projekt1_renaming_photos\Library'

photo_file = FileDiscovery(path)

print('-'*50)
print('''Files in the directory: {}
In this direcory you have {} files.
This is {} different extentions.'''.format(path, photo_file.amount_of_all_files_in_dir(), photo_file.all_extentions_in_dir()))

print('In your directory there is: {}'.format(photo_file.amount_of_specify_extention_dict()))


