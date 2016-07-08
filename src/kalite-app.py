#!/usr/bin/python
import socket
from gi.repository import Gio
from gi.repository import GLib

def request_portal(url):
    bus = Gio.bus_get_sync(Gio.BusType.SESSION, None)
    proxy = Gio.DBusProxy.new_sync(bus, Gio.DBusProxyFlags.NONE, None,
                                   'org.freedesktop.portal.Desktop',
                                   '/org/freedesktop/portal/desktop',
                                   'org.freedesktop.portal.OpenURI', None)

    res = proxy.OpenURI('(ssa{sv})',
                        '',                          # Parent window ID
                        url,                         # URL
                        GLib.Variant('a{sv}', None)) # Options

# run KALite via socket activation
port = 8008
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection = sock.connect_ex(('127.0.0.1', port))

request_portal('http://localhost:8008')

