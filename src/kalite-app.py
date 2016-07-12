#!/usr/bin/python
#
# kalite-app.py
#
# Copyright (C) 2016 Endless Mobile, Inc.
# Authors:
#  Mario Sanchez Prada <mario@endlessm.com>
#  Niv Sardi <xaiki@endlessm.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

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

