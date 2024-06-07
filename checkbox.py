import sys
from PyQt5 import QtWidgets, QtGui

class Pencere (QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.onay_kutusu = QtWidgets.QCheckBox("Okudum")
        self.etiket = QtWidgets.QLabel()
        self.kayit_ol = QtWidgets.QPushButton("Uye ol")

        vb = QtWidgets.QVBoxLayout()
        vb.addWidget(self.onay_kutusu)
        vb.addWidget(self.etiket)
        vb.addWidget(self.kayit_ol)

        self.setLayout(vb)

        self.kayit_ol.clicked.connect(lambda : self.tiklama(self.onay_kutusu.isChecked())) 
        self.show()

    def tiklama(self, onay_kutusu):
        if onay_kutusu:
            self.etiket.setText("Uyelik isleminiz basariyla gerceklesmistir.")
        else:
            self.etiket.setText("Lutfen tekrar deneyiniz")

obje = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
pencere.setGeometry(200,200,400,300)
pencere.setWindowTitle("Checkbox")


sys.exit(obje.exec())