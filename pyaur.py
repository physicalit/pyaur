#!/usr/bin/env python2

import os
import re
import click
import subprocess


@click.group()
@click.version_option()
def cli():
    """Search, install and upgrade AUR packages!"""


@cli.command()
@click.argument('list', required=False)
def list(list):
    """ List installed AUR packages. """
    list = subprocess.run(['pacman', '-Qm'])


@cli.command()
@click.argument('clone', required=False)
def clone(clone):
    """ Clone AUR repositories package name. """
    clone = subprocess.run(['git', 'clone',
                  "https://aur.archlinux.org/{0}.git".format(clone)])


@cli.command()
@click.argument('install', required=False, nargs=-1)
def install(install):
    """ Install or upgrade an AUR package. """
    for ins in install:
        package = "https://aur.archlinux.org/"+ins+".git"
        pathpk = "/tmp/"+ins
        instcheck = subprocess.run(['git', 'clone', str(package), pathpk])
        print(instcheck)
        os.chdir(str(pathpk))
        subprocess.run(['makepkg', '-sri'])
