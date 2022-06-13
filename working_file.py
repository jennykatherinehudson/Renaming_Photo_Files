from LogFileUtil import FolderContents
from LogFileUtil import ExtensionToModify
from FileDiscovery import FileDiscovery
from FileMetadataReading import GenerateFullName
from CreateAndSaveFiles import CreateNewFolder
from CreateAndSaveFiles import CopyFile
from CreateAndSaveFiles import RenameFile

print("!!! Welcome in Hudson's Sollutions project !!!")
print("With this project you can easily rename all of your files in provided directory. \nLet's start!")

# What do you have in your folder?
path = input(r'Please provide a directory with your files: ')
FolderContents(path).folder_contents()

# What extentions do you want to modify?
extension_to_modify = ExtensionToModify(path).extension_to_modify()

# Check if everything files was selected
list_of_selected_photos_dir = ExtensionToModify(
    path).check_selection(extension_to_modify)

# Folder name and main name of the files
folder_name = input('Please provide a folder name: ')
main_name = input('Please provide main name of the files: ')
print('-'*70)

# Create new folder
new_folder_path = input(r'Please provide a new path to the folder: ')
CreateNewFolder(new_folder_path, folder_name).create_new_folder()

# Copy files
for old_photo_dir in list_of_selected_photos_dir:
    CopyFile(new_folder_path, folder_name, old_photo_dir, path).copy_file()
print('Congratulations!!! You have coppied {} files.'.format(
    len(list_of_selected_photos_dir)))
print('-'*70)

# Generate full name of the files
i_for_exc = 1
full_names = []
for i in list_of_selected_photos_dir:
    full_names.append(GenerateFullName(i, str(i_for_exc),
                      main_name, extension_to_modify).generate_full_name())
    i_for_exc += 1
'''full_names = [
    GenerateFullName(i, main_name, extension_to_modify).generate_full_name()
    for i in list_of_selected_photos_dir]'''

# Rename photos
for old_photo_dir, full_name in zip(list_of_selected_photos_dir, full_names):
    RenameFile(new_folder_path, folder_name, old_photo_dir,
               path, full_name).rename_file()
print('Congratulations!!! You have renamed {} files.'.format(
    len(list_of_selected_photos_dir)))
print('-'*70)


# What to do with rest of the files?
rest_extensions = list(FileDiscovery(path).all_extentions_in_dir()).copy()
while True:
    rest_extensions.remove(extension_to_modify)
    if rest_extensions == []:
        print('There is no more files in this folder to copy. Bye!')
        print('*'*70)
        break
    print('What do you want to do with others files?')
    print('In your folder there are {} more files. Would you like to copy and rename some of them?'.format(
        rest_extensions))
    answer = input('Y/N?')
    if answer == 'N':
        print('End the program.')
        print('*'*70)
        break

    # What extentions do you want to modify?
    extension_to_modify = ExtensionToModify(path).extension_to_modify()

    # Check if everything files was selected
    list_of_selected_photos_dir = ExtensionToModify(
        path).check_selection(extension_to_modify)

    # Copy files
    for old_photo_dir in list_of_selected_photos_dir:
        CopyFile(new_folder_path, folder_name, old_photo_dir, path).copy_file()
    print('Congratulations!!! You have coppied {} files.'.format(
        len(list_of_selected_photos_dir)))
    print('-'*70)

    # Generate full name of the files
    for i in list_of_selected_photos_dir:
        full_names.append(GenerateFullName(i, str(i_for_exc),
                          main_name, extension_to_modify).generate_full_name())
        i_for_exc += 1
    '''full_names = [
        GenerateFullName(
            i, main_name, extension_to_modify).generate_full_name()
        for i in list_of_selected_photos_dir]'''

    # Rename photos
    for old_photo_dir, full_name in zip(list_of_selected_photos_dir, full_names):
        RenameFile(new_folder_path, folder_name, old_photo_dir,
                   path, full_name).rename_file()
    print('Congratulations!!! You have renamed {} files.'.format(
        len(list_of_selected_photos_dir)))
    print('-'*70)
