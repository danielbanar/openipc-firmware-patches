################################################################################
#
# gps-db
#
################################################################################

MASINA_CLIENT_DB_SITE = $(call github,danielbanar,masina-client,$(MASINA_CLIENT_DB_VERSION))
MASINA_CLIENT_DB_VERSION = HEAD

define MASINA_CLIENT_DB_BUILD_CMDS
	$(MAKE) OUTPUT=$(@D) -C $(@D)
endef

define MASINA_CLIENT_DB_INSTALL_TARGET_CMDS
	$(INSTALL) -m 755 -d $(TARGET_DIR)/usr/bin
	$(INSTALL) -m 755 -t $(TARGET_DIR)/usr/bin $(@D)/masinaclient
	$(INSTALL) -m 755 -t $(TARGET_DIR)/usr/bin $(@D)/masinatelemetry
	$(INSTALL) -m 755 -t $(TARGET_DIR)/usr/bin $(@D)/modem_link
	$(INSTALL) -m 755 -t $(TARGET_DIR)/usr/bin $(@D)/modem_alink
	$(INSTALL) -m 755 -t $(TARGET_DIR)/usr/bin $(@D)/update_masina

	$(INSTALL) -m 755 -d $(TARGET_DIR)/etc
	$(INSTALL) -m 644 -t $(TARGET_DIR)/etc $(@D)/masina.conf

	$(INSTALL) -m 755 -d $(TARGET_DIR)/etc/init.d
	$(INSTALL) -m 755 -t $(TARGET_DIR)/etc/init.d $(@D)/S90masinaclient
	$(INSTALL) -m 755 -t $(TARGET_DIR)/etc/init.d $(@D)/S91masinatelemetry
	$(INSTALL) -m 755 -t $(TARGET_DIR)/etc/init.d $(@D)/S92modemlink
	$(INSTALL) -m 755 -t $(TARGET_DIR)/etc/init.d $(@D)/S93modemalink
endef

$(eval $(generic-package))
