# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
                     pathex=['youtube-dl','assets'],
                     binaries=[('youtube-dl\\youtube-dl.exe','youtube-dl'),
                               ('youtube-dl\\ffmpeg.exe','youtube-dl'),
                               ('.\\dist\\pydist.dll','.\\dist')
                               ],
                     datas=[('.\\assets\\forward.png'     ,'.\\assets'),
                            ('.\\assets\\stop.png'     ,'.\\assets'),

                            ('.\\assets\\ytdl.png'     ,'.\\assets'),
                            ('.\\assets\\ffmpeg.png'     ,'.\\assets'),
                            ('.\\assets\\ytdl.gif'     ,'.\\assets'),

                            ('.\\settings.json'     ,'.'),

                            ('.\\assets\\kcoloredit.png'     ,'.\\assets'),
                            ('.\\assets\\info.png'     ,'.\\assets'),
                            ('.\\assets\\edit_add.png'      ,'.\\assets'),
                            ('.\\assets\\folder_yellow.png'     ,'.\\assets'),
                            ('.\\assets\\susehelpcenter.png'     ,'.\\assets'),
                            ('.\\assets\\terminal.png'     ,'.\\assets'),
                            ('.\\assets\\help_index.png'     ,'.\\assets'),
                            ('.\\assets\\view_text.png'     ,'.\\assets'),
                            ('.\\assets\\button_cancel.png'     ,'.\\assets'),
                            ('.\\assets\\editcopy.png'     ,'.\\assets'),
                            ('.\\assets\\player_play.png'     ,'.\\assets'),
                            ('.\\assets\\proxy.png'     ,'.\\assets'),
                            ('.\\assets\\kchart.png'     ,'.\\assets'),
                            ],
                     hiddenimports=[],
                     hookspath=['.\\dist\pydisthk.py'],
                     runtime_hooks=[],
                     excludes=['*.ui','*.bat','*_CompTest.py'],
                     win_no_prefer_redirects=False,
                     win_private_assemblies=False,
                     cipher=block_cipher,
                     noarchive=False)
splash = Splash('assets\\splash.png',
                binaries=a.binaries,
                datas=a.datas,
                text_pos=(20, 360),
                text_size=10,
                text_color='white')
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          splash,                   
          splash.binaries,          
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='youtube-dl_GUI',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True, 
          version='dist\\Resources.rc', 
          icon='.\\assets\\ytdl.ico')
