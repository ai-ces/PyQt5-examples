import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.yazi = QtWidgets.QLineEdit()
        self.sil = QtWidgets.QPushButton("Sil")
        self.kaydet = QtWidgets.QPushButton("Kaydet")
        self.etiket = QtWidgets.QLabel()

        vb = QtWidgets.QVBoxLayout()
        vb.addWidget(self.yazi)
        vb.addWidget(self.sil)
        vb.addWidget(self.kaydet)
        vb.addStretch()
        vb.addWidget(self.etiket)

        self.setLayout(vb)
        self.show()

        self.sil.clicked.connect(self.temizle)
        self.kaydet.clicked.connect(self.kayit)
    def temizle(self):
        self.yazi.clear()
    def kayit(self):
        self.etiket.setText(self.yazi.text()+ "  kaydedildi")

obje = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
pencere.setGeometry(200,200,400,300)
sys.exit(obje.exec())