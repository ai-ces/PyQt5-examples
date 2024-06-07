
import sys
from PyQt5 import QtWidgets

obje = QtWidgets.QApplication(sys.argv)
pencere = QtWidgets.QWidget()
pencere.setGeometry(200,200,400,300)

pencere.show()

sys.exit(obje.exec())
