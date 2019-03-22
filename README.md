# pyaur [![Build Status](https://travis-ci.org/physicalit/pyaur.svg?branch=master)](https://travis-ci.org/physicalit/pyaur) [![Requirements Status](https://requires.io/github/physicalit/pyaur/requirements.svg?branch=master)](https://requires.io/github/physicalit/pyaur/requirements/?branch=master)
Small script for installing packages from AUR, only for Arch Linux users.

### Requerments:

  - python 3.6 or latest
  - git

### Instalation:

Download or clone the repo, unzip it if necessary, then cd in to the folder and run the following command:

    sudo ./setup.py install

### Usage:

`pyaur --help` To list usage information.

---

Original repo at [https://bitbucket.org/physicalit/pyaur/src](https://bitbucket.org/physicalit/pyaur/src)

### To Do

 * Install multiple packages, one after the other. - **DONE**
 * Search for aur packages - **DONE**
    * https://aur.archlinux.org/rpc.php
    * https://aur.archlinux.org//rpc/?v=5&type=search&arg=foobar
 * Uninstall package **DONE**
 * Create a binary and add it as release on AUR.
 * Check for updates
 
