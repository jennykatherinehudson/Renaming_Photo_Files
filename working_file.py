import glob
import os
from FileDiscovery import FileDiscovery

path = r'E:\Python\python_my_projekt1_renaming_photos\Library'

photo_files = FileDiscovery(path)

print('-'*50)
print('''Files in the directory: {}
In this direcory you have {} files.
There are {} different extentions.'''.format(path, photo_files.number_files_in_dir(), photo_files.all_extentions_in_dir()))

print('In your directory there are: {}'.format(photo_files.unique_extention()))
print('-'*50)


