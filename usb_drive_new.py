import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton, QMessageBox, QFileDialog
)
from PyQt5.QtCore import Qt
import subprocess  # Para executar comandos do sistema

class BootableUSBCreator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configuração da janela
        self.setWindowTitle('Criar USB Bootável')
        self.setGeometry(100, 100, 400, 200)

        # Layout
        layout = QVBoxLayout()

        # Label e Combobox para selecionar o USB drive
        self.usb_label = QLabel('Selecione o USB Drive:', self)
        layout.addWidget(self.usb_label)

        self.drive_combo = QComboBox(self)
        self.populate_drives()
        layout.addWidget(self.drive_combo)

        # Botão para atualizar a lista de drives
        self.refresh_button = QPushButton('Atualizar Drives', self)
        self.refresh_button.clicked.connect(self.populate_drives)
        layout.addWidget(self.refresh_button)

        # Label e Botão para selecionar o arquivo ISO
        self.iso_label = QLabel('Selecione o arquivo ISO:', self)
        layout.addWidget(self.iso_label)

        self.iso_path_label = QLabel('Nenhum arquivo selecionado', self)
        self.iso_path_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.iso_path_label)

        self.select_iso_button = QPushButton('Selecionar ISO', self)
        self.select_iso_button.clicked.connect(self.select_iso)
        layout.addWidget(self.select_iso_button)

        # Botão para iniciar o processo de criação do USB bootável
        self.create_button = QPushButton('Criar USB Bootável', self)
        self.create_button.clicked.connect(self.create_bootable_usb)
        layout.addWidget(self.create_button)

        # Definir layout
        self.setLayout(layout)

    def populate_drives(self):
        """Preenche o combobox com os drives USB disponíveis."""
        self.drive_combo.clear()
        drives = self.get_usb_drives()
        if drives:
            self.drive_combo.addItems(drives)
        else:
            self.drive_combo.addItem("Nenhum USB Drive encontrado")

    def get_usb_drives(self):
        """Retorna uma lista de drives USB disponíveis."""
        drives = []
        if os.name == 'nt':  # Windows
            import string
            from ctypes import windll
            bitmask = windll.kernel32.GetLogicalDrives()
            for letter in string.ascii_uppercase:
                if bitmask & 1:
                    drive = f"{letter}:\\"
                    if os.path.exists(drive):
                        drives.append(drive)
                bitmask >>= 1
        else:  # Linux/Mac
            drives = [os.path.join('/media', user, drive) for user in os.listdir('/media') for drive in os.listdir(f'/media/{user}')]
        return drives

    def select_iso(self):
        """Abre uma janela para selecionar o arquivo ISO."""
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Selecionar Arquivo ISO', '', 'ISO Files (*.iso)')
        if file_path:
            self.iso_path_label.setText(file_path)

    def create_bootable_usb(self):
        """Inicia o processo de criação do USB bootável."""
        selected_drive = self.drive_combo.currentText()
        iso_path = self.iso_path_label.text()

        # Validações
        if selected_drive == "Nenhum USB Drive encontrado":
            QMessageBox.warning(self, 'Erro', 'Nenhum USB Drive selecionado ou encontrado.')
            return
        if not iso_path or iso_path == 'Nenhum arquivo selecionado':
            QMessageBox.warning(self, 'Erro', 'Nenhum arquivo ISO selecionado.')
            return

        # Confirmação do usuário
        confirm = QMessageBox.question(
            self, 'Confirmação',
            f'Tem certeza que deseja criar um USB bootável?\n'
            f'Drive: {selected_drive}\n'
            f'ISO: {iso_path}\n'
            f'Isso apagará todos os dados no drive!',
            QMessageBox.Yes | QMessageBox.No
        )
        if confirm == QMessageBox.No:
            return

        # Executar o processo de criação do USB bootável
        try:
            if os.name == 'nt':  # Windows
                # Usar Rufus ou outra ferramenta (substitua pelo caminho do Rufus)
                QMessageBox.warning(self, 'Aviso', 'No Windows, use uma ferramenta como Rufus para criar o USB bootável.')
            else:  # Linux/Mac
                # Usar o comando dd
                command = f'sudo dd if={iso_path} of={selected_drive} bs=4M status=progress'
                subprocess.run(command, shell=True, check=True)
                QMessageBox.information(self, 'Sucesso', 'USB bootável criado com sucesso!')
        except Exception as e:
            QMessageBox.critical(self, 'Erro', f'Ocorreu um erro ao criar o USB bootável:\n{str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BootableUSBCreator()
    window.show()
    sys.exit(app.exec_())