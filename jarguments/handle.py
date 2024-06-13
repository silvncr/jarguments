'Handles data relating to command line arguments.'

from __future__ import annotations

from argparse import Action, Namespace
from typing import TYPE_CHECKING, Any, Iterable, Sequence

if TYPE_CHECKING:
	try:
		from .parse import JParser
	except ImportError:
		from parse import JParser


# parse argument name
def parse_name(name: str) -> str | None:
	'Parses an argument name from a string.'

	# validate argument name
	for i in ['--', '-', '/']:
		if name.startswith(i):
			name = name[len(i) :]
	_name = name = name.strip().lower().replace(' ', '-').replace('_', '-')
	for char in _name:
		if not char.isalnum() and char not in ['-', '_']:
			name = name.replace(char, '')
	return name or None


# base argument action
class JAction(Action):
	'Base argument action.'

	def __init__(
		self: JAction,
		option_strings: Sequence[str],
		dest: str,
		nargs: int | str | None = None,
		const: bool | float | str | None = None,
		default: bool | float | str | None = None,
		argtype: type[bool | int | str] | None = None,
		choices: Iterable[bool | int | str] | None = None,
		helpstring: str | None = None,
		metavar: str | tuple[str, ...] | None = None,
		*,
		required: bool = False,
	) -> None:
		'Initialises a new instance of `JAction`.'

		# call base class constructor
		super().__init__(
			option_strings,
			dest,
			nargs=nargs,
			const=const,
			default=default,
			type=argtype,
			choices=choices,
			required=required,
			help=helpstring,
			metavar=metavar,
		)


# boolean argument action
class JBoolAction(JAction):
	'Boolean argument parser. Extends `JAction`.'

	# initialise
	def __init__(
		self: JBoolAction,
		option_strings: Sequence[str],
		dest: str,
		nargs: str = '?',
		const: bool | None = None,
		default: bool | None = None,
		argtype: type[bool] = bool,
		choices: Iterable[bool] | None = None,
		helpstring: str | None = None,
		metavar: str | tuple[str, ...] | None = None,
		*,
		required: bool = False,
	) -> None:
		'Initialises a new instance of `JBoolAction`.'

		# call base class constructor
		super().__init__(
			option_strings,
			dest,
			nargs=nargs,
			const=const,
			default=default,
			argtype=argtype,
			choices=choices,
			helpstring=helpstring,
			metavar=metavar,
			required=required,
		)

	# parse boolean argument
	def __call__(
		self: JBoolAction,
		namespace: Namespace,
		values: str | Sequence[Any] | None,
	) -> None:
		'Parses a boolean argument.'

		# set attribute
		setattr(
			namespace,
			self.dest,
			True
			if values is None
			else not any(str(values).lower().startswith(i) for i in ['f', 'n']),
		)


# integer argument action
class JIntAction(JAction):
	'Integer argument parser. Extends `JAction`.'

# initialise
	def __init__(
		self: JIntAction,
		option_strings: Sequence[str],
		dest: str,
		nargs: str = '?',
		const: int | None = None,
		default: int | None = None,
		argtype: type[int] = int,
		choices: Iterable[int] | None = None,
		helpstring: str | None = None,
		metavar: str | tuple[str, ...] | None = None,
		*,
		required: bool = False,
	) -> None:
		'Initialises a new instance of `JIntAction`.'

		# call base class constructor
		super().__init__(
			option_strings,
			dest,
			nargs=nargs,
			const=const,
			default=default,
			argtype=argtype,
			choices=choices,
			helpstring=helpstring,
			metavar=metavar,
			required=required,
		)

	# parse integer argument
	def __call__(
		self: JIntAction,
		parser: JParser,
		namespace: Namespace,
		values: str | Sequence[Any] | None,
	) -> None:
		'Parses an integer argument.'

		# set attribute
		try:
			setattr(namespace, self.dest, int(str(values)))
		except ValueError:
			parser.error(f'Invalid integer value: {values}')


# string argument action
class JStrAction(JAction):
	'String argument parser. Extends `JAction`.'

# initialise
	def __init__(
		self: JStrAction,
		option_strings: Sequence[str],
		dest: str,
		nargs: str = '?',
		const: str | None = None,
		default: str | None = None,
		argtype: type[str] = str,
		choices: Iterable[str] | None = None,
		helpstring: str | None = None,
		metavar: str | tuple[str, ...] | None = None,
		*,
		required: bool = False,
	) -> None:
		'Initialises a new instance of `JStrAction`.'

		# call base class constructor
		super().__init__(
			option_strings,
			dest,
			nargs=nargs,
			const=const,
			default=default,
			argtype=argtype,
			choices=choices,
			helpstring=helpstring,
			metavar=metavar,
			required=required,
		)

	# parse string argument
	def __call__(
		self: JStrAction,
		namespace: Namespace,
		values: str | Sequence[Any] | None,
	) -> None:
		'Parses a string argument.'

		# set attribute
		setattr(namespace, self.dest, str(values))
