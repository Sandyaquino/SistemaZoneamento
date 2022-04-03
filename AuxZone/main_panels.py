from PyQt5.QtWidgets import QWidget, QGroupBox, QPushButton, QVBoxLayout, QPlainTextEdit, QFormLayout
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QWidget, QGroupBox, QPushButton, QVBoxLayout, QPlainTextEdit, QFormLayout
from PyQt5.QtCore import Qt

import main_actions
import main_toolbar

class C_MainPanel(QWidget):
    def __init__(self, MainWidget):
        QWidget.__init__(self)

        self.MainWidget = MainWidget
        #self. = main_toolbar.C_MenuToolBar()

        self.MainPainel_mainLayout = QVBoxLayout()#Layout da caixa mais externa na tela.

        #GroupBoxs
        self.MainPainel_Enderecos_GroupBox = QGroupBox("Endereços")#Caixa endereço.
        self.MainPainel_Enderecos_GroupBox.setFixedHeight(350)
        self.MainPainel_Enderecos_Vips_GroupBox = QGroupBox("Endereços Vips")  # Caixa endereço.
        self.MainPainel_Enderecos_Vips_GroupBox.setFixedHeight(200)

        #QTextEdit
        self.Main_Recebe_Endereco_QPlainTextEdit = QPlainTextEdit()#Objeto que cria o QTextEdit, widget que recebe o texto do endereço.
        self.Main_Recebe_Endereco_QPlainTextEdit.setFixedHeight(150)
        self.Main_Recebe_Endereco_QPlainTextEdit.setPlaceholderText("Os endereços serão mostrados aqui ...")#Texto Default que será lido na caixa de texto.
        self.Main_Recebe_Endereco_QPlainTextEdit.isReadOnly()
        self.Main_Recebe_Endereco_QPlainTextEdit.setReadOnly(False)
        self.Main_Recebe_Endereco_QPlainTextEdit.setAcceptDrops(False)

        self.Main_Recebe_Arquivo_QPlainTextEdit = QPlainTextEdit()
        self.Main_Recebe_Arquivo_QPlainTextEdit.setFixedHeight(60)
        self.Main_Recebe_Arquivo_QPlainTextEdit.setFixedWidth(300)
        self.Main_Recebe_Arquivo_QPlainTextEdit.setPlaceholderText("Selecione o Arquivo ...")#Texto Default que será lido na caixa de texto.
        self.Main_Recebe_Arquivo_QPlainTextEdit.setAcceptDrops(False)

        #QTextEdit
        self.Main_Recebe_Endereco_vip_QPlainTextEdit = QPlainTextEdit()#Objeto que cria o QTextEdit, widget que recebe o texto do endereço.
        self.Main_Recebe_Endereco_vip_QPlainTextEdit.setFixedHeight(150)
        self.Main_Recebe_Endereco_vip_QPlainTextEdit.setPlaceholderText("Os endereços vips serão mostrados aqui ...")#Texto Default que será lido na caixa de texto.
        self.Main_Recebe_Endereco_vip_QPlainTextEdit.isReadOnly()
        self.Main_Recebe_Endereco_vip_QPlainTextEdit.setReadOnly(False)
        self.Main_Recebe_Endereco_vip_QPlainTextEdit.setAcceptDrops(False)

        #QPushButton
        self.Main_seleciona_endereco_QPushButton = QPushButton("Selecionar Arquivo")
        self.Main_seleciona_endereco_QPushButton.setFixedWidth(150)
        self.Main_seleciona_endereco_QPushButton.clicked.connect(self.selecionar_arquivo)

        self.Main_Copia_Endereco_QPushButton = QPushButton("TESTE")#Botão que aciona a cópia do dendereço.
        self.Main_Copia_Endereco_QPushButton.setFixedWidth(100)
        self.Main_Copia_Endereco_QPushButton.clicked.connect(self.teste)
        self.Main_Limpar_Endereco_QPushButton = QPushButton("Limpar")#Botão que aciona a cópia do dendereço.
        self.Main_Limpar_Endereco_QPushButton.setFixedWidth(150)
        self.Main_Limpar_Endereco_QPushButton.clicked.connect(self.limpar_area_de_arquivo)


        #Layouts
        self.MainPainel_Recebe_Endereco_QFormLayout = QFormLayout()#Layout da caixa de texto que recebera o endereço.
        self.MainPainel_Recebe_Endereco_vip_QFormLayout = QFormLayout()
        self.MainPainel_Recebe_Endereco_QFormLayout.setAlignment(Qt.AlignTop)

        self.MainPainel_Recebe_Endereco_QVBoxLayout = QVBoxLayout()
        self.MainPainel_Recebe_Endereco_vip_QVBoxLayout = QVBoxLayout()

        #Adcionando e posicionando Widget nos Layouts criados
        self.MainPainel_Recebe_Endereco_QFormLayout.addRow(self.Main_Recebe_Arquivo_QPlainTextEdit, self.MainPainel_Recebe_Endereco_QVBoxLayout)
        self.MainPainel_Recebe_Endereco_QFormLayout.addRow(self.Main_Recebe_Endereco_QPlainTextEdit)#Adciona na caixa de endereço um widget na posição indicada.
        self.MainPainel_Recebe_Endereco_QFormLayout.addRow(self.Main_Copia_Endereco_QPushButton)

        self.MainPainel_Recebe_Endereco_vip_QFormLayout.addRow(self.Main_Recebe_Endereco_vip_QPlainTextEdit)

        self.MainPainel_Recebe_Endereco_QVBoxLayout.addWidget(self.Main_seleciona_endereco_QPushButton)
        self.MainPainel_Recebe_Endereco_QVBoxLayout.addWidget(self.Main_Limpar_Endereco_QPushButton)


        self.MainPainel_mainLayout.addWidget(self.MainPainel_Enderecos_GroupBox)
        self.MainPainel_mainLayout.addWidget(self.MainPainel_Enderecos_Vips_GroupBox)


        #SetLayout - indicando o tipo de layout de cada Widget presente.
        self.MainPainel_Enderecos_GroupBox.setLayout(self.MainPainel_Recebe_Endereco_QFormLayout)
        self.MainPainel_Enderecos_Vips_GroupBox.setLayout(self.MainPainel_Recebe_Endereco_vip_QFormLayout)
        self.setLayout(self.MainPainel_mainLayout)

    def escreve_endereco(self, Endereco):
        self.Main_Recebe_Endereco_QPlainTextEdit.setPlainText(Endereco)

    def escreve_enderecos_vips(self, Enderecos_Vips):

        if len(Enderecos_Vips.items()) == 0:
            self.Main_Recebe_Endereco_vip_QPlainTextEdit.insertPlainText("Não Existe cliente Vip")
        for responsavel, tipo_de_vip in Enderecos_Vips.items():
            self.Main_Recebe_Endereco_vip_QPlainTextEdit.insertPlainText(str(responsavel)+": " + str(tipo_de_vip) + "\n")

    def selecionar_arquivo(self):
        self.Actions.execopenFileNamesDialog()

    def limpar_area_de_arquivo(self):
        self.Actions.exec_limpar_area_de_arquivo()

    def teste(self):
        self.Actions.conectar_banco()


    @property
    def MainWidget(self):
        return self.__parent

    @MainWidget.setter
    def MainWidget(self, value):
        self.__parent = value