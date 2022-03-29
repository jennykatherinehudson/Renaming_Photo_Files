import os
import shutil
from FileDiscovery import FileDiscovery
from FileMetadataReading import FileMetadateRading
from FileMetadataReading import GenerateFullName
from CreateAnsSaveFiles import CreateAndSaveFiles


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


def copy_more_files(path, ext_dir_of_photos, new_folder_path, folder_name, new_full_names):
    old_full_names = [i.split(path + '\\')[1] for i in ext_dir_of_photos]
    src = ext_dir_of_photos
    new_folder_dir = os.path.join(new_folder_path, folder_name)
    dst = [os.path.join(new_folder_dir, i) for i in old_full_names]
    for i, j in zip(src, dst):
        shutil.copy(i, j)
    dst_new_name = [os.path.join(new_folder_dir, i) for i in new_full_names]
    for i, j in zip(dst, dst_new_name):
        os.rename(i, j)
    print('Congratulations!!! You have coppied {} files.'.format(len(dst_new_name)))
    print('-'*70)


# What do you have in your folder?
path = r'E:\Python\python_my_projekt1_renaming_photos\Library'
photo_files = FileDiscovery(path)
WhatDoYouHaveInYourFolder(path, photo_files=FileDiscovery(path))

# What extentions do you want to modify?
extension_to_modify = WhatExtensionsToModify(photo_files=FileDiscovery(path))

# Check if everything files was selected
list_of_all_photos = photo_files.path_to_all_files.copy()
ext_dir_of_photos = FiltratedListOfPhotos(
    extension_to_modify, list_of_all_photos)
number_of_selected_photos = len(ext_dir_of_photos)
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
time = FileMetadateRading(ext_dir_of_photos)
date_and_time_for_files = list(time.read_modification_date_time())
new_full_names = GenerateFullName(
    date_and_time_for_files, main_name, extension_to_modify).generate_full_name()


# Create a new folder and save photos in new dir
new_folder_path = input(r'Please provide a new path to the folder: ')
cs_file = CreateAndSaveFiles(
    new_folder_path, folder_name, new_full_names, ext_dir_of_photos, path)
cs_file.create_new_folder()
cs_file.save_copy_photos()

# What to do with rest of the files?
rest_extenstions = list(photo_files.all_extentions_in_dir()).copy()
while True:
    rest_extenstions.remove(extension_to_modify)
    if rest_extenstions == []:
        print('There is no more files in this foler to copy. Bye!')
        print('*'*70)
        break
    print('What do you want to do with others files?')
    print('In your folder there are {} more files. Would you like to copy and rename some of them?'.format(
        rest_extenstions))
    answer = input('Y/N?')
    if answer == 'N':
        print('End the program.')
        print('*'*70)
        break

    # What extentions do you want to modify?
    extension_to_modify = WhatExtensionsToModify(
        photo_files=FileDiscovery(path))

    # Check if everything files was selected
    list_of_all_photos = photo_files.path_to_all_files.copy()
    ext_dir_of_photos = FiltratedListOfPhotos(
        extension_to_modify, list_of_all_photos)
    number_of_selected_photos = len(ext_dir_of_photos)
    number_of_photos = photo_files.unique_extention()[
        '*.' + extension_to_modify]
    if number_of_selected_photos == number_of_photos:
        print('Everything is ok!')
        print('-'*70)
    else:
        print('Something went wrong!')

    # Generate full name of the files
    time = FileMetadateRading(ext_dir_of_photos)
    date_and_time_for_files = list(time.read_modification_date_time())
    new_full_names = GenerateFullName(
        date_and_time_for_files, main_name, extension_to_modify).generate_full_name()

    # Copy and save photos in new dir
    copy_more_files(path, ext_dir_of_photos, new_folder_path,
                    folder_name, new_full_names)
