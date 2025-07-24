"""
This is my first time to carefully write a docstring.
(Oh, VSCode's intelligent code completion !)
This is a module to provide users with self-define message en(de)crypt tool.
(Oh, VSCode's intelligent code completion x2 !!)
There are 3 functions to encrypt messages, and I will make another three to decrypt messages.
(Oh, VSCode's intelligent code completion x3 !!!)
...
"""
from random import choice

__version__ = '0.1.0'
METHODS = ['A', 'B', 'C']


def A_Z_swap(message: str):
    l = list(message)
    for i in range(0, len(l) // 2 * 2 - 1, 2):
        t = l[i]
        try:
            l[i] = l[i + 1]
            l[i + 1] = t
        except IndexError:
            break
    return ''.join(l)


def B_insert(message: str):
    l1 = list(message)
    l2 = []
    for i in l1:
        l2.append(i)
        l2.append(choice(
            'qwe!@#$%&我你他的人了和着过的得地之乎者也如果那么*rtyudylgfshjsajkaSIGOGAIBIUTGUVCUDW^&MUYSiopASD[]{}()FGHJKL'))
    return ''.join(l2)


def Y_rstrip(message: str):
    l = []
    for i in range(0, len(message), 2):
        l.append(message[i])
    return ''.join(l)


def C_X_reverse(message: str):
    return ''.join(reversed(list(message)))


def _check(s: str):
    for i in s.upper():
        if i not in METHODS:
            return False
    return True


def repl():
    print(
        f"""Endecrypter V{__version__}!
'e' to encrypt
'd' to decrypt
'q' to quit."""
    )
    while True:
        command = input('>>> ')
        match command:
            case 'e' | 'encrypt':
                message = input('Message >>> ')
                method = input(
                    """Method
A -> swap letters    ('12345678' -> '21436587')
B -> insert letters  ('12345678' -> '1q2w3e4r5t6y7u8i')
C -> reverse letters ('12345678' -> '87654321')
>>> """
                )
                if not _check(method):
                    print('Invalid method.')
                    continue
                for i in method:
                    match i.upper():
                        case 'A':
                            message = A_Z_swap(message)
                        case 'B':
                            message = B_insert(message)
                        case 'C':
                            message = C_X_reverse(message)

                print(f'Encrypted message:\n{message}')
            case 'd' | 'decrypt':

                message = input('Message >>> ')
                method = input('Method  >>> ')
                if not _check(method):
                    print('Invalid method.')
                    continue
                for i in reversed(list(method)):
                    match i.upper():
                        case 'A':
                            message = A_Z_swap(message)
                        case 'B':
                            message = Y_rstrip(message)
                        case 'C':
                            message = C_X_reverse(message)
                print(f'Decrypted message:\n{message}')
            case 'q' | 'quit':
                break
            case _:
                print('Invalid command.')


if __name__ == '__main__':
    repl()
