
try:
    import pyi_splash as psh
    from PyQt5 import QtGui,QtCore
except:
    psh=False

def Splash_is_alive():
    if psh:
        return psh.is_alive()
    else:
        return False

def Splash_update_text(msg):
    if Splash_is_alive():
        psh.update_text(msg)

def Splash_close():
    if Splash_is_alive():
        psh.close()

def Splash_loadcomplete(close_delay=2500):
    if Splash_is_alive():
        Splash_update_text("Loading Complete!")
        QtCore.QTimer.singleShot(close_delay, Splash_close)

