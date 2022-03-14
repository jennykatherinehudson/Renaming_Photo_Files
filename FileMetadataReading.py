from datetime import datetime
import os
from FileDiscovery import FileDiscovery


class FileMetadateRading:

    def __init__(self, FiltratedListOfPhotos):
        self.list_of_photos = FiltratedListOfPhotos

    def read_modification_date_time(self):
        time_md = [datetime.fromtimestamp(os.path.getmtime(i))
                   for i in self.list_of_photos]
        self.time_md_date_and_time = [
            str(i.date()) + '-' + str(i.time()) for i in time_md]
        return self.time_md_date_and_time


class GenerateFullName:

    def __init__(self, date_and_time_for_files, main_name):
        self.date_and_time_for_files = date_and_time_for_files
        self.main_name = main_name

    def generate_full_name(self):
        full_names = [self.main_name + '_' + i for i in self.date_and_time_for_files]
        return full_names

