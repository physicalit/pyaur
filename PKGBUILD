# Maintainer: Alex Taber <aft dot pokemon at gmail dot com>

pkgname=pyaur
pkgver=0.03
pkgdesc='Installing and upgrading AUR packages on Arch Linux'
arch=('any')
url='https://github.com/physicalit/pyaur'
license=('MIT')
provides=('pyaur')
depends=(
	'python-setuptools'
	'python-click'
	'python')
	'unzip')
install=teamviewer.install
source=("https://github.com/physicalit/pyaur/releases/download/0.03/pyaur-0.3.linux-x86_64.zip")
md5sums=('df17250c53e24c8fc619a751183375e5')

prepare() {
	tar -xf data.tar.bz2
}

package() {
	# Install
	cp -dr --no-preserve=ownership {etc,opt,usr,var} "${pkgdir}"/

	# Additional files
	rm "${pkgdir}"/opt/teamviewer/tv_bin/xdg-utils/xdg-email
	install -D -m0644 "${pkgdir}"/opt/teamviewer/tv_bin/script/teamviewerd.service \
		"${pkgdir}"/usr/lib/systemd/system/teamviewerd.service
	install -d -m0755 "${pkgdir}"/usr/{share/applications,share/licenses/teamviewer}
	ln -s /opt/teamviewer/License.txt \
		"${pkgdir}"/usr/share/licenses/teamviewer/LICENSE
}
