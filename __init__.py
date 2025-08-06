"""
This is my first time to carefully write a docstring.
This is a module to provide users with self-define message en(de)crypt tool.
There are 3 functions to encrypt messages, and I will make another three to decrypt messages.
...
"""
from random import choice
from tkinter import Tk, Label, Button, Entry, Text
from tkinter.messagebox import showwarning
from time import time, strftime
from pathlib import Path

__version__ = '0.3.0'
METHODS = ['A', 'B', 'C']
CHOICE_STR = 'qwe!@#$%&我你他的人了和着过的得地之乎者也如果那么*rtyudylgfshjsajkaSIGOGAIBIUTGUVCUDW^&MUYSiopASD[]{}()FGHJKL'
START = time()
_root_path = Path(__file__).parent


def init_log():
    with open(_root_path / 'logs.log', 'w+') as f:
        f.write(
            f'{strftime("%Y-%m-%d %H:%M:%S")}\nEnDeCrypter v{__version__} started.\n')


def log(s: str, level='info'):
    with open('logs.log', 'a') as f:
        f.write(f'[{(time()-START)*1000}ms][{level.upper()}] {s}\n')


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
        l2.append(choice(CHOICE_STR))
    return ''.join(l2)


def Y_rstrip(message: str):
    l = []
    for i in range(0, len(message), 2):
        l.append(message[i])
    return ''.join(l)


def C_X_reverse(message: str):
    return ''.join(reversed(list(message)))


def Password(message: str, password: str):
    if not _check_password(password):
        showwarning('Warning', 'Invalid password')
        raise ValueError('Invalid password')
    pw = int(password) % 32
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
    message = ''.join(l)
    return message


def passworD(message: str, password: str):
    if not _check_password(password):
        showwarning('Warning', 'Invalid password')
        raise ValueError('Invalid password')
    pw = int(password) % 32
    l = list(message)
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
    try:
        message = Password(message, password)
    except ValueError:
        return

    for i in reversed(method.upper()):
        if i == 'A':
            message = A_Z_swap(message)
        elif i == 'B':
            message = Y_rstrip(message)
        elif i == 'C':
            message = C_X_reverse(message)
    decrypt_text.insert('end', message)


def main():
    init_log()
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
    log(f'Elements created successfully.')
    root.mainloop()


if __name__ == '__main__':
    main()
    log('Program exited successfully.')
