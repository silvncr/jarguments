'Creates command line arguments.'

from __future__ import annotations

try:
	from .handle import parse_name
except ImportError:
	from handle import parse_name


# base argument class
class JArgument:
	'Base argument class.'

	# initialise
	def __init__(
		self: JArgument,
		/,
		name: str,
		argtype: type[bool | int | str],
		*,
		default: bool | float | str | None = None,
		short_name: str | None = None,
		helpstring: str | None = None,
		multiple: bool | None = False,
	) -> None:
		'Initialises a new instance of `JArgument`.'

		# validate argument name
		msg = f'invalid argument name: "{name}";'
		if not name:
			raise ValueError(msg, 'must not be empty')
		if not name[0].isalpha():
			raise ValueError(msg, 'must start with a letter')
		if not name:
			raise ValueError(msg, 'an error occured while processing the name')
		if _name := parse_name(name):
			self.name = _name
			self.python_name = _name.replace('-', '_')

		# set properties
		self.short_name = parse_name(short_name) if short_name else None
		self.type = argtype
		self.default = default
		self.required = default is None
		self.multiple = multiple or False
		self.helpstring = helpstring
		if argtype == bool:
			self.nargs = '?'
		elif multiple:
			self.nargs = '*'
		else:
			self.nargs = None


# boolean argument
class JBool(JArgument):
	'Boolean argument class. Extends `JArgument`.'

	# initialise
	def __init__(
		self: JBool,
		name: str,
		/,
		short_name: str | None = None,
		default: bool | None = None,
		helpstring: str | None = None,
	) -> None:
		'Initialises a new instance of `JBool`.'

		# call base class constructor
		super().__init__(
			name,
			bool,
			default=default,
			short_name=short_name or None,
			multiple=False,
			helpstring=helpstring,
		)


# integer argument
class JInt(JArgument):
	'Integer argument class. Extends `JArgument`.'

	# initialise
	def __init__(
		self: JInt,
		name: str,
		/,
		short_name: str | None = None,
		default: int | None = None,
		helpstring: str | None = None,
	) -> None:
		'Initialises a new instance of `JInt`.'

		# call base class constructor
		super().__init__(
			name,
			int,
			default=default,
			short_name=short_name or None,
			multiple=False,
			helpstring=helpstring,
		)


# string argument
class JStr(JArgument):
	'String argument class. Extends `JArgument`.'

	# initialise
	def __init__(
		self: JStr,
		name: str,
		/,
		short_name: str | None = None,
		default: str | None = None,
		helpstring: str | None = None,
	) -> None:
		'Initialises a new instance of `JStr`.'

		# call base class constructor
		super().__init__(
			name,
			str,
			default=default,
			short_name=short_name or None,
			multiple=None,
			helpstring=helpstring,
		)
