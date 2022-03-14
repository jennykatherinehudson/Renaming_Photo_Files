import glob
import os
from FileDiscovery import FileDiscovery
from FileMetadataReading import FileMetadateRading
from FileMetadataReading import GenerateFullName


def WhatDoYouHaveInYourFolder(path, photo_files):
    print('-'*70)
    print('''Files in the directory: {}
In this direcory you have {} files.
There are {} different extentions.'''.format(path, photo_files.number_files_in_dir(), photo_files.all_extentions_in_dir()))
    print('In your directory there are: {}'.format(
        photo_files.unique_extention()))
    print('-'*70)


def WhatExtensionsToModify(photo_files):
    while True:
        extension_to_modify = input('What extentions do you want to modify? ')
        if extension_to_modify in photo_files.all_extentions_in_dir():
            print('Ok, the {} files will be renamed.'.format(extension_to_modify))
            print('-'*70)
            break
        else:
            print('You need to choose correct extention! Please input once again.')
    return extension_to_modify


def FiltratedListOfPhotos(extension_to_modify, list_of_photos):
    list_of_photos_copy = photo_files.path_to_all_files.copy()
    for i in range(len(list_of_photos)):
        if extension_to_modify not in list_of_photos[i]:
            list_of_photos_copy.remove(list_of_photos[i])
    return list_of_photos_copy


# What do you have in your folder?
path = r'E:\Python\python_my_projekt1_renaming_photos\Library'
photo_files = FileDiscovery(path)
WhatDoYouHaveInYourFolder(path, photo_files=FileDiscovery(path))

# What extentions do you want to modify?
extension_to_modify = WhatExtensionsToModify(photo_files=FileDiscovery(path))

# Check if everything files was selected
list_of_photos = photo_files.path_to_all_files.copy()
number_of_selected_photos = len(
    FiltratedListOfPhotos(extension_to_modify, list_of_photos))
number_of_photos = photo_files.unique_extention()['*.' + extension_to_modify]
if number_of_selected_photos == number_of_photos:
    print('Everything is ok!')
    print('-'*70)
else:
    print('Something went wrong!')

# Folder name and main name of the files
folder_name = input('Please provide a folder name: ')
main_name = input('Please provide main name of the files: ')
print('-'*70)

# Generate full name of the files
time = FileMetadateRading(FiltratedListOfPhotos(
    extension_to_modify, list_of_photos))
date_and_time_for_files = list(time.read_modification_date_time())
full_names = GenerateFullName(date_and_time_for_files, main_name).generate_full_name()
print(full_names)

# Create a new folder

