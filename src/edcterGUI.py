# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edcterGUIxNFgis.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTabWidget,
    QTextEdit, QToolButton, QWidget)

class Ui_root(object):
    def setupUi(self, root):
        if not root.objectName():
            root.setObjectName(u"root")
        root.resize(412, 336)
        self.gridLayoutWidget = QWidget(root)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 411, 331))
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
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 401, 271))
        self.gridLayoutWidget_2.setFont(font)
        self.ect_layout = QGridLayout(self.gridLayoutWidget_2)
        self.ect_layout.setObjectName(u"ect_layout")
        self.ect_layout.setContentsMargins(0, 0, 0, 0)
        self.mtd_label1 = QLabel(self.gridLayoutWidget_2)
        self.mtd_label1.setObjectName(u"mtd_label1")
        self.mtd_label1.setFont(font)

        self.ect_layout.addWidget(self.mtd_label1, 1, 0, 1, 1)

        self.out_label1 = QLabel(self.gridLayoutWidget_2)
        self.out_label1.setObjectName(u"out_label1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out_label1.sizePolicy().hasHeightForWidth())
        self.out_label1.setSizePolicy(sizePolicy)
        self.out_label1.setFont(font)

        self.ect_layout.addWidget(self.out_label1, 4, 0, 1, 1)

        self.msg_label1 = QLabel(self.gridLayoutWidget_2)
        self.msg_label1.setObjectName(u"msg_label1")
        self.msg_label1.setFont(font)

        self.ect_layout.addWidget(self.msg_label1, 0, 0, 1, 1)

        self.mtd_input1 = QLineEdit(self.gridLayoutWidget_2)
        self.mtd_input1.setObjectName(u"mtd_input1")
        self.mtd_input1.setFont(font)

        self.ect_layout.addWidget(self.mtd_input1, 1, 1, 1, 2)

        self.out_text1 = QTextEdit(self.gridLayoutWidget_2)
        self.out_text1.setObjectName(u"out_text1")
        self.out_text1.setFont(font)

        self.ect_layout.addWidget(self.out_text1, 4, 1, 1, 2)

        self.msg_input1 = QLineEdit(self.gridLayoutWidget_2)
        self.msg_input1.setObjectName(u"msg_input1")
        self.msg_input1.setFont(font)

        self.ect_layout.addWidget(self.msg_input1, 0, 1, 1, 2)

        self.psw_label1 = QLabel(self.gridLayoutWidget_2)
        self.psw_label1.setObjectName(u"psw_label1")
        self.psw_label1.setFont(font)

        self.ect_layout.addWidget(self.psw_label1, 3, 0, 1, 1)

        self.mtdFile1 = QGroupBox(self.gridLayoutWidget_2)
        self.mtdFile1.setObjectName(u"mtdFile1")
        self.mtdFile1.setMinimumSize(QSize(0, 20))
        self.mtdFile1.setBaseSize(QSize(0, 20))
        self.mtdFile1.setAutoFillBackground(False)
        self.gridLayoutWidget_4 = QWidget(self.mtdFile1)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(-1, -1, 401, 25))
        self.mtd_layout1 = QGridLayout(self.gridLayoutWidget_4)
        self.mtd_layout1.setObjectName(u"mtd_layout1")
        self.mtd_layout1.setContentsMargins(0, 0, 0, 0)
        self.mtdLoad_button1 = QPushButton(self.gridLayoutWidget_4)
        self.mtdLoad_button1.setObjectName(u"mtdLoad_button1")

        self.mtd_layout1.addWidget(self.mtdLoad_button1, 0, 0, 1, 1)

        self.mtdSave_button1 = QPushButton(self.gridLayoutWidget_4)
        self.mtdSave_button1.setObjectName(u"mtdSave_button1")

        self.mtd_layout1.addWidget(self.mtdSave_button1, 0, 1, 1, 1)


        self.ect_layout.addWidget(self.mtdFile1, 2, 0, 1, 3)

        self.encrypt_button = QPushButton(self.gridLayoutWidget_2)
        self.encrypt_button.setObjectName(u"encrypt_button")
        self.encrypt_button.setFont(font)

        self.ect_layout.addWidget(self.encrypt_button, 5, 0, 1, 3)

        self.psw_input1 = QLineEdit(self.gridLayoutWidget_2)
        self.psw_input1.setObjectName(u"psw_input1")
        self.psw_input1.setFont(font)

        self.ect_layout.addWidget(self.psw_input1, 3, 1, 1, 1)

        self.pswToggle_button2_2 = QToolButton(self.gridLayoutWidget_2)
        self.pswToggle_button2_2.setObjectName(u"pswToggle_button2_2")
        icon = QIcon()
        icon.addFile(u"../../images/disabled.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u"../../images/enabled.ico", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pswToggle_button2_2.setIcon(icon)

        self.ect_layout.addWidget(self.pswToggle_button2_2, 3, 2, 1, 1)

        self.mtd_label1.raise_()
        self.mtd_input1.raise_()
        self.msg_label1.raise_()
        self.msg_input1.raise_()
        self.out_text1.raise_()
        self.out_label1.raise_()
        self.encrypt_button.raise_()
        self.psw_input1.raise_()
        self.psw_label1.raise_()
        self.mtdFile1.raise_()
        self.pswToggle_button2_2.raise_()
        self.main_tab.addTab(self.encrypt_zone, "")
        self.decrypt_zone = QWidget()
        self.decrypt_zone.setObjectName(u"decrypt_zone")
        self.gridLayoutWidget_3 = QWidget(self.decrypt_zone)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 0, 401, 271))
        self.dct_layout = QGridLayout(self.gridLayoutWidget_3)
        self.dct_layout.setObjectName(u"dct_layout")
        self.dct_layout.setContentsMargins(0, 0, 0, 0)
        self.out_label2 = QLabel(self.gridLayoutWidget_3)
        self.out_label2.setObjectName(u"out_label2")

        self.dct_layout.addWidget(self.out_label2, 4, 0, 1, 1)

        self.mtd_label2 = QLabel(self.gridLayoutWidget_3)
        self.mtd_label2.setObjectName(u"mtd_label2")

        self.dct_layout.addWidget(self.mtd_label2, 1, 0, 1, 1)

        self.psw_input2 = QLineEdit(self.gridLayoutWidget_3)
        self.psw_input2.setObjectName(u"psw_input2")

        self.dct_layout.addWidget(self.psw_input2, 3, 1, 1, 1)

        self.psw_label2 = QLabel(self.gridLayoutWidget_3)
        self.psw_label2.setObjectName(u"psw_label2")

        self.dct_layout.addWidget(self.psw_label2, 3, 0, 1, 1)

        self.msg_label2 = QLabel(self.gridLayoutWidget_3)
        self.msg_label2.setObjectName(u"msg_label2")

        self.dct_layout.addWidget(self.msg_label2, 0, 0, 1, 1)

        self.pswToggle_button2 = QToolButton(self.gridLayoutWidget_3)
        self.pswToggle_button2.setObjectName(u"pswToggle_button2")
        self.pswToggle_button2.setIcon(icon)

        self.dct_layout.addWidget(self.pswToggle_button2, 3, 2, 1, 1)

        self.msg_input2 = QLineEdit(self.gridLayoutWidget_3)
        self.msg_input2.setObjectName(u"msg_input2")
        self.msg_input2.setFont(font)

        self.dct_layout.addWidget(self.msg_input2, 0, 1, 1, 2)

        self.mtd_input2 = QLineEdit(self.gridLayoutWidget_3)
        self.mtd_input2.setObjectName(u"mtd_input2")

        self.dct_layout.addWidget(self.mtd_input2, 1, 1, 1, 2)

        self.mtdFile2 = QGroupBox(self.gridLayoutWidget_3)
        self.mtdFile2.setObjectName(u"mtdFile2")
        self.mtdFile2.setMinimumSize(QSize(0, 20))
        self.mtdFile2.setBaseSize(QSize(0, 20))
        self.mtdFile2.setAutoFillBackground(False)
        self.gridLayoutWidget_5 = QWidget(self.mtdFile2)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(-1, -1, 401, 25))
        self.mtd_layout2 = QGridLayout(self.gridLayoutWidget_5)
        self.mtd_layout2.setObjectName(u"mtd_layout2")
        self.mtd_layout2.setContentsMargins(0, 0, 0, 0)
        self.mtdLoad_button2 = QPushButton(self.gridLayoutWidget_5)
        self.mtdLoad_button2.setObjectName(u"mtdLoad_button2")

        self.mtd_layout2.addWidget(self.mtdLoad_button2, 0, 0, 1, 1)

        self.mtdSave_button2 = QPushButton(self.gridLayoutWidget_5)
        self.mtdSave_button2.setObjectName(u"mtdSave_button2")

        self.mtd_layout2.addWidget(self.mtdSave_button2, 0, 1, 1, 1)


        self.dct_layout.addWidget(self.mtdFile2, 2, 0, 1, 3)

        self.out_text2 = QTextEdit(self.gridLayoutWidget_3)
        self.out_text2.setObjectName(u"out_text2")

        self.dct_layout.addWidget(self.out_text2, 4, 1, 1, 2)

        self.decrypt_button = QPushButton(self.gridLayoutWidget_3)
        self.decrypt_button.setObjectName(u"decrypt_button")

        self.dct_layout.addWidget(self.decrypt_button, 5, 0, 1, 3)

        self.main_tab.addTab(self.decrypt_zone, "")

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
        self.main_tab.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.encrypt_zone.setToolTip(QCoreApplication.translate("root", u"<html><head/><body><p>\u52a0\u5bc6\u533a</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.mtd_label1.setText(QCoreApplication.translate("root", u"\u65b9\u6cd5", None))
        self.out_label1.setText(QCoreApplication.translate("root", u"\u8f93\u51fa", None))
        self.msg_label1.setText(QCoreApplication.translate("root", u"\u6d88\u606f", None))
        self.psw_label1.setText(QCoreApplication.translate("root", u"\u5bc6\u7801", None))
        self.mtdFile1.setTitle("")
        self.mtdLoad_button1.setText(QCoreApplication.translate("root", u"\u52a0\u8f7d\u73b0\u6709\u65b9\u6cd5\u6587\u4ef6", None))
        self.mtdSave_button1.setText(QCoreApplication.translate("root", u"\u4fdd\u5b58\u5f53\u524d\u65b9\u6cd5", None))
        self.encrypt_button.setText(QCoreApplication.translate("root", u"\u52a0\u5bc6", None))
        self.pswToggle_button2_2.setText(QCoreApplication.translate("root", u"\u5207\u6362\u5bc6\u7801\u53ef\u89c1\u6027", None))
        self.main_tab.setTabText(self.main_tab.indexOf(self.encrypt_zone), QCoreApplication.translate("root", u"\u52a0\u5bc6\u533a", None))
#if QT_CONFIG(tooltip)
        self.decrypt_zone.setToolTip(QCoreApplication.translate("root", u"<html><head/><body><p>\u89e3\u5bc6\u533a</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.out_label2.setText(QCoreApplication.translate("root", u"\u8f93\u51fa", None))
        self.mtd_label2.setText(QCoreApplication.translate("root", u"\u65b9\u6cd5", None))
        self.psw_label2.setText(QCoreApplication.translate("root", u"\u5bc6\u7801", None))
        self.msg_label2.setText(QCoreApplication.translate("root", u"\u6d88\u606f", None))
        self.pswToggle_button2.setText(QCoreApplication.translate("root", u"\u5207\u6362\u5bc6\u7801\u53ef\u89c1\u6027", None))
        self.mtdFile2.setTitle("")
        self.mtdLoad_button2.setText(QCoreApplication.translate("root", u"\u52a0\u8f7d\u73b0\u6709\u65b9\u6cd5\u6587\u4ef6", None))
        self.mtdSave_button2.setText(QCoreApplication.translate("root", u"\u4fdd\u5b58\u5f53\u524d\u65b9\u6cd5", None))
        self.decrypt_button.setText(QCoreApplication.translate("root", u"\u89e3\u5bc6", None))
        self.main_tab.setTabText(self.main_tab.indexOf(self.decrypt_zone), QCoreApplication.translate("root", u"\u89e3\u5bc6\u533a", None))
    # retranslateUi

