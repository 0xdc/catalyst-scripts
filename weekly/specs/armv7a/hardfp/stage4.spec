version_stamp: @latest@
profile: default/linux/arm/17.0/armv7a
source_subpath: armv7a/hardfp/stage3-armv7a_hardfp-latest
portage_confdir: @REPO_DIR@/confdirs/vboot

stage4/use:
	bindist
	ipv6

stage4/packages:
	app-editors/vim
	app-shells/bash-completion
	dev-embedded/u-boot-tools
	dev-vcs/git
	sys-apps/dtc
	sys-devel/bc
	sys-devel/distcc
	sys-fs/cryptsetup
	sys-fs/dosfstools
	sys-process/htop

stage4/root_overlay: @REPO_DIR@/root_overlays/base

stage4/unmerge:
	app-editors/nano

stage4/empty:
	/root/.ccache
	/tmp
	/usr/src
	/var/cache/edb/dep
	/var/cache/genkernel
	/var/cache/distfiles
	/var/empty
	/var/db/repos
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
