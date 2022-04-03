from PyQt5.QtWidgets import QDockWidget, QAction, QMenuBar, QToolBar, QDialog, QFileDialog
from PyQt5.QtGui import QIcon
import pandas as pd

import main_panels
import config as cfg
import os
import platform

class C_MenuToolBar(QDockWidget):
    def __init__(self, MainWin = None):

        QDockWidget.__init__(self)

        self.MainMenu = QMenuBar()

        self.mainPainal = main_panels.C_MainPanel(None)

        if MainWin != None:
            self.MainWin = MainWin
            self.MainMenu = self.MainWin.menuBar()

        self.MainMenu.setObjectName("MenuApp")

        ########################################################

        # ******* Actions the Power System Network Menu  *******
        self.NetActRef = {'Net_Select_Act': 0}

        # ******* Create the Power System Network Menu *******
        self.NetMenu = self.MainMenu.addMenu('&Endereçamento')

        self.Net_Select_Act = QAction(QIcon(''), 'Seleciona arquivo', self)
        self.Net_Select_Act.setShortcut("Ctrl+N")
        self.Net_Select_Act.setStatusTip('Seleciona Arquivo')
        self.Net_Select_Act.triggered.connect(self.exec_selectFile)
        self.Net_Select_Act.setObjectName('Net_Select_Act')
        self.NetActRef['Net_Select_Act'] = self.Net_Select_Act

        # ******* Setup the Configuration Menu ****
        self.NetMenu.addAction(self.Net_Select_Act)


        # ******* Actions the Power System Network Menu  *******
        self.NetConRef = {'Net_Convert_Act': 0, 'Net_Convert_bloco_Act': 0}

        # ******* Create the Power System Network Menu *******
        self.NetMenuConvert = self.MainMenu.addMenu('&Converter para Excel')

        self.Net_Convert_Act = QAction(QIcon(''), 'Converter para Excel', self)
        self.Net_Convert_Act.setShortcut("Ctrl+1")
        self.Net_Convert_Act.setStatusTip('Seleciona Arquivo para Conversão')
        self.Net_Convert_Act.triggered.connect(self.exec_ConvertFileforExcel)
        self.Net_Convert_Act.setObjectName('Net_Convert_Act')
        self.NetConRef['Net_Convert_Act'] = self.Net_Convert_Act

        self.Net_Convert_bloco_Act = QAction(QIcon(''), 'Converter para Excel em Bloco', self)
        self.Net_Convert_bloco_Act.setShortcut("Ctrl+2")
        self.Net_Convert_bloco_Act.setStatusTip('Seleciona pasta de Arquivos para Conversão')
        self.Net_Convert_bloco_Act.triggered.connect(self.exec_ConvertBlockFileforExcel)
        self.Net_Convert_bloco_Act.setObjectName('Net_Convert_bloco_Act')
        self.NetConRef['Net_Convert_bloco_Act'] = self.Net_Convert_bloco_Act

        # ******* Setup the Configuration Menu ****
        self.NetMenuConvert.addAction(self.Net_Convert_Act)
        self.NetMenuConvert.addAction(self.Net_Convert_bloco_Act)


        # ******* Actions the Help Menu  *******
        self.GerarActRef = {'Gerar_Act': 0}

        # ******* Create the Help Menu *******
        self.GerarMenu = self.MainMenu.addMenu('&Gerar')


        self.Gerar_Act = QAction(QIcon(''), 'G&erar atualização de informações na SI', self)
        self.Gerar_Act.setShortcut("Ctrl+G")
        self.Gerar_Act.setStatusTip('G&erar atualização de informações na SI')
        self.Gerar_Act.triggered.connect(self.exec_GerarAtualizacaodeInformacoes_naSI)
        self.Gerar_Act.setObjectName('Gerar_Act')
        self.GerarActRef['self.Gerar_Act'] = self.Gerar_Act

        self.Gerar_zoneamento_Act = QAction(QIcon(''), 'G&erar Zoneamento', self)
        self.Gerar_zoneamento_Act.setShortcut("Ctrl+Z")
        self.Gerar_zoneamento_Act.setStatusTip('G&erar Arquivo de Zoneamento')
        self.Gerar_zoneamento_Act.triggered.connect(self.exec_GerarArquivo_do_Zoneamento)
        self.Gerar_zoneamento_Act.setObjectName('Gerar_zoneamento_Act')
        self.GerarActRef['self.Gerar_zoneamento_Act'] = self.Gerar_zoneamento_Act

        # ******* Setup the Configuration Menu ****
        self.GerarMenu.addAction(self.Gerar_Act)
        self.GerarMenu.addAction(self.Gerar_zoneamento_Act)



        # ******* Actions the Help Menu  *******
        self.HelpActRef = {'Help_About_Act': 0}

        # ******* Create the Help Menu *******
        self.HelpMenu = self.MainMenu.addMenu('&Ajuda')
        self.Help_About_Act = QAction(QIcon(''), 'So&bre', self)
        self.Help_About_Act.setShortcut("Ctrl+H")
        self.Help_About_Act.setStatusTip('Sobre o Adressing')
        self.Help_About_Act.triggered.connect(self.exec_aboutSIA)
        self.Help_About_Act.setObjectName('Help_About_Act')
        self.HelpActRef['Help_About_Act'] = self.Help_About_Act

        # ******* Create Help  Menu Items ***

        # ******* Setup the Help Menu *******
        self.HelpMenu.addAction(self.Help_About_Act)

        if MainWin != None:
            self.InitToolBar(MainWin)

    def InitToolBar(self, MainWin = None):

            # Dynamically Add Items to the Toolbar

            self.mainToolBar = MainWin.addToolBar("Acesso Rápido")

            self.mainToolBar.setObjectName("ToolBarApp")

            # This represents reading these values in via a Query
            toolBarNetworkLayout =  {0: 'Net_Select_Act',
                                     1: 'Spacer'}

    def exec_selectFile(self): #
        self.Actions.execopenFileNamesDialog()

    def exec_ConvertFileforExcel(self): #
        self.Actions.exec_Convert_arquivo_unico_para_excel()

    def exec_ConvertBlockFileforExcel(self): #
        self.Actions.exec_Convert_varios_arquivos_de_uma_pasta()

    def exec_GerarAtualizacaodeInformacoes_naSI(self):
        self.Actions.exec_adcionar_informacoes_na_si()

    def exec_GerarArquivo_do_Zoneamento(self):
        #self.Actions.exec_gerar_arquivo_final_zoneamento()

        self.Actions.exec_gerar_arquivo_final_zoneamento_teste1()

    def exec_aboutSIA(self):
        print("exec_selectFile")

