import glob
import os


class FileDiscovery:

    def __init__(self, dir):
        self.dir = dir

    def amount_of_all_files_in_dir(self):
        self.all_files_in_dir = os.listdir(self.dir)
        return len(self.all_files_in_dir)

    def all_extentions_in_dir(self):
        splitted_files_list = [i.split('.') for i in self.all_files_in_dir]
        self.all_extentions_set = set({})
        for i in splitted_files_list:
            self.all_extentions_set.add(i[1])
        return self.all_extentions_set

    def amount_of_specify_extention_dict(self):
        extention_name = ['*.' + str(i) for i in self.all_extentions_set]
        amount_of_specify_extention_list = [len(glob.glob(os.path.join(self.dir, i))) for i in extention_name]
        amount_of_specify_extention_dict = {i : j for i,j in zip(extention_name, amount_of_specify_extention_list)}
        return amount_of_specify_extention_dict
    



'''path = r'E:\Python\python_my_projekt1_renaming_photos\Library'

photo_files_test = FileDiscovery(path)
print(photo_files_test.amount_of_all_files_in_dir())
print(photo_files_test.all_files_in_dir)
print(photo_files_test.all_extentions_in_dir())
photo_files_test.amount_of_specify_extention_dict()'''
