import cppyy

from os import listdir
from os.path import join
from typing import Any
from awaits.awaitable import awaitable

class AsyncDownoload:

	def __init__(self, path:str=''):
		if path:
			files = [
				file for file in (listdir(path))
				if file.endwsith((
					'.cc', '.cxx', '.cpp',
					'.c++', '.h', '.hpp',
					'.hh', '.hxx', '.h++'
				))
			]
			for file in files:
				cppyy.include(join(path, file))
		else:
			raise OSError('The folder with C++ files is not specified')

	def __getattr__(self, name:str) -> Any:
		@awaitable
		def wrapper(*args, **kwargs) -> Any:
			function = getattr(cppyy.gbl, name)
			return function(*args, **kwargs)
		return wrapper