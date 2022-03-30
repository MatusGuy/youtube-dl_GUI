import sys,os
import ctypes
import psutil

State_stdout=None

def reopen_stdout():
    global State_stdout
    #clrstr = "\r" + " " * 80 + "\r"
    if State_stdout is None:
        State_stdout= sys.stdout
        sys.stdout = open("CONOUT$", "w")
        #sys.stdout.write(clrstr)
    else:
        pass
        #State.stdout = State.logger.stdout
        #State.logger.stdout = open("CONOUT$", "w")
        #State.logger.stdout.write(clrstr)

def restore_stdout():
    global State_stdout
    sys.stdout.close()
    sys.stdout = State_stdout


###
# Attach/detach console

def attach_console():
    if ctypes.windll.kernel32.GetConsoleWindow() != 0:
        #dprint("Already attached to a console")
        return

    # Find parent cmd.exe if exists
    pid = os.getpid()
    while True:
        try:
            p = psutil.Process(pid)
        except psutil.NoSuchProcess:
            # No such parent - started without console
            pid = -1
            break

        if os.path.basename(p.name()).lower() in [
                "cmd", "cmd.exe", "powershell", "powershell.exe"]:
            # Found it
            break

        # Search parent
        pid = p.ppid()

    # Not found, started without console
    if pid == -1:
        #dprint("No parent console to attach to")
        return

    #dprint("Attaching to console " + str(pid))
    if ctypes.windll.kernel32.AttachConsole(pid) == 0:
        #dprint("Attach failed with error " +
        #    str(ctypes.windll.kernel32.GetLastError()))
        return

    if ctypes.windll.kernel32.GetConsoleWindow() == 0:
        #dprint("Not a console window")
        return

    reopen_stdout()

def detach_console():
    if ctypes.windll.kernel32.GetConsoleWindow() == 0:
        return

    restore_stdout()

    if not ctypes.windll.kernel32.FreeConsole():
        pass
        #dprint("Free console failed with error " +
        #    str(ctypes.windll.kernel32.GetLastError()))
    else:
        pass
        #dprint("Freed console successfully")