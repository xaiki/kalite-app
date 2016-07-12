AC_PREREQ([2.63])
AC_INIT([eos-kalite-app], [1.0.0], [mario@endlessm.com])
AC_CONFIG_MACRO_DIR([m4])
AC_CONFIG_HEADERS([config.h])

AM_INIT_AUTOMAKE([1.11 -Wno-portability foreign no-define tar-ustar no-dist-gzip dist-xz])
AM_MAINTAINER_MODE([enable])
AM_SILENT_RULES([yes])

# Translations

IT_PROG_INTLTOOL([0.40.0])

GETTEXT_PACKAGE=eos-kalite-app
AC_SUBST(GETTEXT_PACKAGE)
AC_DEFINE_UNQUOTED([GETTEXT_PACKAGE], ["$GETTEXT_PACKAGE"],
                   [The domain to use with gettext])

AC_CONFIG_FILES([
Makefile
data/Makefile
src/Makefile
po/Makefile.in
])
AC_OUTPUT

echo "
    KA Lite App $VERSION
"
