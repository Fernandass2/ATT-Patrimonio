from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import sys 
import csv

class localizar_patrimonio(QWidget):
    def __init__(self):
        super().__init__()

        # Vamos configurar a geometria da tela. Setandos valores de posição X e Y,
        # além de largura e altura
        self.setGeometry(500,30,400,600)

        # Texto para a barra de título
        self.setWindowTitle("Patrimônio do Objeto")

        #Gerenciador de layout vertical
        self.layout_v = QVBoxLayout()

        # Labels para o id do objeto
        self.label_id = QLabel("ID do objeto:")
        self.label_id.setStyleSheet("QLabel{font-size:12pt}")
        #LineEdit para o id do objeto
        self.edit_id = QLineEdit()
        self.edit_id.setStyleSheet("QLineEdit{font-size:12pt}")
        #------------------------------------------------------

        # Labels para o número de série do objeto
        self.label_numero = QLabel("Número de série:")
        self.label_numero.setStyleSheet("QLabel{font-size:12pt}")
        #LineEdit para o id do objeto
        self.edit_numero = QLineEdit()
        self.edit_numero.setStyleSheet("QLineEdit{font-size:12pt}")
        #------------------------------------------------------

        # Labels para o nome do patrimônio
        self.label_nome_patrimonio = QLabel("Nome do Patrimônio:")
        self.label_nome_patrimonio.setStyleSheet("QLabel{font-size:12pt}")
        #LineEdit para o nome do patrimônio
        self.edit_nome_patrimonio = QLineEdit()
        self.edit_nome_patrimonio.setStyleSheet("QLineEdit{font-size:12pt}")
        #------------------------------------------------------

        # Labels para o tipo do objeto
        self.label_tipo = QLabel("Tipo do objeto:")
        self.label_tipo.setStyleSheet("QLabel{font-size:12pt}")
        #LineEdit para o tipo do objeto
        self.edit_tipo = QLineEdit()
        self.edit_tipo.setStyleSheet("QLineEdit{font-size:12pt}")
        #------------------------------------------------------

        # Labels para a descrição do objeto
        self.label_descricao = QLabel("Pequena descrição do objeto:")
        self.label_descricao.setStyleSheet("QLabel{font-size:12pt}")
        #LineEdit para o tipo do objeto
        self.edit_descricao = QLineEdit()
        self.edit_descricao.setStyleSheet("QLineEdit{font-size:12pt}")
        #------------------------------------------------------

        # Labels para a localização do objeto
        self.label_localizacao = QLabel("Sua localização:")
        self.label_localizacao.setStyleSheet("QLabel{font-size:12pt}")
        #LineEdit para o tipo do objeto
        self.edit_localizacao = QLineEdit()
        self.edit_localizacao.setStyleSheet("QLineEdit{font-size:12pt}")
        #------------------------------------------------------

        # Labels para a data de fabricação do objeto
        self.label_fabricacao = QLabel("Data de fabricação:")
        self.label_fabricacao.setStyleSheet("QLabel{font-size:12pt}")
        #LineEdit para o tipo do objeto
        self.edit_fabricacao = QLineEdit()
        self.edit_fabricacao.setStyleSheet("QLineEdit{font-size:12pt}")
        #------------------------------------------------------

        # Labels para a data de aquisição do objeto
        self.label_aquisicao = QLabel("Data de aquisição:")
        self.label_aquisicao.setStyleSheet("QLabel{font-size:12pt}")
        #LineEdit para o tipo do objeto
        self.edit_aquisicao = QLineEdit()
        self.edit_aquisicao.setStyleSheet("QLineEdit{font-size:12pt}")
        #------------------------------------------------------

        # Adicionar a Label id e o lineedit ao layout certical
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)
        self.btnbuscar=  QPushButton("Buscar Patrimônio")
        self.layout_v.addWidget(self.btnbuscar)
        self.btnbuscar.clicked.connect(self.localizar)

        # Adicionar a Label números de série e o lineedit ao layout certical
        self.layout_v.addWidget(self.label_numero)
        self.layout_v.addWidget(self.edit_numero)

        # Acionar a Label nome do patrimônio e o lineedit ao layout certical
        self.layout_v.addWidget(self.label_nome_patrimonio)
        self.layout_v.addWidget(self.edit_nome_patrimonio)

        # Acionar a Label tipo e o lineedit ao layout certical
        self.layout_v.addWidget(self.label_tipo)
        self.layout_v.addWidget(self.edit_tipo)

         # Acionar a Label descrição e o lineedit ao layout certical
        self.layout_v.addWidget(self.label_descricao)
        self.layout_v.addWidget(self.edit_descricao)

         # Acionar a Label localização e o lineedit ao layout certical
        self.layout_v.addWidget(self.label_localizacao)
        self.layout_v.addWidget(self.edit_localizacao)

        # Acionar a Label data de fabricação e o lineedit ao layout certical
        self.layout_v.addWidget(self.label_fabricacao)
        self.layout_v.addWidget(self.edit_fabricacao)

        # Acionar a Label data de aquisição e o lineedit ao layout certical
        self.layout_v.addWidget(self.label_aquisicao)
        self.layout_v.addWidget(self.edit_aquisicao)

        
        
        #adicionar o layout_v a tela
        self.setLayout(self.layout_v)

    def localizar(self):
        # Abrir o aquivo csv e atribuir a uma variável 
        arquivo = open("Patrimônio.csv","r",encoding="utf8")
        linhas = csv.reader(arquivo)


        for i in linhas:
            lin = str(i).replace("['","").replace("']","").split(";")
            if(lin[0]==self.edit_id.text()):
                self.edit_numero.setText(lin[1])
                self.edit_nome_patrimonio.setText(lin[2])
                self.edit_tipo.setText(lin[3])
                self.edit_descricao.setText(lin[4])
                self.edit_localizacao.setText(lin[5])
                self.edit_fabricacao.setText(lin[6])
                self.edit_aquisicao.setText(lin[7])

  


#app = QApplication(sys.argv)
# Instancia da classe CadastroCliente para iniciar a janela
#tela = Patrimonio()
# exibir a tela durante a execução
#tela.show()
# ao clicar no botão fechar a tela deve fechar e sair da memória
#app.exec()