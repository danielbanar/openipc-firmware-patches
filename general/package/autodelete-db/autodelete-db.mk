################################################################################
#
# AUTODELETE_DB
#
################################################################################

AUTODELETE_DB_SITE_METHOD = local
AUTODELETE_DB_SITE = $(AUTODELETE_DB_PKGDIR)/files

define AUTODELETE_DB_INSTALL_TARGET_CMDS
	$(INSTALL) -m 755 -d $(TARGET_DIR)/etc/init.d
	$(INSTALL) -m 755 -t $(TARGET_DIR)/etc/init.d $(AUTODELETE_DB_PKGDIR)/files/S97autodelete

	$(INSTALL) -m 755 -d $(TARGET_DIR)/usr/bin
	$(INSTALL) -m 755 -t $(TARGET_DIR)/usr/bin $(AUTODELETE_DB_PKGDIR)/files/autodelete
endef

$(eval $(generic-package))