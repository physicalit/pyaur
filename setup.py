#!/usr/bin/python

from setuptools import setup
import json

NAME = 'pyaur'
VERSION = '1.03'
DESC = 'Installing and upgrading AUR or official repo packages on Arch Linux'
AUTHOR = 'Mihuleac Sergiu'
EMAIL = ''
URL = ''


class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        pass
        install.run(self)

setup(
      name=NAME,
      version=VERSION,
      description=DESC,
      author=AUTHOR,
      py_modules=['pyaur'],
      author_email=EMAIL,
      url=URL,
      cmdclass={'install': PostInstallCommand,}
      install_requires=[
            'Click',
            ],
      entry_points="""
            [console_scripts]
            pyaur=pyaur:cli
      """,
     )
