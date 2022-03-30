import glob
import os

class FileDiscovery:

    def __init__(self, dir):
        self.dir = dir
        self.__load_unique_extensions()

    def __load_unique_extensions(self):
        # for number_files_in_dir
        self.all_files_in_dir = os.listdir(self.dir)
        self.path_to_all_files = [os.path.join(
            self.dir, i) for i in self.all_files_in_dir]
        # for all_extentions_in_dir
        self.__splitted_files_list = set(
            [i.split('.')[1] for i in self.all_files_in_dir])
        # for unique_extention
        extention_name = ['*.' + str(i) for i in self.__splitted_files_list]
        unique_extention_list = [
            len(glob.glob(os.path.join(self.dir, i))) for i in extention_name]
        self.__unique_extention_dict = {i: j for i, j in zip(
            extention_name, unique_extention_list)}

    def number_files_in_dir(self):
        return len(self.all_files_in_dir)

    def all_extentions_in_dir(self):
        return self.__splitted_files_list

    def unique_extention(self):
        return self.__unique_extention_dict

