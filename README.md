# eos-kalite-app

## Description

This package is used by EOS to package ka-lite as a flatpak, to provide the
"client side" entry point to the sandboxed application, as well as the
necessary bits to properly integrate with the desktop environment.

## Detailed description

This package provides the following elements:
  * `kalite-app.py`: launcher script that takes care of loading the URI to
    load the Web UI from the local browser. It relies on the OpenURI portal.
  * `kalite-app.desktop` + `kalite-app.png`: icon and application information
     according to the Desktop Entry Specification, to integrate with the shell.
  * `kalite-app.appdata.xml`: aplication information in AppData format for
    integration with app centers (e.g. GNOME Software)

All this files will be included inside the flatpak bundle, and will be run from
the outside with `flatpak run org.learningequality.KALite`.

The rest of the files will live inside the flatpak bundles but will be also be
exported by flatpak so that the host system can used them from the outside.

## Requirements

This flatpak uses the OpenURI portal and so it requires that the host system has
installed at least the following components:
  * flatpak >= 0.6.6
  * xdg-desktop-portal >= 1.0
  * xdg-desktop-portal-gtk >= 1.0

Besides those details, eos-kalite-app is meant to be bundled together with
the KA Lite server ([source code here](https://github.com/endlessm/ka-lite-source)) which can be either manually started
or automatically started via systemd's socket-activation, which is the ideal
scenario and the one used in Endless (requires [integration with the OS](https://github.com/endlessm/eos-kalite-system-helper)).
