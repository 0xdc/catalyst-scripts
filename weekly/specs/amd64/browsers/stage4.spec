subarch: amd64
target: stage4
version_stamp: browsers-@latest@
rel_type: browsers
profile: default/linux/amd64/17.0/desktop/plasma/systemd
snapshot: @latest@
source_subpath: amd64/plasma/stage4-amd64-plasma-latest
portage_confdir: @REPO_DIR@/portage/browsers

stage4/packages:
	www-client/chromium
	www-client/firefox
	www-client/google-chrome
	www-client/google-chrome-beta
	www-client/google-chrome-unstable

stage4/empty:
	/root/.ccache
	/tmp
	/usr/src
	/var/cache/edb/dep
	/var/cache/genkernel
	/var/cache/portage/distfiles
	/var/empty
	/var/gentoo/repos
	/var/run
	/var/state
	/var/tmp

stage4/rm:
	/etc/*-
	/etc/*.old
	/etc/ssh/ssh_host_*
	/root/.*history
	/root/.lesshst
	/root/.ssh/known_hosts
	/root/.viminfo
	/usr/portage
	# Remove any generated stuff by genkernel
	/usr/share/genkernel
	# This is 3MB of crap for each copy
	/usr/lib64/python*/site-packages/gentoolkit/test/eclean/testdistfiles.tar.gz
