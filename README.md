# passanagen
CLI Password Analyzer and Generator

![Pylint](https://github.com/H3r1CH/passanagen/actions/workflows/pylint.yml/badge.svg)
![Dependency](https://github.com/H3r1CH/passanagen/actions/workflows/dependency-review.yml/badge.svg)
![Publish](https://github.com/H3r1CH/passanagen/actions/workflows/python-publish.yml/badge.svg)

## Installation
```bash
pip install https://github.com/H3r1CH/passanagen/releases/download/v0.2.2/passanagen-0.2.2-py3-none-any.whl
```

### Help
```bash
passanagen --help

 Usage: passanagen [OPTIONS] COMMAND [ARGS]...

 CLI Password Analyzer and Generator.

┌─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ --version                     Show current version of passanagen                                               |
| --install-completion          Install completion for the current shell.                                        │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation. │
│ --help                        Show this message and exit.                                                      │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
┌─ Commands ─────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ ana       Analyze a given password.                                                                            │
│ gen       Generate a password based on selected properties.                                                    │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Analyzer

### Help
```bash
passanagen ana --help

 Usage: passanagen ana [OPTIONS] PASSWORD

 Analyze a given password.

┌─ Arguments ─────────────────────────────────────────┐
│ *    password      TEXT  [default: None] [required] │
└─────────────────────────────────────────────────────┘
┌─ Options ───────────────────────────────────────────┐
│ --help          Show this message and exit.         │
└─────────────────────────────────────────────────────┘
```

### Example
```bash
passanagen ana password123
----------------------
ANALYZED PASSWORD
----------------------
> Password Length:  11
> Uppercase Letters: 0
> Lowercase Letters: 8
> Number count: 3
> Special Character count: 0

[-] Your password "password123" contains NO uppercase!
[-] Your password "password123" contains NO special characters!
----------------------
```

## Generator

### Help
```bash
passanagen gen --help

 Usage: passanagen gen [OPTIONS]

 Generate a password based on selected properties.

┌─ Options ────────────────────────────────────┐
│ --help          Show this message and exit.  │
└──────────────────────────────────────────────┘
```

### Example
```bash
passanagen gen
Select Password length: 11
Password Length = 11
Do you want lower case letters? [y/N]: y
Do you want upper case letters? [y/N]: y
Do you want any numbers? [y/N]: y
Do you want special characters? [y/N]: y
----------------------
GENERATED PASSWORD
----------------------
[+] Your new password is: ;8QBD[H9f/~
----------------------
```
