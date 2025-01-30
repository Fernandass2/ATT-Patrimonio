import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from patrimonio import Patrimonio
from localizacao import localizacao
from localizar_patrimonio import localizar_patrimonio

class TelaInicial(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerenciar")
        self.setGeometry(300,200,200,150)
        self.layout_v = QVBoxLayout()

        self.label_titulo = QLabel("Clique pra abrir a janela")
        self.button = QPushButton("Abrir Patrimônio")
        self.button2 = QPushButton("Abrir Localização")
        self.btnbuscar = QPushButton("Localizar Patrimônio")

        self.layout_v.addWidget(self.label_titulo)
        self.layout_v.addWidget(self.button)
        self.layout_v.addWidget(self.button2)
        self.layout_v.addWidget(self.btnbuscar)
        
        
        self.button.clicked.connect(self.abrir_cadastro)
        self.button2.clicked.connect(self.localizacao)
        self.btnbuscar.clicked.connect(self.localizar_patrimonio)


        self.setLayout(self.layout_v)
    
    def abrir_cadastro(self):
        self.pat = Patrimonio()
        self.pat.show()

    def localizacao(self):
        self.pat = localizacao()
        self.pat.show()

    def localizar_patrimonio(self):
        self.pat = localizar_patrimonio()
        self.pat.show()

app = QApplication(sys.argv)
tela = TelaInicial()
tela.show()
app.exec()
