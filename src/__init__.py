"""
This is my first time to carefully write a docstring.
This is a module to provide users with self-define message en(de)crypt tool.
There are 3 functions to encrypt messages, and I will make another three to decrypt messages.
...
"""
import sys
from pathlib import Path
from datetime import datetime
from time import time
from edcterGUI import Ui_root
from random import choice
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLineEdit
from PySide6.QtWidgets import QMessageBox

showwarning = QMessageBox.warning
asksave = QFileDialog.getSaveFileName
askload = QFileDialog.getOpenFileName

__version__ = '1.1.1'
METHODS = ['A', 'B', 'C']
CHOICE_STR = 'qwe!@#$%&我你他的人了和着过的得地之乎者也如果那么*rtyudylgfshjsajkaSIGOGAIBIUTGUVCUDW^&MUYSiopASD[]{}()FGHJKL++--**|||@*#&@*uhuu|}{[]||///1123817212345678900987654321}'
START: float = time()
rootPath = Path(__file__).parent
if '-D' in sys.argv or '--debug' in sys.argv:
    _DEBUG_MODE = True
else:
    _DEBUG_MODE = False

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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_root()
        self.ui.setupUi(self)
        self.setWindowTitle('EnDeCrypter v' + __version__)

        self.ui.mtdSave_button1.clicked.connect(lambda: self.saveMethod(self.ui.mtd_input1))
        self.ui.mtdLoad_button1.clicked.connect(lambda: self.loadMethod(self.ui.mtd_input1))

        self.ui.mtdSave_button2.clicked.connect(lambda: self.saveMethod(self.ui.mtd_input2))
        self.ui.mtdLoad_button2.clicked.connect(lambda: self.loadMethod(self.ui.mtd_input2))

        self.ui.encrypt_button.clicked.connect(
            lambda: self.encrypt(
                self.ui.msg_input1.text(),
                self.ui.mtd_input1.text(),
                self.ui.psw_input1.text()
                )
            )
        
        self.ui.decrypt_button.clicked.connect(
            lambda: self.decrypt(
                self.ui.msg_input2.text(),
                self.ui.mtd_input2.text(),
                self.ui.psw_input2.text()
                )
            )
        self.ui.exit_button.clicked.connect(sys.exit)

    def saveMethod(self, box):
        filepath, _ = asksave(None, "保存当前方法","","方法 (*.mtd)")
        if filepath:
            with open(filepath, 'w', encoding='utf-8') as file:
                mtd = box.text()
                if not self._check_method(mtd):
                    showwarning(None, '错误', '非法的方法（错误代码：0x000001）')
                    return
                file.write(mtd)

    def loadMethod(self,box):
        filepath, _ = askload(None, "从文件加载方法","","方法 (*.mtd)")
        if filepath:
            box.clear()
            with open(filepath, 'r', encoding='utf-8') as file:
                mtd = file.read()
                if not self._check_method(mtd):
                    showwarning(None, '错误', '非法的方法（错误代码：0x000001）')
                    return
                box.setText(mtd)

    def A_Z_swap(self, message: str):
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

    def B_insert(self, message: str):
        '''A function to insert random characters to strings.
        >>> B_insert('12345678')[::2]
        '12345678'
        >>> B_insert('abcdefgh')[::2]
        'abcdefgh'
        '''
        l1 = list(message)
        l2 = []
        for i in l1:
            l2.append(i)
            l2.append(choice(CHOICE_STR))
        return ''.join(l2)

    def Y_rstrip(self, message: str):
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

    def C_X_reverse(self, message: str):
        '''A function to reverse strings.
        >>> C_X_reverse('12345678')
        '87654321'
        >>> C_X_reverse('abcdefgh')
        'hgfedcba'
        '''
        return ''.join(reversed(list(message)))

    def Password(self, message: str, password: str):
        '''A function to encrypy strings with given password.'''
        if not self._check_password(password):
            showwarning(None, '错误', '非法的密码（错误代码：0x000002）')
            raise ValueError
        pw = (int(password) % 32)**2 % 11
        new = f'{pw:02d}'[0]
        for i in message:
            if i.isalpha():
                new += '-'
                new += chr(ord(i)-pw)
            elif i.isdigit():
                new += '+'
                new += chr(ord(i)+pw)
            else:
                new += '|'
                new += i
        new += f'{pw:02d}'[1]
        return new

    def passworD(self, message: str, password: str):
        '''A function to decrypy strings with given password.'''
        if not self._check_password(password):
            showwarning(None, '错误', '非法的密码（错误代码：0x000002）')
            raise ValueError
        pw = (int(password) % 32)**2 % 11
        wp = int(message[0]+message[-1])
        if (pw != wp):
            showwarning(None, '错误', '解密失败（错误代码：0x000003）')
            raise ValueError
        message = message[1:-1]
        new = ''
        for i in range(0, len(message), 2):
            match message[i]:
                case '-':
                    new += chr(ord(message[i+1])+pw)
                case '+':
                    new += chr(ord(message[i+1])-pw)
                case _:
                    new += message[i+1]
        return new

    def _check_method(self, s: str):
        for i in s.upper():
            if i not in METHODS:
                return False
        return True

    def _check_password(self, s: str):
        try:
            int(s)
        except ValueError:
            return False
        else:
            return True

    def encrypt(self, message: str, method: str, password: str):
        self.ui.out_text1.clear()
        message = message.replace(' ', '·')

        if not self._check_method(method):
            showwarning(None, '错误', '非法的方法（错误代码：0x000001）')
            return
        try:
            message = self.Password(message, password)
        except ValueError:
            return

        for i in method.upper():
            if i == 'A':
                message = self.A_Z_swap(message)
            elif i == 'B':
                message = self.B_insert(message)
            elif i == 'C':
                message = self.C_X_reverse(message)
        self.ui.out_text1.setPlainText(message)

    def decrypt(self, message: str, method: str, password: str):
        self.ui.out_text2.clear()
        message = message.replace('·', ' ')
        if not self._check_method(method):
            showwarning(None, '错误', '非法的方法（错误代码：0x000001）')
            return

        for i in reversed(method.upper()):
            if i == 'A':
                message = self.A_Z_swap(message)
            elif i == 'B':
                message = self.Y_rstrip(message)
            elif i == 'C':
                message = self.C_X_reverse(message)
        try:
            message = self.passworD(message, password)
        except ValueError:
            return
        self.ui.out_text2.setPlainText(message)


if __name__ == '__main__':
    initLog()
    app = QApplication(sys.argv) #type:ignore
    window = MainWindow()
    window.show()
    app.exec()
    log('程序成功退出')
