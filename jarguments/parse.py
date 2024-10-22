'Parses data from command line arguments.'

from __future__ import annotations

from argparse import ArgumentParser, Namespace
from typing import TYPE_CHECKING

try:
	from .handle import JBoolAction, JIntAction, JStrAction
except ImportError:
	from handle import JBoolAction, JIntAction, JStrAction

if TYPE_CHECKING:
	try:
		from .create import JArgument
	except ImportError:
		from create import JArgument


# parser
class JParser(ArgumentParser):
	'Parser for instances of `JArgument` and its extensions.'

	# initialise
	def __init__(
		self: JParser,
		*args: JArgument,
	) -> None:
		'Initialises a new instance of `JParser`.'

		# call base class constructor
		super().__init__()

		# add arguments
		for arg in args:
			args_dict = {
				'default': arg.default,
				'dest': arg.python_name,
				'helpstring': arg.helpstring,
			}
			if arg.type == bool:
				args_dict = {
					**args_dict,
					'action': JBoolAction,
				}
			elif arg.type == int:
				args_dict = {
					**args_dict,
					'action': JIntAction,
				}
			elif arg.type == str:
				args_dict = {
					**args_dict,
					'action': JStrAction,
				}
			else:
				args_dict = {
					**args_dict,
					'nargs': arg.nargs,
					'type': arg.type,
					'required': arg.required,
				}
			if arg.short_name:
				args_dict = {
					**args_dict,
					'name': (f'--{arg.name}', f'-{arg.short_name}'),
				}
			else:
				args_dict = {
					**args_dict,
					'name': (f'--{arg.name}',),
				}
			self.add_argument(*args_dict.pop('name'), **args_dict)

	# parse arguments
	def parse_args(
		self: JParser,
		*args: JArgument,
		**kwargs: JArgument,
	) -> Namespace:
		'Parses arguments.'

		# parse arguments
		namespace = super().parse_args(*args, **kwargs)
		args_dict = vars(namespace)
		args_obj = Namespace()
		for python_name, value in args_dict.items():
			setattr(args_obj, python_name, value)
		return args_obj

	# return parsed arguments
	def __new__(
		cls: ...,
		*args: JArgument,
	) -> Namespace:
		'Parses arguments and returns the result.'

		# parse arguments
		instance = super().__new__(cls)
		instance.__init__(*args)
		return instance.parse_args()
