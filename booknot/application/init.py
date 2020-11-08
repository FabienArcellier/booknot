import io
import os


class InitApplication:

    def __init__(self, directory):
        self.directory = directory

    def run(self):
        booknot_directory = os.path.join(self.directory, ".booknot")

        if not os.path.isdir(booknot_directory):
            os.makedirs(booknot_directory)
