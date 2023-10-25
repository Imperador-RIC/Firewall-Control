# -*- coding: utf-8 -*-

import modules.check, modules.messages.error, modules.messages.notify

from modules.var import *

import subprocess

if (modules.check.system_compatibility ()):

    if (modules.check.powershell_installed ()):

        if (modules.check.user_is_admin ()):

            import pystray as pys
            from PIL import Image

            def set_firewall_on () -> None:
                """Enable Windows Firewall"""

                global firewall_on, firewall_off

                if firewall_on:
                    return

                execute ('Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True')
                modules.messages.notify.notification ('Firewall modification', 'The firewall has been successfully enabled')
                firewall_on = True ; firewall_off = False

            def set_firewall_off () -> None:
                """Disable Windows Firewall"""

                global firewall_on, firewall_off

                if firewall_off:
                    return

                execute ('Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False')
                modules.messages.notify.notification ('Firewall modification', 'The firewall has been successfully disabled')
                firewall_on = False ; firewall_off = True,

            def set_private_profile () -> None:
                """Change Firewall profile to Private"""

                global private_profile, public_profile

                if private_profile:
                    return

                execute ('Set-NetConnectionProfile -NetworkCategory Private')
                modules.messages.notify.notification ('Profile modification', 'Profile has been changed to private')
                private_profile = True ; public_profile = False

            def set_public_profile () -> None:
                """Change Firewall profile to Public"""

                global private_profile, public_profile

                if public_profile:
                    return

                execute ('Set-NetConnectionProfile -NetworkCategory Public')
                modules.messages.notify.notification ('Profile modification', 'Profile has been changed to public')
                private_profile = False ; public_profile = True

            def execute (argv) -> None:
                """Executes the command that is received in PowerShell"""

                subprocess.run (['powershell.exe', argv], stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL, shell = True)

            def exit_app (icon) -> None:
                """Close the application"""

                icon.stop ()
                modules.messages.notify.notification ('Program closure', 'The program ended successfully')
                exit ()

            icon = Image.open (ICON_PATH)
            menu = (pys.MenuItem ('Turn On and Enable Firewall', set_firewall_on, checked = lambda item: firewall_on),
                    pys.MenuItem ('Turn Off and Disable Firewall', set_firewall_off, checked = lambda item: firewall_off),
                    pys.MenuItem ('Set Firewall with Private Profile', set_private_profile, checked = lambda item: private_profile),
                    pys.MenuItem ('Set Firewall with Public Profile', set_public_profile, checked = lambda item: public_profile),
                    pys.MenuItem ('Terminate the Program', exit_app))

            notifications = pys.Icon (APP_NAME, icon, APP_NAME, menu)
            notifications.run ()

        else:
            raise modules.messages.error.RequirementsError ('You must run the program as an administrator to continue!')

    else:
        raise modules.messages.error.RequirementsError ('The program was unable to execute commands in PowerShell!')

else:
    raise modules.messages.error.RequirementsError ('Your operating system is not compatible with the program!')
