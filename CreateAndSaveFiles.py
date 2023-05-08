import os
import shutil


class CreateNewFolder:

    def __init__(self, new_folder_path, folder_name):
        self.new_folder_path = new_folder_path
        self.folder_name = folder_name

    def create_new_folder(self):
        self.new_folder_dir = os.path.join(
            self.new_folder_path, self.folder_name)
        if not os.path.exists(self.new_folder_dir):
            os.makedirs(self.new_folder_dir)
            print('New folder has been created.')
            print('-'*70)
        else:
            print('Folder exists!')


class CopyFile(CreateNewFolder):

    def __init__(self, new_folder_path, folder_name, old_photo_dir, path):
        super().__init__(new_folder_path, folder_name)
        self.old_photo_dir = old_photo_dir
        self.path = path
        self.destination_dir = os.path.join(
            self.new_folder_path, self.folder_name, self.old_photo_dir.split(self.path + '\\')[1])

    def copy_file(self):
        shutil.copy(self.old_photo_dir, self.destination_dir)


class RenameFile(CopyFile):

    def __init__(self, new_folder_path, folder_name, old_photo_dir, path, full_name):
        super().__init__(new_folder_path, folder_name, old_photo_dir, path)
        self.full_name = full_name

    def rename_file(self):
        self.destination_full_name_dir = os.path.join(
            self.new_folder_path, self.folder_name, self.full_name)
        os.rename(self.destination_dir, self.destination_full_name_dir)
