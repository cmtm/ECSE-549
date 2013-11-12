# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Nov  5 2013)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar3 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menubar3.Append( self.m_menu1, u"File" ) 
		
		self.m_menu2 = wx.Menu()
		self.m_menubar3.Append( self.m_menu2, u"View" ) 
		
		self.m_menu3 = wx.Menu()
		self.m_menubar3.Append( self.m_menu3, u"Options" ) 
		
		self.m_menu4 = wx.Menu()
		self.m_menubar3.Append( self.m_menu4, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar3 )
		
		b_top = wx.BoxSizer( wx.VERTICAL )
		
		sb_input = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Input" ), wx.VERTICAL )
		
		b_inType = wx.BoxSizer( wx.HORIZONTAL )
		
		self.st_inType = wx.StaticText( self, wx.ID_ANY, u"Type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_inType.Wrap( -1 )
		b_inType.Add( self.st_inType, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		dd_inType1Choices = []
		self.dd_inType1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, dd_inType1Choices, 0 )
		self.dd_inType1.SetSelection( 0 )
		b_inType.Add( self.dd_inType1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		dd_inType2Choices = []
		self.dd_inType2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, dd_inType2Choices, 0 )
		self.dd_inType2.SetSelection( 0 )
		b_inType.Add( self.dd_inType2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sb_input.Add( b_inType, 0, wx.EXPAND, 5 )
		
		sb_inConstraints = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Constraints" ), wx.VERTICAL )
		
		b_inConsHeader = wx.BoxSizer( wx.HORIZONTAL )
		
		
		b_inConsHeader.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText38 = wx.StaticText( self, wx.ID_ANY, u"Parameter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )
		b_inConsHeader.Add( self.m_staticText38, 2, wx.ALL, 5 )
		
		
		b_inConsHeader.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"Value", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		b_inConsHeader.Add( self.m_staticText41, 1, wx.ALL, 5 )
		
		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, u"Units", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText42.Wrap( -1 )
		b_inConsHeader.Add( self.m_staticText42, 2, wx.ALL, 5 )
		
		self.m_staticText43 = wx.StaticText( self, wx.ID_ANY, u"Hard", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )
		b_inConsHeader.Add( self.m_staticText43, 1, wx.ALL, 5 )
		
		self.m_staticText44 = wx.StaticText( self, wx.ID_ANY, u"Harshness", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )
		b_inConsHeader.Add( self.m_staticText44, 2, wx.ALL, 5 )
		
		
		b_inConsHeader.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText45 = wx.StaticText( self, wx.ID_ANY, u"Goodness Plot", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )
		b_inConsHeader.Add( self.m_staticText45, 2, wx.ALL, 5 )
		
		
		sb_inConstraints.Add( b_inConsHeader, 1, wx.EXPAND, 5 )
		
		self.ph_inConstraintList = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sb_inConstraints.Add( self.ph_inConstraintList, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.bu_addConstraint = wx.Button( self, wx.ID_ANY, u"Add constraint", wx.DefaultPosition, wx.DefaultSize, 0 )
		sb_inConstraints.Add( self.bu_addConstraint, 0, wx.ALL, 5 )
		
		
		sb_input.Add( sb_inConstraints, 1, wx.EXPAND, 5 )
		
		
		b_top.Add( sb_input, 0, wx.EXPAND, 5 )
		
		sb_output = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Output" ), wx.VERTICAL )
		
		
		b_top.Add( sb_output, 1, wx.EXPAND, 5 )
		
		sb_system = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"System" ), wx.VERTICAL )
		
		
		b_top.Add( sb_system, 1, wx.EXPAND, 5 )
		
		self.bu_run = wx.Button( self, wx.ID_ANY, u"Suggest Device", wx.DefaultPosition, wx.DefaultSize, 0 )
		b_top.Add( self.bu_run, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( b_top )
		self.Layout()
		b_top.Fit( self )
		
		# Connect Events
		self.dd_inType1.Bind( wx.EVT_CHOICE, self.OnInType1 )
		self.dd_inType2.Bind( wx.EVT_CHOICE, self.OnInType2 )
		self.bu_addConstraint.Bind( wx.EVT_BUTTON, self.OnInAddConstraint )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnInType1( self, event ):
		event.Skip()
	
	def OnInType2( self, event ):
		event.Skip()
	
	def OnInAddConstraint( self, event ):
		event.Skip()
	

###########################################################################
## Class MyPanel4
###########################################################################

class MyPanel4 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bpButton2 = wx.BitmapButton( self, wx.ID_ANY, , wx.DefaultPosition, wx.Size( -1,-1 ), wx.BU_AUTODRAW )
		bSizer10.Add( self.m_bpButton2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice8Choices = []
		self.m_choice8 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice8Choices, 0 )
		self.m_choice8.SetSelection( 0 )
		bSizer10.Add( self.m_choice8, 4, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice9Choices = []
		self.m_choice9 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice9Choices, 0 )
		self.m_choice9.SetSelection( 0 )
		bSizer10.Add( self.m_choice9, 2, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl81 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_textCtrl81, 2, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText46 = wx.StaticText( self, wx.ID_ANY, u"[units]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )
		bSizer10.Add( self.m_staticText46, 3, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox1, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl2.SetMaxLength( 0 ) 
		bSizer10.Add( self.m_textCtrl2, 4, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText47 = wx.StaticText( self, wx.ID_ANY, u"GOOD PLOT", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )
		bSizer10.Add( self.m_staticText47, 4, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		self.SetSizer( bSizer10 )
		self.Layout()
		bSizer10.Fit( self )
	
	def __del__( self ):
		pass
	

