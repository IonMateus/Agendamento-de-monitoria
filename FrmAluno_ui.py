# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrmAluno.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QRadioButton, QSizePolicy,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QToolBar, QWidget)
import recursos_rc

class Ui_FrmAluno(object):
    def setupUi(self, FrmAluno):
        if not FrmAluno.objectName():
            FrmAluno.setObjectName(u"FrmAluno")
        FrmAluno.resize(622, 412)
        self.actionConex_o = QAction(FrmAluno)
        self.actionConex_o.setObjectName(u"actionConex_o")
        self.actionSair = QAction(FrmAluno)
        self.actionSair.setObjectName(u"actionSair")
        self.actionListar = QAction(FrmAluno)
        self.actionListar.setObjectName(u"actionListar")
        self.actionSair_2 = QAction(FrmAluno)
        self.actionSair_2.setObjectName(u"actionSair_2")
        self.action_Novo = QAction(FrmAluno)
        self.action_Novo.setObjectName(u"action_Novo")
        icon = QIcon()
        icon.addFile(u":/icones/botoes/Add.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Novo.setIcon(icon)
        self.action_Editar = QAction(FrmAluno)
        self.action_Editar.setObjectName(u"action_Editar")
        icon1 = QIcon()
        icon1.addFile(u":/icones/botoes/COPY.BMP", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Editar.setIcon(icon1)
        self.action_Salvar = QAction(FrmAluno)
        self.action_Salvar.setObjectName(u"action_Salvar")
        icon2 = QIcon()
        icon2.addFile(u":/icones/botoes/Save.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Salvar.setIcon(icon2)
        self.action_Excluir = QAction(FrmAluno)
        self.action_Excluir.setObjectName(u"action_Excluir")
        icon3 = QIcon()
        icon3.addFile(u":/icones/botoes/Minus.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Excluir.setIcon(icon3)
        self.action_Cancelar = QAction(FrmAluno)
        self.action_Cancelar.setObjectName(u"action_Cancelar")
        icon4 = QIcon()
        icon4.addFile(u":/icones/botoes/UNDO.BMP", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Cancelar.setIcon(icon4)
        self.action_Buscar = QAction(FrmAluno)
        self.action_Buscar.setObjectName(u"action_Buscar")
        icon5 = QIcon()
        icon5.addFile(u":/icones/botoes/FIND.BMP", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Buscar.setIcon(icon5)
        self.action_Inicio = QAction(FrmAluno)
        self.action_Inicio.setObjectName(u"action_Inicio")
        icon6 = QIcon()
        icon6.addFile(u":/icones/botoes/first.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Inicio.setIcon(icon6)
        self.action_Anterior = QAction(FrmAluno)
        self.action_Anterior.setObjectName(u"action_Anterior")
        icon7 = QIcon()
        icon7.addFile(u":/icones/botoes/prior.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Anterior.setIcon(icon7)
        self.action_Proximo = QAction(FrmAluno)
        self.action_Proximo.setObjectName(u"action_Proximo")
        icon8 = QIcon()
        icon8.addFile(u":/icones/botoes/next.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Proximo.setIcon(icon8)
        self.action_Fim = QAction(FrmAluno)
        self.action_Fim.setObjectName(u"action_Fim")
        icon9 = QIcon()
        icon9.addFile(u":/icones/botoes/last.bmp", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Fim.setIcon(icon9)
        self.action_Sair = QAction(FrmAluno)
        self.action_Sair.setObjectName(u"action_Sair")
        icon10 = QIcon()
        icon10.addFile(u":/icones/botoes/CLOSE1.BMP", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Sair.setIcon(icon10)
        self.centralwidget = QWidget(FrmAluno)
        self.centralwidget.setObjectName(u"centralwidget")
        self.abas = QTabWidget(self.centralwidget)
        self.abas.setObjectName(u"abas")
        self.abas.setGeometry(QRect(0, 0, 611, 381))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.abas.setFont(font)
        self.abas.setCursor(QCursor(Qt.IBeamCursor))
        self.tabCadastro = QWidget()
        self.tabCadastro.setObjectName(u"tabCadastro")
        self.label = QLabel(self.tabCadastro)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 15, 221, 21))
        self.label_2 = QLabel(self.tabCadastro)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 51, 21))
        self.label_3 = QLabel(self.tabCadastro)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 90, 211, 21))
        self.edNome = QLineEdit(self.tabCadastro)
        self.edNome.setObjectName(u"edNome")
        self.edNome.setGeometry(QRect(250, 50, 301, 31))
        self.edNome.setMaxLength(30)
        self.edNome.setReadOnly(True)
        self.edRA = QLineEdit(self.tabCadastro)
        self.edRA.setObjectName(u"edRA")
        self.edRA.setGeometry(QRect(250, 10, 71, 31))
        self.edRA.setMaxLength(5)
        self.edRA.setReadOnly(True)
        self.cbxCurso = QComboBox(self.tabCadastro)
        self.cbxCurso.setObjectName(u"cbxCurso")
        self.cbxCurso.setEnabled(False)
        self.cbxCurso.setGeometry(QRect(250, 91, 301, 31))
        icon11 = QIcon()
        icon11.addFile(u":/icones/COPY.BMP", QSize(), QIcon.Normal, QIcon.Off)
        self.abas.addTab(self.tabCadastro, icon11, "")
        self.tabListagem = QWidget()
        self.tabListagem.setObjectName(u"tabListagem")
        self.grdAluno = QTableWidget(self.tabListagem)
        if (self.grdAluno.columnCount() < 3):
            self.grdAluno.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(255, 255, 0));
        self.grdAluno.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.grdAluno.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.grdAluno.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.grdAluno.setObjectName(u"grdAluno")
        self.grdAluno.setGeometry(QRect(145, 64, 331, 211))
        self.grdAluno.setFrameShadow(QFrame.Sunken)
        self.groupBox = QGroupBox(self.tabListagem)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(130, 4, 361, 51))
        self.groupBox.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.rbPorRA = QRadioButton(self.groupBox)
        self.rbPorRA.setObjectName(u"rbPorRA")
        self.rbPorRA.setGeometry(QRect(10, 20, 91, 17))
        self.rbPorRA.setChecked(True)
        self.rbPorNome = QRadioButton(self.groupBox)
        self.rbPorNome.setObjectName(u"rbPorNome")
        self.rbPorNome.setGeometry(QRect(115, 20, 111, 20))
        self.rbPorCurso = QRadioButton(self.groupBox)
        self.rbPorCurso.setObjectName(u"rbPorCurso")
        self.rbPorCurso.setGeometry(QRect(241, 20, 111, 20))
        icon12 = QIcon()
        icon12.addFile(u":/icones/WINPREV.BMP", QSize(), QIcon.Normal, QIcon.Off)
        self.abas.addTab(self.tabListagem, icon12, "")
        FrmAluno.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(FrmAluno)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 622, 22))
        self.menuCadastro = QMenu(self.menubar)
        self.menuCadastro.setObjectName(u"menuCadastro")
        self.menuListagem = QMenu(self.menubar)
        self.menuListagem.setObjectName(u"menuListagem")
        self.menuSair = QMenu(self.menubar)
        self.menuSair.setObjectName(u"menuSair")
        FrmAluno.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(FrmAluno)
        self.statusbar.setObjectName(u"statusbar")
        FrmAluno.setStatusBar(self.statusbar)
        self.tbBotoes = QToolBar(FrmAluno)
        self.tbBotoes.setObjectName(u"tbBotoes")
        self.tbBotoes.setOrientation(Qt.Horizontal)
        self.tbBotoes.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        FrmAluno.addToolBar(Qt.TopToolBarArea, self.tbBotoes)

        self.menubar.addAction(self.menuCadastro.menuAction())
        self.menubar.addAction(self.menuListagem.menuAction())
        self.menubar.addAction(self.menuSair.menuAction())
        self.menuCadastro.addAction(self.actionConex_o)
        self.menuCadastro.addSeparator()
        self.menuCadastro.addAction(self.actionSair)
        self.menuListagem.addAction(self.actionListar)
        self.menuSair.addAction(self.actionSair_2)
        self.tbBotoes.addAction(self.action_Inicio)
        self.tbBotoes.addAction(self.action_Anterior)
        self.tbBotoes.addAction(self.action_Proximo)
        self.tbBotoes.addAction(self.action_Fim)
        self.tbBotoes.addSeparator()
        self.tbBotoes.addAction(self.action_Buscar)
        self.tbBotoes.addSeparator()
        self.tbBotoes.addAction(self.action_Novo)
        self.tbBotoes.addAction(self.action_Editar)
        self.tbBotoes.addAction(self.action_Salvar)
        self.tbBotoes.addSeparator()
        self.tbBotoes.addAction(self.action_Cancelar)
        self.tbBotoes.addSeparator()
        self.tbBotoes.addAction(self.action_Excluir)
        self.tbBotoes.addSeparator()
        self.tbBotoes.addAction(self.action_Sair)

        self.retranslateUi(FrmAluno)

        self.abas.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(FrmAluno)
    # setupUi

    def retranslateUi(self, FrmAluno):
        FrmAluno.setWindowTitle(QCoreApplication.translate("FrmAluno", u"Manuten\u00e7\u00e3o de Alunos", None))
#if QT_CONFIG(tooltip)
        FrmAluno.setToolTip(QCoreApplication.translate("FrmAluno", u"Cadastro de Alunos", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        FrmAluno.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.actionConex_o.setText(QCoreApplication.translate("FrmAluno", u"Conex\u00e3o", None))
        self.actionSair.setText(QCoreApplication.translate("FrmAluno", u"Sair", None))
        self.actionListar.setText(QCoreApplication.translate("FrmAluno", u"Listar", None))
        self.actionSair_2.setText(QCoreApplication.translate("FrmAluno", u"Sair", None))
        self.action_Novo.setText(QCoreApplication.translate("FrmAluno", u"&Novo", None))
#if QT_CONFIG(tooltip)
        self.action_Novo.setToolTip(QCoreApplication.translate("FrmAluno", u"Incluir novo registro", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_Novo.setShortcut(QCoreApplication.translate("FrmAluno", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.action_Editar.setText(QCoreApplication.translate("FrmAluno", u"&Editar", None))
#if QT_CONFIG(tooltip)
        self.action_Editar.setToolTip(QCoreApplication.translate("FrmAluno", u"Altera dados do registro em exibi\u00e7\u00e3o", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_Editar.setShortcut(QCoreApplication.translate("FrmAluno", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.action_Salvar.setText(QCoreApplication.translate("FrmAluno", u"&Salvar", None))
#if QT_CONFIG(tooltip)
        self.action_Salvar.setToolTip(QCoreApplication.translate("FrmAluno", u"Grava o registro atual no banco de dados", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_Salvar.setShortcut(QCoreApplication.translate("FrmAluno", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_Excluir.setText(QCoreApplication.translate("FrmAluno", u"E&xcluir", None))
#if QT_CONFIG(tooltip)
        self.action_Excluir.setToolTip(QCoreApplication.translate("FrmAluno", u"Exclui o registro exibido na tela", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_Excluir.setShortcut(QCoreApplication.translate("FrmAluno", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.action_Cancelar.setText(QCoreApplication.translate("FrmAluno", u"&Cancelar", None))
#if QT_CONFIG(tooltip)
        self.action_Cancelar.setToolTip(QCoreApplication.translate("FrmAluno", u"Cancela a opera\u00e7\u00e3o atualmente em execu\u00e7\u00e3o", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_Cancelar.setShortcut(QCoreApplication.translate("FrmAluno", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.action_Buscar.setText(QCoreApplication.translate("FrmAluno", u"&Buscar", None))
#if QT_CONFIG(tooltip)
        self.action_Buscar.setToolTip(QCoreApplication.translate("FrmAluno", u"Busca o registro cujo c\u00f3digo foi digitado e o exibe", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_Buscar.setShortcut(QCoreApplication.translate("FrmAluno", u"Ctrl+B", None))
#endif // QT_CONFIG(shortcut)
        self.action_Inicio.setText(QCoreApplication.translate("FrmAluno", u"&In\u00edcio", None))
#if QT_CONFIG(tooltip)
        self.action_Inicio.setToolTip(QCoreApplication.translate("FrmAluno", u"Posiciona visualiza\u00e7\u00e3o no primeiro registro e o exibe", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_Inicio.setShortcut(QCoreApplication.translate("FrmAluno", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.action_Anterior.setText(QCoreApplication.translate("FrmAluno", u"&Anterior", None))
#if QT_CONFIG(tooltip)
        self.action_Anterior.setToolTip(QCoreApplication.translate("FrmAluno", u"Posiciona visualiza\u00e7\u00e3o no registro anterior ao atualmente exibido", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_Anterior.setShortcut(QCoreApplication.translate("FrmAluno", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.action_Proximo.setText(QCoreApplication.translate("FrmAluno", u"&Pr\u00f3ximo", None))
#if QT_CONFIG(tooltip)
        self.action_Proximo.setToolTip(QCoreApplication.translate("FrmAluno", u"Posiciona visualiza\u00e7\u00e3o no registro seguinte ao atual", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_Proximo.setShortcut(QCoreApplication.translate("FrmAluno", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.action_Fim.setText(QCoreApplication.translate("FrmAluno", u"&Fim", None))
#if QT_CONFIG(tooltip)
        self.action_Fim.setToolTip(QCoreApplication.translate("FrmAluno", u"Posiciona visualiza\u00e7\u00e3o no \u00faltimo registro e o exibe", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_Fim.setShortcut(QCoreApplication.translate("FrmAluno", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
        self.action_Sair.setText(QCoreApplication.translate("FrmAluno", u"Sai&r", None))
#if QT_CONFIG(tooltip)
        self.action_Sair.setToolTip(QCoreApplication.translate("FrmAluno", u"Fecha a conex\u00e3o, salva dados e fecha o formul\u00e1rio", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_Sair.setShortcut(QCoreApplication.translate("FrmAluno", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.abas.setToolTip(QCoreApplication.translate("FrmAluno", u"Manuten\u00e7\u00e3o de Alunos", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("FrmAluno", u"RA do(a) aluno(a):", None))
        self.label_2.setText(QCoreApplication.translate("FrmAluno", u"Nome:", None))
        self.label_3.setText(QCoreApplication.translate("FrmAluno", u"Curso:", None))
        self.edNome.setPlaceholderText(QCoreApplication.translate("FrmAluno", u"Nome do(a) Aluno(a)", None))
        self.edRA.setInputMask("")
        self.edRA.setPlaceholderText(QCoreApplication.translate("FrmAluno", u"RA", None))
        self.abas.setTabText(self.abas.indexOf(self.tabCadastro), QCoreApplication.translate("FrmAluno", u"Cadastro", None))
#if QT_CONFIG(tooltip)
        self.abas.setTabToolTip(self.abas.indexOf(self.tabCadastro), QCoreApplication.translate("FrmAluno", u"Manuten\u00e7\u00e3o dos registros de Alunos", None))
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem = self.grdAluno.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FrmAluno", u"RA", None));
        ___qtablewidgetitem1 = self.grdAluno.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FrmAluno", u"Nome", None));
        ___qtablewidgetitem2 = self.grdAluno.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FrmAluno", u"Curso", None));
        self.groupBox.setTitle(QCoreApplication.translate("FrmAluno", u"Ordem", None))
        self.rbPorRA.setText(QCoreApplication.translate("FrmAluno", u"Por RA", None))
        self.rbPorNome.setText(QCoreApplication.translate("FrmAluno", u"Por Nome", None))
        self.rbPorCurso.setText(QCoreApplication.translate("FrmAluno", u"Por Curso", None))
        self.abas.setTabText(self.abas.indexOf(self.tabListagem), QCoreApplication.translate("FrmAluno", u"Listagem", None))
#if QT_CONFIG(tooltip)
        self.abas.setTabToolTip(self.abas.indexOf(self.tabListagem), QCoreApplication.translate("FrmAluno", u"Lista os registros de Alunos", None))
#endif // QT_CONFIG(tooltip)
        self.menuCadastro.setTitle(QCoreApplication.translate("FrmAluno", u"Cadastro", None))
        self.menuListagem.setTitle(QCoreApplication.translate("FrmAluno", u"Listagem", None))
        self.menuSair.setTitle(QCoreApplication.translate("FrmAluno", u"Sair", None))
        self.tbBotoes.setWindowTitle(QCoreApplication.translate("FrmAluno", u"toolBar", None))
#if QT_CONFIG(tooltip)
        self.tbBotoes.setToolTip(QCoreApplication.translate("FrmAluno", u"Bot\u00f5es de a\u00e7\u00e3o", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

