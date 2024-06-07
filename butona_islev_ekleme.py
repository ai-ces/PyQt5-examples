import sys
from PyQt5 import QtWidgets, QtGui

class Pencere (QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.dugme = QtWidgets.QPushButton("Gorseli Getir")
        self.gorsel = QtWidgets.QLabel("Gorsel yuklu degil")

        vb = QtWidgets.QVBoxLayout()
        vb.addWidget(self.gorsel)
        vb.addWidget(self.dugme)
        vb.addStretch()

        hb = QtWidgets.QHBoxLayout()
        hb.addStretch()
        hb.addLayout(vb)
        hb.addStretch

        self.setLayout(hb)
        self.show()

        self.dugme.clicked.connect(self.tiklama)

    def tiklama(self):
        self.gorsel.setPixmap(QtGui.QPixmap(""))

obje = QtWidgets.QApplication(sys.argv)

pencere = Pencere()
pencere.setGeometry(200,200,400,300)

sys.exit(obje.exec())