import jarguments as j

args = j.JParser(
    j.JBool('show-text', help='determines whether "text" is shown'),
    j.JInt('number', default=1),
    j.JArgument('text', type=str, multiple=True),
)

if args.show_text:
    for _ in range(args.number):
        print(args.text)
