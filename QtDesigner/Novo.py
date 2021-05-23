import sys
from QtDesigner.Dolar import *
from PyQt5.QtWidgets import QMainWindow, QApplication
import requests
from bs4 import BeautifulSoup

class Converter(QMainWindow, Ui_Conversor):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.pushButton.clicked.connect(self.converter)

    def converter(self):
        try:
            self.search = self.comboBox.currentText()
            url = f"https://www.google.com/search?q={self.search}"
            r = requests.get(url)
            s = BeautifulSoup(r.text, "html.parser")
            update = s.find("div", class_="BNeawe").text
            t = ""
            for i in update:
                if i == ",":
                    t += "."
                elif i != " ":
                    t += i
                else:
                    break

            t = float(t)
            dig = self.lineEdit.text()
            num = float(dig)
            mt = t * num
            mt = str(mt)
            mt = mt.replace(".", ",")
            t = str(t)
            t = t.replace(".", ",")
            self.label_2.setText(f"1 {self.search} = R${t}")
            self.label.setText("= R$" + mt)
        except:
            self.label_2.setText("")
            self.label.setText("Valor inválido")

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    converter = Converter()
    converter.show()
    qt.exec_()