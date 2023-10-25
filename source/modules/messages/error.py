# -*- coding: utf-8 -*-

"""Module containing only an exception object which comments the error through a dialog box instead of directly in the terminal"""

from modules.var import APP_NAME

from pymsgbox import alert

class RequirementsError (Exception):

    """Special exception in which the Windows dialog box is executed with the error message passed as a parameter"""

    def __init__ (self, text: str) -> None:

        alert (title = APP_NAME, text = text)
        exit ()
