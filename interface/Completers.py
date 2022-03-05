from sys import path
path.insert(1,".")

from copy import copy

from PyQt5.QtWidgets import QCompleter
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtCore import Qt

templates = [
	'%(id)s',
	'%(title)s',
	'%(formats)s',
	'%(thumbnails)s',
	'%(description)s',
	'%(upload_date)s',
	'%(uploader)s',
	'%(uploader_id)s',
	'%(uploader_url)s',
	'%(channel_id)s',
	'%(channel_url)s',
	'%(duration)s',
	'%(view_count)s',
	'%(average_rating)s',
	'%(age_limit)s',
	'%(webpage_url)s',
	'%(categories)s',
	'%(tags)s',
	'%(is_live)s',
	'%(subtitles)s',
	'%(location)s',
	'%(like_count)s',
	'%(channel)s',
	'%(license)s',
	'%(extractor)s',
	'%(webpage_url_basename)s',
	'%(extractor_key)s',
	'%(playlist)s',
	'%(playlist_index)s',
	'%(thumbnail)s',
	'%(display_id)s',
	'%(requested_subtitles)s',
	'%(requested_formats)s',
	'%(format)s',
	'%(format_id)s',
	'%(width)s',
	'%(height)s',
	'%(resolution)s',
	'%(fps)s',
	'%(vcodec)s',
	'%(vbr)s',
	'%(stretched_ratio)s',
	'%(acodec)s',
	'%(abr)s',
	'%(ext)s',
]
__templates__ = copy(templates)

templateCompleter = QCompleter(__templates__)

templateCompleter.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
templateCompleter.setCompletionRole(Qt.ItemDataRole.EditRole)

__oldTemplate__ = ""
def __setOldTemplate__(__value__:str): __oldTemplate__ = __value__

def OnActivated(selected:str):
	print("sdgdgfs")

	for item in __templates__: __templates__[__templates__.index(item)] = templateCompleter.widget().currentText() + item
	print(__templates__)
	templateCompleter.setModel(__templates__)

	#templateCompleter.setCompletionPrefix("")
	#templateCompleter.widget().setCurrentText(templateCompleter.pathFromIndex())

#templateCompleter.activated.connect(OnActivated)