# passanagen
CLI Password Analyzer and Generator

## Installation
```bash
git clone https://github.com/H3r1CH/passanagen.git
cd passanagen
poetry install
poetry shell
```
### Help
```bash
python main.py --help        
Usage: main.py [OPTIONS] COMMAND [ARGS]...

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
python main.py analyze --help
Usage: main.py analyze [OPTIONS] PASSWORD

Arguments:
  PASSWORD  [required]
```

### Example
```bash
python main.py analyze password123 
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
