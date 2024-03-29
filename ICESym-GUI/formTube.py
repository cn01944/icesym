# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Wed Sep 16 08:34:53 2009

import wx
from validations import numberValidator
from extraFunctions import *
from help_texts import help_tube
# begin wxGlade: dependencies
import wx.grid
# end wxGlade

# begin wxGlade: extracode

# end wxGlade

class formTube(wx.Dialog):
    data={}
    edit = -1
    position = (0,0)

    def __init__(self, *args, **kwds):
        # begin wxGlade: formTube.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER|wx.THICK_FRAME
        wx.Dialog.__init__(self, *args, **kwds)
        self.panel_buttons = wx.Panel(self, -1)
        self.panel_configure = wx.Panel(self, -1)
        self.configure_notebook = wx.Notebook(self.panel_configure, -1, style=0)
        self.notebook_state = wx.ScrolledWindow(self.configure_notebook, -1, style=wx.TAB_TRAVERSAL)
        self.notebook_general = wx.ScrolledWindow(self.configure_notebook, -1, style=wx.TAB_TRAVERSAL)
        self.notebook_post = wx.ScrolledWindow(self.configure_notebook, -1, style=wx.TAB_TRAVERSAL)
        self.label_0 = wx.StaticText(self.notebook_general, -1, "Number of Nodes:")
        self.data['nnod'] = wx.TextCtrl(self.notebook_general, -1, "")
        self.label_1 = wx.StaticText(self.notebook_general, -1, "Degress of Freedom: ")
        self.data['ndof'] = wx.TextCtrl(self.notebook_general, -1, "3", style=wx.TE_READONLY)
        self.label_2 = wx.StaticText(self.notebook_general, -1, "Length: ")
        self.data['longitud'] = wx.TextCtrl(self.notebook_general, -1, "")
        self.checkbox_1 = wx.CheckBox(self.notebook_general, -1, "Equispaced")
        self.checkbox_2 = wx.CheckBox(self.notebook_general, -1, "Has Curvature")
        self.panel_1 = wx.Panel(self.notebook_general, -1)
        self.label_4 = wx.StaticText(self.notebook_general, -1, "Xnod:        ")
        self.button_1 = wx.Button(self.notebook_general, -1, "...")
        self.data['xnod'] = wx.grid.Grid(self.notebook_general, -1, size=(1, 1))
        self.label_5 = wx.StaticText(self.notebook_general, -1, "Diameter:          ")
        self.button_2 = wx.Button(self.notebook_general, -1, "...")
        self.data['diameter'] = wx.grid.Grid(self.notebook_general, -1, size=(1, 1))
        self.label_6 = wx.StaticText(self.notebook_general, -1, "TWall:       ")
        self.button_3 = wx.Button(self.notebook_general, -1, "...")
        self.data['twall'] = wx.grid.Grid(self.notebook_general, -1, size=(1, 1))
        self.label_7 = wx.StaticText(self.notebook_general, -1, "Curvature: ")
        self.button_4 = wx.Button(self.notebook_general, -1, "...")
        self.data['curvature'] = wx.grid.Grid(self.notebook_general, -1, size=(1, 1))
        self.data['state_ini'] = wx.grid.Grid(self.notebook_state, -1, size=(1, 1))
        self.button_5 = wx.Button(self.notebook_state, -1, "...")
        self.data['typeSave'] = wx.RadioBox(self.notebook_post, -1, "", choices=["Save State for All Nodes","Save For Normalized Position Nodes","Nothing"], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        #self.data['numNorm'] = wx.CheckBox(self.notebook_post, -1, "Calculate Extras (mass I/O, rate, etc) for Selected Nodes")
        self.label_9 = wx.StaticText(self.notebook_post, -1, "Number of Normalized Points:")
        self.data['numNorm'] = wx.TextCtrl(self.notebook_post, -1, "3")
        #self.label_10 = wx.StaticText(self.notebook_post, -1, "Normalized Position (X/L):")
        self.data['posNorm'] = wx.grid.Grid(self.notebook_post, -1, size=(1, 1))
        self.data['histo'] = wx.TextCtrl(self.notebook_post, -1, "")
        self.data['label'] = wx.TextCtrl(self.notebook_general, -1, "")
        self.label_12 = wx.StaticText(self.notebook_general, -1, "Label:")

        self.button_constDiam = wx.Button(self.notebook_general, -1, "const")
        self.button_linearDiam = wx.Button(self.notebook_general, -1, "linear")
        self.button_constTemp = wx.Button(self.notebook_general, -1, "const")
        self.button_linearTemp = wx.Button(self.notebook_general, -1, "linear")
        
        self.accept = wx.Button(self.panel_buttons, wx.ID_OK, "")
        self.cancel = wx.Button(self.panel_buttons, wx.ID_CANCEL, "")
        self.help = wx.ContextHelpButton(self.panel_buttons)

        self.__set_properties()
        self.setContextualHelp()
        self.__do_layout()

        self.Bind(wx.EVT_TEXT, self.onChangeNodes, self.data['nnod'])
        self.Bind(wx.EVT_TEXT, self.onChangeNdof, self.data['ndof'])
        self.Bind(wx.EVT_TEXT, self.onSetLength, self.data['longitud'])
        self.Bind(wx.EVT_CHECKBOX, self.onEquispaced, self.checkbox_1)
        self.Bind(wx.EVT_CHECKBOX, self.onHasCurvature, self.checkbox_2)
        self.Bind(wx.EVT_BUTTON, self.onLoadxnod, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.onLoadArea, self.button_2)
        self.Bind(wx.EVT_BUTTON, self.onLoadTwall, self.button_3)
        self.Bind(wx.EVT_BUTTON, self.onLoadCurv, self.button_4)
        self.Bind(wx.EVT_BUTTON, self.onLoadState, self.button_5)
        self.Bind(wx.EVT_BUTTON, self.ConfigureAccept, self.accept)
        self.Bind(wx.EVT_RADIOBOX, self.onHistoMode, self.data['typeSave'])
        self.Bind(wx.EVT_TEXT, self.onChangeNumNorm, self.data['numNorm'])
        self.Bind(wx.grid.EVT_GRID_CMD_CELL_CHANGE, self.onChangePosNorm, self.data['posNorm'])
        self.Bind(wx.EVT_BUTTON, self.onConstDiam, self.button_constDiam)
        self.Bind(wx.EVT_BUTTON, self.onLinearDiam, self.button_linearDiam)
        self.Bind(wx.EVT_BUTTON, self.onConstTemp, self.button_constTemp)
        self.Bind(wx.EVT_BUTTON, self.onLinearTemp, self.button_linearTemp)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: formTube.__set_properties
        self.SetTitle("Configure Tube")
        self.SetSize(wx.DLG_SZE(self, (320, 280)))
        self.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.label_0.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['nnod'].SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['nnod'].SetValidator(numberValidator())
        self.label_1.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['ndof'].SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['ndof'].SetValidator(numberValidator())
        self.label_2.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['longitud'].SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['longitud'].SetValidator(numberValidator())
        self.checkbox_1.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.checkbox_2.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.checkbox_2.SetValue(1)
        self.label_4.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.button_1.SetMinSize(wx.DLG_SZE(self.button_1, (16, 12)))
        self.data['xnod'].CreateGrid(1, 1)
        self.data['xnod'].SetRowLabelSize(25)
        self.data['xnod'].SetColLabelSize(15)
        self.data['xnod'].EnableDragColSize(0)
        self.data['xnod'].EnableDragRowSize(0)
        self.data['xnod'].EnableDragGridSize(0)
        self.data['xnod'].SetColLabelValue(0, "Position")
        self.data['xnod'].SetMinSize(wx.DLG_SZE(self.data['xnod'], (62, 100)))
        self.data['xnod'].SetDefaultCellFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['xnod'].SetDefaultRowSize(18)
        self.data['xnod'].SetLabelFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.label_5.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.button_2.SetMinSize(wx.DLG_SZE(self.button_2, (16, 12)))
        self.data['diameter'].CreateGrid(1, 1)
        self.data['diameter'].SetRowLabelSize(25)
        self.data['diameter'].SetColLabelSize(18)
        self.data['diameter'].EnableDragColSize(0)
        self.data['diameter'].EnableDragRowSize(0)
        self.data['diameter'].EnableDragGridSize(0)
        self.data['diameter'].SetColLabelValue(0, "Diameter")
        self.data['diameter'].SetMinSize(wx.DLG_SZE(self.data['diameter'], (60, 100)))
        self.data['diameter'].SetDefaultCellFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['diameter'].SetDefaultRowSize(18)
        self.data['diameter'].SetLabelFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.label_6.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.button_3.SetMinSize(wx.DLG_SZE(self.button_3, (16, 12)))
        self.data['twall'].CreateGrid(1, 1)
        self.data['twall'].SetRowLabelSize(25)
        self.data['twall'].SetColLabelSize(18)
        self.data['twall'].EnableDragColSize(0)
        self.data['twall'].EnableDragRowSize(0)
        self.data['twall'].EnableDragGridSize(0)
        self.data['twall'].SetColLabelValue(0, "Temperature")
        self.data['twall'].SetMinSize(wx.DLG_SZE(self.data['twall'], (60, 100)))
        self.data['twall'].SetDefaultCellFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['twall'].SetDefaultRowSize(18)
        self.data['twall'].SetLabelFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.label_7.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.label_9.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.button_4.SetMinSize(wx.DLG_SZE(self.button_4, (16, 12)))
        self.data['curvature'].CreateGrid(1, 1)
        self.data['curvature'].SetRowLabelSize(25)
        self.data['curvature'].SetColLabelSize(18)
        self.data['curvature'].EnableDragColSize(0)
        self.data['curvature'].EnableDragRowSize(0)
        self.data['curvature'].EnableDragGridSize(0)
        self.data['curvature'].SetColLabelValue(0, "Curvature")
        self.data['curvature'].SetMinSize(wx.DLG_SZE(self.data['curvature'], (60, 100)))
        self.data['curvature'].SetDefaultCellFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['curvature'].SetDefaultRowSize(18)
        self.data['curvature'].SetLabelFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.notebook_general.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.notebook_general.SetScrollRate(10, 10)
        self.data['state_ini'].CreateGrid(1, 3)
        self.data['state_ini'].SetRowLabelSize(25)
        self.data['state_ini'].SetColLabelSize(15)
        self.data['state_ini'].EnableDragColSize(0)
        self.data['state_ini'].EnableDragRowSize(0)
        self.data['state_ini'].EnableDragGridSize(0)
        self.data['state_ini'].SetColLabelValue(0, "Density")
        self.data['state_ini'].SetColLabelValue(1, "Velocity")
        self.data['state_ini'].SetColLabelValue(2, "Pressure")
        self.data['state_ini'].SetMinSize(wx.DLG_SZE(self.data['state_ini'], (161, 100)))
        self.data['state_ini'].SetDefaultCellFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['state_ini'].SetDefaultRowSize(18)
        self.data['state_ini'].SetLabelFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        
        self.data['typeSave'].SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['numNorm'].SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['histo'].SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['numNorm'].Enable(False)
        self.data['posNorm'].Enable(False)
        self.data['histo'].Enable(False)
        self.notebook_post.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.notebook_post.SetScrollRate(10, 10)
        self.data['posNorm'].CreateGrid(3, 1)
        self.data['posNorm'].SetRowLabelSize(25)
        self.data['posNorm'].SetColLabelSize(20)
        self.data['posNorm'].EnableDragColSize(0)
        self.data['posNorm'].EnableDragRowSize(0)
        self.data['posNorm'].EnableDragGridSize(0)
        self.data['posNorm'].SetColLabelValue(0, "X/L [0,1]:")
        self.data['posNorm'].SetMinSize(wx.DLG_SZE(self.data['state_ini'], (58,53)))
        self.data['posNorm'].SetDefaultCellFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['posNorm'].SetDefaultRowSize(18)
        self.data['posNorm'].SetLabelFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['label'].SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.label_12.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.button_constDiam.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.button_constDiam.SetMinSize(wx.DLG_SZE(self.button_2, (25, 12)))
        self.button_constTemp.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.button_constTemp.SetMinSize(wx.DLG_SZE(self.button_2, (25, 12)))
        self.button_linearDiam.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.button_linearDiam.SetMinSize(wx.DLG_SZE(self.button_2, (25, 12)))
        self.button_linearTemp.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.button_linearTemp.SetMinSize(wx.DLG_SZE(self.button_2, (25, 12)))
        self.button_5.SetMinSize(wx.DLG_SZE(self.button_5, (16, 12)))
        self.notebook_state.SetScrollRate(10, 10)
        self.configure_notebook.SetMinSize(wx.DLG_SZE(self.configure_notebook, (270, 362)))
        self.configure_notebook.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.panel_configure.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.accept.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.cancel.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: formTube.__do_layout
        configure_background = wx.BoxSizer(wx.VERTICAL)
        sizer_buttons = wx.GridSizer(1, 3, 0, 0)
        configure_sizer = wx.BoxSizer(wx.HORIZONTAL)

        grid_sizer_back = wx.FlexGridSizer(3, 2, 5, 5)
        grid_sizer_values = wx.FlexGridSizer(5, 2, 0, 0)
        grid_sizer_xnod = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_xnodsub = wx.FlexGridSizer(2, 1, 0, 0)
        grid_sizer_diam = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_diamsub = wx.FlexGridSizer(4, 1, 0, 0)

        grid_sizer_curv = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_curvsub = wx.FlexGridSizer(2, 1, 0, 0)
        grid_sizer_temp = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_tempsub = wx.FlexGridSizer(4, 1, 0, 0)

        grid_sizer_histo = wx.FlexGridSizer(4, 1, 10, 10)
        grid_sizer_state = wx.FlexGridSizer(1, 2, 0, 0)

        grid_sizer_values.Add(self.label_12, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_values.Add(self.data['label'], 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_values.Add(self.label_0, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_values.Add(self.data['nnod'], 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_values.Add(self.label_1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_values.Add(self.data['ndof'], 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_values.Add(self.label_2, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_values.Add(self.data['longitud'], 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_values.Add(self.checkbox_1, 0, 0, 0)
        grid_sizer_values.Add(self.checkbox_2, 0, 0, 0)
        grid_sizer_back.Add(grid_sizer_values, 1, wx.EXPAND, 0)

        grid_sizer_back.Add(self.panel_1, 1, wx.EXPAND, 0)
        
        grid_sizer_xnodsub.Add(self.label_4, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_xnodsub.Add(self.button_1, 0, 0, 0)
        grid_sizer_xnod.Add(grid_sizer_xnodsub, 1, wx.EXPAND, 0)
        grid_sizer_xnod.Add(self.data['xnod'], 1, wx.EXPAND, 0)
        grid_sizer_back.Add(grid_sizer_xnod, 1, wx.EXPAND, 0)

        grid_sizer_diamsub.Add(self.label_5, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_diamsub.Add(self.button_constDiam, 0, 0, 0)
        grid_sizer_diamsub.Add(self.button_linearDiam, 0, 0, 0)
        grid_sizer_diamsub.Add(self.button_2, 0, 0, 0)
        grid_sizer_diam.Add(grid_sizer_diamsub, 1, wx.EXPAND, 0)
        grid_sizer_diam.Add(self.data['diameter'], 1, wx.EXPAND, 0)
        grid_sizer_back.Add(grid_sizer_diam, 1, wx.EXPAND, 0)

        grid_sizer_tempsub.Add(self.label_6, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_tempsub.Add(self.button_constTemp, 0, 0, 0)
        grid_sizer_tempsub.Add(self.button_linearTemp, 0, 0, 0)
        grid_sizer_tempsub.Add(self.button_3, 0, 0, 0)
        grid_sizer_temp.Add(grid_sizer_tempsub, 1, wx.EXPAND, 0)
        grid_sizer_temp.Add(self.data['twall'], 1, wx.EXPAND, 0)
        grid_sizer_back.Add(grid_sizer_temp, 1, wx.EXPAND, 0)

        grid_sizer_curvsub.Add(self.label_7, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_curvsub.Add(self.button_4, 0, 0, 0)
        grid_sizer_curv.Add(grid_sizer_curvsub, 1, wx.EXPAND, 0)
        grid_sizer_curv.Add(self.data['curvature'], 1, wx.EXPAND, 0)
        grid_sizer_back.Add(grid_sizer_curv, 1, wx.EXPAND, 0)

        self.notebook_general.SetSizer(grid_sizer_back)

        grid_sizer_state.Add(self.data['state_ini'], 1, wx.EXPAND, 0)
        grid_sizer_state.Add(self.button_5, 0, 0, 0)
        self.notebook_state.SetSizer(grid_sizer_state)

        grid_sizer_histo.Add(self.label_9, 0, wx.ALIGN_CENTER_VERTICAL, 0) 
        grid_sizer_histo.Add(self.data['typeSave'], 0, 0, 0)
        grid_sizer_histo.Add(self.label_9, 0, wx.ALIGN_CENTER_VERTICAL, 0) 
        grid_sizer_histo.Add(self.data['numNorm'], 0, 0, 0)
        grid_sizer_histo.Add(self.data['posNorm'], 0, 0, 0)
        grid_sizer_histo.Add(self.data['histo'], 0, 0, 0)
        self.notebook_post.SetSizer(grid_sizer_histo)
 
        self.configure_notebook.AddPage(self.notebook_general, "General")
        self.configure_notebook.AddPage(self.notebook_state, "State")
        self.configure_notebook.AddPage(self.notebook_post, "Post Process")

        configure_sizer.Add(self.configure_notebook, 1, wx.EXPAND, 0)
        self.panel_configure.SetSizer(configure_sizer)
        configure_background.Add(self.panel_configure, 1, wx.EXPAND, 0)
        sizer_buttons.Add(self.accept, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_buttons.Add(self.help, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_buttons.Add(self.cancel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT, 0)
        self.panel_buttons.SetSizer(sizer_buttons)
        configure_background.Add(self.panel_buttons, 0, wx.EXPAND, 0)
        self.SetSizer(configure_background)
        configure_background.Fit(self)
        self.Layout()
        # end wxGlade

    def onSetLength(self, event): # wxGlade: formTube.<event_handler>
        if(self.checkbox_1.GetValue()):
		nodes = int(self.data['nnod'].GetValue())
		length = float(self.data['longitud'].GetValue())
		for i in range(nodes):
			value = i*float(length/(nodes-1))
			self.data['xnod'].SetCellValue(i,0,str(value))

    def setContextualHelp(self):
		for key in self.data:
			self.data[key].SetHelpText(help_tube[key])

    def onEquispaced(self, event): # wxGlade: formTube.<event_handler>
        if(self.checkbox_1.GetValue()):
		self.data['xnod'].EnableEditing(0)
		self.onSetLength(1)
	else:
		self.data['xnod'].EnableEditing(1)
		self.data['xnod'].ClearGrid()

    def onHasCurvature(self, event): # wxGlade: formTube.<event_handler>
        if(self.checkbox_2.GetValue()):
		self.data['curvature'].Enable(1)
	else:
		self.data['curvature'].Enable(0)

	
    def ConfigureAccept(self, event): # wxGlade: formTube.<event_handler>
        can_out=1
        for key in self.data:
            if (self.data[key].GetValidator()):
                if(not(self.data[key].GetValidator().Validate(self,'number'))):
                    can_out=0
        
        if(can_out==1):
            self.EndModal(wx.ID_OK)
        else:
            wx.MessageBox("Some fields have some error (empty or no-digit value)!", "Error")

    def onChangeNodes(self, event): # wxGlade: formTube.<event_handler>
        try:
            nodes = int(self.data['nnod'].GetValue())
            nxnod =	self.data['xnod'].GetNumberRows()
            ndiam =	self.data['diameter'].GetNumberRows()
            ntwall = self.data['twall'].GetNumberRows()
            ncurv =	self.data['curvature'].GetNumberRows()
            nstate = self.data['state_ini'].GetNumberRows()
            if(nodes>nxnod):
                self.data['xnod'].AppendRows(nodes-nxnod)
            else:
                if(nodes<nxnod):
                    self.data['xnod'].DeleteRows(nxnod-(nxnod-nodes), nxnod-nodes)
            self.onEquispaced(1)
            if(nodes>ndiam):
                self.data['diameter'].AppendRows(nodes-ndiam)
            else:
                if(nodes<ndiam):
                    self.data['diameter'].DeleteRows(ndiam-(ndiam-nodes), ndiam-nodes)
            if(nodes>ntwall):
                self.data['twall'].AppendRows(nodes-ntwall)
            else:
                if(nodes<ntwall):
                    self.data['twall'].DeleteRows(ntwall-(ntwall-nodes), ntwall-nodes)
            if(nodes>ncurv):
                self.data['curvature'].AppendRows(nodes-ncurv)
            else:
                if(nodes<ncurv):
                    self.data['curvature'].DeleteRows(ncurv-(ncurv-nodes), ncurv-nodes)
            if(nodes>nstate):
                self.data['state_ini'].AppendRows(nodes-nstate)
            else:
                if(nodes<nstate):
                    self.data['state_ini'].DeleteRows(nstate-(nstate-nodes), nstate-nodes)
        except ValueError:
            nnod = None

    def onChangeNdof(self, event): # wxGlade: formTube.<event_handler>
        try:
            ndof = int(self.data['ndof'].GetValue())
            nstate = self.data['state_ini'].GetNumberCols()
            if(ndof>nstate):
                self.data['state_ini'].AppendCols(ndof-nstate)
            else:
                if(ndof<nstate):
                    self.data['state_ini'].DeleteCols(nstate-(nstate-ndof), nstate-ndof)
       	except ValueError:
            ndof = None

    def onLoadxnod(self, event): # wxGlade: formTube.<event_handler>
        try:
            nodes = int(self.data['nnod'].GetValue())
            if self.data['xnod'].IsEnabled():
                dlg = wx.FileDialog(self, message="Open a Data File", defaultDir="./loads",defaultFile="", wildcard="*.txt", style=wx.OPEN)
                if dlg.ShowModal() == wx.ID_OK:
                    namefile = dlg.GetPath()
                    data = loadData(namefile,nodes,1)     
                    if(data==-1):
                       wx.MessageBox("Incorrect data", "Error")
                    else:				
                       setGrid(data,self.data['xnod'])
                       self.checkbox_1.SetValue(0)  
                dlg.Destroy()
            else:
                wx.MessageBox("You must active this field", "Error") 
       	except ValueError:
            wx.MessageBox("You must complete number of nodes first", "Error")

    def onLoadArea(self, event): # wxGlade: formTube.<event_handler>
        try:
            nodes = int(self.data['nnod'].GetValue())
            if self.data['diameter'].IsEnabled():
                dlg = wx.FileDialog(self, message="Open a Data File", defaultDir="./loads",defaultFile="", wildcard="*.txt", style=wx.OPEN)
                if dlg.ShowModal() == wx.ID_OK:
                    namefile = dlg.GetPath()
                    data = loadData(namefile,nodes,1)     
                    if(data==-1):
                       wx.MessageBox("Incorrect data", "Error")
                    else:				
                       setGrid(data,self.data['diameter'])
                dlg.Destroy()
            else:
                wx.MessageBox("You must active this field", "Error") 
       	except ValueError:
            wx.MessageBox("You must complete number of nodes first", "Error")

    def onLoadTwall(self, event): # wxGlade: formTube.<event_handler>
        try:
            nodes = int(self.data['nnod'].GetValue())
            if self.data['twall'].IsEnabled():
                dlg = wx.FileDialog(self, message="Open a Data File", defaultDir="./loads",defaultFile="", wildcard="*.txt", style=wx.OPEN)
                if dlg.ShowModal() == wx.ID_OK:
                    namefile = dlg.GetPath()
                    data = loadData(namefile,nodes,1)     
                    if(data==-1):
                       wx.MessageBox("Incorrect data", "Error")
                    else:				
                       setGrid(data,self.data['twall'])
                dlg.Destroy()
            else:
                wx.MessageBox("You must active this field", "Error") 
       	except ValueError:
            wx.MessageBox("You must complete number of nodes first", "Error")

    def onLoadCurv(self, event): # wxGlade: formTube.<event_handler>
        try:
            nodes = int(self.data['nnod'].GetValue())
            if self.data['curvature'].IsEnabled():
                dlg = wx.FileDialog(self, message="Open a Data File", defaultDir="./loads",defaultFile="", wildcard="*.txt", style=wx.OPEN)
                if dlg.ShowModal() == wx.ID_OK:
                    namefile = dlg.GetPath()
                    data = loadData(namefile,nodes,1)     
                    if(data==-1):
                       wx.MessageBox("Incorrect data", "Error")
                    else:				
                       setGrid(data,self.data['curvature'])
                dlg.Destroy()
            else:
                wx.MessageBox("You must active this field", "Error") 
       	except ValueError:
            wx.MessageBox("You must complete number of nodes first", "Error")
  
    def onLoadState(self, event): # wxGlade: formTube.<event_handler>
        try:
            ndof = int(self.data['ndof'].GetValue())
            nodes = int(self.data['nnod'].GetValue())
            if self.data['state_ini'].IsEnabled():
                dlg = wx.FileDialog(self, message="Open a Data File", defaultDir="./loads",defaultFile="", wildcard="*.txt", style=wx.OPEN)
                if dlg.ShowModal() == wx.ID_OK:
                    namefile = dlg.GetPath()
                    data = loadData(namefile,nodes,ndof)
                    if(data==-1):
                        wx.MessageBox("Incorrect data", "Error")
                    else:	
                        setGrid(data,self.data['state_ini'])
                dlg.Destroy()
            else:
                wx.MessageBox("You must active 'user-defined'", "Error") 
       	except ValueError:
            wx.MessageBox("You must complete number of nodes and degress of freedom first", "Error")


    def onHistoMode(self,event):
		indexNorm = 1
		if self.data['typeSave'].GetSelection() == indexNorm:
			self.data['numNorm'].Enable(True)
			self.data['posNorm'].Enable(True)
		else:
			self.data['numNorm'].Enable(False)
			self.data['posNorm'].Enable(False)

    def onChangeNumNorm(self,event):
		try:
			nNorm = int(self.data['numNorm'].GetValue())
			nodes = int(self.data['nnod'].GetValue())
			if nNorm > nodes:
				wx.MessageBox("Excesive Number of Nodes", "Error")
			else:
				rowNorm = self.data['posNorm'].GetNumberRows()
				if(nNorm>rowNorm):
					self.data['posNorm'].AppendRows(nNorm-rowNorm)
				else:
					if(nNorm<rowNorm):
						self.data['posNorm'].DeleteRows(rowNorm-(rowNorm-nNorm), rowNorm-nNorm)
		except ValueError:
			 nNorm = -1

    def onChangePosNorm(self,event):
		print "here"

    def calculateHisto(self):
		histo = []
		if self.data['typeSave'].GetSelection() == 1:
			length = float(self.data['longitud'].GetValue())
			rows = self.data['xnod'].GetNumberRows()
			xnod = []
			for i in range(rows):
				dat = float(self.data['xnod'].GetCellValue(i,0))
				xnod.append(dat)

			rows = self.data['posNorm'].GetNumberRows()
			posNorm = []
			for i in range(rows):
				dat = float(self.data['posNorm'].GetCellValue(i,0))
				posNorm.append(dat)
		
			for i in range(rows):
				ret = self.findNext(length*posNorm[i],xnod)		
				if not(ret in histo):
					histo.append(ret)
		elif self.data['typeSave'].GetSelection() == 0:
			histo = range(int(self.data['nnod'].GetValue()))
				
		return histo
			

    def findNext(self,pos,xnod):
		distMin = 1000;		
		indMin = 0;
		for i in range(len(xnod)):
			dif = abs(xnod[i]-pos)
			if dif<distMin:
				indMin = i
				distMin = dif
		return indMin	

    def onConstTemp(self,event):
		msg = wx.TextEntryDialog(self,"Input Constante Value for Temperature","Input","")
		ret = msg.ShowModal()
		if ret==5100:
			try:
				value = float(msg.GetValue())
				str_value = msg.GetValue()
				rows = self.data['twall'].GetNumberRows()
				for i in range(rows):
					 self.data['twall'].SetCellValue(i,0,str_value)
			except ValueError:
		 		wx.MessageBox("Input Format Error", "Error")
		
    def onConstDiam(self,event):
		msg = wx.TextEntryDialog(self,"Input Constante Value for Diameter","Input","")
		ret = msg.ShowModal()
		if ret==5100:
			try:
				value = float(msg.GetValue())
				str_value = msg.GetValue()
				rows = self.data['diameter'].GetNumberRows()
				for i in range(rows):
					 self.data['diameter'].SetCellValue(i,0,str_value)
			except ValueError:
		 		wx.MessageBox("Input Format Error", "Error")
		
    def onLinearTemp(self,event):
		msg1 = wx.TextEntryDialog(self,"Input First Value for Temperature","Input","")
		ret = msg1.ShowModal()
		if ret==5100:
			try:
				first_value = float(msg1.GetValue())
				msg2 = wx.TextEntryDialog(self,"Input Last Value for Temperature","Input","")
				ret = msg2.ShowModal()
				if ret==5100:
					try:
						last_value = float(msg2.GetValue())
						rows = self.data['twall'].GetNumberRows()
						for i in range(rows):
							value = first_value + i*(last_value-first_value)/(rows-1)
							self.data['twall'].SetCellValue(i,0,str(value))
					except ValueError:
				 		wx.MessageBox("Input Format Error", "Error")
			except ValueError:
		 		wx.MessageBox("Input Format Error", "Error")

    def onLinearDiam(self,event):
		msg1 = wx.TextEntryDialog(self,"Input First Value for Temperature","Input","")
		ret = msg1.ShowModal()
		if ret==5100:
			try:
				first_value = float(msg1.GetValue())
				msg2 = wx.TextEntryDialog(self,"Input Last Value for Temperature","Input","")
				ret = msg2.ShowModal()
				if ret==5100:
					try:
						last_value = float(msg2.GetValue())
						rows = self.data['diameter'].GetNumberRows()
						for i in range(rows):
							value = first_value + i*(last_value-first_value)/(rows-1)
							self.data['diameter'].SetCellValue(i,0,str(value))
					except ValueError:
				 		wx.MessageBox("Input Format Error", "Error")
			except ValueError:
		 		wx.MessageBox("Input Format Error", "Error")

    def setLabels(self):
		self.data['state_ini'].SetColLabelValue(0, "Density")
		self.data['state_ini'].SetColLabelValue(1, "Velocity")
		self.data['state_ini'].SetColLabelValue(2, "Pressure")
		self.data['xnod'].SetColLabelValue(0, "mts")
		self.data['diameter'].SetColLabelValue(0, "mts")
		self.data['twall'].SetColLabelValue(0, "K")
		self.data['curvature'].SetColLabelValue(0, "Curvature")

# end of class formTube


