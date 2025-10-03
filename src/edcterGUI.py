# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edcterGUIgYShlV.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTabWidget, QTextEdit,
    QWidget)

class Ui_root(object):
    def setupUi(self, root):
        if not root.objectName():
            root.setObjectName(u"root")
        root.resize(412, 315)
        self.gridLayoutWidget = QWidget(root)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 411, 311))
        font = QFont()
        font.setFamilies([u"Consolas"])
        self.gridLayoutWidget.setFont(font)
        self.main_layout = QGridLayout(self.gridLayoutWidget)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.exit_button = QPushButton(self.gridLayoutWidget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setFont(font)

        self.main_layout.addWidget(self.exit_button, 1, 1, 1, 1)

        self.clear_button = QPushButton(self.gridLayoutWidget)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setFont(font)

        self.main_layout.addWidget(self.clear_button, 1, 0, 1, 1)

        self.main_tab = QTabWidget(self.gridLayoutWidget)
        self.main_tab.setObjectName(u"main_tab")
        self.main_tab.setFont(font)
        self.encrypt_zone = QWidget()
        self.encrypt_zone.setObjectName(u"encrypt_zone")
        self.gridLayoutWidget_2 = QWidget(self.encrypt_zone)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 0, 381, 241))
        self.gridLayoutWidget_2.setFont(font)
        self.ect_layout = QGridLayout(self.gridLayoutWidget_2)
        self.ect_layout.setObjectName(u"ect_layout")
        self.ect_layout.setContentsMargins(0, 0, 0, 0)
        self.mtd_label1 = QLabel(self.gridLayoutWidget_2)
        self.mtd_label1.setObjectName(u"mtd_label1")
        self.mtd_label1.setFont(font)

        self.ect_layout.addWidget(self.mtd_label1, 1, 0, 1, 1)

        self.psw_label1 = QLabel(self.gridLayoutWidget_2)
        self.psw_label1.setObjectName(u"psw_label1")
        self.psw_label1.setFont(font)

        self.ect_layout.addWidget(self.psw_label1, 2, 0, 1, 1)

        self.mtd_input1 = QLineEdit(self.gridLayoutWidget_2)
        self.mtd_input1.setObjectName(u"mtd_input1")
        self.mtd_input1.setFont(font)

        self.ect_layout.addWidget(self.mtd_input1, 1, 1, 1, 1)

        self.msg_label1 = QLabel(self.gridLayoutWidget_2)
        self.msg_label1.setObjectName(u"msg_label1")
        self.msg_label1.setFont(font)

        self.ect_layout.addWidget(self.msg_label1, 0, 0, 1, 1)

        self.msg_input1 = QLineEdit(self.gridLayoutWidget_2)
        self.msg_input1.setObjectName(u"msg_input1")
        self.msg_input1.setFont(font)

        self.ect_layout.addWidget(self.msg_input1, 0, 1, 1, 1)

        self.psw_input1 = QLineEdit(self.gridLayoutWidget_2)
        self.psw_input1.setObjectName(u"psw_input1")
        self.psw_input1.setFont(font)

        self.ect_layout.addWidget(self.psw_input1, 2, 1, 1, 1)

        self.out_text1 = QTextEdit(self.gridLayoutWidget_2)
        self.out_text1.setObjectName(u"out_text1")
        self.out_text1.setFont(font)

        self.ect_layout.addWidget(self.out_text1, 3, 1, 1, 1)

        self.out_label1 = QLabel(self.gridLayoutWidget_2)
        self.out_label1.setObjectName(u"out_label1")
        self.out_label1.setFont(font)

        self.ect_layout.addWidget(self.out_label1, 3, 0, 1, 1)

        self.encrypt_button = QPushButton(self.gridLayoutWidget_2)
        self.encrypt_button.setObjectName(u"encrypt_button")
        self.encrypt_button.setFont(font)

        self.ect_layout.addWidget(self.encrypt_button, 4, 0, 1, 2)

        self.main_tab.addTab(self.encrypt_zone, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayoutWidget_3 = QWidget(self.tab_2)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 0, 381, 241))
        self.dct_layout = QGridLayout(self.gridLayoutWidget_3)
        self.dct_layout.setObjectName(u"dct_layout")
        self.dct_layout.setContentsMargins(0, 0, 0, 0)
        self.mtd_label2 = QLabel(self.gridLayoutWidget_3)
        self.mtd_label2.setObjectName(u"mtd_label2")

        self.dct_layout.addWidget(self.mtd_label2, 1, 0, 1, 1)

        self.psw_label2 = QLabel(self.gridLayoutWidget_3)
        self.psw_label2.setObjectName(u"psw_label2")

        self.dct_layout.addWidget(self.psw_label2, 2, 0, 1, 1)

        self.mtd_input2 = QLineEdit(self.gridLayoutWidget_3)
        self.mtd_input2.setObjectName(u"mtd_input2")

        self.dct_layout.addWidget(self.mtd_input2, 1, 1, 1, 1)

        self.msg_label2 = QLabel(self.gridLayoutWidget_3)
        self.msg_label2.setObjectName(u"msg_label2")

        self.dct_layout.addWidget(self.msg_label2, 0, 0, 1, 1)

        self.msg_input2 = QLineEdit(self.gridLayoutWidget_3)
        self.msg_input2.setObjectName(u"msg_input2")
        self.msg_input2.setFont(font)

        self.dct_layout.addWidget(self.msg_input2, 0, 1, 1, 1)

        self.psw_input2 = QLineEdit(self.gridLayoutWidget_3)
        self.psw_input2.setObjectName(u"psw_input2")

        self.dct_layout.addWidget(self.psw_input2, 2, 1, 1, 1)

        self.out_text2 = QTextEdit(self.gridLayoutWidget_3)
        self.out_text2.setObjectName(u"out_text2")

        self.dct_layout.addWidget(self.out_text2, 3, 1, 1, 1)

        self.out_label2 = QLabel(self.gridLayoutWidget_3)
        self.out_label2.setObjectName(u"out_label2")

        self.dct_layout.addWidget(self.out_label2, 3, 0, 1, 1)

        self.decrypt_button = QPushButton(self.gridLayoutWidget_3)
        self.decrypt_button.setObjectName(u"decrypt_button")

        self.dct_layout.addWidget(self.decrypt_button, 4, 0, 1, 2)

        self.main_tab.addTab(self.tab_2, "")

        self.main_layout.addWidget(self.main_tab, 0, 0, 1, 2)


        self.retranslateUi(root)

        self.main_tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(root)
    # setupUi

    def retranslateUi(self, root):
        root.setWindowTitle(QCoreApplication.translate("root", u"EnDeCrypter v1.0.0", None))
        self.exit_button.setText(QCoreApplication.translate("root", u"\u9000\u51fa", None))
        self.clear_button.setText(QCoreApplication.translate("root", u"\u6e05\u7a7a", None))
#if QT_CONFIG(tooltip)
        self.main_tab.setToolTip(QCoreApplication.translate("root", u"<html><head/><body><p>\u52a0\u5bc6\u533a</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.mtd_label1.setText(QCoreApplication.translate("root", u"\u65b9\u6cd5", None))
        self.psw_label1.setText(QCoreApplication.translate("root", u"\u5bc6\u7801", None))
        self.msg_label1.setText(QCoreApplication.translate("root", u"\u6d88\u606f", None))
        self.out_label1.setText(QCoreApplication.translate("root", u"\u8f93\u51fa", None))
        self.encrypt_button.setText(QCoreApplication.translate("root", u"\u52a0\u5bc6", None))
        self.main_tab.setTabText(self.main_tab.indexOf(self.encrypt_zone), QCoreApplication.translate("root", u"\u52a0\u5bc6\u533a", None))
        self.mtd_label2.setText(QCoreApplication.translate("root", u"\u65b9\u6cd5", None))
        self.psw_label2.setText(QCoreApplication.translate("root", u"\u5bc6\u7801", None))
        self.msg_label2.setText(QCoreApplication.translate("root", u"\u6d88\u606f", None))
        self.out_label2.setText(QCoreApplication.translate("root", u"\u8f93\u51fa", None))
        self.decrypt_button.setText(QCoreApplication.translate("root", u"\u89e3\u5bc6", None))
        self.main_tab.setTabText(self.main_tab.indexOf(self.tab_2), QCoreApplication.translate("root", u"\u89e3\u5bc6\u533a", None))
    # retranslateUi

