#!/usr/bin/python3

import os
import click
import subprocess
import urllib.request
import json

def search_print(result, o):
    for pkg in result:
        if o:
            print("Name: {0} {1}".format(pkg['pkgname'], pkg['pkgver']))
            print("Description: {0}".format(pkg['pkgdesc']))
            print()
        else:
            print("Name: {0} {1}".format(pkg['Name'], pkg['Version']))
            print("Description: {0}".format(pkg['Description']))
            print()

@click.group()
@click.version_option()
def cli():
    """Search, install, remove and upgrade packages!"""


@cli.command()
@click.argument('list', required=False)
@click.option('-o', is_flag=True, help="Use official repo", 
            default=False, metavar='')
def list(list, o):
    """ List installed AUR or official repo packages. """
    if o:
        print(subprocess.run(['pacman', '-Qn']))
    else:
        print(subprocess.run(['pacman', '-Qm']))


@cli.command()
@click.argument('clone', required=False)
def clone(clone):
    """ Clone AUR repositories package name. """
    subprocess.run(['git', 'clone',
                    "https://aur.archlinux.org/{0}.git".format(clone)])

@cli.command()
@click.argument('remove', required=False, nargs=-1)
def remove(remove):
    """ Remove packages """
    for pkg in remove:
        subprocess.run(['pacman', 'Rsn', pkg])

@cli.command()
@click.argument('install', required=False, nargs=-1)
@click.option('-o', is_flag=True, help="Use official repo", 
            default=False, metavar='')
@click.option('--yes', is_flag=True, metavar='',
            help="Do you want to ask questions? Default: NO")
def install(install, o, yes):
    """ Install or upgrade packages (AUR or official repo). """
    for ins in install:
        if o:
            if yes:
                subprocess.run(['pacman', '-Syu' '--needed', ins])
            else:
                subprocess.run(['pacman', '-Syu' '--needed', '--noconfirm', ins])
        else:
            package = "https://aur.archlinux.org/{0}.git".format(ins)
            pathpk = "/var/tmp/{0}".format(ins)
            subprocess.run(['git', 'clone', str(package), pathpk])
            os.chdir(str(pathpk))
            if yes:
                subprocess.run(['makepkg', '-sri --needed'])
            else:
                subprocess.run(['makepkg', '-sri', '--needed', '--noconfirm'])


@cli.command()
@click.argument('search', required=False, nargs=-1)
@click.option('-o', is_flag=True, help="Use official repo", 
            default=False, metavar='')
def search(search, o):
    """ Search for a package. """
    for srch in search:
        if o:
            url = 'https://www.archlinux.org/packages/search/json/?q={0}'.format(srch)
        else:
            url = 'https://aur.archlinux.org//rpc/?v=5&type=search&arg={0}'.format(srch)
        packs = urllib.request.urlopen(url).read()
        result = json.loads(packs)['results']
        search_print(result, o)