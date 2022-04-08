import sys,subprocess

sys.path.insert(1,'.')

from PyQt5.QtGui import QIcon, QTextCursor, QTextCharFormat, QColor, QPixmap, QWheelEvent, QScrollEvent
from interface.cmdlineHelpTextboxUi import Ui_Cmd as ui
from PyQt5.QtWidgets import QDialog, qApp, QTextEdit, QWidget, QSpinBox
from PyQt5.QtCore import Qt, QEvent, QObject, QPointF

from dist import pydist as pd

class CmdHelpDialog(ui,QDialog):
    def eventFilter(self, object:QObject, event:QEvent):
        event.accept()
        if event.type() == QEvent.Type.Wheel:
            modifiers = qApp.keyboardModifiers()
            ctrl = modifiers == Qt.KeyboardModifier.ControlModifier
            print(ctrl)
            if ctrl:
                # looked on how to convert qevent to qwheelevent, didn't work, enjoy the white function names
                delta = event.angleDelta()
                if delta.y()   >0: self.IncreaseTextSize()
                elif delta.y() <0: self.DecreaseTextSize()
                return True
            return False
        elif event.type() == QEvent.Type.Scroll:
            modifiers = qApp.keyboardModifiers()
            ctrl = modifiers == Qt.KeyboardModifier.ControlModifier
            print(ctrl)
            if ctrl:
                # looked on how to convert qevent to qwheelevent, didn't work, enjoy the white function names
                delta = event.contentPos()
                if delta.y()   >0: self.IncreaseTextSize()
                elif delta.y() <0: self.DecreaseTextSize()
                return True
            return False
        else:
            return False

    def __init__(self,windowTitle:str="youtube-dl command line help") -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(windowTitle)
        self.setWindowIcon(QIcon(pd.__PyDist__._WorkDir+"assets/ytdl.png"))
        self.ChangeTextSize(9)
        self.setWindowFlags(Qt.WindowType.WindowCloseButtonHint)
        self.HideFind()
        self.InitIcons()
        #self.InitContextMenu()

        self.addActions([self.ZoomIn,self.ZoomOut])
        
        self.Find.toggled.connect(self.SetFindVisible)
        self.ZoomIn.triggered.connect (self.IncreaseTextSize)
        self.ZoomOut.triggered.connect(self.DecreaseTextSize)

        self.FindInput.textEdited.connect(self.FindText)

        self.Clear.pressed.connect(lambda: (self.FindInput.clear(),self.FindText()))
        self.Next.pressed.connect(lambda: self.GoToNext(self.FindInput.text()))

        self.TextSizeInput.valueChanged.connect(self.ChangeTextSize)
        #self.Text.installEventFilter(self)
    
    def IncreaseTextSize(self): self.TextSizeInput.setValue(self.TextSizeInput.value()+1)
    def DecreaseTextSize(self): self.TextSizeInput.setValue(self.TextSizeInput.value()-1)
    
    def InitIcons(self):
        self.Find.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/magnifier"))
        self.FindAction.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/magnifier"))
        self.TextSizeLabel.setPixmap(QPixmap(pd.__PyDist__._WorkDir+"assets/letter.png"))
        self.Clear.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/button_cancel.png"))
        self.Next.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/down.png"))
        self.Prev.setIcon(QIcon(pd.__PyDist__._WorkDir+"assets/up.png"))
    
    def InitContextMenu(self):
        self.Text.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.FindAction.toggled.connect(self.SetFindVisible)
        self.Text.addAction(self.FindAction)
        self.Text.addActions([self.ZoomIn,self.ZoomOut])
    
    def ChangeTextSize(self,size:int):
        self.Text.setStyleSheet(f"""
            background-color: rgb(12, 12, 12);
            color: rgb(204, 204, 204);
            selection-color: rgb(12, 12, 12);
            selection-background-color: rgb(204, 204, 204);
            font: {size}pt "Consolas";
        """)
    
    def HideFind(self): self.FindWidget.hide()
    def ShowFind(self): self.FindWidget.show()
    def SetFindVisible(self,visible:bool):
        self.FindAction.setChecked(visible)
        self.Find.setChecked(visible)
        if visible: self.ShowFind()
        else: self.HideFind()
    
    def FindText(self,text:str=...):
        if text == ...: text = self.FindInput.text()

        self.doc = self.Text.document()
        self.doc.undo()

        self.highlightCursor = QTextCursor(self.doc)
        self.docCursor = QTextCursor(self.doc)
        
        self.docCursor.beginEditBlock()

        self.ref = 0
        self.selected = 0

        #plainFormat  = QTextCharFormat()
        self.colourFormat = QTextCharFormat()
        self.colourFormat.setBackground(QColor(107, 94, 25))
        self.selectedFormat=QTextCharFormat()
        self.selectedFormat.setBackground(QColor(107, 64, 25))
        
        while not self.highlightCursor.isNull() and not self.highlightCursor.atEnd():
            self.highlightCursor = self.doc.find(text,self.highlightCursor)

            if not self.highlightCursor.isNull():
                self.ref += 1
                self.highlightCursor.movePosition(
                    QTextCursor.MoveOperation.NoMove,
                    QTextCursor.MoveMode.KeepAnchor
                )
                self.highlightCursor.mergeCharFormat(self.selectedFormat if self.ref==1 else self.colourFormat)
        
        self.References.setText(f"{self.ref}")
            
        self.docCursor.endEditBlock()
    
    def GoToNext(self,text:str=...):
        if text == ...: text = self.FindInput.text()

        self.docCursor.beginEditBlock()

        if self.selected+1 < self.ref:
            for i in range(self.selected+2):
                self.highlightCursor = self.doc.find(text)
                if i == self.selected+1:
                    self.selected += 1

                    self.Text.setTextCursor(self.highlightCursor)
        
        self.docCursor.endEditBlock()

    def GetHelp(self,cmd):
        self.Text.setPlainText(self.ExecCmd(cmd))
        self.exec_()

    @staticmethod
    def ExecCmd(cmd) -> str:
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags|=subprocess.STARTF_USESHOWWINDOW
        process = subprocess.Popen(cmd,
            startupinfo=startupinfo,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE
        )
        data = process.stdout.read()
        process.stdout.close()
        return data.decode("utf-8")