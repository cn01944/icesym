#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Mon May 18 09:43:57 2009

import wx
from Home import Home

class SimulatorGUI(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        home = Home(None, -1, "")
        self.SetTopWindow(home)
        home.Show()
        return 1

# end of class SimulatorGUI

if __name__ == "__main__":
    SimulatorGUI = SimulatorGUI(0)
    SimulatorGUI.MainLoop()