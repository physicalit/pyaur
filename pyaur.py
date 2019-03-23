#!/usr/bin/python3

from os import chdir, system
from tempfile import TemporaryDirectory, NamedTemporaryFile
import click
import urllib.request
import json

def exec_command(com):
    with NamedTemporaryFile(mode='r') as file:
        path = file.name
        system("{0} >> {1}".format(com, path))
        result = file.readlines()
    return [l.rstrip('\n') for l in result]

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
        print(exec_command('/usr/bin/pacman -Qn'))
    else:
        print(exec_command('/usr/bin/pacman -Qm'))


@cli.command()
@click.argument('clone', required=False)
def clone(clone):
    """ Clone AUR repositories package name. """
    exec_command(['git', 'clone',
                    "https://aur.archlinux.org/{0}.git".format(clone)])

@cli.command()
@click.argument('remove', required=False, nargs=-1)
def remove(remove):
    """ Remove packages """
    for pkg in remove:
        exec_command(['/usr/bin/pacman', '-Rsn', pkg])

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
                exec_command(['/usr/bin/pacman', '-Syu', '--needed', ins])
            else:
                exec_command(['/usr/bin/pacman', '-Syu', '--needed', '--noconfirm', ins])
        else:
            package = "https://aur.archlinux.org/{0}.git".format(ins)
            pathpk = "/var/tmp/{0}".format(ins)
            exec_command(['/usr/bin/git', 'clone', str(package), pathpk])
            chdir(str(pathpk))
            if yes:
                exec_command(['/usr/bin/makepkg', '-sri', '--needed'])
            else:
                exec_command(['/usr/bin/makepkg', '-sri', '--needed', '--noconfirm'])


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