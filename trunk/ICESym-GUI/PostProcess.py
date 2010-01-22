# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Tue Nov 10 00:50:57 2009

import wx
import os.path
from formAnglePlots import anglePlots
from formTimePlots import timePlots
from formSpacePlots import spacePlots
from formCyclePlots import cyclePlots
from formRPMPlots import RPMPlots
from extraFunctions import *
from unitsData import *
import  wx.lib.plot as libPlot
import sys

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

# end wxGlade

class PostProcess(wx.Frame):
    colours = ['blue','red','green','yellow','black','pink','cyan','grey']	    
    figures = []
    typeFigures = []
    dataFigures = []
    configData = ""
    angleData = dict()
    timeData = dict()
    spaceData = dict()
    cycleData = dict()
    rpmData = dict()
    panel_figure = []
    panel_buttons = []
    buttons_figure = []
    canvas_list = []
    path = ""
    files = ['cyl_','tube_','tank_','junc_']
    id_button = 0;
    nButtons = 6
    nDelete = []
    thisFile = "untitled.post"
    saved = 1
    calcGlobals = []
    def __init__(self, *args, **kwds):
		# begin wxGlade: PostProcess.__init__
		kwds["style"] = wx.DEFAULT_FRAME_STYLE
		wx.Frame.__init__(self, *args, **kwds)

		# Menu Bar
		self.PostProcess_menubar = wx.MenuBar()
		wxglade_tmp_menu = wx.Menu()
		self.openPost = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "Open Post", "Open other Post", wx.ITEM_NORMAL)
		wxglade_tmp_menu.AppendItem(self.openPost)
		self.savePost = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "Save", "Save the Current Status", wx.ITEM_NORMAL)
		wxglade_tmp_menu.AppendItem(self.savePost)
		self.saveAsPost = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "Save As...", "Save As the Current Status", wx.ITEM_NORMAL)
		wxglade_tmp_menu.AppendItem(self.saveAsPost)
		self.close = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "Close", "Close Post Process", wx.ITEM_NORMAL)
		wxglade_tmp_menu.AppendItem(self.close)
		self.PostProcess_menubar.Append(wxglade_tmp_menu, "File")
		wxglade_tmp_menu = wx.Menu()
		self.timePlots = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "Time Plots", "Time Plots", wx.ITEM_NORMAL)
		wxglade_tmp_menu.AppendItem(self.timePlots)
		self.anglePlots = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "Angle Plots", "Angle Plots", wx.ITEM_NORMAL)
		wxglade_tmp_menu.AppendItem(self.anglePlots)
		self.spacePlots = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "Space Plots", "Space Plots", wx.ITEM_NORMAL)
		wxglade_tmp_menu.AppendItem(self.spacePlots)
		self.cyclePlots = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "Cycle Plots", "Cycle Plots", wx.ITEM_NORMAL)
		wxglade_tmp_menu.AppendItem(self.cyclePlots)
		self.rpmPlots = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "RPM Plots", "RPM Plots", wx.ITEM_NORMAL)
		wxglade_tmp_menu.AppendItem(self.rpmPlots)
		self.PostProcess_menubar.Append(wxglade_tmp_menu, "Graphics")
		self.SetMenuBar(self.PostProcess_menubar)
		self.notebook = wx.Notebook(self, -1, style=0)
		# Menu Bar end

       	#self.__set_properties()
		self.__do_layout()
		self.__set_properties()
		self.Bind(wx.EVT_MENU, self.onOpenPost, self.openPost)
		self.Bind(wx.EVT_MENU, self.onSavePost, self.savePost)
		self.Bind(wx.EVT_MENU, self.onSaveAsPost, self.saveAsPost)
		self.Bind(wx.EVT_MENU, self.onClose, self.close)
		self.Bind(wx.EVT_MENU, self.onTimePlots, self.timePlots)
		self.Bind(wx.EVT_MENU, self.onAnglePlots, self.anglePlots)
		self.Bind(wx.EVT_MENU, self.onSpacePlots, self.spacePlots)
		self.Bind(wx.EVT_MENU, self.onCyclePlots, self.cyclePlots)
		self.Bind(wx.EVT_MENU, self.onRPMPlots, self.rpmPlots)
		#self.Bind(wx.EVT_SIZE, self, self.onResize)
		wx.EVT_SIZE(self, self.onResize)
		# end wxGlade

    def __set_properties(self):
		# begin wxGlade: PostProcess.__set_properties
		self.SetTitle("PostProcess")
		self.notebook.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
		# end wxGlade

    def __do_layout(self):
		# begin wxGlade: PostProcess.__do_layout
		sizer_1 = wx.GridSizer(1, 1, 0, 0)
		for i in range(len(self.dataFigures)):
			self.addNewTab(i)
			pc = self.plotData(i,self.dataFigures[i])
			self.canvas_list.append(pc)
		sizer_1.Add(self.notebook, 0, wx.EXPAND, 0)
		self.SetSizer(sizer_1)
		self.Layout()
		# end wxGlade

    def onOpenPost(self,event):
        dlg = wx.FileDialog(self, message="Open a File", defaultDir=self.path,defaultFile="", wildcard="*.post", style=wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            namefile = dlg.GetPath()
            self.readFile(namefile)
        dlg.Destroy()

    def onSavePost(self, event): # wxGlade: PostProcess.<event_handler>
		if self.thisFile == "untitled.post":
			dlg = wx.FileDialog(self, message="Save File", defaultDir=self.path,defaultFile=self.thisFile, wildcard="*.post", style=wx.SAVE|wx.OVERWRITE_PROMPT)
			if dlg.ShowModal() == wx.ID_OK:
				namefile = dlg.GetPath()
				self.saveFile(namefile)
			dlg.Destroy()
		else:
			self.saveFile(self.thisFile)

    def onSaveAsPost(self,event):
		dlg = wx.FileDialog(self, message="Save File As", defaultDir=self.path,defaultFile=self.thisFile, wildcard="*.post", style=wx.SAVE)
		if dlg.ShowModal() == wx.ID_OK:
			namefile = dlg.GetPath()
			self.saveFile(namefile)
		dlg.Destroy()

    def onClose(self, event): # wxGlade: PostProcess.<event_handler>
        if self.saved == 1:
            self.Close()
        else:
            md = wx.MessageDialog(None, 'Save changes in ' + self.thisFile + ' ?','Confirm', wx.YES_NO| wx.CANCEL | wx.ICON_QUESTION)
            res = md.ShowModal()
            print res
            if res == 5104: #NO
                self.Close()
            if res == 5103: #YES
                self.onSavePost("")
                self.Close()
            #if res == 5104: #CANCEL retorna al Simulador

    def onTimePlots(self, event): # wxGlade: PostProcess.<event_handler>
		plot = timePlots(self, -1, "")
		ret = plot.ShowModal()

    def onAnglePlots(self, event): # wxGlade: PostProcess.<event_handler>
		plot = anglePlots(self, -1, "")
		fig = []
		for i in range(len(self.typeFigures)):
			if self.typeFigures[i]=="Angle":
				fig.append(str(i))

		self.angleData['figure'] = fig + ["new figure"]
		plot.setParameters(self.angleData)
		ret = plot.ShowModal()
		if(ret==5100):
			for rpm in plot.parsedData['rpm']:
				if plot.parsedData['element'] > 0:
					dataFile = self.path + "RPM_" + str(rpm) + "/" + self.files[int(plot.parsedData['element'])-1]	
					e = -1			
					if plot.parsedData['element_ndof'] < 3: #caso de variables de estado
						dataFile = dataFile + str(plot.parsedData['element_number']) + ".txt" 
					else:
						dataFile = dataFile + "extras_" + str(plot.parsedData['element_number']) + ".txt"
						if self.files[int(plot.parsedData['element'])-1] == "cyl_":
							e = 1 #para que cargue desde extras de cyl
						else:
							e = 2 #para que cargue desde extras de tank
					for c in plot.parsedData['cycle']:
						dataFig = dict()
						dataFig['label'] = plot.parsedData['label'] + "_" + str(rpm)
						dataFig['data'] = loadAngleTXT(dataFile,int(c),int(plot.parsedData['element_nnod']),plot.parsedData['element_ndof'],e)
						dataFig['data'] = conversion(dataFig['data'],plot.parsedData['units'])
						dataFig['y_axis'] = plot.parsedData['element_number_str'] + " - " + plot.parsedData['element_ndof_str'] + " ["+str(plot.parsedData['units'])+"]"
						dataFig['x_axis'] = 'Angle'
						if (plot.parsedData['figure'] == "new figure"):
							l = len(self.dataFigures)					
							self.dataFigures.append([])
							self.dataFigures[l].append(dataFig)
							self.addNewTab(l)
							pc = self.plotData(l,self.dataFigures[l])
							self.canvas_list.append(pc)
							self.typeFigures.append('Angle')
							plot.parsedData['figure'] = l
						else:
							l = int(plot.parsedData['figure'])
							self.dataFigures[l].append(dataFig)	
							pc = self.plotData(l,self.dataFigures[l])
							self.canvas_list[l] = pc
				
    def onSpacePlots(self, event): # wxGlade: PostProcess.<event_handler>
		plot = spacePlots(self, -1, "")
		fig = []
		for i in range(len(self.typeFigures)):
			if self.typeFigures[i]=="Space":
				fig.append(str(i))

		self.spaceData['figure'] = fig + ["new figure"]
		plot.setParameters(self.spaceData)
		ret = plot.ShowModal()
		if(ret==5100):
			if plot.parsedData['element'] > 0:
				dataFile = self.path + "RPM_" + str(plot.parsedData['rpm']) + "/tube_ " + str(self.spaceData['ntube'][plot.parsedData['element_number']]) + ".txt" 
				dataFig = dict()
				dataFig['label'] = plot.parsedData['label']
				dataFig['data'] = loadSpaceTXT(dataFile,plot.parsedData['time'],plot.parsedData['element_ndof'])
				dataFig['data'] = conversion(dataFig['data'],plot.parsedData['units'])
				dataFig['y_axis'] = plot.parsedData['element_number_str'] + " - " + plot.parsedData['element_ndof_str']  + " ["+str(plot.parsedData['units'])+"]"
				dataFig['x_axis'] = 'Space'
				if (plot.parsedData['figure'] == "new figure"):
					l = len(self.dataFigures)					
					self.dataFigures.append([])
					self.dataFigures[l].append(dataFig)
					self.addNewTab(l)
					pc = self.plotData(l,self.dataFigures[l])
					self.canvas_list.append(pc)
					self.typeFigures.append('Space')
					plot.parsedData['figure'] = l
				else:
					l = int(plot.parsedData['figure'])
					self.dataFigures[l].append(dataFig)	
					pc = self.plotData(l,self.dataFigures[l])
					self.canvas_list[l] = pc

    def onCyclePlots(self, event): # wxGlade: PostProcess.<event_handler>
		plot = cyclePlots(self, -1, "")
		fig = []
		for i in range(len(self.typeFigures)):
			if self.typeFigures[i]=="Cycle":
				fig.append(str(i))

		self.cycleData['figure'] = fig + ["new figure"]
		plot.setParameters(self.cycleData)
		ret = plot.ShowModal()
		if(ret==5100):
			for rpm in plot.parsedData['rpm']:
				if plot.parsedData['element'] > 0:
					dataFile = self.path + "RPM_" + str(rpm) + "/" + self.files[int(plot.parsedData['element'])-1]	
					e = -1			
					if plot.parsedData['element_ndof'] < 3: #caso de variables de estado
						dataFile = dataFile + str(plot.parsedData['element_number']) + ".txt" 
					else:
						dataFile = dataFile + "extras_" + str(plot.parsedData['element_number']) + ".txt"
						if self.files[int(plot.parsedData['element'])-1] == "cyl_":
							e = 1 #para que cargue desde extras de cyl
						else:
							e = 2 #para que cargue desde extras de tank

					dataFig = dict()
					dataFig['label'] = plot.parsedData['label']+ "_" + str(rpm)
					dataFig['data'] = loadCycleTXT(dataFile,int(plot.parsedData['element_nnod']),plot.parsedData['element_ndof'],e)
					dataFig['data'] = conversion(dataFig['data'],plot.parsedData['units'])
					dataFig['y_axis'] = plot.parsedData['element_number_str'] + " - " + plot.parsedData['element_ndof_str']  + " ["+str(plot.parsedData['units'])+"]"
					dataFig['x_axis'] = 'Cycle'
					if (plot.parsedData['figure'] == "new figure"):
						l = len(self.dataFigures)					
						self.dataFigures.append([])
						self.dataFigures[l].append(dataFig)
						self.addNewTab(l)
						pc = self.plotData(l,self.dataFigures[l])
						self.canvas_list.append(pc)
						self.typeFigures.append('Cycle')
						plot.parsedData['figure'] = l
					else:
						l = int(plot.parsedData['figure'])
						self.dataFigures[l].append(dataFig)	
						pc = self.plotData(l,self.dataFigures[l])
						self.canvas_list[l] = pc

    def onRPMPlots(self, event): # wxGlade: PostProcess.<event_handler>
		plot = RPMPlots(self, -1, "")
		fig = []
		for i in range(len(self.typeFigures)):
			if self.typeFigures[i]=="RPM":
				fig.append(str(i))

		self.rpmData['figure'] = fig + ["new figure"]
		plot.setParameters(self.rpmData)
		ret = plot.ShowModal()
		if(ret==5100):
			for icycle in plot.parsedData['cycle']:
				dataFig = dict()
				if plot.parsedData['element'] > 0:
					print "buscar en cada archivo de rpm del elemento seleccionado"
					cdata = []
					for irpm in self.rpmData['rpm']:
						dataFile = self.path + "RPM_" + str(irpm) + "/" + self.files[int(plot.parsedData['element'])-1]	
						e = -1			
						if plot.parsedData['element_ndof'] < 3: #caso de variables de estado
							dataFile = dataFile + str(plot.parsedData['element_number']) + ".txt" 
						else:
							dataFile = dataFile + "extras_" + str(plot.parsedData['element_number']) + ".txt"
							if self.files[int(plot.parsedData['element'])-1] == "cyl_":
								e = 1 #para que cargue desde extras de cyl
							else:
								e = 2 #para que cargue desde extras de tank
						cdata.append(loadCycleTXT(dataFile,int(plot.parsedData['element_nnod']),plot.parsedData['element_ndof'],e))
					dataFig['data'] = getRPMfromCycle(cdata,self.rpmData['rpm'],icycle)	
					dataFig['y_axis'] = plot.parsedData['element_number_str'] + " - " + plot.parsedData['element_ndof_str'] + " ["+str(plot.parsedData['units'])+"]"
				else:
					if self.calcGlobals == []:
						maxPD = len(self.rpmData['rpm'])*len(self.rpmData['Cylinders']['labels'])+1
						pd = wx.ProgressDialog("Please Wait...", "loading data...",maxPD,self)
						pd.Show()
						self.calcGlobals = calcGlobalsData(self.path, self.rpmData,pd)
					variable = self.calcGlobals[plot.parsedData['global_variable']]
					if plot.parsedData['global_variable'] in ['IMEP_per_cylinder','FMEP_per_cylinder','BMEP_per_cylinder','volumetric_efficiency_per_cylinder']:
						for icyl in range(len(self.rpmData['Cylinders']['labels'])):
							dataFig = dict()
							dataFig['data'] = variable[icyl][int(icycle)-1]
							dataFig['data'] = conversion(dataFig['data'],plot.parsedData['units'])
							dataFig['label'] = plot.parsedData['label']+ "_cycle" + str(icycle) + "_" + self.rpmData['Cylinders']['labels'][icyl]
							dataFig['y_axis'] = plot.parsedData['global_variable'] + " ["+str(plot.parsedData['units'])+"]"
							dataFig['x_axis'] = 'RPM'
							if (plot.parsedData['figure'] == "new figure"):
								l = len(self.dataFigures)					
								self.dataFigures.append([]) 
								self.dataFigures[l].append(dataFig)
								self.addNewTab(l)
								pc = self.plotData(l,self.dataFigures[l])
								self.canvas_list.append(pc)
								self.typeFigures.append('RPM')
								plot.parsedData['figure'] = l
							else:
								l = int(plot.parsedData['figure'])
								self.dataFigures[l].append(dataFig)	
								pc = self.plotData(l,self.dataFigures[l])
								self.canvas_list[l] = pc
						return
					else:	
						dataFig['data'] = variable[int(icycle)-1]
						dataFig['y_axis'] = plot.parsedData['global_variable'] + " ["+str(plot.parsedData['units'])+"]"
				
				print "a graficar: ", dataFig['data']
				dataFig['data'] = conversion(dataFig['data'],plot.parsedData['units'])
				dataFig['label'] = plot.parsedData['label']+ "_cycle" + str(icycle)
				dataFig['x_axis'] = 'RPM'
				if (plot.parsedData['figure'] == "new figure"):
					l = len(self.dataFigures)					
					self.dataFigures.append([]) 
					self.dataFigures[l].append(dataFig)
					self.addNewTab(l)
					pc = self.plotData(l,self.dataFigures[l])
					self.canvas_list.append(pc)
					self.typeFigures.append('RPM')
					plot.parsedData['figure'] = l
				else:
					l = int(plot.parsedData['figure'])
					self.dataFigures[l].append(dataFig)	
					pc = self.plotData(l,self.dataFigures[l])
					self.canvas_list[l] = pc

    def loadResults(self,folder_name):
		
		exists = os.path.exists(folder_name)
		if not(exists):
			return False
		filename = folder_name+'/header.py'
		archi = open(filename, "r")
		import sys
		i1 = filename.rfind("/")
		pathName = ''
		for j in range(i1):
			pathName = pathName + filename[j]
		i2 = filename.rfind(".")
		moduleName = ''
		for j in range(i2-i1-1):
			moduleName = moduleName + filename[j+i1+1]

		sys.path.append(str(pathName))
		self.configData = __import__(str(moduleName))
		self.path = folder_name

		self.orderingData()
		return True

    def plotData(self,nf,dataFigure):
		plot_canvas = libPlot.PlotCanvas(self.panel_figure[nf])
		frame_size = self.panel_figure[nf].GetSize()
		plot_canvas.SetInitialSize(size=frame_size)
		# optionally allow scrolling
		plot_canvas.SetShowScrollbars(True)
		plot_canvas.SetFontSizeLegend(9)
		plot_canvas.SetFontSizeTitle(8)
		plot_canvas.SetUseScientificNotation(True)
		plot_canvas.SetEnableZoom(True)
		plot_canvas.SetFontSizeAxis(point=8)
		plot_canvas.SetFontSizeTitle(point=10)

		lines = []
		title = ''
		#title = " FIGURE 1"
		for i in range(len(dataFigure)):
			lines.append(libPlot.PolyLine(dataFigure[i]['data'], colour=self.colours[i], width=1, legend=dataFigure[i]['label']))
			#title = title + dataFigure[i]['label'] + " (" +  self.colours[i] + ") - "

		gc = libPlot.PlotGraphics(lines,title,dataFigure[-1]['x_axis'],dataFigure[-1]['y_axis'])
		plot_canvas.Draw(gc)
		plot_canvas.SetEnableLegend(True)
		#plot_canvas.SaveFile(fileName='Cyl1vsCyl2.jpg') 
		s = self.GetSize()
		s = (s[0]+1,s[1]+1)
		self.SetSize(s)
		self.onResize("")
		self.saved = 0
		return plot_canvas
		# optionally save the plot to an image file
		
		

    def onResize(self,event):
		s = self.GetSize()
		self.notebook.SetSize(s)
		for i in range(len(self.canvas_list)):
			frame_size = self.panel_figure[i].GetSize()
			self.canvas_list[i].SetClientSize(size=frame_size)

    def addNewTab(self, i):
		print i
		self.figures.append(wx.ScrolledWindow(self.notebook, -1, style=wx.TAB_TRAVERSAL))
		self.panel_figure.append(wx.Panel(self.figures[i], -1, size=(200,30)))
		self.panel_buttons.append(wx.Panel(self.figures[i], -1, size=(200,30)))

		grid_sizer_aux = wx.BoxSizer(wx.VERTICAL)
		grid_sizer_aux1 = wx.FlexGridSizer(1, 1, 0, 0)
		grid_sizer_aux2 = wx.FlexGridSizer(1, 6, 0, 0)

		self.buttons_figure.append(dict())
		self.buttons_figure[i]['reset'] = wx.Button(self.panel_buttons[i], self.id_button, "reset", size=(60,23))
		self.buttons_figure[i]['save'] = wx.Button(self.panel_buttons[i], self.id_button+1, "save", size=(60,23))
		self.buttons_figure[i]['grid'] = wx.Button(self.panel_buttons[i], self.id_button+2, "grid", size=(60,23))
		self.buttons_figure[i]['remove'] = wx.Button(self.panel_buttons[i], self.id_button+3, "remove", size=(60,23))
		self.buttons_figure[i]['x_label'] = wx.Button(self.panel_buttons[i], self.id_button+4, "X label", size=(60,23))
		self.buttons_figure[i]['y_label'] = wx.Button(self.panel_buttons[i], self.id_button+5, "Y label", size=(60,23))
		self.id_button = self.id_button+self.nButtons
		for j in self.buttons_figure[i]:
			self.buttons_figure[i][j].SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
			grid_sizer_aux2.Add(self.buttons_figure[i][j], 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
		self.Bind(wx.EVT_BUTTON, self.onResetCanvas, self.buttons_figure[i]['reset'])
		self.Bind(wx.EVT_BUTTON, self.onSaveCanvas, self.buttons_figure[i]['save'])
		self.Bind(wx.EVT_BUTTON, self.onGridCanvas, self.buttons_figure[i]['grid'])
		self.Bind(wx.EVT_BUTTON, self.onRemoveCanvas, self.buttons_figure[i]['remove'])
		self.Bind(wx.EVT_BUTTON, self.onXAxis, self.buttons_figure[i]['x_label'])
		self.Bind(wx.EVT_BUTTON, self.onYAxis, self.buttons_figure[i]['y_label'])

		self.panel_buttons[i].SetSizer(grid_sizer_aux2)
		self.panel_figure[i].SetSizer(grid_sizer_aux1)
		grid_sizer_aux.Add(self.panel_figure[i],5,flag=wx.EXPAND)		
		grid_sizer_aux.Add(self.panel_buttons[i],1,flag=wx.EXPAND)
		self.figures[i].SetSizer(grid_sizer_aux)
		self.notebook.AddPage(self.figures[i], "Figure "+str(i))

    def onResetCanvas(self,event):
		nf = int(event.GetId() / self.nButtons)
		aux = 0
		for d in self.nDelete:
			if nf > d:
				aux = aux + 1
		nf = nf - aux
		self.canvas_list[nf].Reset()

    def onSaveCanvas(self,event):
		nf = int(event.GetId() / self.nButtons)
		aux = 0
		for d in self.nDelete:
			if nf > d:
				aux = aux + 1
		nf = nf - aux
		dlg = wx.FileDialog(self, message="Save Figure As", defaultDir=self.path,defaultFile="untitled.jpg", wildcard="*.jpg", style=wx.SAVE)
		if dlg.ShowModal() == wx.ID_OK:
			namefile = dlg.GetPath()
			self.canvas_list[nf].SaveFile(namefile) #bug en wxpython, ver: http://www.daniweb.com/forums/thread196744.html#
		dlg.Destroy()

    def onGridCanvas(self,event):
		nf = int(event.GetId() / self.nButtons)
		aux = 0
		for d in self.nDelete:
			if nf > d:
				aux = aux + 1
		nf = nf - aux
		flag = self.canvas_list[nf].GetEnableGrid()
		self.canvas_list[nf].SetEnableGrid(not(flag))

    def onRemoveCanvas(self,event):
		nf = int(event.GetId() / self.nButtons)
		aux = 0
		for d in self.nDelete:
			if nf > d:
				aux = aux + 1
		nf = nf - aux
		nLines = len(self.dataFigures[nf])
		lista = []
		for f in self.dataFigures[nf]:
			lista.append(f['label'])
		popup = wx.SingleChoiceDialog(self,"Choose Line to remove: ", "Remove", lista)
		ret = popup.ShowModal()
		if ret==5100:
			rm = popup.GetSelection()
			del self.dataFigures[nf][rm]
			if len(self.dataFigures[nf]) == 0:
				del self.dataFigures[nf]
				self.notebook.DeletePage(nf)
				del self.figures[nf]
				del self.typeFigures[nf]
				del self.panel_buttons[nf]
				del self.panel_figure[nf]
				del self.buttons_figure[nf]
				del self.canvas_list[nf]
				self.nDelete = self.nDelete + [nf]
			else:
				pc = self.plotData(nf,self.dataFigures[nf])
				self.canvas_list[nf] = pc

    def onXAxis(self,event):
		nf = int(event.GetId() / self.nButtons) - self.nDelete
		msg = wx.TextEntryDialog(self,"Insert X Axis label: ","Input",str(self.dataFigures[nf][-1]['x_axis']))
		ret = msg.ShowModal()
		if ret==5100:
			lab = msg.GetValue()
			self.dataFigures[nf][-1]['x_axis'] = str(lab)
			pc = self.plotData(nf,self.dataFigures[nf])
			self.canvas_list[nf] = pc
		
    def onYAxis(self,event):
		nf = int(event.GetId() / self.nButtons) - self.nDelete
		msg = wx.TextEntryDialog(self,"Insert Y Axis label: ","Input",str(self.dataFigures[nf][-1]['y_axis']))
		ret = msg.ShowModal()
		if ret==5100:
			lab = msg.GetValue()
			self.dataFigures[nf][-1]['y_axis'] = str(lab)
			pc = self.plotData(nf,self.dataFigures[nf])
			self.canvas_list[nf] = pc

#fijarse de ordenar todos los datos no solo de angle
    def orderingData(self):

		self.angleData['rpm'] = List2StringList(self.configData.rpms)
		listCycles = []
		for i in range(self.configData.ncycles):
			listCycles.append(i+1)
		self.rpmData['nstroke'] = self.configData.nstroke
		self.rpmData['rho'] = self.configData.rho
		self.angleData['cycle'] = List2StringList(listCycles)
		
		Globals = dict()
		Globals['labels'] = []
		if self.configData.Globals['engine_data'] == 1: # si esta activada la bandera
			Globals['labels'] = ['power_indicated','power_effective','torque_indicated','torque_effective','IMEP_per_cylinder','IMEP_global','FMEP_per_cylinder','FMEP_global', 'BMEP_per_cylinder','BMEP_global','SFC_indicated','SFC_effective','mechanical_efficiency','volumetric_efficiency_per_cylinder','volumetric_efficiency_global',
'fuel_conversion_efficiency_indicated', 'fuel_conversion_efficiency_effective']
			
		self.spaceData['time'] = List2StringList(self.configData.final_times)
		Cylinders = dict()
		Cylinders['histos'] = []
		Cylinders['extras'] = []		
		Cylinders['labels'] = []
		Cylinders['valves_intake'] = []
		Cylinders['valves_exhaust'] = []
		Cylinders['crank_radius'] = []
		Cylinders['angleClose'] = []
		Cylinders['Q_fuel'] = self.configData.Cylinders[0]['Q_fuel']
		for c in self.configData.Cylinders:
			Cylinders['labels'].append(c['label'])
			Cylinders['extras'].append(c['extras'])
			Cylinders['crank_radius'].append(c['crank_radius'])
			Cylinders['angleClose'].append(c['angleClose'])
			vi = range(1,1+c['nvi'])
			ve = range(1+c['nvi'],1+c['nvi']+c['nve'])
			aux = []
			auxvi = []
			auxve = []
			for h in c['histo']:
				if h in vi:				
					auxvi.append(str(h)+' (intake)')
				elif h in ve:
					auxve.append(str(h)+' (exhaust)')	
				else:
					aux.append(str(h))
			Cylinders['histos'].append(aux)
			Cylinders['valves_intake'].append(auxvi)
			Cylinders['valves_exhaust'].append(auxve)
		self.angleData['Cylinders'] = Cylinders

		self.spaceData['Tubes'] = dict()
		self.spaceData['Tubes']['labels'] = []
		self.spaceData['Tubes']['ntube'] = []
		Tubes = dict()
		Tubes['histos'] = []
		Tubes['labels'] = []
		ntube = 0
		for t in self.configData.Tubes:
			Tubes['labels'].append(t['label'])
			aux = []
			if t['nnod'] == t['histo']:
				self.spacePlots['Tubes']['labels'].append(t['label'])
				self.spacePlots['Tubes']['ntube'].append(ntube)
			for h in t['histo']:
				aux.append(str(h))
			Tubes['histos'].append(aux)
			ntube = ntube + 1
		self.angleData['Tubes'] = Tubes

		Tanks = dict()
		Tanks['histos'] = []
		Tanks['labels'] = []
		Tanks['extras'] = []
		for t in self.configData.Tanks:
			Tanks['labels'].append(t['label'])
			Tanks['extras'].append(t['extras'])
			aux = []
			for h in t['histo']:
				aux.append(str(h))
			Tanks['histos'].append(aux)
		self.angleData['Tanks'] = Tanks

		Junctions = dict()
		Junctions['histos'] = []
		Junctions['labels'] = []
		for j in self.configData.Junctions:
			Junctions['labels'].append(j['label'])
			aux = []
			for h in j['histo']:
				aux.append(str(h))
			Junctions['histos'].append(aux)
		self.angleData['Junctions'] = Junctions

		#self.cycleData['Globals'] = Globals
		self.cycleData['rpm'] = self.angleData['rpm']
		self.cycleData['Cylinders'] = self.angleData['Cylinders']
		self.cycleData['Tubes'] = self.angleData['Tubes']
		self.cycleData['Tanks'] = self.angleData['Tanks']
		self.cycleData['Junctions'] = self.angleData['Junctions']

		#self.spaceData['Globals'] = []
		self.spaceData['rpm'] = self.angleData['rpm']
		#self.spaceData['cycle'] = self.angleData['cycle']

		self.rpmData['Globals'] = Globals
		self.rpmData['rpm'] = self.angleData['rpm']
		self.rpmData['cycle'] = self.angleData['cycle']
		self.rpmData['Cylinders'] = self.angleData['Cylinders']
		self.rpmData['Tubes'] = self.angleData['Tubes']
		self.rpmData['Tanks'] = self.angleData['Tanks']
		self.rpmData['Junctions'] = self.angleData['Junctions']


    def readFile(self,filename):
		archi = open(filename, "r")
		try:  
			import cPickle as pickle  
		except ImportError:  
			import pickle  

		self.dataFigures = pickle.load(archi)
		self.typeFigures = pickle.load(archi)
		self.path = pickle.load(archi)
		self.loadResults(self.path)
		self.__do_layout()
		self.thisFile = filename     
		print "Leido: ",filename
		s = self.GetSize()
		s = (s[0]+1,s[1]+1)
		self.SetSize(s)
		self.onResize("")
		self.saved = 1


    def saveFile(self,filename):
		archi = open(filename, "w")
		try:  
			import cPickle as pickle  
		except ImportError:  
			import pickle  
		pickle.dump(self.dataFigures, archi, 2) 
		pickle.dump(self.typeFigures, archi, 2)
		pickle.dump(self.path, archi, 2)
		archi.close()
		
		print "Guardado: ",filename
		self.saved = 1
	
# end of class PostProcess


