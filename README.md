# Logless = Logging with Less

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/logless.svg)](https://pypi.org/project/logless/) [![PyPI version](https://badge.fury.io/py/logless.svg)](https://badge.fury.io/py/logless) [![CI/CD Badge (master)](https://github.com/slalom-ggp/dataops-tools/workflows/CI/CD%20Builds/badge.svg)](https://github.com/slalom-ggp/dataops-tools/actions?query=workflow%3A%22CI/CD%20Builds%22) [![Docker Publish (latest)](<https://github.com/slalom-ggp/dataops-tools/workflows/Docker%20Publish%20(latest)/badge.svg>)](https://github.com/slalom-ggp/dataops-tools/actions?query=workflow%3A%22Docker+Publish+%28latest%29%22)

The goal of Logless is that we can all spend less time writing logging code and that
properly logged code can be just as beautiful as code without the same logging. Logless was
originally designed for data projects where we wanted to log how long any function would
take to execute, but without copy-pasting the same rudundant code snippets at the top and
bottom of each function.

Logless gives you a beautiful way to wrap any function or code block and get helpful and
informative logs, without having to change how you write your programs and without
cluttering up your code with messy print statements.

## Installation

Compatible with Python 3.7 and 3.8.

```bash
pip install logless
```

## Simple Logging

In its simplest form, simply wrap functions with `logged` or wrap code blocks with
`logged_block`. In both cases, you'll get one log event at start (`Beginning sleeping`), one
log event every five minutes (`Still sleeping (5min elapsed)`) and one log event at completion
(`Completed sleeping (7min elapsed)`).

```python
from logless import logged_block, logged

def my_func_a():
    with logged_block("napping"):
        # Nap for 7 minutes
        for x in 1 to 7:
            sleep 60

@logged("snoozing")
def my_func_a():
    # Snooze for 10 minutes
    sleep 600
```

For more advanced usage, you can also pass an f-string-style status message, consuming
function arguments in the log string. This allows the log decorator to be generic, while
still providing unique log outputs based upon the specifical values sent to the function.

```
@logged("building {how_many} {what}s")
def build_some(what: str, how_many: int):
    for x in 1 to how_many:
        build_one(what)

```
