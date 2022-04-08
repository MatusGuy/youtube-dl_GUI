Thank you for using youtube-dl GUI, by MatusGuy!

You made a great decision to read this before starting the app.
There are some important warnings you need to read:

- ANTIVIRUS FALSE-POSITIVE WARNING
    I'm not bothering to pay for a minimum 60€ code signature.
    Soon, I'm changing compilers, hopefully, it'll fix this problem.
    Go to your anitvirus and mark the executable as an exception.

- Relocate executable to seperate folder
    When you run the executable for the first time, it spreads two files:

    - settings.json
        All the settings and saved user information that the app uses.
    
    - _hideConsole.py
        Code that hides the console on startup.
        Relocate this to another folder to disable it.

    The reason why I want you to make a specific folder for the app is so that the files don't spread to places they shouldn't.
    If you want to relocate the app to another folder, relocate the executable and those two files I mentioned

- "What is youtube-dl_GUI-recovery.exe??"
    This is a recovery tool.

    The idea is to keep an old version of the app so that when the newer version doesn't work, you use the old one that hopefully works.

    If the app crashes before showing the window but after showing the splash screen, follow these steps to report this issue:
        1. In the explorer's address bar, delete everything and type "cmd" (open the terminal in the current directory)
        2. Inside the terminal, type the name to your executable (should always be "youtube-dl_GUI.exe")
        3. Wait until something saying "Traceback" appears. If nothing appeared, ignore step 4. (Wait for the error)
        4. Copy that chunk of text to your clipboard. (Ctrl+C) (Copy the error)
        5. Go to https://github.com/MatusGuy/youtube-dl_GUI/issues and make an issue: (Must have a GitHub account)
            - describe what happened
            - if you copied anything in step 4, paste it aswell
    
    Urgently need the app? Follow these steps:
        1. Delete youtube-dl_GUI.exe (and youtube-dl_GUI.bak if it exists aswell).
        2. Duplicate youtube-dl_GUI-recovery.exe and re-name it to anything but "youtube-dl_GUI.exe".
        3. Hopefully, it works.