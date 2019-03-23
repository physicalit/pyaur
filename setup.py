#!/usr/bin/python

from setuptools import setup

setup(
      name='pyaur',
      version='1.00',
      description='Installing and upgrading AUR or official repo packages on Arch Linux',
      author='Mihuleac Sergiu',
      py_modules=['pyaur'],
      author_email='',
      url='',
      install_requires=[
            'Click',
            ],
      entry_points="""
            [console_scripts]
            pyaur=pyaur:cli
      """,
     )
