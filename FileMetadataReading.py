from datetime import datetime
import os
from FileDiscovery import FileDiscovery

""" image_file = r'E:\Python\python_my_projekt1_renaming_photos\Library\2017_dress_002.jpg'

time_creation = datetime.fromtimestamp(os.path.getctime(image_file))
time_modification = datetime.fromtimestamp(os.path.getmtime(image_file))

print(time_creation.date())
print(time_modification.time())

print('Creation date: {}'.format(time_creation))
print('Modification date: {}'.format(time_modification)) """

""" class FileMetadateRading: 

    def __init__(self, dir, images_list):
        self.dir = dir
        self.images_list = images_list
        self.__time_working()

    def __time_working(self):
        self.time_creation_in_dir = []
        for image in self.dir: 
            self.time_creation_in_dir.append(datetime.fromtimestamp(os.path.getctime(image)))
    
    def time_creation(self):
        return self.time_creation_in_dir """


path = r'E:\Python\python_my_projekt1_renaming_photos\Library'
photo_files = FileDiscovery(path)
#photo_metadata = FileMetadateRading(path, photo_files.path_to_all_files)
# print(photo_metadata.time_creation())


time_md = [datetime.fromtimestamp(os.path.getmtime(i))
           for i in photo_files.path_to_all_files]
time_md_date_and_time = [str(i.date()) + '-' + str(i.time()) for i in time_md]
print(time_md_date_and_time)
# print(time_modification)
