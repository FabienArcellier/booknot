import os
import shutil

import click

from booknot.resources import RESOURCES_DIR


class InitApplication:

    def __init__(self, directory):
        self.directory = os.path.realpath(directory)

    def run(self):
        booknot_directory = os.path.join(self.directory, ".booknot")

        if os.path.isdir(booknot_directory):
            raise click.ClickException(f'booknot already exists: {booknot_directory}')

        try:
            if not os.path.isdir(booknot_directory):
                shutil.copytree(os.path.join(RESOURCES_DIR, 'booknot_root'), os.path.join(self.directory, '.booknot'))
        except Exception as exception:
            if os.path.isdir(booknot_directory):
                shutil.rmtree(booknot_directory)

            raise click.ClickException(f'invalid exception - {exception}')
