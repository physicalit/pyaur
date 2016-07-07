#!/usr/bin/env python2

import os
import click

from subprocess import call

@click.group()
@click.version_option()
def cli():
    """Search, install and upgrade AUR packages!"""


@cli.command()
@click.argument('list', required=False)
def list(list):
    """ List installed AUR packages. """
    list = call(['pacman', '-Qm'])

@cli.command()
@click.argument('clone', required=False)
def clone(clone):
    """ Clone AUR repositories package name. """
    clone = call(['git', 'clone', "https://aur.archlinux.org/{0}.git".format(clone)])

@cli.command()
@click.argument('install', required=False)
def install(install):
    """ Install or upgrade an AUR package. """
    call(['git', 'clone', "https://aur.archlinux.org/{0}.git".format(install)])
    os.chdir("./{0}".format(install))
    call(['makepkg', '-sri'])
