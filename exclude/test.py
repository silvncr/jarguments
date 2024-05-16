'test lol'

from jarguments import create, parse

args = parse.JParser(
	create.JBool('show-text', helpstring='determines whether "text" is shown'),
	create.JInt('number', default=1),
	create.JStr('text'),
)

if args.show_text:
	print('\n'.join(args.text for _ in range(args.number)))
