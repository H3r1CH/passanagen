import typer

letters = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
numbers = ('0','1','2','3','4','5','6','7','8','9')
spec_chars = ('`','~','!','@','#','$','%','^','&','*','(',')','-','+','=','_','{','}','[',']','\\','|','/','?','>','<')
length = ''

app = typer.Typer(help="CLI Password Analyzer and Generator.")

@app.command(help="Analyze a given password.")
def analyze(password: str):
    print('-' * 22)
    print('PASSWORD DETAILS')
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
        elif u in numbers:
            num_count += 1
        elif u in spec_chars:
            char_count += 1
        else:
            print('something else')          
    print('> Uppercase Letters:', upper_count)
    print('> Lowercase Letters:', lower_count)
    print('> Number count:', num_count)
    print('> Special Character count:', char_count)

    print('-' * 22)
    print('PASSWORD STRENGTH')
    print('-' * 22)
    if len(password) < 8:
        print(f'[-] Your password "{password}" is too short! Use a minimum length of 8!')
    if upper_count < 1:
        print(f'[-] Your password "{password}" contains NO uppercase!')
    if lower_count < 1:
        print(f'[-] Your password "{password}" contains NO lowercase!')
    if num_count < 1:
        print(f'[-] Your password "{password}" contains NO numbers!')
    if char_count < 1:
        print(f'[-] Your password "{password}" contains NO special characters!')
    if (len(password) > 8 and upper_count > 0 and lower_count > 0 and num_count > 0 and char_count > 0):
        print(f'[+] Your password "{password}" is STRONG!!')
    print('-' * 22)


@app.command(help="Generate a password based on selected properties.")
def generate(password: str):
    print(f"This is the {password}")


if __name__ == "__main__":
    app()
