import sys
from PyQt5 import QtWidgets, QtGui

class Pencere (QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.soru = QtWidgets.QLabel("En cok hangi sporu seviyorsunuz ?")
        self.futbol = QtWidgets.QRadioButton("Futbol")
        self.basketbol = QtWidgets.QRadioButton("Basketbol")
        self.voleybol = QtWidgets.QRadioButton("Voleybol")
        self.yuzme = QtWidgets.QRadioButton("Yuzme")
        self.etiket = QtWidgets.QLabel()
        self.dugme = QtWidgets.QPushButton("Kaydet")


        vb = QtWidgets.QVBoxLayout()
        vb.addWidget(self.soru)
        vb.addWidget(self.futbol)
        vb.addWidget(self.basketbol)
        vb.addWidget(self.voleybol)
        vb.addWidget(self.yuzme)
        vb.addStretch()
        vb.addWidget(self.etiket)
        vb.addWidget(self.dugme)

        self.dugme.clicked.connect(lambda : self.tiklama(self.futbol.isChecked(),self.basketbol.isChecked(),self.voleybol.isChecked(),self.yuzme.isChecked(),self.etiket))

        self.setLayout(vb)
        self.show()

    def tiklama(self, futbol,basketbol,voleybol,yuzme, etiket):
        if futbol:
            self.etiket.setText("Futbol kaydedildi.")
        if basketbol:
            self.etiket.setText("Basketbol kaydedildi.")
        if voleybol:
            self.etiket.setText("Voleybol kaydedildi.")
        if yuzme:
            self.etiket.setText("Yuzme kaydedildi.")



obje = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
pencere.setGeometry(200,200,400,300)
pencere.setWindowTitle("Checkbox")


sys.exit(obje.exec())