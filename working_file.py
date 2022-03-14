import glob
import os
from FileDiscovery import FileDiscovery


def WhatDoYouHaveInYourFolder(path, photo_files):
    print('-'*50)
    print('''Files in the directory: {}
In this direcory you have {} files.
There are {} different extentions.'''.format(path, photo_files.number_files_in_dir(), photo_files.all_extentions_in_dir()))
    print('In your directory there are: {}'.format(
        photo_files.unique_extention()))
    print('-'*50)


def WhatExtensionsToModify(photo_files):
    while True:
        extension_to_modify = input('What extentions do you want to modify?')
        if extension_to_modify in photo_files.all_extentions_in_dir():
            print('Ok, the {} files will be renamed.'.format(extension_to_modify))
            print('-'*50)
            break
        else:
            print('You need to choose correct extention! Please input once again.')


# What do you have in your folder?
path = r'E:\Python\python_my_projekt1_renaming_photos\Library'
WhatDoYouHaveInYourFolder(path, photo_files=FileDiscovery(path))

# What extentions do you want to modify?
WhatExtensionsToModify(photo_files=FileDiscovery(path))

""" photo_files = FileDiscovery(path)
print(photo_files.all_extentions_in_dir()) """
