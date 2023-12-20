<!-- omit from toc -->
# jarguments

simplifying args jargon

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
git clone https://github.com/silvncr/jarguments.git
cd jarguments
python setup.py install
```

## Usage

### Library

There are three steps to using the jarguments library:

1. Import the jarguments library.

    ```py
    from jarguments import *
    ```

2. Provide your arguments with jarguments' classes.

    ```py
    args = JParser(
      JBool('show_text', help='determines whether "text" is shown'),
      JStr('text'),
    )
    ```

3. Use your outputs; they are parsed automatically.

    ```py
    if args.show_text:
      print(args.text)
    ```

### Command-line

- Now you can run your script with arguments:

    ```sh
    $ python script.py --show_text --text "hello world"
    hello world
    ```

- Arguments without a default value are required. If you don't provide them, the script will raise an error:

    ```sh
    $ python script.py --show_text
    error: the following arguments are required: --text
    ```

- If you want to see help messages, run your script with the `-h` or `--help` flag:

    ```sh
    $ python script.py -h
    usage: script.py [-h] [--show_text] --text TEXT

    options:
      -h, --help            show this help message and exit   
      --show_text [SHOW_TEXT]
                            determines whether "text" is shown
      --text TEXT
    ```
