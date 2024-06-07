import sys
from PyQt5 import QtWidgets, QtGui

obje = QtWidgets.QApplication(sys.argv)
pencere = QtWidgets.QWidget()
pencere.setGeometry(200,200,600,400)

# etiket = QtWidgets.QLabel(pencere)
# etiket.setPixmap(QtGui.QPixmap("")) // resim ekleme


dugme = QtWidgets.QPushButton(pencere)
dugme.setText("Tamam")
dugme.move(150,50)

pencere.show()

sys.exit(obje.exec())