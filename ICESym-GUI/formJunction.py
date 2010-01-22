# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Thu Sep 17 20:05:00 2009

import wx
from validations import numberValidator
from extraFunctions import *
# begin wxGlade: dependencies
import wx.grid
# end wxGlade

# begin wxGlade: extracode

# end wxGlade

class formJunction(wx.Dialog):
    data={}
    edit = -1
    position = (0,0)

    def __init__(self, *args, **kwds):
        # begin wxGlade: formJunction.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER|wx.THICK_FRAME
        wx.Dialog.__init__(self, *args, **kwds)
        self.panel_buttons = wx.Panel(self, -1)
        self.panel_configure = wx.ScrolledWindow(self, -1, style=wx.TAB_TRAVERSAL)
        self.configure_notebook = wx.Notebook(self.panel_configure, -1, style=0)
        self.notebook_post = wx.ScrolledWindow(self.configure_notebook, -1, style=wx.TAB_TRAVERSAL)
        self.notebook_general = wx.ScrolledWindow(self.configure_notebook, -1, style=wx.TAB_TRAVERSAL) 
        self.data['ndof'] = wx.TextCtrl(self.notebook_general, -1, "3")
        self.label_1 = wx.StaticText(self.notebook_general, -1, "Number of Nodes: ")
        self.data['nnod'] = wx.TextCtrl(self.notebook_general, -1, "", style=wx.TE_READONLY)
        self.data['modelo_junc'] = wx.RadioBox(self.notebook_general, -1, "", choices=["modelo 1"], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        #self.label_3 = wx.StaticText(self.notebook_general, -1, "State:       ")
        #self.button_5 = wx.Button(self.notebook_general, -1, "...")
        #self.data['histo'] = wx.grid.Grid(self.notebook_general, -1, size=(1, 1))
        self.data['histo'] = wx.CheckListBox(self.notebook_post, -1, (20, 20), (200, 150), [],wx.LB_MULTIPLE)
        self.data['extras'] = wx.CheckBox(self.notebook_post, -1, "Calculate Extras (mass I/O, rate, etc")
        self.data['label'] = wx.TextCtrl(self.notebook_general, -1, "")
        self.accept = wx.Button(self.panel_buttons, wx.ID_OK, "")
        self.cancel = wx.Button(self.panel_buttons, wx.ID_CANCEL, "")

        self.__set_properties()
        self.__do_layout()

        #self.Bind(wx.EVT_TEXT, self.onChangeNdof, self.data['ndof'])
        #self.Bind(wx.EVT_BUTTON, self.onLoadState, self.button_5)
        self.Bind(wx.EVT_BUTTON, self.ConfigureAccept, self.accept)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: formJunction.__set_properties
        self.SetTitle("Configure Junction")
        self.SetSize((450, 250))
        self.data['ndof'].SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['ndof'].SetValidator(numberValidator())
        self.label_1.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['nnod'].SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['modelo_junc'].SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['modelo_junc'].SetSelection(0)
        #self.label_3.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        #self.button_5.SetMinSize(wx.DLG_SZE(self.button_5, (16, 12)))
        #self.data['histo'].CreateGrid(1, 3)
        #self.data['histo'].SetRowLabelSize(18)
        #self.data['histo'].SetColLabelSize(18)
        #self.data['histo'].EnableDragColSize(0)
        #self.data['histo'].EnableDragRowSize(0)
        #self.data['histo'].EnableDragGridSize(0)
        #self.data['histo'].SetColLabelValue(0, "ndof 1")
        #self.data['histo'].SetColLabelValue(1, "ndof 2")
        #self.data['histo'].SetColLabelValue(2, "ndof 3")
        #self.data['histo'].SetMinSize(wx.DLG_SZE(self.data['histo'], (147, 100)))
        #self.data['histo'].SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        #self.data['histo'].SetDefaultCellFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        #self.data['histo'].SetDefaultRowSize(18)
        #self.data['histo'].hide()
        #self.label_3.hide()
        #self.data['histo'].SetLabelFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['histo'].SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['extras'].SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.data['label'].SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.panel_configure.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.panel_configure.SetScrollRate(10, 10)
        self.configure_notebook.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.accept.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.cancel.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: formJunction.__do_layout
        configure_background = wx.BoxSizer(wx.VERTICAL)
        sizer_buttons = wx.GridSizer(1, 2, 0, 0)
        configure_sizer = wx.BoxSizer(wx.HORIZONTAL)
        #grid_sizer_23 = wx.FlexGridSizer(1, 1, 0, 10)
        #grid_sizer_25 = wx.FlexGridSizer(2, 2, 0, 0)
        #grid_sizer_40 = wx.FlexGridSizer(2, 1, 0, 0)
        grid_sizer_24 = wx.FlexGridSizer(4, 2, 0, 0)
        grid_sizer_111 = wx.FlexGridSizer(1, 2, 0, 0)
        label_0 = wx.StaticText(self.notebook_general, -1, "Degress of Freedom: ")
        label_0.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        label_2 = wx.StaticText(self.notebook_general, -1, "Model Junction: ")
        label_2.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        label_6 = wx.StaticText(self.notebook_general, -1, "Label: ")
        label_6.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))

        grid_sizer_24.Add(label_6, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_24.Add(self.data['label'], 0, 0, 0)
        grid_sizer_24.Add(label_0, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_24.Add(self.data['ndof'], 0, 0, 0)
        grid_sizer_24.Add(self.label_1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_24.Add(self.data['nnod'], 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_24.Add(label_2, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_24.Add(self.data['modelo_junc'], 0, wx.ALIGN_CENTER_VERTICAL, 0)
        #grid_sizer_23.Add(grid_sizer_24, 1, wx.EXPAND, 0)
        #grid_sizer_40.Add(self.label_3, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        #grid_sizer_40.Add(self.button_5, 0, 0, 0)
        #grid_sizer_25.Add(grid_sizer_40, 1, wx.EXPAND, 0)
        #grid_sizer_25.Add(self.data['histo'], 1, wx.EXPAND, 0)
        #grid_sizer_25.Add(self.panel_15, 1, wx.EXPAND, 0)
        #grid_sizer_25.Add(self.panel_14, 1, wx.EXPAND, 0)
        #grid_sizer_23.Add(grid_sizer_25, 1, wx.EXPAND, 0)
        #self.notebook_general.SetSizer(grid_sizer_23)
        self.notebook_general.SetSizer(grid_sizer_24)

        grid_sizer_111.Add(self.data['histo'], 0, 0, 0)
        grid_sizer_111.Add(self.data['extras'], 0, 0, 0)
        self.notebook_post.SetSizer(grid_sizer_111)

        self.configure_notebook.AddPage(self.notebook_general, "General")
        self.configure_notebook.AddPage(self.notebook_post, "Post Process")
        configure_sizer.Add(self.configure_notebook, 1, wx.EXPAND, 0)
        self.panel_configure.SetSizer(configure_sizer)
        configure_background.Add(self.panel_configure, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 8)
        sizer_buttons.Add(self.accept, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_buttons.Add(self.cancel, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        self.panel_buttons.SetSizer(sizer_buttons)
        configure_background.Add(self.panel_buttons, 0, wx.EXPAND, 0)
        self.SetSizer(configure_background)
        self.Layout()
        # end wxGlade

    def ConfigureAccept(self, event): # wxGlade: formJunction.<event_handler>
        can_out=1
        for key in self.data:
            if (self.data[key].GetValidator()):
                if(not(self.data[key].GetValidator().Validate(self,'number'))):
                    can_out=0
        
        if(can_out==1):
            self.EndModal(wx.ID_OK)
        else:
            wx.MessageBox("Some fields have some error (empty or no-digit value)!", "Error")
        #if self.Validate() and self.TransferDataFromWindow():
        #    self.EndModal(wx.ID_OK)
        
        #event.Skip()

    def onChangeNdof(self, event): # wxGlade: formJunction.<event_handler>
		self.ndof = self.data['ndof']        
		self.state = self.data['histo']
	
		try:
			ndof = int(self.ndof.GetValue())
			nstate = self.state.GetNumberCols()
			for i in range(ndof):
				self.state.SetColLabelValue(i,"ndof %d" % (i+1))
			if(ndof>nstate):
				self.state.AppendCols(ndof-nstate)
			else:
				if(ndof<nstate):
					self.state.DeleteCols(nstate-(nstate-ndof), nstate-ndof)
		except ValueError:
		   	ndof = None

    def onChangeNodes(self, event): # wxGlade: formJunction.<event_handler>
        try:
           nodes = int(self.data['nnod'].GetValue())
           nstate = self.data['histo'].GetNumberRows()
           if(nodes>nstate):
                self.data['histo'].AppendRows(nodes-nstate)
           else:
                if(nodes<nstate):
                    self.data['histo'].DeleteRows(nstate-(nstate-nodes), nstate-nodes)
        except ValueError:
		   	nodes = None

    def onLoadState(self, event): # wxGlade: formJunction.<event_handler>
        try:
            ndof = int(self.data['nnod'].GetValue())
            nodes = int(self.data['ndof'].GetValue())
            if self.data['histo'].IsEnabled():
                dlg = wx.FileDialog(self, message="Open a Data File", defaultDir="./loads",defaultFile="", wildcard="*.txt", style=wx.OPEN)
                if dlg.ShowModal() == wx.ID_OK:
                    namefile = dlg.GetPath()
                    data = loadData(namefile,nodes,ndof)
                    if(data==-1):
                        wx.MessageBox("Incorrect data", "Error")
                    else:	
                        setGrid(data,self.data['histo'])
                dlg.Destroy()
            else:
                wx.MessageBox("You must active 'user-defined'", "Error") 
       	except ValueError:
            wx.MessageBox("You must complete number of nodes and degress of freedom first", "Error")

    def addHisto(self, labels=[]):
		nodes = int(self.data['nnod'].GetValue())
		for i in range(nodes):
			self.data['histo'].Append("Connection with " + labels[i])


# end of class formJunction

