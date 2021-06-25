import sys
from validacpf import valida_cpf
from geradorDeCPF import gera_cpf
from PyQt5.QtWidgets import QApplication, QMainWindow
import janela

class GeraValidaCPF(QMainWindow, janela.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnGeraCpf.clicked.connect(self.gera_cpf)
        self.btnValidaCpf.clicked.connect(self.valida_cpf)

    def gera_cpf(self):
        cpf = gera_cpf()
        self.inputValidaCpf.setText(str(cpf))

    def valida_cpf(self):
        cpf = self.inputValidaCpf.text()
        self.labelRetorno.setText(
            str(valida_cpf(cpf))
        )
        if not valida_cpf(cpf):
            self.labelRetorno.setStyleSheet(
                '*{color: red;}'
            )
        else:
            self.labelRetorno.setStyleSheet(
                '*{color: green;}'
            )

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gera_valida_cpf = GeraValidaCPF()
    gera_valida_cpf.show()
    qt.exec_()