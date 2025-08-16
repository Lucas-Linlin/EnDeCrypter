"""
This is my first time to carefully write a docstring.
This is a module to provide users with self-define message en(de)crypt tool.
There are 3 functions to encrypt messages, and I will make another three to decrypt messages.
...
"""
from random import choice
from tkinter import Tk, Label, Button, Entry, Text
from tkinter.messagebox import showwarning
from time import time
from datetime import datetime
from pathlib import Path

__version__ = '0.3.2-alpha'
METHODS = ['A', 'B', 'C']
CHOICE_STR = 'qwe!@#$%&我你他的人了和着过的得地之乎者也如果那么*rtyudylgfshjsajkaSIGOGAIBIUTGUVCUDW^&MUYSiopASD[]{}()FGHJKL'
START: float = time()
rootPath = Path(__file__).parent
_DEBUG_MODE = True


def initLog():
    if not _DEBUG_MODE:
        return
    with open(rootPath / 'logs.log', 'w', encoding='utf-8') as file:
        file.write(
            f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\nEnDeCrypter v{__version__}\n')


def log(log: str, level: str = 'info'):
    if not _DEBUG_MODE:
        return
    current = time()
    elapsed = int((current - START) * 1000)
    with open(rootPath / 'logs.log', 'a', encoding='utf-8') as file:
        file.write(f"[{elapsed:7} ms] [{level.upper()}] {log}\n")


def A_Z_swap(message: str):
    '''A function to swap strings.
    >>> A_Z_swap('12345678')
    '21436587'
    >>> A_Z_swap('abcdefgh')
    'badcfehg'
    '''
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
    '''A function to insert random characters to strings.
    >>> B_insert('12345678') #doctest:+ELLIPSIS
    '1...2...3...4...5...6...7...8...'
    >>> B_insert('abcdefgh') #doctest:+ELLIPSIS
    'a...b...c...d...e...f...g...h...'
    '''
    l1 = list(message)
    l2 = []
    for i in l1:
        l2.append(i)
        l2.append(choice(CHOICE_STR))
    return ''.join(l2)


def Y_rstrip(message: str):
    '''A function to remove the spare characters in each pair of the string.
    >>> Y_rstrip('12345678')
    '1357'
    >>> Y_rstrip('1a2b3c4d5e')
    '12345'
    '''
    l = []
    for i in range(0, len(message), 2):
        l.append(message[i])
    return ''.join(l)


def C_X_reverse(message: str):
    '''A function to reverse strings.
    >>> C_X_reverse('12345678')
    '87654321'
    >>> C_X_reverse('abcdefgh')
    'hgfedcba'
    '''
    return ''.join(reversed(list(message)))


def Password(message: str, password: str):
    '''A function to encrypy strings with given password.'''
    if not _check_password(password):
        showwarning('Warning', 'Invalid password')
        raise ValueError('Invalid password')
    pw = ((int(password) % 16)**2) % 16
    l = list(message)

    for i, c in enumerate(l):
        if c.isalpha():
            if c.isupper():
                l[i] = chr(ord(c)+pw)
            else:
                l[i] = chr(ord(c)-pw)
        elif c.isdigit():
            if int(c)+(pw % 10) < 10:
                l[i] = str(int(c)+(pw % 10))
            elif int(c)-(pw % 10) >= 0:
                l[i] = str(int(c)-(pw % 10))
            else:
                l[i] = c
        else:
            l[i] = c
    pw = f'{pw:02d}'
    message = ''.join(l)
    return message+pw


def passworD(message: str, password: str):
    '''A function to decrypy strings with given password.'''
    if not _check_password(password):
        showwarning('Warning', 'Invalid password')
        raise ValueError('Invalid password')
    pw = ((int(password) % 16)**2) % 16
    l = list(message)
    if int(message[-2:])!=pw:
        showwarning('Warning', 'Invalid password')
        return
    for i, c in enumerate(l):
        if c.isalpha():
            if c.isupper():
                l[i] = chr(ord(c)-pw)
            else:
                l[i] = chr(ord(c)+pw)
        elif c.isdigit():
            if int(c)+(pw % 10) >= 10:
                l[i] = str(int(c)-(pw % 10))
            elif int(c)-(pw % 10) < 0:
                l[i] = str(int(c)+(pw % 10))
            else:
                l[i] = c
        else:
            l[i] = c

    message = ''.join(l)
    return message


def _check_method(s: str):
    for i in s.upper():
        if i not in METHODS:
            return False
    return True


def _check_password(s: str):
    try:
        int(s)
        return True
    except ValueError:
        return False


def encrypt(message: str, method: str, password: str):
    global encrypt_text
    encrypt_text.delete('1.0', 'end')
    message = message.replace(' ', '·')

    if not _check_method(method):
        showwarning('Warning', 'Invalid method')
        return
    try:
        message = Password(message, password)
    except ValueError:
        return

    for i in method.upper():
        if i == 'A':
            message = A_Z_swap(message)
        elif i == 'B':
            message = B_insert(message)
        elif i == 'C':
            message = C_X_reverse(message)
    encrypt_text.insert('end', message)


def decrypt(message: str, method: str, password: str):
    global decrypt_text
    decrypt_text.delete('1.0', 'end')
    message = message.replace('·', ' ')
    if not _check_method(method):
        showwarning('Warning', 'Invalid method')
        return

    for i in reversed(method.upper()):
        if i == 'A':
            message = A_Z_swap(message)
        elif i == 'B':
            message = Y_rstrip(message)
        elif i == 'C':
            message = C_X_reverse(message)
    try:
        message = Password(message, password)
    except ValueError:
        return
    decrypt_text.insert('end', message)


def main():
    log('Enter main().')
    global encrypt_text, decrypt_text
    root = Tk()
    root.title(f'EnDeCrypter v{__version__}')

    # Spacer
    Label(root, text=f' Encrypt Zone{' '*25}|{' '*25}Decrypt Zone').grid(
        column=0, row=0, columnspan=5)

    # Encrypt
    l1 = Label(root, text='Message:')
    l1.grid(column=0, row=1)

    e1 = Entry(root, width=30)
    e1.grid(column=1, row=1)

    l2 = Label(root, text=' Method:')
    l2.grid(column=0, row=2)

    e2 = Entry(root, width=30)
    e2.grid(column=1, row=2)

    l3 = Label(root, text=' Password:')
    l3.grid(column=0, row=3)

    e3 = Entry(root, width=30)
    e3.grid(column=1, row=3)

    b1 = Button(
        root,
        text='Encrypt',
        width=20,
        command=lambda: encrypt(
            e1.get(),
            e2.get(),
            e3.get()
        ))
    b1.grid(column=0, row=4, columnspan=2)

    encrypt_text = Text(root, width=40, height=5)
    encrypt_text.grid(column=0, row=5, columnspan=2)

    # Spacer
    Label(root, text='  ').grid(column=2, row=1)

    # Decrypt
    l4 = Label(root, text='Message:')
    l4.grid(column=3, row=1)

    e4 = Entry(root, width=30)
    e4.grid(column=4, row=1)

    l5 = Label(root, text=' Method:')
    l5.grid(column=3, row=2)

    e5 = Entry(root, width=30)
    e5.grid(column=4, row=2)

    l6 = Label(root, text=' Password:')
    l6.grid(column=3, row=3)

    e6 = Entry(root, width=30)
    e6.grid(column=4, row=3)

    b2 = Button(
        root,
        text='Decrypt',
        width=20,
        command=lambda: decrypt(
            e4.get(),
            e5.get(),
            e6.get()
        ))
    b2.grid(column=3, row=4, columnspan=2)

    decrypt_text = Text(root, width=40, height=5)
    decrypt_text.grid(column=3, row=5, columnspan=2)

    # End
    B1 = Button(root, text='Quit', width=40, command=root.quit)
    B1.grid(column=0, row=6, columnspan=2)

    B2 = Button(
        root,
        text='Clear',
        width=40,
        command=lambda: [
            e1.delete(0, 'end'),
            e2.delete(0, 'end'),
            e3.delete(0, 'end'),
            e4.delete(0, 'end'),
            encrypt_text.delete('1.0', 'end'),
            decrypt_text.delete('1.0', 'end')
        ])
    B2.grid(column=3, row=6, columnspan=2)
    log('Elements inited successfully.')
    root.mainloop()


if __name__ == '__main__':
    initLog()
    main()
    log('Program exited successfully.')
