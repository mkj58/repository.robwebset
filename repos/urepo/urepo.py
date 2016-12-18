# -*- coding: utf-8 -*-
import xbmcgui
import xbmcaddon


# Call with the following code
#
# from resources.lib.urepo import URepoDialog
# URepoDialog.showURepoDialog('script.XXX')
class URepoDialog(xbmcgui.WindowXMLDialog):
    CLOSE_BUTTON = 302

    @staticmethod
    def showURepoDialog(addonName):
        # Check if a dialog has already been shown
        if xbmcgui.Window(10000).getProperty("RobwebsetURepoDialogShown") in ["", None]:
            xbmcgui.Window(10000).setProperty("RobwebsetURepoDialogShown", "true")

            dialog = URepoDialog("urepo-repository.xml", xbmcaddon.Addon(id=addonName).getAddonInfo('path').decode("utf-8"))
            dialog.doModal()
            del dialog

    def onClick(self, controlID):
        # Play button has been clicked
        if controlID == URepoDialog.CLOSE_BUTTON:
            xbmcgui.WindowXMLDialog.close(self)
