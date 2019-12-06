# encoding: utf-8
# module PySide.QtGui
# from C:\Python27\lib\site-packages\PySide\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


from QDialog import QDialog

class QMessageBox(QDialog):
    # no doc
    def about(self, *args, **kwargs): # real signature unknown
        pass

    def aboutQt(self, *args, **kwargs): # real signature unknown
        pass

    def addButton(self, *args, **kwargs): # real signature unknown
        pass

    def button(self, *args, **kwargs): # real signature unknown
        pass

    def buttonClicked(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def buttonRole(self, *args, **kwargs): # real signature unknown
        pass

    def buttons(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clickedButton(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def critical(self, *args, **kwargs): # real signature unknown
        pass

    def defaultButton(self, *args, **kwargs): # real signature unknown
        pass

    def detailedText(self, *args, **kwargs): # real signature unknown
        pass

    def escapeButton(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def icon(self, *args, **kwargs): # real signature unknown
        pass

    def iconPixmap(self, *args, **kwargs): # real signature unknown
        pass

    def information(self, *args, **kwargs): # real signature unknown
        pass

    def informativeText(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def open(self, *args, **kwargs): # real signature unknown
        pass

    def question(self, *args, **kwargs): # real signature unknown
        pass

    def removeButton(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def setDefaultButton(self, *args, **kwargs): # real signature unknown
        pass

    def setDetailedText(self, *args, **kwargs): # real signature unknown
        pass

    def setEscapeButton(self, *args, **kwargs): # real signature unknown
        pass

    def setIcon(self, *args, **kwargs): # real signature unknown
        pass

    def setIconPixmap(self, *args, **kwargs): # real signature unknown
        pass

    def setInformativeText(self, *args, **kwargs): # real signature unknown
        pass

    def setStandardButtons(self, *args, **kwargs): # real signature unknown
        pass

    def setText(self, *args, **kwargs): # real signature unknown
        pass

    def setTextFormat(self, *args, **kwargs): # real signature unknown
        pass

    def setWindowModality(self, *args, **kwargs): # real signature unknown
        pass

    def setWindowTitle(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def standardButton(self, *args, **kwargs): # real signature unknown
        pass

    def standardButtons(self, *args, **kwargs): # real signature unknown
        pass

    def text(self, *args, **kwargs): # real signature unknown
        pass

    def textFormat(self, *args, **kwargs): # real signature unknown
        pass

    def warning(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    Abort = PySide.QtGui.QMessageBox.StandardButton.Abort
    AcceptRole = PySide.QtGui.QMessageBox.ButtonRole.AcceptRole
    ActionRole = PySide.QtGui.QMessageBox.ButtonRole.ActionRole
    Apply = PySide.QtGui.QMessageBox.StandardButton.Apply
    ApplyRole = PySide.QtGui.QMessageBox.ButtonRole.ApplyRole
    ButtonMask = PySide.QtGui.QMessageBox.StandardButton.ButtonMask
    ButtonRole = None # (!) real value is "<type 'PySide.QtGui.QMessageBox.ButtonRole'>"
    Cancel = PySide.QtGui.QMessageBox.StandardButton.Cancel
    Close = PySide.QtGui.QMessageBox.StandardButton.Close
    Critical = PySide.QtGui.QMessageBox.Icon.Critical
    Default = PySide.QtGui.QMessageBox.StandardButton.Default
    DestructiveRole = PySide.QtGui.QMessageBox.ButtonRole.DestructiveRole
    Discard = PySide.QtGui.QMessageBox.StandardButton.Discard
    Escape = PySide.QtGui.QMessageBox.StandardButton.Escape
    FirstButton = PySide.QtGui.QMessageBox.StandardButton.FirstButton
    FlagMask = PySide.QtGui.QMessageBox.StandardButton.FlagMask
    Help = PySide.QtGui.QMessageBox.StandardButton.Help
    HelpRole = PySide.QtGui.QMessageBox.ButtonRole.HelpRole
    Icon = None # (!) real value is "<type 'PySide.QtGui.QMessageBox.Icon'>"
    Ignore = PySide.QtGui.QMessageBox.StandardButton.Ignore
    Information = PySide.QtGui.QMessageBox.Icon.Information
    InvalidRole = PySide.QtGui.QMessageBox.ButtonRole.InvalidRole
    LastButton = PySide.QtGui.QMessageBox.StandardButton.LastButton
    No = PySide.QtGui.QMessageBox.StandardButton.No
    NoAll = PySide.QtGui.QMessageBox.StandardButton.NoAll
    NoButton = PySide.QtGui.QMessageBox.StandardButton.NoButton
    NoIcon = PySide.QtGui.QMessageBox.Icon.NoIcon
    NoRole = PySide.QtGui.QMessageBox.ButtonRole.NoRole
    NoToAll = PySide.QtGui.QMessageBox.StandardButton.NoToAll
    NRoles = PySide.QtGui.QMessageBox.ButtonRole.NRoles
    Ok = PySide.QtGui.QMessageBox.StandardButton.Ok
    Open = PySide.QtGui.QMessageBox.StandardButton.Open
    Question = PySide.QtGui.QMessageBox.Icon.Question
    RejectRole = PySide.QtGui.QMessageBox.ButtonRole.RejectRole
    Reset = PySide.QtGui.QMessageBox.StandardButton.Reset
    ResetRole = PySide.QtGui.QMessageBox.ButtonRole.ResetRole
    RestoreDefaults = PySide.QtGui.QMessageBox.StandardButton.RestoreDefaults
    Retry = PySide.QtGui.QMessageBox.StandardButton.Retry
    Save = PySide.QtGui.QMessageBox.StandardButton.Save
    SaveAll = PySide.QtGui.QMessageBox.StandardButton.SaveAll
    StandardButton = None # (!) real value is "<type 'PySide.QtGui.QMessageBox.StandardButton'>"
    StandardButtons = None # (!) real value is "<type 'StandardButtons'>"
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x0000000004C0EC08>'
    Warning = PySide.QtGui.QMessageBox.Icon.Warning
    Yes = PySide.QtGui.QMessageBox.StandardButton.Yes
    YesAll = PySide.QtGui.QMessageBox.StandardButton.YesAll
    YesRole = PySide.QtGui.QMessageBox.ButtonRole.YesRole
    YesToAll = PySide.QtGui.QMessageBox.StandardButton.YesToAll


