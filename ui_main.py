# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QDateEdit, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSplitter, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QTimeEdit, QToolBox, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1056, 584)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"\n"
"border:none;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_container = QFrame(self.centralwidget)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setMaximumSize(QSize(200, 520))
        self.left_container.setStyleSheet(u"background-color:rgb(242, 158, 207);\n"
"border-top-left-radius:50px;\n"
"")
        self.left_container.setFrameShape(QFrame.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.left_container)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(160, 16777215))
        self.frame.setLayoutDirection(Qt.RightToLeft)
        self.frame.setStyleSheet(u"border-top-left-radius:100px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color:rgb(255,255,255)")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(239, 25, 172);\n"
"\n"
"}\n"
"\n"
"QToolBox{\n"
"	text-align: left;\n"
"	background-color: rgb(239, 25, 172);\n"
"	color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(239, 25, 172);\n"
"	text-align: left;\n"
"    color:rgb(255, 255, 255)\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 0, 0, 0)
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(255, 85, 255);\n"
"	border-top-left-radius: 15px;\n"
"}\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 173, 402))
        self.page.setStyleSheet(u"background-color:rgb(242, 158, 207);")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(100, 32))
        self.btn_home.setMaximumSize(QSize(170, 16777215))
        self.btn_home.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_home.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 85, 255);\n"
"	border-top-left-radius: 15px;\n"
"}\n"
"QPushButton{\n"
"	font: 700 12pt \"Times New Roman\";\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/img/7911202.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon)
        self.btn_home.setIconSize(QSize(42, 42))

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_cadastro = QPushButton(self.page)
        self.btn_cadastro.setObjectName(u"btn_cadastro")
        self.btn_cadastro.setMinimumSize(QSize(100, 32))
        self.btn_cadastro.setMaximumSize(QSize(170, 16777215))
        self.btn_cadastro.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_cadastro.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 85, 255);\n"
"	border-top-left-radius: 15px;\n"
"}\n"
"QPushButton{\n"
"	font: 700 12pt \"Times New Roman\";\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/img/m001t0324_e_19aug22-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastro.setIcon(icon1)
        self.btn_cadastro.setIconSize(QSize(42, 42))

        self.verticalLayout_4.addWidget(self.btn_cadastro)

        self.btn_agenda = QPushButton(self.page)
        self.btn_agenda.setObjectName(u"btn_agenda")
        self.btn_agenda.setMinimumSize(QSize(100, 32))
        self.btn_agenda.setMaximumSize(QSize(170, 16777215))
        self.btn_agenda.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_agenda.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 85, 255);\n"
"	border-top-left-radius: 15px;\n"
"}\n"
"QPushButton{\n"
"	font: 700 12pt \"Times New Roman\";\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/img/calendar-with-checklist-date-schedule-3d-icon-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_agenda.setIcon(icon2)
        self.btn_agenda.setIconSize(QSize(42, 42))

        self.verticalLayout_4.addWidget(self.btn_agenda)

        self.btn_sobre = QPushButton(self.page)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(150, 32))
        self.btn_sobre.setMaximumSize(QSize(170, 16777215))
        self.btn_sobre.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_sobre.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 85, 255);\n"
"	border-top-left-radius: 15px;\n"
"}\n"
"QPushButton{\n"
"	font: 700 12pt \"Times New Roman\";\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/img/m003t0636_c_confution_decision_06oct_22-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sobre.setIcon(icon3)
        self.btn_sobre.setIconSize(QSize(42, 42))
        self.btn_sobre.setAutoDefault(False)

        self.verticalLayout_4.addWidget(self.btn_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        icon4 = QIcon()
        icon4.addFile(u"img/recrutamento.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page, icon4, u"Pagina de Cadastro")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 173, 402))
        self.page_2.setStyleSheet(u"background-color:rgb(242, 158, 207);")
        self.layoutWidget = QWidget(self.page_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 174, 461))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_consulestoque = QPushButton(self.layoutWidget)
        self.btn_consulestoque.setObjectName(u"btn_consulestoque")
        self.btn_consulestoque.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 85, 255);\n"
"	border-top-left-radius: 15px;\n"
"}\n"
"QPushButton{\n"
"	font: 700 12pt \"Times New Roman\";\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"img/estoque-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_consulestoque.setIcon(icon5)
        self.btn_consulestoque.setIconSize(QSize(42, 42))

        self.verticalLayout_7.addWidget(self.btn_consulestoque)

        self.btn_promo = QPushButton(self.layoutWidget)
        self.btn_promo.setObjectName(u"btn_promo")
        self.btn_promo.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 85, 255);\n"
"	border-top-left-radius: 15px;\n"
"}\n"
"QPushButton{\n"
"	font: 700 12pt \"Times New Roman\";\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"img/4925861-social-icon-line-color-gratis-vetor-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_promo.setIcon(icon6)
        self.btn_promo.setIconSize(QSize(32, 32))

        self.verticalLayout_7.addWidget(self.btn_promo)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.toolBox.addItem(self.page_2, icon4, u"Pagina de Monitoramento")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.left_container)

        self.main_c = QFrame(self.centralwidget)
        self.main_c.setObjectName(u"main_c")
        self.main_c.setMaximumSize(QSize(900, 16777215))
        self.main_c.setStyleSheet(u"\n"
"border-bottom-right-radius:100px;")
        self.main_c.setFrameShape(QFrame.StyledPanel)
        self.main_c.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_c)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 9, 9)
        self.top = QFrame(self.main_c)
        self.top.setObjectName(u"top")
        self.top.setMaximumSize(QSize(16777215, 42))
        self.top.setLayoutDirection(Qt.LeftToRight)
        self.top.setStyleSheet(u"background-color: rgb(239, 25, 172);\n"
"\n"
"")
        self.top.setFrameShape(QFrame.StyledPanel)
        self.top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 9, 0)
        self.btn_toogle = QPushButton(self.top)
        self.btn_toogle.setObjectName(u"btn_toogle")
        self.btn_toogle.setMaximumSize(QSize(40, 40))
        self.btn_toogle.setLayoutDirection(Qt.LeftToRight)
        self.btn_toogle.setAutoFillBackground(False)
        self.btn_toogle.setStyleSheet(u"font: 700 12pt \"Times New Roman\";")
        icon7 = QIcon()
        icon7.addFile(u":/icons/img/pngtree-menu-button-3d-icon-render-png-image_6139824.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toogle.setIcon(icon7)
        self.btn_toogle.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.btn_toogle)

        self.label = QLabel(self.top)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.RightToLeft)
        self.label.setStyleSheet(u"font: 700 15pt \"Segoe Print\";\n"
"color: rgb(255,255,255);\n"
"")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.top)

        self.main_frame = QFrame(self.main_c)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setStyleSheet(u"")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.pages = QStackedWidget(self.main_frame)
        self.pages.setObjectName(u"pages")
        self.pages.setGeometry(QRect(0, 0, 851, 511))
        self.pages.setMinimumSize(QSize(0, 0))
        self.pages.setAcceptDrops(False)
        self.pages.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius: 15px;\n"
"	color:#fff\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(243, 243, 243);\n"
"}\n"
"\n"
"")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.pg_home.setStyleSheet(u"border-bottom-right-radius:100px;")
        self.verticalLayout_6 = QVBoxLayout(self.pg_home)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.logo = QLabel(self.pg_home)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(1000, 500))
        self.logo.setStyleSheet(u"image: url(:/icons/pexels-dmitry-zvolskiy-1570807-removebg-preview.png);\n"
"background-color: rgb(239, 156, 205);")
        self.logo.setPixmap(QPixmap(u"img/ab6a617076b030b35aed35e60581c64e-removebg-preview (1).png"))
        self.logo.setScaledContents(True)
        self.logo.setWordWrap(False)
        self.logo.setOpenExternalLinks(False)

        self.verticalLayout_6.addWidget(self.logo)

        self.pages.addWidget(self.pg_home)
        self.pg_cad = QWidget()
        self.pg_cad.setObjectName(u"pg_cad")
        self.pg_cad.setStyleSheet(u"background-color:rgb(242, 158, 207);")
        self.verticalLayout_9 = QVBoxLayout(self.pg_cad)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.pg_cad)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"\n"
"background-color:rgb(242, 158, 207);\n"
"\n"
"\n"
"QComboBox{\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
" 	border-radius:15px;\n"
"\n"
"}\n"
"\n"
"QTextEdit{\n"
"	border-radius:15px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.frame_4 = QFrame(self.tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(7, 0, 801, 101))
        self.frame_4.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.txt_endcadcli = QLineEdit(self.frame_4)
        self.txt_endcadcli.setObjectName(u"txt_endcadcli")
        self.txt_endcadcli.setGeometry(QRect(536, 28, 261, 31))
        self.txt_endcadcli.setAlignment(Qt.AlignCenter)
        self.txt_pescli = QLineEdit(self.frame_4)
        self.txt_pescli.setObjectName(u"txt_pescli")
        self.txt_pescli.setGeometry(QRect(23, 68, 151, 31))
        self.txt_pescli.setAlignment(Qt.AlignCenter)
        self.btn_pescliente = QPushButton(self.frame_4)
        self.btn_pescliente.setObjectName(u"btn_pescliente")
        self.btn_pescliente.setGeometry(QRect(180, 67, 41, 31))
        self.btn_pescliente.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius: 15px;\n"
"	color:#fff\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color:rgb(242, 158, 207);\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u"img/png-transparent-magnifying-glass-of-magnifying-glass-glass-glasses-computer-icons-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pescliente.setIcon(icon8)
        self.btn_pescliente.setIconSize(QSize(32, 32))
        self.btn_inccli = QPushButton(self.frame_4)
        self.btn_inccli.setObjectName(u"btn_inccli")
        self.btn_inccli.setGeometry(QRect(588, 66, 101, 30))
        self.btn_inccli.setMinimumSize(QSize(0, 30))
        self.btn_inccli.setStyleSheet(u"QPushButton:hover{\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius: 15px;\n"
"	color:#fff\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	border-radius: 15px;\n"
"	background-color: rgb(243, 243, 243);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"img/o-homem-d-que-mostra-o-gesto-aprovado-com-verde-mais-assina-sobre-o-fundo-branco-32812036-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_inccli.setIcon(icon9)
        self.btn_inccli.setIconSize(QSize(40, 60))
        self.btn_inccli.setAutoDefault(False)
        self.btn_inccli.setFlat(False)
        self.btn_exccli = QPushButton(self.frame_4)
        self.btn_exccli.setObjectName(u"btn_exccli")
        self.btn_exccli.setGeometry(QRect(705, 66, 91, 30))
        self.btn_exccli.setMinimumSize(QSize(0, 30))
        self.btn_exccli.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	border-radius: 15px;\n"
"	color:#fff\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(243, 243, 243);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"img/unnamed.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exccli.setIcon(icon10)
        self.btn_exccli.setIconSize(QSize(28, 28))
        self.txt_telcadcli = QLineEdit(self.frame_4)
        self.txt_telcadcli.setObjectName(u"txt_telcadcli")
        self.txt_telcadcli.setGeometry(QRect(425, 28, 106, 31))
        self.txt_telcadcli.setAlignment(Qt.AlignCenter)
        self.txt_nomcadcli = QLineEdit(self.frame_4)
        self.txt_nomcadcli.setObjectName(u"txt_nomcadcli")
        self.txt_nomcadcli.setGeometry(QRect(312, 28, 106, 31))
        self.txt_nomcadcli.setStyleSheet(u"")
        self.txt_nomcadcli.setInputMethodHints(Qt.ImhNone)
        self.txt_nomcadcli.setAlignment(Qt.AlignCenter)
        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 10, 131, 20))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(242, 158, 207, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.label_13.setPalette(palette)
        font = QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"font: 20pt \"Onyx\";")
        self.tableWidget_2 = QTableWidget(self.tab)
        if (self.tableWidget_2.columnCount() < 4):
            self.tableWidget_2.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget_2.rowCount() < 1):
            self.tableWidget_2.setRowCount(1)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(0, 2, __qtablewidgetitem7)
        font1 = QFont()
        font1.setKerning(True)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFont(font1);
        self.tableWidget_2.setItem(0, 3, __qtablewidgetitem8)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(20, 100, 791, 351))
        self.tableWidget_2.setStyleSheet(u"\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(148	, 148, 148);\n"
"	color: rgb(252, 252, 252);\n"
"	border-radius: 5px;\n"
"}\n"
"QHeaderView::section3{\n"
"	width: 50px\n"
"}\n"
"")
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.frame_7 = QFrame(self.tab_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(150, 330, 551, 121))
        self.frame_7.setStyleSheet(u"\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.txt_nomcadfun = QLineEdit(self.frame_7)
        self.txt_nomcadfun.setObjectName(u"txt_nomcadfun")
        self.txt_nomcadfun.setGeometry(QRect(12, 40, 130, 31))
        self.txt_nomcadfun.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"\n"
"}")
        self.txt_nomcadfun.setAlignment(Qt.AlignCenter)
        self.txt_endcadfun = QLineEdit(self.frame_7)
        self.txt_endcadfun.setObjectName(u"txt_endcadfun")
        self.txt_endcadfun.setGeometry(QRect(280, 40, 261, 31))
        self.txt_endcadfun.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"\n"
"}")
        self.txt_endcadfun.setAlignment(Qt.AlignCenter)
        self.txt_telcadfun = QLineEdit(self.frame_7)
        self.txt_telcadfun.setObjectName(u"txt_telcadfun")
        self.txt_telcadfun.setGeometry(QRect(147, 40, 129, 31))
        self.txt_telcadfun.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"\n"
"}")
        self.txt_telcadfun.setAlignment(Qt.AlignCenter)
        self.btn_incfun = QPushButton(self.frame_7)
        self.btn_incfun.setObjectName(u"btn_incfun")
        self.btn_incfun.setGeometry(QRect(109, 85, 101, 31))
        self.btn_incfun.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	border-radius: 15px;\n"
"	color:#fff\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(243, 243, 243);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}")
        self.btn_incfun.setIcon(icon9)
        self.btn_incfun.setIconSize(QSize(42, 42))
        self.btn_altfun = QPushButton(self.frame_7)
        self.btn_altfun.setObjectName(u"btn_altfun")
        self.btn_altfun.setGeometry(QRect(229, 85, 100, 30))
        self.btn_altfun.setMinimumSize(QSize(100, 30))
        self.btn_altfun.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	border-radius: 15px;\n"
"	color:#fff\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(243, 243, 243);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"img/pngtree-exchange-vector-icon-png-image_3710708-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_altfun.setIcon(icon11)
        self.btn_altfun.setIconSize(QSize(42, 42))
        self.btn_excfun = QPushButton(self.frame_7)
        self.btn_excfun.setObjectName(u"btn_excfun")
        self.btn_excfun.setGeometry(QRect(349, 85, 100, 30))
        self.btn_excfun.setMinimumSize(QSize(100, 30))
        self.btn_excfun.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	border-radius: 15px;\n"
"	color:#fff\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(243, 243, 243);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}")
        self.btn_excfun.setIcon(icon10)
        self.btn_excfun.setIconSize(QSize(32, 32))
        self.tableWidget = QTableWidget(self.tab_2)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setBackground(QColor(85, 255, 255));
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem11.setBackground(QColor(85, 255, 255));
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem12.setBackground(QColor(85, 255, 255));
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(0, 1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(0, 2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(0, 3, __qtablewidgetitem17)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(3, 33, 811, 331))
        self.tableWidget.setContextMenuPolicy(Qt.PreventContextMenu)
        self.tableWidget.setStyleSheet(u"\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(148	, 148, 148);\n"
"	color: rgb(252, 252, 252);\n"
"	border-radius: 5px;\n"
"\n"
"}\n"
"")
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setDragDropOverwriteMode(True)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 10, 221, 20))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.label_12.setPalette(palette1)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"font: 20pt \"Onyx\";")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_9.addWidget(self.tabWidget)

        self.pages.addWidget(self.pg_cad)
        self.pg_agend = QWidget()
        self.pg_agend.setObjectName(u"pg_agend")
        self.pg_agend.setStyleSheet(u"background-color: rgb(229, 229, 229);")
        self.frame_5 = QFrame(self.pg_agend)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(9, 9, 871, 231))
        self.frame_5.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"\n"
"}\n"
"QTextEdit{\n"
"\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QDateTimeEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.txt_nomage = QLineEdit(self.frame_5)
        self.txt_nomage.setObjectName(u"txt_nomage")
        self.txt_nomage.setGeometry(QRect(309, 5, 231, 31))
        self.txt_nomage.setAlignment(Qt.AlignCenter)
        self.txt_telagend = QLineEdit(self.frame_5)
        self.txt_telagend.setObjectName(u"txt_telagend")
        self.txt_telagend.setGeometry(QRect(309, 42, 113, 31))
        self.txt_telagend.setAlignment(Qt.AlignCenter)
        self.txt_servagend = QTextEdit(self.frame_5)
        self.txt_servagend.setObjectName(u"txt_servagend")
        self.txt_servagend.setGeometry(QRect(309, 78, 361, 71))
        self.txt_servagend.setStyleSheet(u"background: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.txt_agecom = QComboBox(self.frame_5)
        self.txt_agecom.setObjectName(u"txt_agecom")
        self.txt_agecom.setGeometry(QRect(547, 6, 121, 31))
        self.txt_agecom.setStyleSheet(u"QComboBox{\n"
" 	border-radius: 15px;\n"
"}")
        self.txt_date = QDateEdit(self.frame_5)
        self.txt_date.setObjectName(u"txt_date")
        self.txt_date.setGeometry(QRect(440, 42, 111, 31))
        self.txt_date.setStyleSheet(u"QDateEdit{\n"
" 	border-radius: 15px;\n"
"}")
        self.txt_date.setAlignment(Qt.AlignCenter)
        self.txt_date.setDateTime(QDateTime(QDate(2023, 2, 3), QTime(0, 0, 0)))
        self.txt_date.setCalendarPopup(True)
        self.txt_valage = QLineEdit(self.frame_5)
        self.txt_valage.setObjectName(u"txt_valage")
        self.txt_valage.setGeometry(QRect(607, 42, 61, 31))
        self.txt_valage.setAlignment(Qt.AlignCenter)
        self.txt_pesqcli = QLineEdit(self.frame_5)
        self.txt_pesqcli.setObjectName(u"txt_pesqcli")
        self.txt_pesqcli.setGeometry(QRect(10, 199, 141, 31))
        self.txt_pesqcli.setAlignment(Qt.AlignCenter)
        self.btn_pescli = QPushButton(self.frame_5)
        self.btn_pescli.setObjectName(u"btn_pescli")
        self.btn_pescli.setGeometry(QRect(155, 189, 51, 51))
        self.btn_pescli.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius: 15px;\n"
"	color:#fff\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color:rgb(242, 158, 207);\n"
"}")
        self.btn_pescli.setIcon(icon8)
        self.btn_pescli.setIconSize(QSize(32, 32))
        self.btn_pesval = QPushButton(self.frame_5)
        self.btn_pesval.setObjectName(u"btn_pesval")
        self.btn_pesval.setGeometry(QRect(387, 189, 51, 51))
        self.btn_pesval.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius: 15px;\n"
"	color:#fff\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color:rgb(242, 158, 207);\n"
"}")
        self.btn_pesval.setIcon(icon8)
        self.btn_pesval.setIconSize(QSize(32, 32))
        self.txt_pesqvalor = QLineEdit(self.frame_5)
        self.txt_pesqvalor.setObjectName(u"txt_pesqvalor")
        self.txt_pesqvalor.setGeometry(QRect(213, 198, 171, 31))
        self.txt_pesqvalor.setAlignment(Qt.AlignCenter)
        self.txt_valor = QLineEdit(self.frame_5)
        self.txt_valor.setObjectName(u"txt_valor")
        self.txt_valor.setEnabled(False)
        self.txt_valor.setGeometry(QRect(732, 200, 71, 31))
        self.txt_valor.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(6, 0, 261, 201))
        self.label_7.setStyleSheet(u"background-color:rgb(242, 158, 207);")
        self.label_7.setPixmap(QPixmap(u"img/2390-removebg-preview.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setWordWrap(False)
        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(-10, 0, 881, 231))
        self.frame_8.setStyleSheet(u"background-color:rgb(242, 158, 207);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_11 = QFrame(self.frame_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(10, 0, 871, 501))
        self.frame_11.setStyleSheet(u"background-color:rgb(242, 158, 207);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.frame_11)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(730, 180, 71, 20))
        self.label_9.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.txt_datini = QDateEdit(self.frame_11)
        self.txt_datini.setObjectName(u"txt_datini")
        self.txt_datini.setGeometry(QRect(507, 200, 81, 31))
        self.txt_datini.setStyleSheet(u"QDateEdit{\n"
" 	border-radius: 15px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.txt_datini.setAlignment(Qt.AlignCenter)
        self.txt_datini.setDateTime(QDateTime(QDate(2023, 2, 3), QTime(0, 0, 0)))
        self.txt_datini.setCalendarPopup(True)
        self.txt_datfim = QDateEdit(self.frame_11)
        self.txt_datfim.setObjectName(u"txt_datfim")
        self.txt_datfim.setGeometry(QRect(594, 200, 81, 31))
        self.txt_datfim.setStyleSheet(u"QDateEdit{\n"
" 	border-radius: 15px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.txt_datfim.setAlignment(Qt.AlignCenter)
        self.txt_datfim.setDateTime(QDateTime(QDate(2023, 2, 3), QTime(0, 0, 0)))
        self.txt_datfim.setCalendarPopup(True)
        self.btn_pesqini = QPushButton(self.frame_11)
        self.btn_pesqini.setObjectName(u"btn_pesqini")
        self.btn_pesqini.setGeometry(QRect(670, 190, 51, 51))
        self.btn_pesqini.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius: 15px;\n"
"	color:#fff\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color:rgb(242, 158, 207);\n"
"}")
        self.btn_pesqini.setIcon(icon8)
        self.btn_pesqini.setIconSize(QSize(32, 32))
        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(522, 180, 61, 16))
        font2 = QFont()
        font2.setBold(True)
        self.label_4.setFont(font2)
        self.label_11 = QLabel(self.frame_11)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(606, 180, 61, 16))
        self.label_11.setFont(font2)
        self.label_19 = QLabel(self.frame_11)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(546, 47, 61, 21))
        self.label_19.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.label_19.setAlignment(Qt.AlignCenter)
        self.btn_agendar = QPushButton(self.frame_8)
        self.btn_agendar.setObjectName(u"btn_agendar")
        self.btn_agendar.setGeometry(QRect(691, 44, 109, 30))
        self.btn_agendar.setMinimumSize(QSize(0, 30))
        self.btn_agendar.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	border-radius: 15px;\n"
"	color:#fff\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(243, 243, 243);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u"img/calendar-with-checklist-date-schedule-3d-icon-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_agendar.setIcon(icon12)
        self.btn_agendar.setIconSize(QSize(42, 42))
        self.pushButton = QPushButton(self.frame_8)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(691, 80, 109, 30))
        self.pushButton.setMinimumSize(QSize(0, 30))
        self.pushButton.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	border-radius: 15px;\n"
"	color:#fff\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(243, 243, 243);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}")
        self.pushButton.setIcon(icon11)
        self.pushButton.setIconSize(QSize(42, 42))
        self.btn_excagend = QPushButton(self.frame_8)
        self.btn_excagend.setObjectName(u"btn_excagend")
        self.btn_excagend.setGeometry(QRect(691, 116, 109, 30))
        self.btn_excagend.setMinimumSize(QSize(0, 30))
        self.btn_excagend.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius: 15px;\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	color:#fff\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(243, 243, 243);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}")
        self.btn_excagend.setIcon(icon10)
        self.btn_excagend.setIconSize(QSize(32, 32))
        self.label_14 = QLabel(self.frame_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(7, 10, 101, 31))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.label_14.setPalette(palette2)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"background-color: rgb(242, 158, 207);\n"
"font: 20pt \"Onyx\";")
        self.frame_8.raise_()
        self.txt_nomage.raise_()
        self.txt_telagend.raise_()
        self.txt_servagend.raise_()
        self.txt_agecom.raise_()
        self.txt_date.raise_()
        self.txt_valage.raise_()
        self.btn_pesval.raise_()
        self.txt_valor.raise_()
        self.label_7.raise_()
        self.btn_pescli.raise_()
        self.txt_pesqcli.raise_()
        self.txt_pesqvalor.raise_()
        self.label_14.raise_()
        self.frame_6 = QFrame(self.pg_agend)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(9, 239, 871, 261))
        self.frame_6.setStyleSheet(u"background-color:rgb(242, 158, 207);\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.tableWidget_3 = QTableWidget(self.frame_6)
        if (self.tableWidget_3.columnCount() < 7):
            self.tableWidget_3.setColumnCount(7)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem24)
        if (self.tableWidget_3.rowCount() < 1):
            self.tableWidget_3.setRowCount(1)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_3.setVerticalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        self.tableWidget_3.setItem(0, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_3.setItem(0, 1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_3.setItem(0, 2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_3.setItem(0, 3, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_3.setItem(0, 4, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_3.setItem(0, 5, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_3.setItem(0, 6, __qtablewidgetitem32)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(10, 3, 791, 231))
        self.tableWidget_3.setStyleSheet(u"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(148	, 148, 148);\n"
"	color: rgb(252, 252, 252);\n"
"	border-radius: 5px;\n"
"\n"
"}\n"
"")
        self.tableWidget_3.setAutoScroll(True)
        self.tableWidget_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_3.setRowCount(1)
        self.tableWidget_3.horizontalHeader().setMinimumSectionSize(32)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setMinimumSectionSize(24)
        self.tableWidget_3.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_3.verticalHeader().setStretchLastSection(False)
        self.pages.addWidget(self.pg_agend)
        self.pg_consul = QWidget()
        self.pg_consul.setObjectName(u"pg_consul")
        self.frame_12 = QFrame(self.pg_consul)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(0, 10, 891, 491))
        self.frame_12.setStyleSheet(u"\n"
"background-color:rgb(242, 158, 207);\n"
"\n"
"\n"
"QComboBox{\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
" 	border-radius:15px;\n"
"\n"
"}\n"
"\n"
"QTextEdit{\n"
"	border-radius:15px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.tabelaestoque = QTableWidget(self.frame_12)
        if (self.tabelaestoque.columnCount() < 5):
            self.tabelaestoque.setColumnCount(5)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter);
        self.tabelaestoque.setHorizontalHeaderItem(0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter);
        self.tabelaestoque.setHorizontalHeaderItem(1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignCenter);
        self.tabelaestoque.setHorizontalHeaderItem(2, __qtablewidgetitem35)
        font3 = QFont()
        font3.setStyleStrategy(QFont.PreferAntialias)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem36.setFont(font3);
        self.tabelaestoque.setHorizontalHeaderItem(3, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setTextAlignment(Qt.AlignCenter);
        self.tabelaestoque.setHorizontalHeaderItem(4, __qtablewidgetitem37)
        if (self.tabelaestoque.rowCount() < 1):
            self.tabelaestoque.setRowCount(1)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tabelaestoque.setVerticalHeaderItem(0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setTextAlignment(Qt.AlignCenter);
        self.tabelaestoque.setItem(0, 0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setTextAlignment(Qt.AlignCenter);
        self.tabelaestoque.setItem(0, 1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setTextAlignment(Qt.AlignCenter);
        self.tabelaestoque.setItem(0, 2, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setTextAlignment(Qt.AlignCenter);
        self.tabelaestoque.setItem(0, 3, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setTextAlignment(Qt.AlignCenter);
        self.tabelaestoque.setItem(0, 4, __qtablewidgetitem43)
        self.tabelaestoque.setObjectName(u"tabelaestoque")
        self.tabelaestoque.setGeometry(QRect(0, 120, 811, 351))
        self.tabelaestoque.setStyleSheet(u"\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(148	, 148, 148);\n"
"	color: rgb(252, 252, 252);\n"
"	border-radius: 5px;\n"
"}\n"
"QHeaderView::section3{\n"
"	width: 50px\n"
"}")
        self.tabelaestoque.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabelaestoque.horizontalHeader().setStretchLastSection(True)
        self.tabelaestoque.verticalHeader().setStretchLastSection(False)
        self.txt_produto = QLineEdit(self.frame_12)
        self.txt_produto.setObjectName(u"txt_produto")
        self.txt_produto.setGeometry(QRect(307, 10, 171, 31))
        self.txt_produto.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
" 	border-radius:15px;\n"
"\n"
"}")
        self.txt_produto.setAlignment(Qt.AlignCenter)
        self.txt_valproesto = QLineEdit(self.frame_12)
        self.txt_valproesto.setObjectName(u"txt_valproesto")
        self.txt_valproesto.setGeometry(QRect(515, 10, 51, 31))
        self.txt_valproesto.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
" 	border-radius:15px;\n"
"\n"
"}")
        self.txt_valproesto.setAlignment(Qt.AlignCenter)
        self.txt_valproesto.setReadOnly(False)
        self.txt_datproesto = QDateEdit(self.frame_12)
        self.txt_datproesto.setObjectName(u"txt_datproesto")
        self.txt_datproesto.setGeometry(QRect(578, 10, 101, 31))
        self.txt_datproesto.setStyleSheet(u"QDateEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
" 	border-radius:15px;\n"
"\n"
"}")
        self.txt_datproesto.setAlignment(Qt.AlignCenter)
        self.txt_qtdesto = QLineEdit(self.frame_12)
        self.txt_qtdesto.setObjectName(u"txt_qtdesto")
        self.txt_qtdesto.setGeometry(QRect(688, 10, 81, 31))
        self.txt_qtdesto.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
" 	border-radius:15px;\n"
"\n"
"}")
        self.txt_qtdesto.setAlignment(Qt.AlignCenter)
        self.txt_pesqesto = QLineEdit(self.frame_12)
        self.txt_pesqesto.setObjectName(u"txt_pesqesto")
        self.txt_pesqesto.setGeometry(QRect(20, 87, 191, 31))
        self.txt_pesqesto.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
" 	border-radius:15px;\n"
"\n"
"}")
        self.txt_pesqesto.setAlignment(Qt.AlignCenter)
        self.btn_pesqestoq = QPushButton(self.frame_12)
        self.btn_pesqestoq.setObjectName(u"btn_pesqestoq")
        self.btn_pesqestoq.setGeometry(QRect(220, 87, 41, 31))
        self.btn_pesqestoq.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	border-radius: 15px;\n"
"	color:#fff\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	\n"
"	background-color: rgb(242, 158, 207);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}")
        self.btn_pesqestoq.setIcon(icon8)
        self.btn_pesqestoq.setIconSize(QSize(32, 32))
        self.btn_inclestoq = QPushButton(self.frame_12)
        self.btn_inclestoq.setObjectName(u"btn_inclestoq")
        self.btn_inclestoq.setGeometry(QRect(455, 50, 91, 31))
        self.btn_inclestoq.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	border-radius: 15px;\n"
"	color:#fff\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(243, 243, 243);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}")
        self.btn_inclestoq.setIcon(icon9)
        self.btn_inclestoq.setIconSize(QSize(32, 32))
        self.btn_altestoque = QPushButton(self.frame_12)
        self.btn_altestoque.setObjectName(u"btn_altestoque")
        self.btn_altestoque.setGeometry(QRect(560, 50, 91, 31))
        self.btn_altestoque.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	border-radius: 15px;\n"
"	color:#fff\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(243, 243, 243);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}")
        self.btn_altestoque.setIcon(icon11)
        self.btn_altestoque.setIconSize(QSize(32, 32))
        self.btn_exclestoq = QPushButton(self.frame_12)
        self.btn_exclestoq.setObjectName(u"btn_exclestoq")
        self.btn_exclestoq.setGeometry(QRect(665, 50, 91, 31))
        self.btn_exclestoq.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	border-radius: 15px;\n"
"	color:#fff\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(243, 243, 243);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}")
        self.btn_exclestoq.setIcon(icon10)
        self.btn_exclestoq.setIconSize(QSize(32, 32))
        self.txt_valtotoestoq = QLineEdit(self.frame_12)
        self.txt_valtotoestoq.setObjectName(u"txt_valtotoestoq")
        self.txt_valtotoestoq.setEnabled(False)
        self.txt_valtotoestoq.setGeometry(QRect(750, 89, 61, 31))
        self.txt_valtotoestoq.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
" 	border-radius:15px;\n"
"\n"
"}")
        self.txt_valtotoestoq.setAlignment(Qt.AlignCenter)
        self.txt_valtotoestoq.setDragEnabled(True)
        self.label_10 = QLabel(self.frame_12)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(680, 94, 71, 20))
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";\n"
"background-color: rgb(255, 255, 255, 0);")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_15 = QLabel(self.frame_12)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 10, 131, 20))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.label_15.setPalette(palette3)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"font: 20pt \"Onyx\";")
        self.label_20 = QLabel(self.frame_12)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(470, 13, 61, 21))
        self.label_20.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_20.raise_()
        self.tabelaestoque.raise_()
        self.txt_produto.raise_()
        self.txt_valproesto.raise_()
        self.txt_datproesto.raise_()
        self.txt_qtdesto.raise_()
        self.txt_pesqesto.raise_()
        self.btn_pesqestoq.raise_()
        self.btn_inclestoq.raise_()
        self.btn_altestoque.raise_()
        self.btn_exclestoq.raise_()
        self.txt_valtotoestoq.raise_()
        self.label_10.raise_()
        self.label_15.raise_()
        self.pages.addWidget(self.pg_consul)
        self.pagepromo = QWidget()
        self.pagepromo.setObjectName(u"pagepromo")
        self.pagepromo.setMaximumSize(QSize(825, 16777215))
        self.frame_50 = QFrame(self.pagepromo)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setGeometry(QRect(0, -1, 851, 511))
        self.frame_50.setStyleSheet(u"background-color: rgb(242, 158, 207);")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.tabelapromoes = QTableWidget(self.frame_50)
        if (self.tabelapromoes.columnCount() < 4):
            self.tabelapromoes.setColumnCount(4)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setTextAlignment(Qt.AlignCenter);
        self.tabelapromoes.setHorizontalHeaderItem(0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setTextAlignment(Qt.AlignCenter);
        self.tabelapromoes.setHorizontalHeaderItem(1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setTextAlignment(Qt.AlignCenter);
        self.tabelapromoes.setHorizontalHeaderItem(2, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setTextAlignment(Qt.AlignCenter);
        self.tabelapromoes.setHorizontalHeaderItem(3, __qtablewidgetitem47)
        if (self.tabelapromoes.rowCount() < 1):
            self.tabelapromoes.setRowCount(1)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tabelapromoes.setVerticalHeaderItem(0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setTextAlignment(Qt.AlignCenter);
        self.tabelapromoes.setItem(0, 0, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setTextAlignment(Qt.AlignCenter);
        self.tabelapromoes.setItem(0, 1, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setTextAlignment(Qt.AlignCenter);
        self.tabelapromoes.setItem(0, 2, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem52.setFont(font1);
        self.tabelapromoes.setItem(0, 3, __qtablewidgetitem52)
        self.tabelapromoes.setObjectName(u"tabelapromoes")
        self.tabelapromoes.setGeometry(QRect(10, 140, 811, 341))
        self.tabelapromoes.setStyleSheet(u"\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(148	, 148, 148);\n"
"	color: rgb(252, 252, 252);\n"
"	border-radius: 5px;\n"
"}\n"
"QHeaderView::section3{\n"
"	width: 50px\n"
"}")
        self.tabelapromoes.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabelapromoes.setShowGrid(True)
        self.tabelapromoes.horizontalHeader().setCascadingSectionResizes(False)
        self.tabelapromoes.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabelapromoes.horizontalHeader().setStretchLastSection(True)
        self.tabelapromoes.verticalHeader().setVisible(False)
        self.tabelapromoes.verticalHeader().setProperty("showSortIndicator", False)
        self.tabelapromoes.verticalHeader().setStretchLastSection(False)
        self.txt_textopromo = QTextEdit(self.frame_50)
        self.txt_textopromo.setObjectName(u"txt_textopromo")
        self.txt_textopromo.setGeometry(QRect(170, 30, 461, 91))
        self.txt_textopromo.setStyleSheet(u"background: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"font: 9pt \"Segoe Fluent Icons\";")
        self.btn_envipromo = QPushButton(self.frame_50)
        self.btn_envipromo.setObjectName(u"btn_envipromo")
        self.btn_envipromo.setGeometry(QRect(640, 60, 101, 31))
        self.btn_envipromo.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius: 15px;\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	color:#fff\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(243, 243, 243);\n"
"	border-radius: 15px;\n"
"}")
        self.label_16 = QLabel(self.frame_50)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 4, 131, 31))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.label_16.setPalette(palette4)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(u"font: 20pt \"Onyx\";")
        self.pages.addWidget(self.pagepromo)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.pg_sobre.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"\n"
"}")
        self.label_6 = QLabel(self.pg_sobre)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(370, -10, 551, 591))
        self.label_6.setStyleSheet(u"background-color:rgb(242, 158, 207);")
        self.label_6.setPixmap(QPixmap(u"img/HORARIO_1_-removebg-preview.png"))
        self.label_6.setScaledContents(True)
        self.frame_3 = QFrame(self.pg_sobre)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 501, 191))
        self.frame_3.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QTextEdit{\n"
"\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QDateTimeEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.txt_servagendhora = QTextEdit(self.frame_3)
        self.txt_servagendhora.setObjectName(u"txt_servagendhora")
        self.txt_servagendhora.setGeometry(QRect(10, 86, 381, 101))
        self.txt_servagendhora.setStyleSheet(u"border-radius: 10px;")
        self.txt_nomagehora = QLineEdit(self.frame_3)
        self.txt_nomagehora.setObjectName(u"txt_nomagehora")
        self.txt_nomagehora.setGeometry(QRect(10, 10, 241, 31))
        self.txt_nomagehora.setAlignment(Qt.AlignCenter)
        self.txt_telagendhora = QLineEdit(self.frame_3)
        self.txt_telagendhora.setObjectName(u"txt_telagendhora")
        self.txt_telagendhora.setGeometry(QRect(10, 48, 91, 31))
        self.txt_telagendhora.setAlignment(Qt.AlignCenter)
        self.txt_agecomhora = QComboBox(self.frame_3)
        self.txt_agecomhora.setObjectName(u"txt_agecomhora")
        self.txt_agecomhora.setGeometry(QRect(263, 10, 131, 31))
        self.txt_agecomhora.setStyleSheet(u"QComboBox{\n"
"	border-radius:15px;\n"
"}")
        self.txt_valagehora = QLineEdit(self.frame_3)
        self.txt_valagehora.setObjectName(u"txt_valagehora")
        self.txt_valagehora.setGeometry(QRect(312, 48, 81, 31))
        self.txt_valagehora.setAlignment(Qt.AlignCenter)
        self.txt_datehora = QDateEdit(self.frame_3)
        self.txt_datehora.setObjectName(u"txt_datehora")
        self.txt_datehora.setGeometry(QRect(110, 48, 91, 31))
        self.txt_datehora.setStyleSheet(u"QDateEdit{\n"
"	border-radius:15px;\n"
"}")
        self.txt_datehora.setAlignment(Qt.AlignCenter)
        self.timemarcar = QTimeEdit(self.frame_3)
        self.timemarcar.setObjectName(u"timemarcar")
        self.timemarcar.setGeometry(QRect(205, 48, 61, 31))
        self.timemarcar.setStyleSheet(u"QTimeEdit{\n"
"	border-radius:15px;\n"
"}")
        self.splitter = QSplitter(self.frame_3)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(399, 60, 101, 116))
        self.splitter.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"background-color:rgb(242, 158, 207);")
        self.splitter.setOrientation(Qt.Vertical)
        self.btn_agendhora = QPushButton(self.splitter)
        self.btn_agendhora.setObjectName(u"btn_agendhora")
        self.btn_agendhora.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius: 15px;\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	color:#fff\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(243, 243, 243);\n"
"	border-radius: 15px;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u"img/Capa-Blog-Dicas-para-evitar-erros-na-agenda-de-saloes-e-barbearias-no-final-de-ano-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_agendhora.setIcon(icon13)
        self.btn_agendhora.setIconSize(QSize(42, 42))
        self.splitter.addWidget(self.btn_agendhora)
        self.btn_althora = QPushButton(self.splitter)
        self.btn_althora.setObjectName(u"btn_althora")
        self.btn_althora.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius: 15px;\n"
"	color:#fff\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(243, 243, 243);\n"
"}")
        self.btn_althora.setIcon(icon11)
        self.btn_althora.setIconSize(QSize(42, 42))
        self.splitter.addWidget(self.btn_althora)
        self.btn_excagendhora = QPushButton(self.splitter)
        self.btn_excagendhora.setObjectName(u"btn_excagendhora")
        self.btn_excagendhora.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius: 15px;\n"
"	color:#fff\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(243, 243, 243);\n"
"}")
        self.btn_excagendhora.setIcon(icon10)
        self.btn_excagendhora.setIconSize(QSize(32, 32))
        self.splitter.addWidget(self.btn_excagendhora)
        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(0, 0, 821, 241))
        self.frame_9.setStyleSheet(u"background-color:rgb(242, 158, 207);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_18 = QLabel(self.frame_9)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(265, 50, 61, 21))
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 14pt \"Segoe UI\";\n"
"")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.frame_9.raise_()
        self.txt_servagendhora.raise_()
        self.txt_nomagehora.raise_()
        self.txt_telagendhora.raise_()
        self.txt_agecomhora.raise_()
        self.txt_valagehora.raise_()
        self.txt_datehora.raise_()
        self.timemarcar.raise_()
        self.splitter.raise_()
        self.tableagehora = QTableWidget(self.pg_sobre)
        if (self.tableagehora.columnCount() < 8):
            self.tableagehora.setColumnCount(8)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setTextAlignment(Qt.AlignCenter);
        self.tableagehora.setHorizontalHeaderItem(0, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setTextAlignment(Qt.AlignCenter);
        self.tableagehora.setHorizontalHeaderItem(1, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setTextAlignment(Qt.AlignCenter);
        self.tableagehora.setHorizontalHeaderItem(2, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setTextAlignment(Qt.AlignCenter);
        self.tableagehora.setHorizontalHeaderItem(3, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setTextAlignment(Qt.AlignCenter);
        self.tableagehora.setHorizontalHeaderItem(4, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setTextAlignment(Qt.AlignCenter);
        self.tableagehora.setHorizontalHeaderItem(5, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setTextAlignment(Qt.AlignCenter);
        self.tableagehora.setHorizontalHeaderItem(6, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem60.setBackground(QColor(0, 0, 0));
        self.tableagehora.setHorizontalHeaderItem(7, __qtablewidgetitem60)
        if (self.tableagehora.rowCount() < 1):
            self.tableagehora.setRowCount(1)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tableagehora.setVerticalHeaderItem(0, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setTextAlignment(Qt.AlignCenter);
        self.tableagehora.setItem(0, 0, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setTextAlignment(Qt.AlignCenter);
        self.tableagehora.setItem(0, 1, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setTextAlignment(Qt.AlignCenter);
        self.tableagehora.setItem(0, 2, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setTextAlignment(Qt.AlignCenter);
        self.tableagehora.setItem(0, 3, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setTextAlignment(Qt.AlignCenter);
        self.tableagehora.setItem(0, 4, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setTextAlignment(Qt.AlignCenter);
        self.tableagehora.setItem(0, 5, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        __qtablewidgetitem68.setTextAlignment(Qt.AlignCenter);
        self.tableagehora.setItem(0, 6, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        __qtablewidgetitem69.setTextAlignment(Qt.AlignCenter);
        self.tableagehora.setItem(0, 7, __qtablewidgetitem69)
        self.tableagehora.setObjectName(u"tableagehora")
        self.tableagehora.setGeometry(QRect(10, 230, 811, 251))
        self.tableagehora.setTabletTracking(False)
        self.tableagehora.setAcceptDrops(False)
        self.tableagehora.setAutoFillBackground(False)
        self.tableagehora.setStyleSheet(u"\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(148	, 148, 148);\n"
"	color: rgb(252, 252, 252);\n"
"	border-radius: 5px;\n"
"}\n"
"QHeaderView::section3{\n"
"	width: 50px\n"
"}")
        self.tableagehora.setAutoScroll(True)
        self.tableagehora.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableagehora.setTabKeyNavigation(True)
        self.tableagehora.setProperty("showDropIndicator", True)
        self.tableagehora.setDragEnabled(False)
        self.tableagehora.setDragDropOverwriteMode(True)
        self.tableagehora.setAlternatingRowColors(False)
        self.tableagehora.setShowGrid(True)
        self.tableagehora.setSortingEnabled(False)
        self.tableagehora.setWordWrap(True)
        self.tableagehora.setCornerButtonEnabled(True)
        self.tableagehora.setColumnCount(8)
        self.tableagehora.horizontalHeader().setCascadingSectionResizes(False)
        self.tableagehora.horizontalHeader().setDefaultSectionSize(90)
        self.tableagehora.horizontalHeader().setHighlightSections(True)
        self.tableagehora.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableagehora.horizontalHeader().setStretchLastSection(True)
        self.tableagehora.verticalHeader().setMinimumSectionSize(24)
        self.tableagehora.verticalHeader().setDefaultSectionSize(30)
        self.tableagehora.verticalHeader().setStretchLastSection(False)
        self.txt_pesqvalorhora = QLineEdit(self.pg_sobre)
        self.txt_pesqvalorhora.setObjectName(u"txt_pesqvalorhora")
        self.txt_pesqvalorhora.setGeometry(QRect(270, 199, 131, 31))
        self.txt_pesqvalorhora.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"\n"
"}")
        self.txt_pesqvalorhora.setAlignment(Qt.AlignCenter)
        self.txt_valorhora = QLineEdit(self.pg_sobre)
        self.txt_valorhora.setObjectName(u"txt_valorhora")
        self.txt_valorhora.setEnabled(False)
        self.txt_valorhora.setGeometry(QRect(741, 207, 71, 31))
        self.txt_valorhora.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"\n"
"")
        self.txt_valorhora.setAlignment(Qt.AlignCenter)
        self.btn_pesvalhora = QPushButton(self.pg_sobre)
        self.btn_pesvalhora.setObjectName(u"btn_pesvalhora")
        self.btn_pesvalhora.setGeometry(QRect(400, 201, 41, 31))
        self.btn_pesvalhora.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius: 15px;\n"
"	color:#fff\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color:rgb(242, 158, 207);\n"
"}")
        self.btn_pesvalhora.setIcon(icon8)
        self.btn_pesvalhora.setIconSize(QSize(32, 32))
        self.btn_pesvalhora.setAutoRepeat(False)
        self.btn_pesvalhora.setAutoExclusive(False)
        self.btn_pesvalhora.setAutoDefault(False)
        self.btn_pesvalhora.setFlat(False)
        self.btn_pesclihora = QPushButton(self.pg_sobre)
        self.btn_pesclihora.setObjectName(u"btn_pesclihora")
        self.btn_pesclihora.setGeometry(QRect(141, 201, 41, 31))
        self.btn_pesclihora.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius: 15px;\n"
"	color:#fff\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color:rgb(242, 158, 207);\n"
"}")
        self.btn_pesclihora.setIcon(icon8)
        self.btn_pesclihora.setIconSize(QSize(32, 32))
        self.btn_pesclihora.setAutoDefault(False)
        self.btn_pesclihora.setFlat(False)
        self.txt_pesclihora = QLineEdit(self.pg_sobre)
        self.txt_pesclihora.setObjectName(u"txt_pesclihora")
        self.txt_pesclihora.setGeometry(QRect(10, 199, 131, 31))
        self.txt_pesclihora.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"\n"
"}")
        self.txt_pesclihora.setAlignment(Qt.AlignCenter)
        self.frame_10 = QFrame(self.pg_sobre)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(0, 190, 821, 311))
        self.frame_10.setStyleSheet(u"background-color:rgb(242, 158, 207);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.pg_sobre)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(666, 213, 71, 20))
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_17 = QLabel(self.pg_sobre)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(640, 6, 91, 21))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush2 = QBrush(QColor(234, 153, 201, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.label_17.setPalette(palette5)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(u"background-color: rgb(234, 153, 201);\n"
"font: 20pt \"Onyx\";")
        self.pages.addWidget(self.pg_sobre)
        self.frame_10.raise_()
        self.label_6.raise_()
        self.frame_3.raise_()
        self.tableagehora.raise_()
        self.txt_pesqvalorhora.raise_()
        self.txt_valorhora.raise_()
        self.btn_pesvalhora.raise_()
        self.btn_pesclihora.raise_()
        self.txt_pesclihora.raise_()
        self.label_8.raise_()
        self.label_17.raise_()

        self.verticalLayout.addWidget(self.main_frame)

        self.footer = QFrame(self.main_c)
        self.footer.setObjectName(u"footer")
        self.footer.setMaximumSize(QSize(900, 16777215))
        self.footer.setStyleSheet(u"")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.footer)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.footer)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setStyleSheet(u"font: 10pt \"Leelawadee\";\n"
"background-color:rgb(242, 158, 207);\n"
"color:(255,255,255);\n"
"")
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer)


        self.horizontalLayout.addWidget(self.main_c)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.txt_nomcadcli, self.txt_telcadcli)
        QWidget.setTabOrder(self.txt_telcadcli, self.txt_endcadcli)
        QWidget.setTabOrder(self.txt_endcadcli, self.txt_pescli)
        QWidget.setTabOrder(self.txt_pescli, self.txt_nomcadfun)
        QWidget.setTabOrder(self.txt_nomcadfun, self.btn_inccli)
        QWidget.setTabOrder(self.btn_inccli, self.btn_exccli)
        QWidget.setTabOrder(self.btn_exccli, self.btn_agenda)
        QWidget.setTabOrder(self.btn_agenda, self.btn_sobre)
        QWidget.setTabOrder(self.btn_sobre, self.btn_toogle)
        QWidget.setTabOrder(self.btn_toogle, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.tableWidget_2)
        QWidget.setTabOrder(self.tableWidget_2, self.btn_incfun)
        QWidget.setTabOrder(self.btn_incfun, self.btn_home)
        QWidget.setTabOrder(self.btn_home, self.btn_cadastro)
        QWidget.setTabOrder(self.btn_cadastro, self.txt_endcadfun)
        QWidget.setTabOrder(self.txt_endcadfun, self.btn_pescliente)
        QWidget.setTabOrder(self.btn_pescliente, self.txt_telcadfun)
        QWidget.setTabOrder(self.txt_telcadfun, self.btn_altfun)
        QWidget.setTabOrder(self.btn_altfun, self.btn_excfun)
        QWidget.setTabOrder(self.btn_excfun, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.txt_nomage)
        QWidget.setTabOrder(self.txt_nomage, self.txt_telagend)
        QWidget.setTabOrder(self.txt_telagend, self.txt_servagend)
        QWidget.setTabOrder(self.txt_servagend, self.txt_agecom)
        QWidget.setTabOrder(self.txt_agecom, self.txt_date)
        QWidget.setTabOrder(self.txt_date, self.txt_valage)
        QWidget.setTabOrder(self.txt_valage, self.txt_pesqcli)
        QWidget.setTabOrder(self.txt_pesqcli, self.btn_pescli)
        QWidget.setTabOrder(self.btn_pescli, self.tableWidget_3)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)
        self.btn_inccli.setDefault(False)
        self.btn_pesvalhora.setDefault(False)
        self.btn_pesclihora.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(whatsthis)
        self.frame.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">FSGSDR</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_3.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"MENU DE OP\u00c7\u00d5ES", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.btn_agenda.setText(QCoreApplication.translate("MainWindow", u"Servi\u00e7os do Dia", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Hora Marcada", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Pagina de Cadastro", None))
        self.btn_consulestoque.setText(QCoreApplication.translate("MainWindow", u"Estoque", None))
#if QT_CONFIG(tooltip)
        self.btn_promo.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.btn_promo.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">fsdafasd</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_promo.setText(QCoreApplication.translate("MainWindow", u"Enviar Promo\u00e7oes", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Pagina de Monitoramento", None))
        self.btn_toogle.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sistema de Cadastros e Agendamentos", None))
        self.logo.setText("")
        self.txt_endcadcli.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O", None))
        self.txt_pescli.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DIGITE O NOME", None))
        self.btn_pescliente.setText("")
        self.btn_inccli.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
        self.btn_exccli.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.txt_telcadcli.setInputMask(QCoreApplication.translate("MainWindow", u"(99)99999-9999", None))
        self.txt_telcadcli.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        self.txt_nomcadcli.setInputMask("")
        self.txt_nomcadcli.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Cadastro de Cliente", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O", None));
        ___qtablewidgetitem4 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"1", None));

        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cadastro Cliente", None))
        self.txt_nomcadfun.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME", None))
        self.txt_endcadfun.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O", None))
        self.txt_telcadfun.setInputMask(QCoreApplication.translate("MainWindow", u"(99)99999-9999", None))
        self.txt_telcadfun.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        self.btn_incfun.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
        self.btn_altfun.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excfun.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"1", None));

        __sortingEnabled1 = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled1)

        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Cadastro de funcion\u00e1rios", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Funcion\u00e1rias", None))
        self.txt_nomage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME CLIENTE", None))
        self.txt_telagend.setInputMask(QCoreApplication.translate("MainWindow", u"(99)99999-9999", None))
        self.txt_telagend.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        self.txt_agecom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"FUNCION\u00c1RIO(A)", None))
        self.txt_date.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy", None))
        self.txt_valage.setInputMask(QCoreApplication.translate("MainWindow", u"999.00", None))
        self.txt_valage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"VALOR", None))
        self.txt_pesqcli.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PESQUISAR POR NOME", None))
        self.btn_pescli.setText("")
        self.btn_pesval.setText("")
        self.txt_pesqvalor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PESQUISAR FUNCIONARIO(A)", None))
        self.txt_valor.setInputMask(QCoreApplication.translate("MainWindow", u"R$999.00", None))
        self.txt_valor.setText(QCoreApplication.translate("MainWindow", u"R$.", None))
        self.txt_valor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"VALOR", None))
        self.label_7.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Valor Toral", None))
        self.txt_datini.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy", None))
        self.txt_datfim.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy", None))
        self.btn_pesqini.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Dat. Inicial", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Dat. Final", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"R$:", None))
        self.btn_agendar.setText(QCoreApplication.translate("MainWindow", u"Agendar", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excagend.setText(QCoreApplication.translate("MainWindow", u"   Excluir", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Servi\u00e7os do Dia", None))
        ___qtablewidgetitem10 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem11 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"CLIENTE", None));
        ___qtablewidgetitem12 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"FUNCIONARIA", None));
        ___qtablewidgetitem13 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem14 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"DATA/HORA", None));
        ___qtablewidgetitem15 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"VALOR", None));
        ___qtablewidgetitem16 = self.tableWidget_3.horizontalHeaderItem(6)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"OBSERVA\u00c7\u00d5ES", None));
        ___qtablewidgetitem17 = self.tableWidget_3.verticalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"1", None));

        __sortingEnabled2 = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        self.tableWidget_3.setSortingEnabled(__sortingEnabled2)

        ___qtablewidgetitem18 = self.tabelaestoque.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem19 = self.tabelaestoque.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"PRODUTO", None));
        ___qtablewidgetitem20 = self.tabelaestoque.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"VALOR UN.", None));
        ___qtablewidgetitem21 = self.tabelaestoque.horizontalHeaderItem(3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"DATA DE ENTRADA", None));
        ___qtablewidgetitem22 = self.tabelaestoque.horizontalHeaderItem(4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"QUANTIDADE", None));
        ___qtablewidgetitem23 = self.tabelaestoque.verticalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"1", None));

        __sortingEnabled3 = self.tabelaestoque.isSortingEnabled()
        self.tabelaestoque.setSortingEnabled(False)
        self.tabelaestoque.setSortingEnabled(__sortingEnabled3)

        self.txt_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PRODUTO", None))
        self.txt_valproesto.setInputMask(QCoreApplication.translate("MainWindow", u"999.00", None))
        self.txt_valproesto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"VALOR", None))
        self.txt_datproesto.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy", None))
        self.txt_qtdesto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"QUANTIDADE", None))
        self.txt_pesqesto.setText("")
        self.txt_pesqesto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PESQUISAR PRODUTO", None))
        self.btn_pesqestoq.setText("")
        self.btn_inclestoq.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
        self.btn_altestoque.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_exclestoq.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.txt_valtotoestoq.setInputMask(QCoreApplication.translate("MainWindow", u"R$999.00", None))
        self.txt_valtotoestoq.setText(QCoreApplication.translate("MainWindow", u"R$.", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Valor Total:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Controle de Estoque", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"R$:", None))
        ___qtablewidgetitem24 = self.tabelapromoes.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem25 = self.tabelapromoes.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem26 = self.tabelapromoes.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem27 = self.tabelapromoes.horizontalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O", None));
        ___qtablewidgetitem28 = self.tabelapromoes.verticalHeaderItem(0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"1", None));

        __sortingEnabled4 = self.tabelapromoes.isSortingEnabled()
        self.tabelapromoes.setSortingEnabled(False)
        self.tabelapromoes.setSortingEnabled(__sortingEnabled4)

        self.txt_textopromo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite aqui as promo\u00e7\u00f5es:", None))
        self.btn_envipromo.setText(QCoreApplication.translate("MainWindow", u"Enviar Promo\u00e7\u00e3o", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Envio de Promo\u00e7\u00f5es", None))
        self.label_6.setText("")
        self.txt_nomagehora.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME CLIENTE", None))
        self.txt_telagendhora.setInputMask(QCoreApplication.translate("MainWindow", u"(99)99999-9999", None))
        self.txt_telagendhora.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        self.txt_agecomhora.setPlaceholderText(QCoreApplication.translate("MainWindow", u"FUNCION\u00c1RIO(A)", None))
        self.txt_valagehora.setInputMask(QCoreApplication.translate("MainWindow", u"999.00", None))
        self.txt_valagehora.setPlaceholderText(QCoreApplication.translate("MainWindow", u"VALOR", None))
        self.txt_datehora.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy", None))
        self.timemarcar.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm", None))
        self.btn_agendhora.setText(QCoreApplication.translate("MainWindow", u"Marcar", None))
        self.btn_althora.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excagendhora.setText(QCoreApplication.translate("MainWindow", u"   Excluir", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"R$:", None))
        ___qtablewidgetitem29 = self.tableagehora.horizontalHeaderItem(0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem30 = self.tableagehora.horizontalHeaderItem(1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"NOME CLIENTE", None));
        ___qtablewidgetitem31 = self.tableagehora.horizontalHeaderItem(2)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"FUNCIONARIO(A)", None));
        ___qtablewidgetitem32 = self.tableagehora.horizontalHeaderItem(3)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem33 = self.tableagehora.horizontalHeaderItem(4)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"DATA/HORA", None));
        ___qtablewidgetitem34 = self.tableagehora.horizontalHeaderItem(5)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"HORA", None));
        ___qtablewidgetitem35 = self.tableagehora.horizontalHeaderItem(6)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"VALOR", None));
        ___qtablewidgetitem36 = self.tableagehora.horizontalHeaderItem(7)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"OBSERVA\u00c7\u00c3O", None));
        ___qtablewidgetitem37 = self.tableagehora.verticalHeaderItem(0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"1", None));

        __sortingEnabled5 = self.tableagehora.isSortingEnabled()
        self.tableagehora.setSortingEnabled(False)
        self.tableagehora.setSortingEnabled(__sortingEnabled5)

        self.txt_pesqvalorhora.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PESQUISAR FUN.", None))
        self.txt_valorhora.setInputMask(QCoreApplication.translate("MainWindow", u"R$999.00", None))
        self.btn_pesvalhora.setText("")
        self.btn_pesclihora.setText("")
        self.txt_pesclihora.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PESQUISAR POR NOME", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Valor Total:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Hora Marcada", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"@ BruTha 2023", None))
    # retranslateUi

