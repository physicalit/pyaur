#!/usr/bin/python3

import os
import click
import subprocess
import urllib.request
import json


@click.group()
@click.version_option()
def cli():
    """Search, install and upgrade AUR packages!"""


@cli.command()
@click.argument('list', required=False)
def list(list):
    """ List installed AUR packages. """
    list = subprocess.run(['pacman', '-Qm'])
    print(list)


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
        package = "https://aur.archlinux.org/" + ins + ".git"
        pathpk = "/tmp/" + ins
        subprocess.run(['git', 'clone', str(package), pathpk])
        os.chdir(str(pathpk))
        subprocess.run(['makepkg', '-sri'])


@cli.command()
@click.argument('search', required=False, nargs=-1)
def search(search):
    """ Search AUR repositorie for package name. """
    for srch in search:
        packs = urllib.request.urlopen(
            "https://aur.archlinux.org//rpc/?v=5&type=search&arg=" + srch).read()
        somejson = json.loads(packs)
        somej = somejson['results']
        print(type(somej))
        for pkg in somej:
            print("Name: " + pkg['Name'])
            print("Version: " + pkg['Version'])
            print("Desc: " + pkg['Description'])
            print("################")
