<!-- omit from toc -->
# jarguments

simplifying args jargon

![[license](LICENSE)](https://img.shields.io/github/license/silvncr/jarguments)
![[publish status](https://github.com/silvncr/jarguments/actions/workflows/python-publish.yml)](https://img.shields.io/github/actions/workflow/status/silvncr/jarguments/python-publish.yml)
![[latest release](https://github.com/silvncr/jarguments/releases/latest)](https://img.shields.io/github/v/release/silvncr/jarguments)

## Summary

Providing a straightforward way to create command-line arguments.

> Works on Python 3.6 and above. Tested on Windows 10.

## Contents

- [Summary](#summary)
- [Contents](#contents)
- [Installation](#installation)
- [Usage](#usage)
  - [Library](#library)
  - [Command-line](#command-line)

## Installation

```sh
pip install jarguments
```

## Usage

### Library

There are three steps to using the jarguments library:

1. Import the jarguments library.

    ```py
    import jarguments as j
    ```

2. Provide your arguments with jarguments' classes.

    ```py
    args = j.JParser(
      j.JBool('show-text', help='determines whether "text" is shown'),
      j.JInt('number', default=1),
      j.JArgument('text', type=str, multiple=True),
    )
    ```

3. Use the outputs; they're parsed automatically!

    ```py
    if args.show_text:
      for _ in range(args.number):
        print(args.text)
    ```

### Command-line

- Now you can run your script with arguments:

    ```sh
    $ python example.py --show-text --text "hello" "world"
    ["hello", "world"]
    ```

- Arguments without a default value are required. If you don't provide them, the script will raise an error:

    ```sh
    $ python example.py --show-text
    error: the following arguments are required: --text
    ```

- If you want to see help messages, run your script with the `-h` or `--help` flag:

    ```sh
    $ python example.py -h
    usage: example.py [-h] [--show-text [SHOW_TEXT]] [--number NUMBER] --text [TEXT ...]

    options:
      -h, --help            show this help message and exit
      --show-text [SHOW_TEXT]
                            determines whether "text" is shown
      --number NUMBER
      --text [TEXT ...]
    ```
