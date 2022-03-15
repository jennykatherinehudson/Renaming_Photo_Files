import os
import shutil


class CreateAndSaveFiles:

    def __init__(self, new_folder_path, folder_name, new_full_names, ext_dir_of_photos, path):
        self.new_folder_path = new_folder_path
        self.folder_name = folder_name
        self.new_full_names = new_full_names
        self.ext_dir_of_photos = ext_dir_of_photos
        self.path = path

    def create_new_folder(self):
        self.new_folder_dir = os.path.join(
            self.new_folder_path, self.folder_name)
        if not os.path.exists(self.new_folder_dir):
            os.makedirs(self.new_folder_dir)
            print('New folder has been created.')
            print('-'*70)
        else:
            print('File exists!')

    def save_copy_photos(self):
        old_full_names = [i.split(self.path + '\\')[1] for i in self.ext_dir_of_photos]
        src = self.ext_dir_of_photos
        dst = [os.path.join(self.new_folder_dir, i) for i in old_full_names]
        for i, j in zip(src, dst):
            shutil.copy(i,j)
        dst_new_name = [os.path.join(self.new_folder_dir, i) for i in self.new_full_names]
        for i,j in zip(dst, dst_new_name):
            os.rename(i,j)
        print('Congratulations!!! You have coppied {} files.'.format(len(dst_new_name)))
        print('-'*70) 
