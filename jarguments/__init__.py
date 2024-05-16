'Provides a straightforward way to create command line arguments.'

try:
	from . import create, handle, parse
except ImportError:
	import create
	import handle
	import parse


# metadata
__author__ = 'silvncr'
__license__ = 'MIT'
__module_name__ = 'jarguments'
__python_version__ = '3.8'
__version__ = '0.2.0'
