# -*- coding: utf-8 -*-

"""Module to check if the operating system is windows 8 or higher, and if the system has PowerShell enabled or not"""

import platform, subprocess
import win32com.client

from ctypes import windll
from typing import Union

def system_compatibility () -> bool:

    """Function that checks if the operating system is windows 8 or higher

    Returns:
        bool: Returns true if the system is windows 8 or higher, and false if the system is 7, lower than 7, or other (May return a false positive for alternate Windows systems such as Windows ARM or other Windows)
    """

    system = platform.system ()
    version = platform.release ()

    if system == 'Windows' and float (version) > 6.1:
        del system, version
        return True

    else:
        return False

def powershell_installed () -> bool:

    """Function that checks whether PowerShell is enabled

    Returns:
        bool: Returns true if PowerShell is found as a system command, and false if not (This is a way to check if PowerShell is enabled or not on the system)
    """

    try:
        subprocess.check_output (['where', 'powershell.exe'], creationflags = subprocess.CREATE_NO_WINDOW)
        return True

    except (subprocess.CalledProcessError):
        return False

def user_is_admin () -> bool:

    """Function that verifies that the program is running as an administrator

    Returns:
        bool: Returns true if the program is running as an administrator, and false if it is not running as an administrator
    """

    if (windll.shell32.IsUserAnAdmin () != 0):
        return True

    else:
        return False

def get_firewall_profile () -> Union [int, None]:

    """Function that checks what the Firewall profile is at the moment

       Returns:
            int: Returns the number equivalent to each Firewall profile, 0 for "Domain", 1 for "Private", and 2 for "Public"
            None: If none of the previous 3 alternatives are returned, regardless of what is detected, the result returned will be None
    """

    firewall = win32com.client.Dispatch ('HNetCfg.FwMgr')
    profile = firewall.LocalPolicy.CurrentProfile

    if profile.FirewallEnabled:
        return profile.Type

    return None
