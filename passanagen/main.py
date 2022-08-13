from mimetypes import init
from multiprocessing.sharedctypes import Value
from os import TMP_MAX
import typer
import random
import string

lcl = string.ascii_lowercase
ucl = string.ascii_uppercase
num = string.digits
char = string.punctuation
pass_length_min = 8

app = typer.Typer(help="CLI Password Analyzer and Generator.")


@app.command("ana", help="Analyze a given password.")
def analyze(password: str):
    print('-' * 22)
    print('ANALYZED PASSWORD')
    print('-' * 22)
    print('> Password Length: ', len(password))
    upper_count = 0
    lower_count = 0
    num_count = 0
    char_count = 0
    for u in password:
        if u.isupper():
            upper_count += 1
        elif u.islower():
            lower_count += 1
        elif u in num:
            num_count += 1
        elif u in char:
            char_count += 1
        else:
            print('[-] Unknown character!')          
    print('> Uppercase Letters:', upper_count)
    print('> Lowercase Letters:', lower_count)
    print('> Number count:', num_count)
    print('> Special Character count:', char_count)
    print()

    if len(password) < pass_length_min:
        print(f'[-] Your password "{password}" is too short! Use a minimum length of {pass_length_min}!')
    if upper_count < 1:
        print(f'[-] Your password "{password}" contains NO uppercase!')
    if lower_count < 1:
        print(f'[-] Your password "{password}" contains NO lowercase!')
    if num_count < 1:
        print(f'[-] Your password "{password}" contains NO numbers!')
    if char_count < 1:
        print(f'[-] Your password "{password}" contains NO special characters!')
    if (len(password) > pass_length_min and upper_count > 0 and lower_count > 0 and num_count > 0 and char_count > 0):
        print(f'[+] Your password "{password}" is STRONG!!')
    print('-' * 22)


@app.command("gen", help="Generate a password based on selected properties.")
def generate():
    pass_length = typer.prompt("Select Password length")
    try:
        pass_length_num = int(pass_length)
        if pass_length_num < pass_length_min:
            print(f'[-] Password is too short. Please use at least {pass_length_min} characters.')
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
                lower_password = random.choice(lcl)
                initial_password += lower_password
                unique_case += 1
                combined += lcl
            if up_case:
                upper_password = random.choice(ucl)
                initial_password += upper_password
                unique_case += 1
                combined += ucl
            if a_number:
                num_password = random.choice(num)
                initial_password += num_password
                unique_case += 1
                combined += num
            if a_char:
                char_password = random.choice(char)
                initial_password += char_password
                unique_case += 1
                combined += char

            if not any([low_case, up_case, a_number, a_char]):
                print("[+] Defaulting to only lowercase letters.")
                lower_password = random.choice(lcl)
                initial_password += lower_password
                unique_case += 1
                combined += lcl
            
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
