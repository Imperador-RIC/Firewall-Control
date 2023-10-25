# -*- coding: utf-8 -*-

"""Module containing the main program variables defined with their default values"""

from os import path

from modules.check import get_firewall_profile

PATH = path.abspath (path.join (path.dirname (__file__), '..'))

APP_NAME = 'Firewall Control'
ICON_PATH = fr'{path.join (PATH, "image", "icon.ico")}'

firewall_on = True
firewall_off = False

private_profile = False
public_profile = False

firewall_profile = get_firewall_profile ()

if firewall_profile == 1:
    private_profile = True

elif firewall_profile == 2:
    public_profile = True

else:
    firewall_on = False ; firewall_off = True
