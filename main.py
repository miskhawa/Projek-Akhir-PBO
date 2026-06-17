import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Kalkulator import Ui_MainWindow

class Kalkulator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ekspresi = ""

        # Tombol angka
        self.ui.btn0.clicked.connect(lambda: self.tambah("0"))
        self.ui.btn1.clicked.connect(lambda: self.tambah("1"))
        self.ui.btn2.clicked.connect(lambda: self.tambah("2"))
        self.ui.btn3.clicked.connect(lambda: self.tambah("3"))
        self.ui.btn4.clicked.connect(lambda: self.tambah("4"))
        self.ui.btn5.clicked.connect(lambda: self.tambah("5"))
        self.ui.btn6.clicked.connect(lambda: self.tambah("6"))
        self.ui.btn7.clicked.connect(lambda: self.tambah("7"))
        self.ui.btn8.clicked.connect(lambda: self.tambah("8"))
        self.ui.btn9.clicked.connect(lambda: self.tambah("9"))

        # Operator
        self.ui.btnPlus.clicked.connect(lambda: self.tambah("+"))
        self.ui.btnMinus.clicked.connect(lambda: self.tambah("-"))
        self.ui.btnMultiply.clicked.connect(lambda: self.tambah("*"))
        self.ui.btnDivide.clicked.connect(lambda: self.tambah("/"))
        self.ui.btnDot.clicked.connect(lambda: self.tambah("."))

        # Tombol fungsi
        self.ui.btnEqual.clicked.connect(self.hitung)
        self.ui.btnClear.clicked.connect(self.clear)

    def tambah(self, karakter):
        if self.ekspresi == "" and karakter in "+-*/":
            return

        self.ekspresi += karakter
        self.ui.lblDisplay.setText(self.ekspresi)

    def clear(self):
        self.ekspresi = ""
        self.ui.lblDisplay.setText("0")

    def hitung(self):
        try:
            hasil = eval(self.ekspresi)
        
            if isinstance(hasil, float) and hasil.is_integer():
                hasil = int(hasil)
        
            self.ui.lblDisplay.setText(str(hasil))
            self.ekspresi = str(hasil)
        
        except ZeroDivisionError:
            self.ui.lblDisplay.setText("Tidak bisa dibagi 0")
            self.ekspresi = ""
        
        except Exception:
            self.ui.lblDisplay.setText("Error")
            self.ekspresi = ""
        
if __name__ == "__main__":
    app = QApplication(sys.argv)

window = Kalkulator()
window.setWindowTitle("Kalkulator Sederhana")
window.show()

sys.exit(app.exec())
