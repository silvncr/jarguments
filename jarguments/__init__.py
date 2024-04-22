'''
Providing a straightforward way to create command-line arguments.
'''


# imports
from argparse import Action, ArgumentParser, Namespace
from typing import Any, Optional, Type, Union


# module info
__author__ = 'silvncr'
__license__ = 'MIT'
__module_name__ = 'jarguments'
__python_version__ = '3.6'
__version__ = '0.1.0'


# parse argument name
def parse_argument_name(name: str) -> Optional[str]:
	'''
	Used to parse an argument name from a string.
	'''
	for i in ['--', '-', '/']:
		if name.startswith(i):
			name = name[len(i):]
	_name = name = name.strip().lower().replace(' ', '-').replace('_', '-')
	for char in _name:
		if not char.isalnum() and char not in ['-', '_']:
			name = name.replace(char, '')
	return name or None


# base argument class
class JArgument:
	'''
	Base argument class.
	'''
	def __init__(
		self,
		name: str,
		type: Type[Union[bool, int, str]],
		default: Union[Any, Optional[bool]] = None,
		short_name: Optional[str] = None,
		multiple: Optional[bool] = False,
		help: Optional[str] = None,
	):
		if not name:
			raise ValueError(f'invalid argument name: "{name}"; \
					must not be empty')
		if not name[0].isalpha():
			raise ValueError(f'invalid argument name: "{name}"; \
					must start with a letter')
		elif name:
			if _name := parse_argument_name(name):
				self.name = _name
				self.python_name = _name.replace('-', '_')
		else:
			raise ValueError(f'invalid argument name: "{name}"; \
					an error occured while processing the name')
		self.short_name = parse_argument_name(short_name) if short_name else None
		self.type = type
		self.default = default
		self.required = default is None
		self.multiple = multiple or False
		self.help = help
		if type == bool:
			self.nargs = '?'
		elif multiple:
			self.nargs = '*'
		else:
			self.nargs = None


# boolean argument
class JBool(JArgument):
	'''
	Boolean argument class. Extends `JArgument`.
	'''
	def __init__(
		self,
		name: str,
		short_name: Optional[str] = None,
		default: Optional[bool] = None,
		help: Optional[str] = None,
	):
		super().__init__(
			name,
			bool,
			default,
			short_name or None,
			False,
			help,
		)


# integer argument
class JInt(JArgument):
	'''
	Integer argument class. Extends `JArgument`.
	'''
	def __init__(
		self,
		name: str,
		short_name: Optional[str] = None,
		default: Optional[int] = None,
		help: Optional[str] = None,
	):
		super().__init__(
			name,
			int,
			default,
			short_name or None,
			False,
			help,
		)


# string argument
class JStr(JArgument):
	'''
	String argument class. Extends `JArgument`.
	'''
	def __init__(
		self,
		name: str,
		short_name: Optional[str] = None,
		default: Optional[str] = None,
		help: Optional[str] = None,
	):
		super().__init__(
			name,
			str,
			default,
			short_name or None,
			None,
			help,
		)


# base argument action
class JAction(Action):
	'''
	Base argument parser.
	'''
	def __init__(
		self,
		option_strings,
		dest,
		nargs=None,
		const=None,
		default=None,
		type=None,
		choices=None,
		required=False,
		help=None,
		metavar=None,
	):
		super(JAction, self).__init__(
			option_strings,
			dest,
			nargs=nargs,
			const=const,
			default=default,
			type=type,
			choices=choices,
			required=required,
			help=help,
			metavar=metavar,
		)


# boolean argument action
class JBoolAction(JAction):
	'''
	Boolean argument parser. Extends `JAction`.
	'''
	def __init__(
		self,
		option_strings,
		dest,
		nargs='?',
		const=True,
		default=None,
		type=str,
		choices=None,
		required=False,
		help=None,
		metavar=None,
	):
		super(JBoolAction, self).__init__(
			option_strings,
			dest,
			nargs=nargs,
			const=const, # type: ignore
			default=default,
			type=type, # type: ignore
			choices=choices,
			required=required,
			help=help,
			metavar=metavar,
		)

	# generate boolean value from string
	def __call__(
		self,
		parser,
		namespace,
		values,
		option_string=None,
	):
		setattr(
			namespace, self.dest, True if values is None else not any(
				str(values).lower().startswith(i)
				for i in ['f', 'n']
			),
		)


# integer argument action
class JIntAction(JAction):
	'''
	Integer argument parser. Extends `JAction`.
	'''
	def __call__(self, parser, namespace, values, option_string=None):
		try:
			setattr(namespace, self.dest, int(str(values)))
		except ValueError:
			parser.error(f"Invalid integer value: {values}")


# string argument action
class JStrAction(JAction):
	'''
	String argument parser. Extends `JAction`.
	'''
	def __call__(self, parser, namespace, values, option_string=None):
		setattr(namespace, self.dest, str(values))


# parser
class JParser(ArgumentParser):
	'''
	Parser for instances of `JArgument` and its extensions.
	'''
	def __init__(self, *args: JArgument):
		super().__init__()
		for arg in args:
			args_dict = {
				'default': arg.default,
				'dest': arg.python_name,
				'help': arg.help,
			}
			if arg.type == bool:
				args_dict = {
					**args_dict, **{
						'action': JBoolAction,
					}
				}
			elif arg.type == int:
				args_dict = {
					**args_dict, **{
						'action': JIntAction,
					}
				}
			elif arg.type == str:
				args_dict = {
					**args_dict, **{
						'action': JStrAction,
					}
				}
			else:
				args_dict = {
					**args_dict, **{
						'nargs': arg.nargs,
						'type': arg.type,
						'required': arg.required,
					}
				}
			if arg.short_name:
				args_dict = {
					**args_dict, **{
						'name': (f'--{arg.name}', f'-{arg.short_name}'),
					}
				}
			else:
				args_dict = {
					**args_dict, **{
						'name': (f'--{arg.name}',),
					}
				}
			self.add_argument(*args_dict.pop('name'), **args_dict)

	# parse arguments
	def parse_args(self, *args, **kwargs) -> Namespace:
		namespace = super().parse_args(*args, **kwargs)
		args_dict = vars(namespace)
		args_obj = Namespace()
		for python_name, value in args_dict.items():
			setattr(args_obj, python_name, value)
		return args_obj

	# return parsed arguments
	def __new__(cls, *args: JArgument) -> Namespace:
		instance = super().__new__(cls)
		instance.__init__(*args)
		return instance.parse_args()
