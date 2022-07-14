# passanagen
CLI Password Analyzer and Generator

## Installation
```bash
pip install https://github.com/H3r1CH/passanagen/releases/download/v0.1.0/passanagen-0.1.0-py3-none-any.whl
```
or
```bash
git clone https://github.com/H3r1CH/passanagen.git
cd passanagen
poetry install
poetry shell
```
or
```bash
git clone https://github.com/H3r1CH/passanagen.git
cd passanagen
poetry install
poetry build
pip install dist/passanagen-0.1.0-py3-none-any.whl
```

### Help
```bash
passanagen --help        
Usage: passanagen [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.
  --help                Show this message and exit.

Commands:
  analyze
  generate
```

## Analyzer

### Help
```bash
passanagen analyze --help
Usage: passanagen analyze [OPTIONS] PASSWORD

Arguments:
  PASSWORD  [required]
```

### Example
```bash
passanagen analyze password123 
----------------------
PASSWORD DETAILS
----------------------
> Password Length:  11
> Uppercase Letters: 0
> Lowercase Letters: 8
> Number count: 3
> Special Character count: 0
----------------------
PASSWORD STRENGTH
----------------------
[-] Your password "password123" contains NO uppercase!
[-] Your password "password123" contains NO special characters!
```

## Generator

### Help

### Example
