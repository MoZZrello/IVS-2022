# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mockup_calculator_5mxYCVJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class window_calc(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(244, 490)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"Calculator_logo_blue.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTipDuration(-15)
        MainWindow.setStyleSheet(u"background-color:rgb(34, 40, 49);")
        self.actionMarek_3pirka = QAction(MainWindow)
        self.actionMarek_3pirka.setObjectName(u"actionMarek_3pirka")
        self.actionMarek_3pirka.setMenuRole(QAction.AboutRole)
        self.actionKate_ina_Lojdov = QAction(MainWindow)
        self.actionKate_ina_Lojdov.setObjectName(u"actionKate_ina_Lojdov")
        self.actionAndrea_Michl_kov = QAction(MainWindow)
        self.actionAndrea_Michl_kov.setObjectName(u"actionAndrea_Michl_kov")
        self.actionRichard = QAction(MainWindow)
        self.actionRichard.setObjectName(u"actionRichard")
        self.actionZad_v_n_seln_ch_hodnot = QAction(MainWindow)
        self.actionZad_v_n_seln_ch_hodnot.setObjectName(u"actionZad_v_n_seln_ch_hodnot")
        self.actionC_sma_e_cel_dek = QAction(MainWindow)
        self.actionC_sma_e_cel_dek.setObjectName(u"actionC_sma_e_cel_dek")
        self.action_sma_e_jeden_zadan_znak = QAction(MainWindow)
        self.action_sma_e_jeden_zadan_znak.setObjectName(u"action_sma_e_jeden_zadan_znak")
        self.action_se_te_dv_hodnoty = QAction(MainWindow)
        self.action_se_te_dv_hodnoty.setObjectName(u"action_se_te_dv_hodnoty")
        self.action_ode_te_dv_hodnoty = QAction(MainWindow)
        self.action_ode_te_dv_hodnoty.setObjectName(u"action_ode_te_dv_hodnoty")
        self.actionx_vyn_sob_dv_hodnoty = QAction(MainWindow)
        self.actionx_vyn_sob_dv_hodnoty.setObjectName(u"actionx_vyn_sob_dv_hodnoty")
        self.action_vyd_l_dv_hodnoty = QAction(MainWindow)
        self.action_vyd_l_dv_hodnoty.setObjectName(u"action_vyd_l_dv_hodnoty")
        self.action_prvn_hodnotu_umocn_na_druhou_zadanou_hodnotu = QAction(MainWindow)
        self.action_prvn_hodnotu_umocn_na_druhou_zadanou_hodnotu.setObjectName(u"action_prvn_hodnotu_umocn_na_druhou_zadanou_hodnotu")
        self.action_obecn_odmocnina = QAction(MainWindow)
        self.action_obecn_odmocnina.setObjectName(u"action_obecn_odmocnina")
        self.action_faktori_l = QAction(MainWindow)
        self.action_faktori_l.setObjectName(u"action_faktori_l")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.button_delete = QPushButton(self.centralwidget)
        self.button_delete.setObjectName(u"button_delete")
        self.button_delete.setGeometry(QRect(183, 106, 61, 61))
        font = QFont()
        font.setFamily(u"Microsoft YaHei UI")
        font.setPointSize(14)
        self.button_delete.setFont(font)
        self.button_delete.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"background-color:rgb(80, 87, 99);\n"
"border-style:none\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color:rgb(0,0,0);\n"
"background-color:rgb(149, 153, 160);\n"
"}")
        self.display_bottom = QLabel(self.centralwidget)
        self.display_bottom.setObjectName(u"display_bottom")
        self.display_bottom.setGeometry(QRect(0, 41, 244, 61))
        font1 = QFont()
        font1.setFamily(u"Microsoft YaHei UI")
        font1.setPointSize(24)
        self.display_bottom.setFont(font1)
        self.display_bottom.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.display_bottom.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)
        self.display_bottom.setMargin(10)
        self.button_clear_all = QPushButton(self.centralwidget)
        self.button_clear_all.setObjectName(u"button_clear_all")
        self.button_clear_all.setGeometry(QRect(122, 106, 61, 61))
        font2 = QFont()
        font2.setFamily(u"Microsoft YaHei UI")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setWeight(50)
        self.button_clear_all.setFont(font2)
        self.button_clear_all.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"background-color:rgb(80, 87, 99);\n"
"border-style:none\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color:rgb(0,0,0);\n"
"background-color:rgb(149, 153, 160);\n"
"}")
        self.button_number_six = QPushButton(self.centralwidget)
        self.button_number_six.setObjectName(u"button_number_six")
        self.button_number_six.setGeometry(QRect(122, 289, 61, 61))
        self.button_number_six.setFont(font2)
        self.button_number_six.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"border-style:none\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color:rgb(0,0,0);\n"
"background-color:rgb(149, 153, 160);\n"
"}")
        self.button_number_five = QPushButton(self.centralwidget)
        self.button_number_five.setObjectName(u"button_number_five")
        self.button_number_five.setGeometry(QRect(61, 289, 61, 61))
        self.button_number_five.setFont(font2)
        self.button_number_five.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"border-style:none\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color:rgb(0,0,0);\n"
"background-color:rgb(149, 153, 160);\n"
"}")
        self.button_exponent = QPushButton(self.centralwidget)
        self.button_exponent.setObjectName(u"button_exponent")
        self.button_exponent.setGeometry(QRect(61, 106, 61, 61))
        self.button_exponent.setFont(font)
        self.button_exponent.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"background-color:rgb(80, 87, 99);\n"
"border-style:none\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color:rgb(0,0,0);\n"
"background-color:rgb(149, 153, 160);\n"
"}")
        self.button_decimal = QPushButton(self.centralwidget)
        self.button_decimal.setObjectName(u"button_decimal")
        self.button_decimal.setGeometry(QRect(0, 411, 61, 61))
        font3 = QFont()
        font3.setFamily(u"Microsoft YaHei UI")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.button_decimal.setFont(font3)
        self.button_decimal.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"border-style:none\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color:rgb(0,0,0);\n"
"background-color:rgb(149, 153, 160);\n"
"}")
        self.button_number_zero = QPushButton(self.centralwidget)
        self.button_number_zero.setObjectName(u"button_number_zero")
        self.button_number_zero.setGeometry(QRect(61, 411, 61, 61))
        font4 = QFont()
        font4.setFamily(u"Microsoft JhengHei UI")
        font4.setPointSize(14)
        font4.setBold(False)
        font4.setWeight(50)
        self.button_number_zero.setFont(font4)
        self.button_number_zero.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"border-style:none\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color:rgb(0,0,0);\n"
"background-color:rgb(149, 153, 160);\n"
"}")
        self.button_equal = QPushButton(self.centralwidget)
        self.button_equal.setObjectName(u"button_equal")
        self.button_equal.setGeometry(QRect(183, 411, 61, 61))
        self.button_equal.setFont(font2)
        self.button_equal.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"background-color:rgb(0, 196, 206);\n"
"border-style:none\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color:rgb(0,0,0);\n"
"background-color:rgb(107, 233, 239);\n"
"}")
        self.button_multiply = QPushButton(self.centralwidget)
        self.button_multiply.setObjectName(u"button_multiply")
        self.button_multiply.setGeometry(QRect(183, 228, 61, 61))
        font5 = QFont()
        font5.setFamily(u"Microsoft YaHei UI")
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setWeight(50)
        self.button_multiply.setFont(font5)
        self.button_multiply.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"background-color:rgb(80, 87, 99);\n"
"border-style:none\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color:rgb(0,0,0);\n"
"background-color:rgb(149, 153, 160);\n"
"}")
        self.button_number_seven = QPushButton(self.centralwidget)
        self.button_number_seven.setObjectName(u"button_number_seven")
        self.button_number_seven.setGeometry(QRect(0, 350, 61, 61))
        self.button_number_seven.setFont(font2)
        self.button_number_seven.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"border-style:none\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color:rgb(0,0,0);\n"
"background-color:rgb(149, 153, 160);\n"
"}")
        self.button_number_eight = QPushButton(self.centralwidget)
        self.button_number_eight.setObjectName(u"button_number_eight")
        self.button_number_eight.setGeometry(QRect(61, 350, 61, 61))
        self.button_number_eight.setFont(font2)
        self.button_number_eight.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"border-style:none\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color:rgb(0,0,0);\n"
"background-color:rgb(149, 153, 160);\n"
"}")
        self.button_sub = QPushButton(self.centralwidget)
        self.button_sub.setObjectName(u"button_sub")
        self.button_sub.setGeometry(QRect(183, 289, 61, 61))
        font6 = QFont()
        font6.setFamily(u"Microsoft YaHei UI")
        font6.setPointSize(20)
        font6.setBold(False)
        font6.setWeight(50)
        self.button_sub.setFont(font6)
        self.button_sub.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"background-color:rgb(80, 87, 99);\n"
"border-style:none\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color:rgb(0,0,0);\n"
"background-color:rgb(149, 153, 160);\n"
"}")
        self.button_division = QPushButton(self.centralwidget)
        self.button_division.setObjectName(u"button_division")
        self.button_division.setGeometry(QRect(183, 167, 61, 61))
        self.button_division.setFont(font2)
        self.button_division.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"background-color:rgb(80, 87, 99);\n"
"border-style:none\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color:rgb(0,0,0);\n"
"background-color:rgb(149, 153, 160);\n"
"}")
        self.button_number_nine = QPushButton(self.centralwidget)
        self.button_number_nine.setObjectName(u"button_number_nine")
        self.button_number_nine.setGeometry(QRect(122, 350, 61, 61))
        self.button_number_nine.setFont(font2)
        self.button_number_nine.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"border-style:none\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color:rgb(0,0,0);\n"
"background-color:rgb(149, 153, 160);\n"
"}")
        self.button_number_one = QPushButton(self.centralwidget)
        self.button_number_one.setObjectName(u"button_number_one")
        self.button_number_one.setGeometry(QRect(0, 228, 61, 61))
        self.button_number_one.setFont(font2)
        self.button_number_one.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"border-style:none\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color:rgb(0,0,0);\n"
"background-color:rgb(149, 153, 160);\n"
"}")
        self.button_open = QPushButton(self.centralwidget)
        self.button_open.setObjectName(u"button_open")
        self.button_open.setGeometry(QRect(0, 167, 61, 61))
        self.button_open.setFont(font2)
        self.button_open.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"border-style:none\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color:rgb(0,0,0);\n"
"background-color:rgb(149, 153, 160);\n"
"}")
        self.button_number_four = QPushButton(self.centralwidget)
        self.button_number_four.setObjectName(u"button_number_four")
        self.button_number_four.setGeometry(QRect(0, 289, 61, 61))
        self.button_number_four.setFont(font2)
        self.button_number_four.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"border-style:none\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color:rgb(0,0,0);\n"
"background-color:rgb(149, 153, 160);\n"
"}")
        self.button_close = QPushButton(self.centralwidget)
        self.button_close.setObjectName(u"button_close")
        self.button_close.setGeometry(QRect(61, 167, 61, 61))
        self.button_close.setFont(font2)
        self.button_close.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"border-style:none\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color:rgb(0,0,0);\n"
"background-color:rgb(149, 153, 160);\n"
"}")
        self.button_add = QPushButton(self.centralwidget)
        self.button_add.setObjectName(u"button_add")
        self.button_add.setGeometry(QRect(183, 350, 61, 61))
        self.button_add.setFont(font2)
        self.button_add.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"background-color:rgb(80, 87, 99);\n"
"border-style:none\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color:rgb(0,0,0);\n"
"background-color:rgb(149, 153, 160);\n"
"}")
        self.button_number_two = QPushButton(self.centralwidget)
        self.button_number_two.setObjectName(u"button_number_two")
        self.button_number_two.setGeometry(QRect(61, 228, 61, 61))
        self.button_number_two.setFont(font2)
        self.button_number_two.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"border-style:none\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color:rgb(0,0,0);\n"
"background-color:rgb(149, 153, 160);\n"
"}")
        self.button_factorial = QPushButton(self.centralwidget)
        self.button_factorial.setObjectName(u"button_factorial")
        self.button_factorial.setGeometry(QRect(122, 411, 61, 61))
        self.button_factorial.setFont(font2)
        self.button_factorial.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"border-style:none\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color:rgb(0,0,0);\n"
"background-color:rgb(149, 153, 160);\n"
"}")
        self.button_number_three = QPushButton(self.centralwidget)
        self.button_number_three.setObjectName(u"button_number_three")
        self.button_number_three.setGeometry(QRect(122, 228, 61, 61))
        self.button_number_three.setFont(font2)
        self.button_number_three.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"border-style:none\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color:rgb(0,0,0);\n"
"background-color:rgb(149, 153, 160);\n"
"}")
        self.button_sqrt = QPushButton(self.centralwidget)
        self.button_sqrt.setObjectName(u"button_sqrt")
        self.button_sqrt.setGeometry(QRect(0, 106, 61, 61))
        self.button_sqrt.setFont(font)
        self.button_sqrt.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"background-color:rgb(80, 87, 99);\n"
"border-style:none\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color:rgb(0,0,0);\n"
"background-color:rgb(149, 153, 160);\n"
"}")
        self.display_top = QLabel(self.centralwidget)
        self.display_top.setObjectName(u"display_top")
        self.display_top.setGeometry(QRect(0, 0, 244, 41))
        self.display_top.setFont(font)
        self.display_top.setStyleSheet(u"color: rgb(180, 180, 180);\n"
"")
        self.display_top.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)
        self.display_top.setMargin(5)
        self.button_e = QPushButton(self.centralwidget)
        self.button_e.setObjectName(u"button_e")
        self.button_e.setGeometry(QRect(122, 167, 61, 61))
        self.button_e.setFont(font)
        self.button_e.setStyleSheet(u"QPushButton{\n"
"color:rgb(255,255,255);\n"
"border-style:none\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color:rgb(0,0,0);\n"
"background-color:rgb(149, 153, 160);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 244, 26))
        self.menubar.setStyleSheet(u"QMenuBar{\n"
"color:rgb(255,255,255);\n"
"border-style:none\n"
"}\n"
"\n"
"QMenu:hover{\n"
"color:rgb(0, 0, 0);\n"
"border-style:none\n"
"}")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuHelp.setStyleSheet(u"QMenu{\n"
"color:rgb(255,255,255);\n"
"border-style:none\n"
"}\n"
"\n"
"QMenu:hover{\n"
"color:rgb(0,0,0);\n"
"background-color:rgb(149, 153, 160);\n"
"}")
        self.menuMaz_n_zadan_ch_hodnot = QMenu(self.menuHelp)
        self.menuMaz_n_zadan_ch_hodnot.setObjectName(u"menuMaz_n_zadan_ch_hodnot")
        self.menuMatematick_operace = QMenu(self.menuHelp)
        self.menuMatematick_operace.setObjectName(u"menuMatematick_operace")
        self.menucreators = QMenu(self.menubar)
        self.menucreators.setObjectName(u"menucreators")
        self.menucreators.setStyleSheet(u"QMenu{\n"
"color:rgb(255,255,255);\n"
"border-style:none\n"
"}")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menucreators.menuAction())
        self.menuHelp.addAction(self.menuMatematick_operace.menuAction())
        self.menuHelp.addAction(self.menuMaz_n_zadan_ch_hodnot.menuAction())
        self.menuMaz_n_zadan_ch_hodnot.addAction(self.actionC_sma_e_cel_dek)
        self.menuMaz_n_zadan_ch_hodnot.addAction(self.action_sma_e_jeden_zadan_znak)
        self.menuMatematick_operace.addAction(self.action_se_te_dv_hodnoty)
        self.menuMatematick_operace.addAction(self.action_ode_te_dv_hodnoty)
        self.menuMatematick_operace.addAction(self.actionx_vyn_sob_dv_hodnoty)
        self.menuMatematick_operace.addAction(self.action_vyd_l_dv_hodnoty)
        self.menuMatematick_operace.addAction(self.action_prvn_hodnotu_umocn_na_druhou_zadanou_hodnotu)
        self.menuMatematick_operace.addAction(self.action_obecn_odmocnina)
        self.menuMatematick_operace.addAction(self.action_faktori_l)
        self.menucreators.addAction(self.actionMarek_3pirka)
        self.menucreators.addAction(self.actionKate_ina_Lojdov)
        self.menucreators.addAction(self.actionAndrea_Michl_kov)
        self.menucreators.addAction(self.actionRichard)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CalXO", None))
        self.actionMarek_3pirka.setText(QCoreApplication.translate("MainWindow", u"Marek \u0160pirka", None))
        self.actionKate_ina_Lojdov.setText(QCoreApplication.translate("MainWindow", u"Kate\u0159ina Lojdov\u00e1", None))
        self.actionAndrea_Michl_kov.setText(QCoreApplication.translate("MainWindow", u"Andrea Michl\u00edkov\u00e1", None))
        self.actionRichard.setText(QCoreApplication.translate("MainWindow", u"Richard Harman", None))
        self.actionZad_v_n_seln_ch_hodnot.setText(QCoreApplication.translate("MainWindow", u"Zad\u00e1v\u00e1n\u00ed \u010d\u00edseln\u00fdch hodnot", None))
        self.actionC_sma_e_cel_dek.setText(QCoreApplication.translate("MainWindow", u"C sma\u017ee cel\u00fd \u0159\u00e1dek", None))
        self.action_sma_e_jeden_zadan_znak.setText(QCoreApplication.translate("MainWindow", u"\u232b sma\u017ee jeden zadan\u00fd znak", None))
        self.action_se_te_dv_hodnoty.setText(QCoreApplication.translate("MainWindow", u"+ se\u010dte dv\u011b hodnoty", None))
        self.action_ode_te_dv_hodnoty.setText(QCoreApplication.translate("MainWindow", u"- ode\u010dte dv\u011b hodnoty", None))
        self.actionx_vyn_sob_dv_hodnoty.setText(QCoreApplication.translate("MainWindow", u"x vyn\u00e1sob\u00ed dv\u011b hodnoty", None))
        self.action_vyd_l_dv_hodnoty.setText(QCoreApplication.translate("MainWindow", u"\u00f7 vyd\u011bl\u00ed dv\u011b hodnoty", None))
        self.action_prvn_hodnotu_umocn_na_druhou_zadanou_hodnotu.setText(QCoreApplication.translate("MainWindow", u"^ obecn\u00e1 mocnina", None))
        self.action_obecn_odmocnina.setText(QCoreApplication.translate("MainWindow", u"\u221a obecn\u00e1 odmocnina", None))
        self.action_faktori_l.setText(QCoreApplication.translate("MainWindow", u"! faktori\u00e1l", None))
        self.button_delete.setText(QCoreApplication.translate("MainWindow", u"\u232b", None))
        self.display_bottom.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.button_clear_all.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.button_number_six.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.button_number_five.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.button_exponent.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.button_decimal.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.button_number_zero.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(whatsthis)
        self.button_equal.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p><p><br/></p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.button_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.button_multiply.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.button_number_seven.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.button_number_eight.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.button_sub.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.button_division.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.button_number_nine.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.button_number_one.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.button_open.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.button_number_four.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.button_close.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.button_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.button_number_two.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.button_factorial.setText(QCoreApplication.translate("MainWindow", u"!", None))
        self.button_number_three.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.button_sqrt.setText(QCoreApplication.translate("MainWindow", u"\u221ax", None))
        self.display_top.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.button_e.setText(QCoreApplication.translate("MainWindow", u"e", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuMaz_n_zadan_ch_hodnot.setTitle(QCoreApplication.translate("MainWindow", u"Maz\u00e1n\u00ed zadan\u00fdch hodnot", None))
        self.menuMatematick_operace.setTitle(QCoreApplication.translate("MainWindow", u"Matematick\u00e9 operace", None))
        self.menucreators.setTitle(QCoreApplication.translate("MainWindow", u"Creators", None))
    # retranslateUi

