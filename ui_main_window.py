# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1131, 767)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: #333333; /* Cor de fundo */\n"
"    color: #FFFFFF; /* Opcional: para o texto ficar branco e visível */\n"
"}\n"
"/* Você pode estilizar outros elementos se quiser um tema escuro */\n"
"QLabel {\n"
"    color: #FFFFFF; /* Texto dos labels brancos */\n"
"}\n"
"QLineEdit {\n"
"    background-color: #444444; /* Campo de texto mais escuro */\n"
"    color: #FFFFFF;\n"
"}\n"
"QListWidget {\n"
"    background-color: #444444; /* Fundo da lista */\n"
"    color: #FFFFFF;\n"
"}\n"
"QPushButton {\n"
"    background-color: #555555; /* Botões mais escuros */\n"
"    color: #FFFFFF;\n"
"    border: 1px solid #777777; /* Borda sutil */\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl_header_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_header_title.setFont(font)
        self.lbl_header_title.setStyleSheet("QLabel#lbl_header_title { /* O #lbl_header_title é para aplicar o estilo apenas a este QLabel específico */\n"
"    border: 2px solid #55aaff; /* Borda de 2px, sólida, cor azul clara */\n"
"    border-radius: 10px; /* Bordas arredondadas (opcional) */\n"
"    padding: 5px; /* Espaçamento interno entre o texto e a borda */\n"
"    background-color: #444444; /* Cor de fundo para o label, para destacá-lo (opcional) */\n"
"    color: #FFFFFF; /* Cor do texto (se o fundo for escuro) */\n"
"    /* Outras propriedades de fonte, alinhamento, etc., podem ser definidas aqui ou nas propriedades normais */\n"
"    font-size: 24pt; /* Exemplo: tamanho da fonte. \'pt\' é pontos */\n"
"    font-weight: bold; /* Exemplo: texto em negrito */\n"
"    qproperty-alignment: AlignCenter; /* Exemplo: alinhamento central. Note que aqui é \'qproperty-alignment\' */\n"
"}")
        self.lbl_header_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_header_title.setObjectName("lbl_header_title")
        self.verticalLayout_3.addWidget(self.lbl_header_title)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_timer = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Digital-7")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_timer.setFont(font)
        self.lbl_timer.setStyleSheet("QLabel#lbl_timer {\n"
"    background-color: #333333; /* Fundo bem escuro, quase preto */\n"
"    color: #00FF00; /* Cor verde brilhante (ou use #00FFFF para ciano, #FF0000 para vermelho) */\n"
"    border: 2px solid #00AA00; /* Borda verde um pouco mais escura */\n"
"    border-radius: 10px; /* Cantos arredondados */\n"
"    padding: 15px; /* Espaçamento interno generoso */\n"
"\n"
"    /* Fontes que parecem digitais (ou genéricas que funcionam bem) */\n"
"    font-family: \"Digital-7\", \"Consolas\", \"Monospace\"; /* Tente Digital-7 se instalada, senão Consolas ou Monospace */\n"
"    font-size: 72pt; /* Tamanho da fonte, pode ajustar */\n"
"    font-weight: bold; /* Negrito */\n"
"\n"
"    qproperty-alignment: AlignCenter; /* Garante que o texto esteja centralizado */\n"
"}")
        self.lbl_timer.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_timer.setObjectName("lbl_timer")
        self.verticalLayout.addWidget(self.lbl_timer)
        self.btn_start_pause = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start_pause.setObjectName("btn_start_pause")
        self.verticalLayout.addWidget(self.btn_start_pause)
        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.setObjectName("btn_reset")
        self.verticalLayout.addWidget(self.btn_reset)
        self.btn_skip = QtWidgets.QPushButton(self.centralwidget)
        self.btn_skip.setObjectName("btn_skip")
        self.verticalLayout.addWidget(self.btn_skip)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txt_new_task = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_new_task.setObjectName("txt_new_task")
        self.horizontalLayout.addWidget(self.txt_new_task)
        self.btn_add_task = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add_task.setObjectName("btn_add_task")
        self.horizontalLayout.addWidget(self.btn_add_task)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.list_tasks = QtWidgets.QListWidget(self.centralwidget)
        self.list_tasks.setObjectName("list_tasks")
        self.verticalLayout_2.addWidget(self.list_tasks)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_complete_task = QtWidgets.QPushButton(self.centralwidget)
        self.btn_complete_task.setObjectName("btn_complete_task")
        self.horizontalLayout_3.addWidget(self.btn_complete_task)
        self.btn_remove_task = QtWidgets.QPushButton(self.centralwidget)
        self.btn_remove_task.setObjectName("btn_remove_task")
        self.horizontalLayout_3.addWidget(self.btn_remove_task)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1131, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gerenciador Pomodoro"))
        self.lbl_header_title.setText(_translate("MainWindow", "Gerenciador de Produtividade"))
        self.lbl_timer.setText(_translate("MainWindow", "25:00"))
        self.btn_start_pause.setText(_translate("MainWindow", "iniciar"))
        self.btn_reset.setText(_translate("MainWindow", "Resetar"))
        self.btn_skip.setText(_translate("MainWindow", "Pular"))
        self.txt_new_task.setPlaceholderText(_translate("MainWindow", "Digite uma nova tarefa aqui...."))
        self.btn_add_task.setText(_translate("MainWindow", "Adicionar Tarefa"))
        self.btn_complete_task.setText(_translate("MainWindow", "Marcar Concluída"))
        self.btn_remove_task.setText(_translate("MainWindow", "Remover Tarefa"))
