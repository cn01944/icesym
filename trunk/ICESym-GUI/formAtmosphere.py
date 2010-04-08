# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Thu Sep 17 20:05:00 2009

import wx
from validations import numberValidator
from help_texts import help_atmosphere
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

# end wxGlade

class formAtmosphere(wx.Dialog):
    data = {}
    edit = -1
    position = (0,0)

    def __init__(self, *args, **kwds):
        # begin wxGlade: formAtmosphere.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER|wx.THICK_FRAME
        wx.Dialog.__init__(self, *args, **kwds)
        self.panel_buttons = wx.Panel(self, -1)
        self.panel_configure = wx.ScrolledWindow(self, -1, style=wx.TAB_TRAVERSAL)
        self.panel = wx.Panel(self.panel_configure, -1)
        self.label_0 = wx.StaticText(self.panel, -1, "Density: ")
        self.data['rho'] = wx.TextCtrl(self.panel, -1, "")
        self.label_1 = wx.StaticText(self.panel, -1, "Velocity: ")
        self.data['u'] = wx.TextCtrl(self.panel, -1, "")
        self.label_2 = wx.StaticText(self.panel, -1, "Pressure: ")
        self.data['p'] = wx.TextCtrl(self.panel, -1, "")
        self.accept = wx.Button(self.panel_buttons, wx.ID_OK, "")
        self.cancel = wx.Button(self.panel_buttons, wx.ID_CANCEL, "")
        self.help = wx.ContextHelpButton(self.panel_buttons)

        self.__set_properties()
        self.setContextualHelp()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.ConfigureAccept, self.accept)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: formAtmosphere.__set_properties
        self.SetTitle("Configure Atmosphere")
        self.SetSize(wx.DLG_SZE(self, (140, 70)))
        self.label_0.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['rho'].SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['rho'].SetValidator(numberValidator())
        self.label_1.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['u'].SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['u'].SetValidator(numberValidator())
        self.label_2.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['p'].SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['p'].SetValidator(numberValidator())
        self.panel_configure.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.panel_configure.SetScrollRate(10, 10)
        self.accept.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.cancel.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: formAtmosphere.__do_layout
        configure_background = wx.BoxSizer(wx.VERTICAL)
        sizer_buttons = wx.GridSizer(1, 3, 0, 0)
        configure_sizer = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_6 = wx.FlexGridSizer(3, 2, 0, 0)
        grid_sizer_6.Add(self.label_0, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_6.Add(self.data['rho'], 0, 0, 0)
        grid_sizer_6.Add(self.label_1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_6.Add(self.data['u'], 0, 0, 0)
        grid_sizer_6.Add(self.label_2, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_6.Add(self.data['p'], 0, 0, 0)
        self.panel.SetSizer(grid_sizer_6)
        configure_sizer.Add(self.panel, 1, wx.ALL|wx.EXPAND, 8)
        self.panel_configure.SetSizer(configure_sizer)
        configure_background.Add(self.panel_configure, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 1)
        sizer_buttons.Add(self.accept, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_buttons.Add(self.help, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_buttons.Add(self.cancel, 0, wx.ALIGN_CENTER_VERTICAL| wx.ALIGN_LEFT, 0)
        self.panel_buttons.SetSizer(sizer_buttons)
        configure_background.Add(self.panel_buttons, 0, wx.EXPAND, 0)
        self.SetSizer(configure_background)
        self.Layout()
        # end wxGlade

    def setContextualHelp(self):
		for key in self.data:
			self.data[key].SetHelpText(help_atmosphere[key])


    def ConfigureAccept(self, event): # wxGlade: formAtmosphere.<event_handler>
        can_out=1
        for key in self.data:
            if (self.data[key].GetValidator()):
                if(not(self.data[key].GetValidator().Validate(self,'number'))):
                    can_out=0
        
        if(can_out==1):
            self.EndModal(wx.ID_OK)
        else:
            wx.MessageBox("Some fields have some error (empty or no-digit value)!", "Error")

# end of class formAtmosphere

