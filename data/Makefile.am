@INTLTOOL_DESKTOP_RULE@
@INTLTOOL_XML_RULE@

desktopdir = $(datadir)/applications
desktop_in_files = org.learningequality.KALite.desktop.in
desktop_DATA = $(desktop_in_files:.desktop.in=.desktop)

icon64dir = $(datadir)/icons/hicolor/64x64/apps
icon64_DATA = org.learningequality.KALite.png

appdatadir = $(datadir)/appdata
appdata_in_files = org.learningequality.KALite.appdata.xml.in
appdata_DATA = $(appdata_in_files:.xml.in=.xml)


CLEANFILES = \
	$(appdata_DATA) \
	$(desktop_DATA) \
	$(NULL)

EXTRA_DIST = \
	$(appdata_in_files) \
	$(desktop_in_files) \
	$(icon64_DATA) \
	$(NULL)
