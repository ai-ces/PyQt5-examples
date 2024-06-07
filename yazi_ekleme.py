import sys
from PyQt5 import QtWidgets

obje = QtWidgets.QApplication(sys.argv)
pencere = QtWidgets.QWidget()
pencere.setWindowTitle("Pencereye yazi ekleme")
pencere.setGeometry(200,200,400,300)

etiket = QtWidgets.QLabel(pencere)
etiket.setText("abcd")
etiket.move(175,135)

pencere.show()

sys.exit(obje.exec())