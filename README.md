# time-until-cli
> Application that calculate time duration until reach a given date.

**Main objective**: Understanding the logic of _Python_ app publishing and documenting it on a simple project.
## Installation

You may install application package on PyPI:

```bash
pip install time-until
```

## Usage

```bash
time_until 22h
```

## Application flow & use cases

Using CLI to calculate time duration to a given input date or timestamp. 

| Input | Output / Response |
| :---- | :---------------- |
| `time-until 23h` | Time remaining: 8 hour(s) 22 minute(s) 42 second(s) |
| `time-until 2023-02-27` | Time remaining: 04 month(s) 14 day(s) 8 hour(s) 22 minute(s) 42 second(s)  |

![app-flow-example](assets/time_until_app.png)

## Main goals

Build a Python app that works as a CLI (Command-line Interface) that receives a future date or time and returns a calculation of remaining time from now until that given date or time.

Once working, this project must be configured and submitted as Python package thru PyPI Modules. The process of development, build, release and publishing is the core of the project, to understand it and provice ideas and thoghts of process automation.

Feel free to initiate a discusison, open a issue or a pull request to this project. All kinds of contributions and ideas are welcome. **_Let's code!_**

## Developing

Please read and make use of the [Makefile](Makefile) to help you with the common development processes like installing dependencies, test and build the Python package. 

```bash
# to install dependencies
make setup

# to execute the tests
make test

# to generate test coverage reports - stdout & HTML file
make coverage

# to generate a local build of the CLI time-until
make build
```

This project is currently using [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) methodology to maintain the readability of the code versioning.