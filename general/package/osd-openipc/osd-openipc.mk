################################################################################
#
# osd-openipc
#
################################################################################

OSD_OPENIPC_SITE = $(call github,danielbanar,openipc-osd,$(OSD_OPENIPC_VERSION))
OSD_OPENIPC_LICENSE = MIT
OSD_OPENIPC_LICENSE_FILES = LICENSE

ifeq ($(OPENIPC_VARIANT),dash)
	OSD_OPENIPC_VERSION = dash
else
	OSD_OPENIPC_VERSION = HEAD
endif

ifeq ($(BR2_TOOLCHAIN_USES_GLIBC),y)
	OSD_OPENIPC_OPTIONS = "-rdynamic -s -Os -lm"
else
	OSD_OPENIPC_OPTIONS = "-rdynamic -s -Os"
endif

define OSD_OPENIPC_BUILD_CMDS
	$(MAKE) CC=$(TARGET_CC) OPT=$(OSD_OPENIPC_OPTIONS) -C $(@D)/src
endef

define OSD_OPENIPC_INSTALL_TARGET_CMDS
	$(INSTALL) -m 755 -d $(TARGET_DIR)/etc
	$(INSTALL) -m 644 -t $(TARGET_DIR)/etc $(@D)/osd.yaml
	
	$(INSTALL) -m 755 -d $(TARGET_DIR)/root
	$(INSTALL) -m 644 -t $(TARGET_DIR)/root $(@D)/openipc_logo.bmp

	$(INSTALL) -m 755 -d $(TARGET_DIR)/usr/bin
	$(INSTALL) -m 755 $(@D)/osd $(TARGET_DIR)/usr/bin/osd_server

	$(INSTALL) -m 755 -d $(TARGET_DIR)/etc/init.d
	$(INSTALL) -m 755 -t $(TARGET_DIR)/etc/init.d $(@D)/S97osd
endef

$(eval $(generic-package))
