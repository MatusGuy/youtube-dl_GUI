import ctypes
print ("Hello world from python")
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )
print ("Done")