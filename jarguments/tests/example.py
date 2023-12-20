from jarguments import JParser, JBool, JStr

args = JParser(
	JBool('show_text', help='determines whether "text" is shown'),
	JStr('text'),
)

if args.show_text:
	print(args.text)
