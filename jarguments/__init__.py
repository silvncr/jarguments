'Provides a straightforward way to create command line arguments.'

try:
	from . import create, handle, parse
except ImportError:
	import create
	import handle
	import parse


__author__ = 'silvncr'
__license__ = 'MIT'
__module__ = 'jarguments'
__version__ = '0.3.0'
