import glob
import os

class FileDiscovery:

    def __init__(self, dir):
        self.dir = dir
        self.__extention_working()

    def __extention_working(self):
        #for number_files_in_dir
        self.__all_files_in_dir = os.listdir(self.dir)
        #for all_extentions_in_dir
        self.__splitted_files_list = set(
            [i.split('.')[1] for i in self.__all_files_in_dir])
        #for unique_extention
        extention_name = ['*.' + str(i) for i in self.__splitted_files_list]
        unique_extention_list = [
            len(glob.glob(os.path.join(self.dir, i))) for i in extention_name]
        self.__unique_extention_dict = {i: j for i, j in zip(
            extention_name, unique_extention_list)}

    def number_files_in_dir(self):
        return len(self.__all_files_in_dir)

    def all_extentions_in_dir(self):
        return self.__splitted_files_list

    def unique_extention(self):
        return self.__unique_extention_dict


""" path = r'E:\Python\python_my_projekt1_renaming_photos\Library'

photo_files_test = FileDiscovery(path)
print(photo_files_test.number_files_in_dir())
print(photo_files_test.all_extentions_in_dir())
print(photo_files_test.unique_extention()) """
