import io
import json
import os

import click

from booknot.crawler.crawler import Crawler


class CaptureApplication:

    def __init__(self, crawler: Crawler, directory, url):
        self.crawler = crawler
        self.directory = os.path.realpath(directory)
        self.url = url

    def run(self):
        booknot_path = os.path.join(self.directory, '.booknot')
        template_booknot_path = os.path.join(self.directory, '.booknot', 'index.rst.j2')

        if not os.path.isdir(booknot_path):
            raise click.ClickException(f'you have to initialise booknot repository wiht booknot init :  {booknot_path}')

        if not os.path.isfile(template_booknot_path):
            raise click.ClickException(f'template for booknot does not exists {template_booknot_path}')

        metadata = self.crawler.fetch(self.url)

        booknot_note_path = os.path.join(self.directory, metadata.sanitize_dir())
        os.makedirs(booknot_note_path)
        with io.open(os.path.join(booknot_note_path, 'manifest.json'), 'w') as filep:
            json.dump(metadata.tomanifest(), filep, indent=4)
