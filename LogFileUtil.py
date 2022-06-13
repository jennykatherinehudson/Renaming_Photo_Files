from FileDiscovery import FileDiscovery


class FolderContents(FileDiscovery):

    def __init__(self, path):
        self.path = path
        self.photo_files = FileDiscovery(path)

    def folder_contents(self):
        print('-'*70)
        print('''Files in the directory: {}
In this direcory you have {} files.
There are {} different extentions.'''.format(self.path, self.photo_files.number_files_in_dir(), self.photo_files.all_extentions_in_dir()))
        print('In your directory there are: {}'.format(
            self.photo_files.unique_extention()))
        print('-'*70)


class ExtensionToModify(FolderContents):

    def __init__(self, path):
        super().__init__(path)

    def extension_to_modify(self):
        while True:
            extension = input('What extentions do you want to modify? ')
            if extension in self.photo_files.all_extentions_in_dir():
                print('Ok, the {} files will be renamed.'.format(extension))
                print('-'*70)
                break
            else:
                print('You need to choose correct extention! Please input once again.')
        return extension

    def check_selection(self, extension):
        list_of_all_photos = self.photo_files.path_to_all_files.copy()
        list_of_photos_copy = list_of_all_photos.copy()
        for i in range(len(list_of_all_photos)):
            if extension not in list_of_all_photos[i]:
                list_of_photos_copy.remove(list_of_all_photos[i])
        number_of_selected_photos = len(list_of_photos_copy)
        number_of_photos = self.photo_files.unique_extention()[
            '*.' + extension]
        if number_of_selected_photos == number_of_photos:
            print('Everything is ok!')
            print('-'*70)
        else:
            print('Something went wrong!')
        return list_of_photos_copy
