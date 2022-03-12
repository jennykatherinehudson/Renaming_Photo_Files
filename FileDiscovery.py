import glob
import os

class FileDiscovery:

    def __init__(self, dir):
        self.dir = dir 

    def amount_of_all_files_in_dir(self):
        self.amount_of_files = len(os.listdir(self.dir))
