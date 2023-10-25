# -*- coding: utf-8 -*-

"""Module containing a function for displaying notifications in Windows"""

from modules.var import APP_NAME, ICON_PATH

from winotify import Notification

def notification (title: str, msg: str) -> None:

    """Function for displaying custom notifications using the Windows API

    Receive:
        title: string containing the title of the notification
        msg: string containing the notification message

    Returns:
        None: There is no return in the function
    """

    notify = Notification (app_id = APP_NAME, icon = ICON_PATH, duration = 'short', title = title, msg = msg)
    notify.show ()

    return None
