# pyaur
Small script for installing packages from AUR, only for Arch Linux users.

### Requerments:

  - python 3
  - git

### Instalation:

Download or clone the repo, unzip it if necessary, then cd in to the folder and run the following command:

`. venv/bin/activate`
`./setup.py`
`sudo ln -s $(pwd)/venv/bin/pyaur /usr/bin/`

### Usage:

`pyaur --help` To list usage information.

---

Original repo at [https://bitbucket.org/physicalit/pyaur/src](https://bitbucket.org/physicalit/pyaur/src)

### To Do

 * Install multiple packages, one after the other.
 * Search for aur packages
 * Uninstall package
