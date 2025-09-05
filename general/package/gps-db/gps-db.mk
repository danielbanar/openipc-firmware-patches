################################################################################
#
# gps-db
#
################################################################################

GPS_DB_SITE = $(call github,danielbanar,gps-nmea-interface,$(GPS_DB_VERSION))
GPS_DB_VERSION = openipc

define GPS_DB_BUILD_CMDS
	(cd $(@D); $(TARGET_CC) -O2 -s gps.c -o gps -lm)
	(cd $(@D); $(TARGET_CC) -O2 -s gps_monitor.c -o gps_monitor)
endef

define GPS_DB_INSTALL_TARGET_CMDS
	$(INSTALL) -m 755 -d $(TARGET_DIR)/usr/bin
	$(INSTALL) -m 644 -t $(TARGET_DIR)/usr/bin $(@D)/gps
	$(INSTALL) -m 644 -t $(TARGET_DIR)/usr/bin $(@D)/gps_monitor

	$(INSTALL) -m 755 -d $(TARGET_DIR)/etc
	$(INSTALL) -m 644 -t $(TARGET_DIR)/etc $(@D)/gps.conf

	$(INSTALL) -m 755 -d $(TARGET_DIR)/etc/init.d
	$(INSTALL) -m 755 -t $(TARGET_DIR)/etc/init.d $(@D)/S71gps
endef

$(eval $(generic-package))
