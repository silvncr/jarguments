<!-- omit from toc -->
# jarguments

simplifying args jargon

![version](https://img.shields.io/pypi/v/jarguments)
![status](https://img.shields.io/github/actions/workflow/status/silvncr/jarguments/python-publish.yml)
![downloads](https://img.shields.io/pypi/dm/jarguments)

![license](https://img.shields.io/github/license/silvncr/jarguments)
![format](https://img.shields.io/pypi/format/jarguments)
![pyversions](https://img.shields.io/pypi/pyversions/jarguments)

![repo-size](https://img.shields.io/github/repo-size/silvncr/jarguments)
![code-size](https://img.shields.io/github/languages/code-size/silvncr/jarguments)

## Summary

Provides a straightforward way to create command line arguments.

- :snake: Supports Python 3.8 and above. Tested on Windows 10.
- :construction: This project is still in development. Contributions are welcome!
- :star: Show your support by leaving a star!

## Contents

- [Summary](#summary)
- [Contents](#contents)
- [Installation](#installation)
- [Usage](#usage)

## Installation

```sh
python -m pip install --upgrade jarguments
```

> [!WARNING]
> All versions before `0.3.0` have been unpublished [due to a major oversight](https://silvncr.github.io/random/2024/10/21/regarding-deleted-commit-histories.html). Please update to the latest version.

## Usage

There are three steps to using the jarguments library:

1. Import the jarguments library.

    ```py
    from jarguments import create, parse
    ```

2. Provide your arguments with jarguments' classes.

    ```py
    # argument parser
    args = parse.JParser(

      # boolean argument
      create.JBool('show-text', helpstring='determines whether "text" is shown'),

      # integer argument
      create.JInt('number', default=1),

      # string argument
      create.JStr('text'),
    )
    ```

3. Use the outputs; they're parsed automatically!

    ```py
    if args.show_text:
      for _ in range(args.number):
        print(args.text)
    ```

Now it works just like any other command line application.

  ```sh
  $ python example.py --show-text --text "hello" "world"
  ["hello", "world"]
  ```

- Arguments without a default value are required. If you don't provide them, the script will raise an error:

    ```sh
    $ python example.py --show-text
    error: the following arguments are required: --text
    ```

- The `--help`/`-h` flag displays help messages:

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
