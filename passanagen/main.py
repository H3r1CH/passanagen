"""Provides some arithmetic functions"""
import random
import string
import typer


LCL = string.ascii_lowercase
UCL = string.ascii_uppercase
NUM = string.digits
CHAR = string.punctuation
PASS_LENGTH_MIN = 8

app = typer.Typer(help="CLI Password Analyzer and Generator.")

__version__ = "0.2.3"


def version_callback(value: bool):
    """Version callback function to get the version"""
    if value:
        typer.echo(f"passanagen version: {__version__}")
        raise typer.Exit()


@app.callback()
def main(version: bool = typer.Option(None, "--version",
callback=version_callback, is_eager=True, help="Show current version of passanagen")):
    """Callback function to get the version"""
    print(version)


@app.command("ana", help="Analyze a given password.")
def analyze(password: str):
    """Function to analyze a given password from the CLI."""
    print('-' * 22)
    print('ANALYZED PASSWORD')
    print('-' * 22)
    print('> Password Length: ', len(password))
    upper_count = 0
    lower_count = 0
    num_count = 0
    char_count = 0
    for i in password:
        if i.isupper():
            upper_count += 1
        elif i.islower():
            lower_count += 1
        elif i in NUM:
            num_count += 1
        elif i in CHAR:
            char_count += 1
        else:
            print('[-] Unknown CHARacter!')
    print('> Uppercase Letters:', upper_count)
    print('> Lowercase Letters:', lower_count)
    print('> Number count:', num_count)
    print('> Special Characters count:', char_count)
    print()

    if len(password) < PASS_LENGTH_MIN:
        print(f'[-] Your password "{password}" is too short! \
            Use a minimum length of {PASS_LENGTH_MIN}!')
    if upper_count < 1:
        print(f'[-] Your password "{password}" contains NO uppercase!')
    if lower_count < 1:
        print(f'[-] Your password "{password}" contains NO lowercase!')
    if num_count < 1:
        print(f'[-] Your password "{password}" contains NO numbers!')
    if char_count < 1:
        print(f'[-] Your password "{password}" contains NO special characters!')
    if (len(password) > PASS_LENGTH_MIN and upper_count > 0 and lower_count > 0 and \
        num_count > 0 and char_count > 0):
        print(f'[+] Your password "{password}" is STRONG!!')
    print('-' * 22)


@app.command("gen", help="Generate a password based on selected properties.")
def generate():
    """Function to generate a password based on selected properties."""
    pass_length = typer.prompt("Select Password length")
    try:
        pass_length_num = int(pass_length)
        if pass_length_num < PASS_LENGTH_MIN:
            print(f'[-] Password is too short. Please use at least {PASS_LENGTH_MIN} characters.')
            generate()
        else:
            print(f"Password Length = {pass_length_num}")
            low_case = typer.confirm("Do you want lowercase letters?")
            up_case = typer.confirm("Do you want uppercase letters?")
            a_number = typer.confirm("Do you want any numbers?")
            a_char = typer.confirm("Do you want special characters?")

            initial_password = ''
            unique_case = 0
            combined = ''
            remaining_password = ''

            if low_case:
                lower_password = random.choice(LCL)
                initial_password += lower_password
                unique_case += 1
                combined += LCL
            if up_case:
                upper_password = random.choice(UCL)
                initial_password += upper_password
                unique_case += 1
                combined += UCL
            if a_number:
                num_password = random.choice(NUM)
                initial_password += num_password
                unique_case += 1
                combined += NUM
            if a_char:
                char_password = random.choice(CHAR)
                initial_password += char_password
                unique_case += 1
                combined += CHAR

            if not any([low_case, up_case, a_number, a_char]):
                print("[+] Defaulting to only lowercase letters.")
                lower_password = random.choice(LCL)
                initial_password += lower_password
                unique_case += 1
                combined += LCL

            for _ in range(pass_length_num - unique_case):
                remaining_password += random.choice(combined)

            temp_password = ''.join(initial_password + remaining_password)
            new_passowrd = ''.join(random.sample(temp_password,len(temp_password)))
            print('-' * 22)
            print('GENERATED PASSWORD')
            print('-' * 22)
            print('[+] Your new password is:', new_passowrd)
            print('-' * 22)

    except ValueError:
        print("[-] Not a valid digit. Please enter in a number.")
        generate()


if __name__ == "__main__":
    app()
