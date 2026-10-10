################################################################################
#
# WIREGUARD_DB
#
################################################################################

WIREGUARD_DB_SITE = $(call github,danielbanar,openipc-wireguard,$(WIREGUARD_DB_VERSION))
WIREGUARD_DB_VERSION = HEAD

define WIREGUARD_DB_INSTALL_TARGET_CMDS
	$(INSTALL) -m 755 -d $(TARGET_DIR)/etc
	$(INSTALL) -m 644 -t $(TARGET_DIR)/etc $(@D)/wireguard

	$(INSTALL) -m 755 -d $(TARGET_DIR)/etc/init.d
	$(INSTALL) -m 755 -t $(TARGET_DIR)/etc/init.d $(@D)/S80wireguard

	$(INSTALL) -m 755 -d $(TARGET_DIR)/usr/bin
	$(INSTALL) -m 755 -t $(TARGET_DIR)/usr/bin $(@D)/update_wg
endef

$(eval $(generic-package))