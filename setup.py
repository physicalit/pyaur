#!venv/bin/python3

from setuptools import setup

setup(
      name='pyaur',
      version='0.03',
      description='Installing and upgrading AUR packages on Arch Linux',
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
