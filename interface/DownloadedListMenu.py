from sys import path
path.insert(1,".")

from os import system as RunCmd

from PyQt5.QtWidgets import QTableWidget, QMenu, QAction, QTableWidgetItem, QWidget
from PyQt5.QtGui import QIcon, QCursor, QClipboard
from PyQt5.QtCore import Qt

from dist import pydist as pd

class DownloadedListMenu(QMenu):
    table = QTableWidget
    clipboard = QClipboard
    selected = QTableWidgetItem

    def __init__(self,table:QTableWidget,clipboard:QClipboard,widget:QWidget):
        self.clipboard = clipboard
        self.table = table
        self.InitMenu()
        widget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        widget.customContextMenuRequested.connect(lambda: self.Execute())

    def GetSelectedItem(self) -> QTableWidgetItem: return self.table.selectedItems()[0]
    
    def InitMenu(self):
        super().__init__()

        self.label = QAction("",self)
        self.label.setDisabled(True)
        
        self.openAction = QAction(
            QIcon(pd.__PyDist__._WorkDir+"assets/folder_yellow.png"),
            "Open folder",
            self
        )
        self.openAction.triggered.connect(lambda: RunCmd(f'explorer /select,"{self.selected.text()}"'))

        self.playAction = QAction(
            QIcon(pd.__PyDist__._WorkDir+"assets/player_play.png"),
            "Play",
            self
        )
        self.playAction.triggered.connect(lambda: RunCmd("explorer "+self.selected.text()))

        self.copyAction = QAction(
            QIcon(pd.__PyDist__._WorkDir+"assets/editcopy.png"),
            "Copy filename",
            self
        )
        self.copyAction.triggered.connect(lambda: self.clipboard.setText(self.selected.text()))

        self.clearAction = QAction(
            QIcon(pd.__PyDist__._WorkDir+"assets/button_cancel.png"),
            "Clear list",
            self
        )
        self.clearAction.triggered.connect(lambda: self.table.setRowCount(0))

        self.itemSpecificActions = [self.copyAction,self.playAction,self.openAction]
        self.postDownloadingSpecificActions = [self.playAction,self.openAction]

        self.addAction(self.label)
        self.addSeparator()
        self.addActions(self.itemSpecificActions)
        self.addSeparator()
        self.addAction(self.clearAction)

    def Execute(self):
        if len(self.table.selectedItems())==1 and self.GetSelectedItem().column()==0:
            self.selected = self.GetSelectedItem()
            self.label.setText(self.selected.text())
        else:
            self.label.setText("invalid selection")
        for item in self.itemSpecificActions: item.setEnabled(len(self.table.selectedItems())==1 and self.GetSelectedItem().column()==0)
        if self.playAction.isEnabled() and self.openAction.isEnabled():
            for item in self.postDownloadingSpecificActions:
                #get the text from the item in the selected row at the 3rd column
                totalTimeStatus = self.table.item(self.table.indexFromItem(self.GetSelectedItem()).row(),2).text()
                item.setDisabled(totalTimeStatus != "Downloading" and totalTimeStatus != "Canceled")
        self.exec_(QCursor.pos())