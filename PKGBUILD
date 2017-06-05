# Maintainer: Mihuleac Sergiu

pkgname=pyaur
pkgver=0.04
pkgdesc='Installing and upgrading AUR packages on Arch Linux'
arch=('any')
url='https://github.com/physicalit/pyaur'
license=('MIT')
pkgrel=2
provides=('pyaur')
depends=(
	'python-setuptools'
	'python-click'
	'python')
source=("https://github.com/physicalit/pyaur/releases/download/0.04/pyaur.tar")
md5sums=('de7338097549f52d90198c6e65f5e8b3')

prepare() {
	tar -xvzf pyaur.tar
}

package() {
	# Install
	sudo pyapp/setup.py install
}
