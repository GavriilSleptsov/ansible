# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\test.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import fileinput
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1012, 599)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\logo_window_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        self.centralwidget.setFont(font)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.MainBackground = QtWidgets.QLabel(self.centralwidget)
        self.MainBackground.setGeometry(QtCore.QRect(0, 0, 1071, 601))
        self.MainBackground.setStyleSheet("QLabel#MainBackground {\n"
"    background: qlineargradient(spread:reflect, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(94, 2, 1, 255), stop:0.85 rgba(6, 0, 156, 255))\n"
"};")
        self.MainBackground.setText("")
        self.MainBackground.setObjectName("MainBackground")
        self.OpacityBackground_2 = QtWidgets.QLabel(self.centralwidget)
        self.OpacityBackground_2.setGeometry(QtCore.QRect(10, 10, 321, 581))
        self.OpacityBackground_2.setStyleSheet("QLabel#OpacityBackground_2 {\n"
"    background: rgba(255,255,255,0.35);\n"
"    border-radius: 20px;\n"
"};")
        self.OpacityBackground_2.setText("")
        self.OpacityBackground_2.setObjectName("OpacityBackground_2")
        self.AnsiblePlaybook_Button = QtWidgets.QPushButton(self.centralwidget)
        self.AnsiblePlaybook_Button.setGeometry(QtCore.QRect(20, 20, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.AnsiblePlaybook_Button.setFont(font)
        self.AnsiblePlaybook_Button.setStyleSheet("QPushButton#AnsiblePlaybook_Button {\n"
"    border: 2px solid #333; /* Цвет рамки */\n"
"    border-radius: 5px; /* Скругление углов */\n"
"    padding: 5px 10px; /* Внутренний отступ */\n"
"    background-color: #fff; /* Цвет фона */\n"
"}\n"
"\n"
"QPushButton#AnsiblePlaybook_Button:hover {\n"
"    background-color: #444; /* Цвет фона при наведении */\n"
"    color: #fff; /* Цвет текста при наведении */\n"
"}\n"
"\n"
"QPushButton#AnsiblePlaybook_Button:pressed {\n"
" background-color: #666; /* Цвет фона при нажатии */\n"
"    color: #fff; /* Цвет текста при нажатии */\n"
"}")
        self.AnsiblePlaybook_Button.setAutoDefault(False)
        self.AnsiblePlaybook_Button.setObjectName("AnsiblePlaybook_Button")
        self.AnsibleScroll_Area = QtWidgets.QScrollArea(self.centralwidget)
        self.AnsibleScroll_Area.setGeometry(QtCore.QRect(340, 5, 661, 591))
        self.AnsibleScroll_Area.setStyleSheet("background: transparent;\n"
"border: none;")
        self.AnsibleScroll_Area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.AnsibleScroll_Area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.AnsibleScroll_Area.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.AnsibleScroll_Area.setWidgetResizable(True)
        self.AnsibleScroll_Area.setObjectName("AnsibleScroll_Area")
        self.AnsibleContent = QtWidgets.QWidget()
        self.AnsibleContent.setGeometry(QtCore.QRect(0, 0, 644, 1000))
        self.AnsibleContent.setMinimumSize(QtCore.QSize(0, 1000))
        font = QtGui.QFont()
        font.setFamily("Niagara Engraved")
        self.AnsibleContent.setFont(font)
        self.AnsibleContent.setStyleSheet("")
        self.AnsibleContent.setObjectName("AnsibleContent")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.AnsibleContent)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Ansible_network_and_domain = QtWidgets.QFrame(self.AnsibleContent)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        self.Ansible_network_and_domain.setFont(font)
        self.Ansible_network_and_domain.setStyleSheet("QFrame#Ansible_network_and_domain {\n"
"    background: rgba(255,255,255,0.2);\n"
"    border-radius: 20px;\n"
"}")
        self.Ansible_network_and_domain.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Ansible_network_and_domain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Ansible_network_and_domain.setObjectName("Ansible_network_and_domain")
        self.network_and_domain_frame = QtWidgets.QFrame(self.Ansible_network_and_domain)
        self.network_and_domain_frame.setGeometry(QtCore.QRect(310, 10, 311, 301))
        self.network_and_domain_frame.setStyleSheet("QFrame#network_and_domain_frame {\n"
"    background: rgba(255,255,255,1);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"\n"
"QFrame > QLineEdit {\n"
"    border: 1px solid rgba(0,0,0,0.2);\n"
"    background-color: rgba(0,0,0,0.1);\n"
"}\n"
"")
        self.network_and_domain_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.network_and_domain_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.network_and_domain_frame.setObjectName("network_and_domain_frame")
        self.IP = QtWidgets.QLineEdit(self.network_and_domain_frame)
        self.IP.setGeometry(QtCore.QRect(10, 40, 291, 25))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(13)
        self.IP.setFont(font)
        self.IP.setText("")
        self.IP.setClearButtonEnabled(True)
        self.IP.setObjectName("IP")
        self.Netmask = QtWidgets.QLineEdit(self.network_and_domain_frame)
        self.Netmask.setGeometry(QtCore.QRect(10, 70, 291, 25))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(13)
        self.Netmask.setFont(font)
        self.Netmask.setClearButtonEnabled(True)
        self.Netmask.setObjectName("Netmask")
        self.Gateway = QtWidgets.QLineEdit(self.network_and_domain_frame)
        self.Gateway.setGeometry(QtCore.QRect(10, 100, 291, 25))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(13)
        self.Gateway.setFont(font)
        self.Gateway.setClearButtonEnabled(True)
        self.Gateway.setObjectName("Gateway")
        self.DNS = QtWidgets.QLineEdit(self.network_and_domain_frame)
        self.DNS.setGeometry(QtCore.QRect(10, 130, 291, 25))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(13)
        self.DNS.setFont(font)
        self.DNS.setClearButtonEnabled(True)
        self.DNS.setObjectName("DNS")
        self.SearchDomain = QtWidgets.QLineEdit(self.network_and_domain_frame)
        self.SearchDomain.setGeometry(QtCore.QRect(10, 160, 291, 25))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(13)
        self.SearchDomain.setFont(font)
        self.SearchDomain.setClearButtonEnabled(True)
        self.SearchDomain.setObjectName("SearchDomain")
        self.Hostname = QtWidgets.QLineEdit(self.network_and_domain_frame)
        self.Hostname.setGeometry(QtCore.QRect(10, 190, 291, 25))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(13)
        self.Hostname.setFont(font)
        self.Hostname.setClearButtonEnabled(True)
        self.Hostname.setObjectName("Hostname")
        self.LoginAdmin = QtWidgets.QLineEdit(self.network_and_domain_frame)
        self.LoginAdmin.setGeometry(QtCore.QRect(10, 220, 291, 25))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(13)
        self.LoginAdmin.setFont(font)
        self.LoginAdmin.setClearButtonEnabled(True)
        self.LoginAdmin.setObjectName("LoginAdmin")
        self.PasswordAdmin = QtWidgets.QLineEdit(self.network_and_domain_frame)
        self.PasswordAdmin.setGeometry(QtCore.QRect(10, 250, 291, 25))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(13)
        self.PasswordAdmin.setFont(font)
        self.PasswordAdmin.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.PasswordAdmin.setClearButtonEnabled(True)
        self.PasswordAdmin.setObjectName("PasswordAdmin")
        self.network_and_domain_frame_title = QtWidgets.QLabel(self.network_and_domain_frame)
        self.network_and_domain_frame_title.setGeometry(QtCore.QRect(63, 5, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.network_and_domain_frame_title.setFont(font)
        self.network_and_domain_frame_title.setStyleSheet("QLabel#network_and_domain_frame_title {\n"
"    background: transparent;\n"
"}")
        self.network_and_domain_frame_title.setAlignment(QtCore.Qt.AlignCenter)
        self.network_and_domain_frame_title.setObjectName("network_and_domain_frame_title")
        self.network_and_domain_text = QtWidgets.QTextBrowser(self.Ansible_network_and_domain)
        self.network_and_domain_text.setGeometry(QtCore.QRect(10, 10, 291, 301))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.network_and_domain_text.setFont(font)
        self.network_and_domain_text.setStyleSheet("QTextBrowser#network_and_domain_text {\n"
"    background: rgba(0,0,0,0.5);\n"
"    border-radius: 20px;\n"
"    padding: 5px 0px 0px 0px;\n"
"}\n"
"")
        self.network_and_domain_text.setObjectName("network_and_domain_text")
        self.line = QtWidgets.QFrame(self.Ansible_network_and_domain)
        self.line.setGeometry(QtCore.QRect(27, 120, 251, 2))
        self.line.setStyleSheet("background: #fff;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.check_network = QtWidgets.QCheckBox(self.Ansible_network_and_domain)
        self.check_network.setGeometry(QtCore.QRect(20, 135, 251, 17))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.check_network.setFont(font)
        self.check_network.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_network.setStyleSheet("QCheckBox#check_network {\n"
"    color: #fff;\n"
"}")
        self.check_network.setCheckable(True)
        self.check_network.setChecked(False)
        self.check_network.setObjectName("check_network")
        self.stable_repo = QtWidgets.QCheckBox(self.Ansible_network_and_domain)
        self.stable_repo.setGeometry(QtCore.QRect(20, 160, 251, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.stable_repo.setFont(font)
        self.stable_repo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stable_repo.setStyleSheet("QCheckBox#stable_repo {\n"
"    color: #fff;\n"
"}")
        self.stable_repo.setObjectName("stable_repo")
        self.frozen_repo = QtWidgets.QCheckBox(self.Ansible_network_and_domain)
        self.frozen_repo.setGeometry(QtCore.QRect(20, 185, 251, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.frozen_repo.setFont(font)
        self.frozen_repo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frozen_repo.setStyleSheet("QCheckBox#frozen_repo {\n"
"    color: #fff;\n"
"}")
        self.frozen_repo.setObjectName("frozen_repo")
        self.change_hostname = QtWidgets.QCheckBox(self.Ansible_network_and_domain)
        self.change_hostname.setGeometry(QtCore.QRect(20, 210, 251, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.change_hostname.setFont(font)
        self.change_hostname.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.change_hostname.setStyleSheet("QCheckBox#change_hostname {\n"
"    color: #fff;\n"
"}")
        self.change_hostname.setObjectName("change_hostname")
        self.change_domain = QtWidgets.QCheckBox(self.Ansible_network_and_domain)
        self.change_domain.setGeometry(QtCore.QRect(20, 235, 251, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.change_domain.setFont(font)
        self.change_domain.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.change_domain.setStyleSheet("QCheckBox#change_domain {\n"
"    color: #fff;\n"
"}")
        self.change_domain.setObjectName("change_domain")
        self.change_wallpaper = QtWidgets.QCheckBox(self.Ansible_network_and_domain)
        self.change_wallpaper.setGeometry(QtCore.QRect(20, 260, 251, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.change_wallpaper.setFont(font)
        self.change_wallpaper.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.change_wallpaper.setStyleSheet("QCheckBox#change_wallpaper {\n"
"    color: #fff;\n"
"}")
        self.change_wallpaper.setObjectName("change_wallpaper")
        self.change_wallpaper_background = QtWidgets.QCheckBox(self.Ansible_network_and_domain)
        self.change_wallpaper_background.setGeometry(QtCore.QRect(20, 285, 251, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.change_wallpaper_background.setFont(font)
        self.change_wallpaper_background.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.change_wallpaper_background.setStyleSheet("QCheckBox#change_wallpaper_background {\n"
"    color: #fff;\n"
"}")
        self.change_wallpaper_background.setObjectName("change_wallpaper_background")
        self.verticalLayout.addWidget(self.Ansible_network_and_domain)
        self.Ansible_network_folders = QtWidgets.QFrame(self.AnsibleContent)
        self.Ansible_network_folders.setStyleSheet("background: rgba(255,255,255,0.2);\n"
"border-radius: 20px;")
        self.Ansible_network_folders.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Ansible_network_folders.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Ansible_network_folders.setObjectName("Ansible_network_folders")
        self.verticalLayout.addWidget(self.Ansible_network_folders)
        self.frame = QtWidgets.QFrame(self.AnsibleContent)
        self.frame.setStyleSheet("background: rgba(255,255,255,0.2);\n"
"border-radius: 20px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)
        self.AnsibleScroll_Area.setWidget(self.AnsibleContent)
        self.MainBackground.raise_()
        self.AnsibleScroll_Area.raise_()
        self.OpacityBackground_2.raise_()
        self.AnsiblePlaybook_Button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.AnsiblePlaybook_Button, self.AnsibleScroll_Area)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "АйтекИнфо"))
        self.AnsiblePlaybook_Button.setText(_translate("MainWindow", "Ansible Playbook\'и"))
        self.IP.setPlaceholderText(_translate("MainWindow", "IP-адрес"))
        self.Netmask.setPlaceholderText(_translate("MainWindow", "Маска подсети (в виде 24)"))
        self.Gateway.setPlaceholderText(_translate("MainWindow", "Шлюз"))
        self.DNS.setPlaceholderText(_translate("MainWindow", "IP-адрес DNS"))
        self.SearchDomain.setPlaceholderText(_translate("MainWindow", "Имя домена"))
        self.Hostname.setPlaceholderText(_translate("MainWindow", "Новый hostname для хоста"))
        self.LoginAdmin.setPlaceholderText(_translate("MainWindow", "Логин доменного админа"))
        self.PasswordAdmin.setPlaceholderText(_translate("MainWindow", "Пароль доменного админа"))
        self.network_and_domain_frame_title.setText(_translate("MainWindow", "Введите данные"))
        self.network_and_domain_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sitka Heading\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; color:#ffffff;\">Роль: </span><span style=\" font-family:\'MS Shell Dlg 2\'; text-decoration: underline; color:#ffffff;\">Сетевая настройка и присоединение к домену</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; color:#ffffff;\">Выберите ниже пункты, которые хотите сейчас настроить</span></p></body></html>"))
        self.check_network.setText(_translate("MainWindow", "Сетевая настройка хоста"))
        self.stable_repo.setText(_translate("MainWindow", "Включение стандартного репозитория"))
        self.frozen_repo.setText(_translate("MainWindow", "Включение frozen репозитория 1.7.5"))
        self.change_hostname.setText(_translate("MainWindow", "Изменение hostname хоста"))
        self.change_domain.setText(_translate("MainWindow", "Присоединение к домену"))
        self.change_wallpaper.setText(_translate("MainWindow", "Изменение обоев рабочего стола"))
        self.change_wallpaper_background.setText(_translate("MainWindow", "Изменение обоев при входе"))

        
        ##### Нажимаются при запуске программы #####
        ############################################
        self.check_networkClicked()
        self.check_hostnameClicked()
        self.check_domainClicked()
        
        ##### ВАЛИДАТОРЫ #####
        ######################
        ##### IP #####
        ip_validator = QtGui.QRegExpValidator(QtCore.QRegExp("[0-9.]*"))
        self.IP.setValidator(ip_validator)
        self.IP.textChanged.connect(self.update_ip_in_file)
        
        ##### DNS #####
        dns_validator = QtGui.QRegExpValidator(QtCore.QRegExp("[0-9.]*"))
        self.DNS.setValidator(dns_validator)
        self.DNS.textChanged.connect(self.update_dns_in_file)
        
        ##### GATEWAY #####
        gateway_validator = QtGui.QRegExpValidator(QtCore.QRegExp("[0-9.]*"))
        self.Gateway.setValidator(gateway_validator)
        self.Gateway.textChanged.connect(self.update_gateway_in_file)
        
        ##### NETMASK #####
        netmask_validator = QtGui.QRegExpValidator(QtCore.QRegExp("[0-9.]*"))
        self.Netmask.setValidator(netmask_validator)
        self.Netmask.textChanged.connect(self.update_netmask_in_file)
        
        ##### HOSTNAME #####
        self.Hostname.textChanged.connect(self.update_hostname_in_file)
        
        ##### DOMAIN #####
        self.SearchDomain.textChanged.connect(self.update_domain_in_file)
        
        ##### DOMAIN ADMIN LOGIN#####
        self.LoginAdmin.textChanged.connect(self.update_admin_login_in_file)
        
        ##### DOMAIN ADMIN LOGIN#####
        self.PasswordAdmin.textChanged.connect(self.update_admin_password_in_file)
        
        ##### CONNECT КОДЫ #####
        ########################
        #### STABLE репозитории #####
        self.stable_repo.clicked.connect(self.toggle_stable_repo)
        
        ##### FROZEN репозитории #####
        self.frozen_repo.clicked.connect(self.toggle_frozen_repo)
        
        ##### Сетевая настройка #####
        self.check_network.clicked.connect(self.toggle_change_network)
        
        ##### Изменение hostname хоста #####
        self.change_hostname.clicked.connect(self.toggle_change_hostname)
        
        ##### Присоединение к домену #####
        self.change_domain.clicked.connect(self.toggle_change_domain)
        
        ##### Изменение обоев рабочего стола #####
        self.change_wallpaper.clicked.connect(self.toggle_change_wallpaper)
        
        ##### Изменение обоев при входе #####
        self.change_wallpaper_background.clicked.connect(self.toggle_change_wallpaper_background)
        
        ##### Сетевая настройка #####
        self.check_network.clicked.connect(self.check_networkClicked)
        
        ##### Присоединение к домену #####
        self.change_domain.clicked.connect(self.check_domainClicked)
        
        ##### Изменение hostname хоста #####
        self.change_hostname.clicked.connect(self.check_hostnameClicked)
        
        ##### Изменение hostname хоста #####
        self.change_hostname.clicked.connect(self.check_hostnameClicked)
        
    ##### ФУНКЦИЯ STABLE репозитории #####
    ######################################
    def toggle_stable_repo(self):
        if self.stable_repo.isChecked():
            self.update_file_line_stable_repo('change_stable_repositories: true')
        else:
            self.update_file_line_stable_repo('change_stable_repositories: false')

    def update_file_line_stable_repo(self, new_line):
        with fileinput.FileInput('../roles/network_and_domain/vars/main.yml', inplace=True) as file:
            for line in file:
                if 'change_stable_repositories:' in line:
                    print(new_line)
                else:
                    print(line, end='')
    
    ##### ФУНКЦИЯ FROZEN репозитории #####
    ######################################
    def toggle_frozen_repo(self):
        if self.frozen_repo.isChecked():
            self.update_file_line_frozen_repo('change_frozen_repositories: true')
        else:
            self.update_file_line_frozen_repo('change_frozen_repositories: false')

    def update_file_line_frozen_repo(self, new_line):
        with fileinput.FileInput('../roles/network_and_domain/vars/main.yml', inplace=True) as file:
            for line in file:
                if 'change_frozen_repositories:' in line:
                    print(new_line)
                else:
                    print(line, end='')
    
    ##### Сетевая настройка хоста #####
    ###################################
    def toggle_change_network(self):
        if self.check_network.isChecked():
            self.update_file_line_check_network('change_network: true')
        else:
            self.update_file_line_check_network('change_network: false')

    def update_file_line_check_network(self, new_line):
        with fileinput.FileInput('../roles/network_and_domain/vars/main.yml', inplace=True) as file:
            for line in file:
                if 'change_network:' in line:
                    print(new_line)
                else:
                    print(line, end='')
    
    ##### Изменение hostname хоста #####
    ####################################
    def toggle_change_hostname(self):
        if self.change_hostname.isChecked():
            self.update_file_line_change_hostname('change_hostname: true')
        else:
            self.update_file_line_change_hostname('change_hostname: false')

    def update_file_line_change_hostname(self, new_line):
        with fileinput.FileInput('../roles/network_and_domain/vars/main.yml', inplace=True) as file:
            for line in file:
                if 'change_hostname:' in line:
                    print(new_line)
                else:
                    print(line, end='')
                    
    ##### Присоединение к домену ######
    ###################################
    def toggle_change_domain(self):
        if self.change_domain.isChecked():
            self.update_file_line_change_domain('change_domain: true')
        else:
            self.update_file_line_change_domain('change_domain: false')

    def update_file_line_change_domain(self, new_line):
        with fileinput.FileInput('../roles/network_and_domain/vars/main.yml', inplace=True) as file:
            for line in file:
                if 'change_domain:' in line:
                    print(new_line)
                else:
                    print(line, end='')
    
    ##### Изменение обоев рабочего стола ######
    ###########################################
    def toggle_change_wallpaper(self):
        if self.change_wallpaper.isChecked():
            self.update_file_line_change_wallpaper('change_wallpaper: true')
        else:
            self.update_file_line_change_wallpaper('change_wallpaper: false')

    def update_file_line_change_wallpaper(self, new_line):
        with fileinput.FileInput('../roles/network_and_domain/vars/main.yml', inplace=True) as file:
            for line in file:
                if 'change_wallpaper:' in line:
                    print(new_line)
                else:
                    print(line, end='')
                    
    ##### Изменение обоев при входе #####
    #####################################
    def toggle_change_wallpaper_background(self):
        if self.change_wallpaper_background.isChecked():
            self.update_file_line_change_wallpaper_background('change_wallpaper_background: true')
        else:
            self.update_file_line_change_wallpaper_background('change_wallpaper_background: false')

    def update_file_line_change_wallpaper_background(self, new_line):
        with fileinput.FileInput('../roles/network_and_domain/vars/main.yml', inplace=True) as file:
            for line in file:
                if 'change_wallpaper_background:' in line:
                    print(new_line)
                else:
                    print(line, end='')
    
    ##### Функции проверяюих кнопок #####
    #####################################
    ##### Сетевая настройка #####
    def check_networkClicked(self):
        if self.check_network.isChecked():
            self.DNS.setEnabled(True)
            self.IP.setEnabled(True)
            self.Netmask.setEnabled(True)
            self.Gateway.setEnabled(True)
        else:
            self.DNS.setEnabled(False)
            self.IP.setEnabled(False)
            self.Netmask.setEnabled(False)
            self.Gateway.setEnabled(False)
            
    ##### Изменение hostname хоста #####
    def check_hostnameClicked(self):
        if self.change_hostname.isChecked():
            self.Hostname.setEnabled(True)
        else:
            self.Hostname.setEnabled(False)
    
    ##### Присоединение к домену #####
    def check_domainClicked(self):
        if self.change_domain.isChecked():
            self.SearchDomain.setEnabled(True)
            self.PasswordAdmin.setEnabled(True)
            self.LoginAdmin.setEnabled(True)
        else:
            self.SearchDomain.setEnabled(False)
            self.PasswordAdmin.setEnabled(False)
            self.LoginAdmin.setEnabled(False)
    
    ##### ОБНОВЛЕНИЕ СТРОК #####
    ############################
    ##### ОБНОВЛЕНИЕ СТРОКИ IP #####
    def update_ip_in_file(self, ip):
        file_path = "../roles/network_and_domain/vars/main.yml"
        need_line = "ip4: "
        with fileinput.FileInput(file_path, inplace=True) as file:
            for line in file:
                if need_line in line:
                    updated_line = need_line + '"' + ip + '"\n'
                    print(updated_line, end='')
                else:
                    print(line, end='')
                    
    def IP(self):
        ip = self.IP.text()
        self.update_ip_in_file(ip)

    ##### ОБНОВЛЕНИЕ СТРОКИ DNS #####
    def update_dns_in_file(self, dns):
        file_path = "../roles/network_and_domain/vars/main.yml"
        need_line = "dns: "
        with fileinput.FileInput(file_path, inplace=True) as file:
            for line in file:
                if need_line in line:
                    updated_line = need_line + '"' + dns + '"\n'
                    print(updated_line, end='')
                else:
                    print(line, end='')
                    
    def DNS(self):
        dns = self.DNS.text()
        self.update_dns_in_file(dns)
        
    ##### ОБНОВЛЕНИЕ СТРОКИ GATEWAY #####
    def update_gateway_in_file(self, gateway):
        file_path = "../roles/network_and_domain/vars/main.yml"
        need_line = "gateway: "
        with fileinput.FileInput(file_path, inplace=True) as file:
            for line in file:
                if need_line in line:
                    updated_line = need_line + '"' + gateway + '"\n'
                    print(updated_line, end='')
                else:
                    print(line, end='')
                    
    def Gateway(self):
        gateway = self.Gateway.text()
        self.update_gateway_in_file(gateway)
        
    ##### ОБНОВЛЕНИЕ СТРОКИ NETMASK #####
    def update_netmask_in_file(self, netmask):
        file_path = "../roles/network_and_domain/vars/main.yml"
        need_line = "netmask: "
        with fileinput.FileInput(file_path, inplace=True) as file:
            for line in file:
                if need_line in line:
                    updated_line = need_line + '"' + netmask + '"\n'
                    print(updated_line, end='')
                else:
                    print(line, end='')
                    
    def Netmask(self):
        netmask = self.Netmask.text()
        self.update_netmask_in_file(netmask)

    ##### ОБНОВЛЕНИЕ СТРОКИ HOSTNAME #####
    def update_hostname_in_file(self, hostname):
        file_path = "../roles/network_and_domain/vars/main.yml"
        need_line = "new_hostname: "
        with fileinput.FileInput(file_path, inplace=True) as file:
            for line in file:
                if need_line in line:
                    updated_line = need_line + '"' + hostname + '"\n'
                    print(updated_line, end='')
                else:
                    print(line, end='')
                    
    def Hostname(self):
        hostname = self.Hostname.text()
        self.update_hostname_in_file(hostname)
        
        
    ##### ОБНОВЛЕНИЕ ИМЕНИ ДОМЕНА #####    
    def update_domain_in_file(self, domain):
        file_path = "../roles/network_and_domain/vars/main.yml"
        need_line = "domain_search: "
        with fileinput.FileInput(file_path, inplace=True) as file:
            for line in file:
                if need_line in line:
                    updated_line = need_line + '"' + domain + '"\n'
                    print(updated_line, end='')
                else:
                    print(line, end='')
                    
    def SearchDomain(self):
        domain = self.SearchDomain.text()
        self.update_domain_in_file(domain)
        
    ##### ОБНОВЛЕНИЕ ИМЕНИ АДМИНА ДОМЕНА #####    
    def update_admin_login_in_file(self, admin_login):
        file_path = "../roles/network_and_domain/vars/main.yml"
        need_line = "domain_admin: "
        with fileinput.FileInput(file_path, inplace=True) as file:
            for line in file:
                if need_line in line:
                    updated_line = need_line + '"' + admin_login + '"\n'
                    print(updated_line, end='')
                else:
                    print(line, end='')
                    
    def LoginAdmin(self):
        admin_login = self.LoginAdmin.text()
        self.update_admin_login_in_file(admin_login)
        
    ##### ОБНОВЛЕНИЕ ПАРОЛЯ АДМИНА ДОМЕНА #####    
    def update_admin_password_in_file(self, admin_password):
        file_path = "../roles/network_and_domain/vars/main.yml"
        need_line = "domain_admin_password: "
        with fileinput.FileInput(file_path, inplace=True) as file:
            for line in file:
                if need_line in line:
                    updated_line = need_line + '"' + admin_password + '"\n'
                    print(updated_line, end='')
                else:
                    print(line, end='')
                    
    def PasswordAdmin(self):
        admin_password = self.PasswordAdmin.text()
        self.update_admin_password_in_file(admin_password)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
