#!/usr/bin/python
# coding=utf-8

from __future__ import print_function

import os

import click
import requests
from bs4 import BeautifulSoup

from booknot.application.init import InitApplication


@click.group()
def cli():
    pass


@click.command('init')
def init():
    # init booknot root
    workdir = os.getcwd()
    init_application = InitApplication(workdir)
    init_application.run()


@click.command('capture')
@click.argument('url')
def capture(url):
    # check booknot root
    # fetch meta information with request & beautiful soup
    # write the directory

    r = requests.get(url)
    content = r.content
    soup = BeautifulSoup(content, 'html.parser')
    title = soup.head.title.string
    description = soup.head.find('meta', property="og:description")["content"]

    print(title)
    print(description)


cli.add_command(init)
cli.add_command(capture)

if __name__ == '__main__':
    cli()
