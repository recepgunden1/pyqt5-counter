import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.yazi_alani = QtWidgets.QLabel("Daha kimse tıklamadı :)")
        self.buton = QtWidgets.QPushButton("Tikla burayaa !!!")
        self.say = 0

        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setGeometry(800,400,500,500)
        self.setLayout(h_box)
        self.buton.clicked.connect(self.click)
        self.show()

    def click(self):
        self.say += 1
        self.yazi_alani.setText("Bana " + str(self.say) + " defa tiklandi.")

app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
