from datetime import datetime
from exif import Image
import os

class TimeModification:

    def __init__(self, path_of_photo, i_for_exc):
        self.path_of_photo = path_of_photo
        self.i_for_exc = i_for_exc

    def modification_time(self):
        try:
            with open(self.path_of_photo, 'rb') as image_file:
                my_image = Image(image_file)
            return my_image.datetime_original.replace(" ", "_").replace(':', '') + '_' + self.i_for_exc
        except KeyError:
            mod_time = datetime.fromtimestamp(os.path.getmtime(self.path_of_photo))
            self.modification_date_time = (
                str(mod_time.date()) + '_' + str(mod_time.time())).split('.')[0].replace(':', '')
            return self.modification_date_time
        '''except FileExistsError:
            return self.modification_date_time + '_' + self.i_for_exc'''


class GenerateFullName(TimeModification):

    def __init__(self, path_of_photo, i_for_exc, main_name, extension_to_modify):
        super().__init__(path_of_photo, i_for_exc)
        self.main_name = main_name
        self.extension_to_modify = extension_to_modify

    def generate_full_name(self):
        full_name = self.main_name + '_' + super().modification_time() + \
            '.' + self.extension_to_modify
        return full_name


