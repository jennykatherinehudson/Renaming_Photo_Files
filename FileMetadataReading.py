from datetime import datetime
import os

class TimeModification:

    def __init__(self, path_of_photo):
        self.path_of_photo = path_of_photo

    def modification_time(self):
        mod_time = datetime.fromtimestamp(os.path.getmtime(self.path_of_photo))
        self.modification_date_time = (str(mod_time.date()) + '_' + str(mod_time.time())).split('.')[0].replace(':', '-')
        return self.modification_date_time


class GenerateFullName(TimeModification):

    def __init__(self, path_of_photo, main_name, extension_to_modify):
        super().__init__(path_of_photo)
        self.main_name = main_name
        self.extension_to_modify = extension_to_modify

    def generate_full_name(self):
        full_name = self.main_name + '_' + super().modification_time() + '.' + self.extension_to_modify
        return full_name