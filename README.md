# pyaur [![Build Status](https://travis-ci.org/physicalit/pyaur.svg?branch=master)](https://travis-ci.org/physicalit/pyaur) [![Requirements Status](https://requires.io/github/physicalit/pyaur/requirements.svg?branch=master)](https://requires.io/github/physicalit/pyaur/requirements/?branch=master) ![GitHub](https://img.shields.io/github/license/physicalit/pyaur.svg) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/physicalit/pyaur.svg?label=Version)

Small script for installing packages from AUR, only for Arch Linux users.

### Requirements:

Only click library will be installed when using the install command.

### Installation:

Download or clone the repository, unzip it if necessary, then `cd` in to the directory and run the following command:

```sh
sudo ./setup.py install
```

### Usage:

List usage information.

```
[physicalit@mylaptop pyaur]$ pyaur --help
Usage: pyaur [OPTIONS] COMMAND [ARGS]...

  Search, install, remove and upgrade packages!

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  clone    Clone AUR repositories package name.
  install  Install or upgrade packages (AUR or official repo).
  list     List installed AUR or official repo packages.
  remove   Remove packages
  search   Search for a package.
```

```sh
[physicalit@mylaptop pyaur]$ pyaur install --help
Usage: pyaur install [OPTIONS] [INSTALL]...

  Install or upgrade packages (AUR or official repo).

Options:
  -o      Use official repo
  --yes   Do you want to ask questions? Default: NO
  --help  Show this message and exit.
```

### Features
| Function | Description |
|---|---|
| clone | Clone specified repository from AUR |
| install | Install/Upgrade package from `AUR` or official repository |
| list | List installed packages from `AUR` or official repository |
| search | Search for a packages in `AUR` or official repository |
| remove | Remove a packages |