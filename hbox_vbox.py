import sys
from PyQt5 import QtWidgets, QtGui

obje = QtWidgets.QApplication(sys.argv)
pencere = QtWidgets.QWidget()
pencere.setGeometry(200,200,600,400)

kaydet = QtWidgets.QPushButton()
kaydet.setText("Kaydet")

cikis = QtWidgets.QPushButton()
cikis.setText("Cikis")

# hb = QtWidgets.QHBoxLayout()

# hb.addWidget(kaydet)
# hb.addWidget(cikis)
# hb.addStretch()

vb = QtWidgets.QVBoxLayout()
vb.addWidget(kaydet)
vb.addWidget(cikis)

pencere.setLayout(vb)



pencere.show()

sys.exit(obje.exec())