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
__version__ = '0.0.1'


# base argument
class JArgument:
	def __init__(
		self,
		name: str,
		type: Type[Union[bool, str]],
		default: Union[Any, Optional[bool]] = None,
		short_name: Optional[str] = None,
		multiple: Optional[bool] = False,
		help: Optional[str] = None,
	):
		self.name = name
		self.short_name = short_name or None
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


# string argument
class JStr(JArgument):
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


# boolean argument parser
class JBooleanAction(Action):
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
		super(JBooleanAction, self).__init__(
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


# base parser
class JParser(ArgumentParser):
	def __init__(self, *args: JArgument):
		super().__init__()
		for arg in args:
			args_dict = {
				'name': (f'--{arg.name}',),
				'default': arg.default,
				'help': arg.help,
			}
			if arg.type == bool:
				args_dict = {
					**args_dict, **{
						'action': JBooleanAction,
						'dest': arg.name,
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
				args_dict['name'] = (f'--{arg.name}', f'-{arg.short_name}')
			self.add_argument(*args_dict.pop('name'), **args_dict)

	# return parsed arguments
	def __new__(cls, *args: JArgument) -> Namespace:
		instance = super().__new__(cls)
		instance.__init__(*args)
		return instance.parse_args()
