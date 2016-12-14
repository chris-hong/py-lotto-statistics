import tkinter.messagebox

from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot

class PLS_Form(QtWidgets.QDialog):

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("designer.ui", self)
        self.ui.show()

    @pyqtSlot()
    def slot_update(self):
        tkinter.messagebox.showinfo('확인', '클릭 UPDATE')

    @pyqtSlot()
    def slot_analyze(self):
        tkinter.messagebox.showinfo('확인', '클릭 ANALYZE')


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PLS_Form()
    sys.exit(app.exec())