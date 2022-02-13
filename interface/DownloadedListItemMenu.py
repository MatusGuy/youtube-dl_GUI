from sys import path
path.insert(1,".")

from os import system as RunCmd

from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QMenu, QAction
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import Qt

from dist import pydist as pd

class DownloadedListItemMenu(QMenu):
    table = QTableWidget

    def __init__(self,item:QTableWidgetItem,table:QTableWidget):
        self.table = table

        self.table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
    
    def InitMenu(self):
        super().__init__()
        
        self.openAction = QAction(
            QIcon(pd.__PyDist__._WorkDir+"assets/folder_yellow.png"),
            "Open",
            self
        )

        self.playAction = QAction(
            QIcon(pd.__PyDist__._WorkDir+"assets/player_play.png"),
            "Play",
            self
        )

        self.copyAction = QAction(
            QIcon(pd.__PyDist__._WorkDir+"assets/player_play.png"),
            "Play",
            self
        )

    def Execute(self):
        if len(self.table.selectedItems())==1 and self.table.selectedItems()[0].column()==0:
            self.exec_(QCursor.pos())