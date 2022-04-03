import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QStyleFactory, QSplashScreen

import config
import main_toolbar
import main_panels
import main_actions

class mainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)

        self.titleWindow = config.__name__ + " - Version: " + config.__version__
        self.iconWindow = config.Addressing_icon
        self.stylesheet = "fusion"

        self.setWindowTitle(self.titleWindow)
        self.setWindowIcon(QIcon(self.iconWindow))  # ícone da janela
        #self.resize(1366, 768)
        self.resize(500, 500)
        #self.showMaximized()
        self.setStyle(QStyleFactory.create('Cleanlooks'))  # Estilo da Interface

        self.initUI()

    def initUI(self):
        self.mainToolBar = main_toolbar.C_MenuToolBar(self)  # Menu e ToolBar
        self.mainPainelCentral = main_panels.C_MainPanel(self)  # Painel Central
        self.mainActions = main_actions.C_MainActions()  # MainActions

        self.setCentralWidget(self.mainPainelCentral)

        ### Passando os Dados para o Actions
        #Passando endereçamento de memoria para os objetos criados no momento do primeiro instanciamento
        self.mainActions.MainWindowToolBar = self.mainToolBar
        self.mainActions.MainPainel = self.mainPainelCentral

        ### Passando os Dados
        self.mainToolBar.Actions = self.mainActions
        self.mainPainelCentral.Actions = self.mainActions



if __name__ == '__main__':
    AddressingApp = QApplication(sys.argv)

    # Create and display the splash screen
    #splash_pix = QPixmap('')
    #splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    #splash.setMask(splash_pix.mask())
    #splash.show()
    #AddressingApp.processEvents()

    GUI = mainWindow()
    GUI.show()
    #splash.close()
    sys.exit(AddressingApp.exec())
