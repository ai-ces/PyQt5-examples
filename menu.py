import sys
from PyQt5.QtWidgets import QApplication, QAction, qApp, QMainWindow

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        menubar = self.menuBar()
        dosya = menubar.addMenu("Dosya")
        duzenle = menubar.addMenu("Duzenle")

        ac = QAction("Ac", self)
        ac.setShortcut("Ctrl+0")

        kaydet = QAction("Kaydet",self)
        kaydet.setShortcut("Ctrl+S")

        cikis = QAction("Cikis",self)
        cikis.setShortcut("Ctrl+Q")

        dosya.addAction(ac)
        dosya.addAction(kaydet)
        dosya.addAction(cikis)

        self.setWindowTitle("Menu")
        self.show()

        ekle = duzenle.addMenu("Ekle")

        sayfa = QAction("Sayfa Ekle",self)
        resim = QAction("Resim Ekle",self)

        ekle.addAction(sayfa)
        ekle.addAction(resim)


        cikis.triggered.connect(self.cikis_yap)
        dosya.triggered.connect(self.tiklama)

    def cikis_yap(self):
        qApp.quit()

    def tiklama(self, action):
        if action.text() == "Ac":
            print("Ac komutu calistirildi")
        elif action.text() == "Kaydet":
            print("Kaydet komutu calistirildi")


obje = QApplication(sys.argv)
menu = Menu()

sys.exit(obje.exec())