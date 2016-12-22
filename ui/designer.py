# import tkinter.messagebox
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class PLS_Form(QtWidgets.QDialog):

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("designer.ui", self)
        self.ui.show()

    @pyqtSlot()
    def slot_update(self):
        # tkinter.messagebox.showinfo('확인', '클릭 UPDATE')

        my_array = [[10, 15],
                    [7, 14],
                    [3, 44]]

        tableModel = TableModel(my_array, self)
        self.tableView.setModel(tableModel)

    @pyqtSlot()
    def slot_analyze(self):
        # tkinter.messagebox.showinfo('확인', '클릭 ANALYZE')
        foods = [
            'cookies',
            'spaghetti',
            'chocolate',
            'cream',
            'soup'
        ]
        listModel = ListModel(foods, self)
        self.listView.setModel(listModel)


class TableModel(QAbstractTableModel):
    header = ['Hits', 'Num']

    def __init__(self, dataIn, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.tableData = dataIn

    def rowCount(self, parent):
        return len(self.tableData)

    def columnCount(self, parent):
        return len(self.tableData[0])

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.header[section]
        return QAbstractTableModel.headerData(self, section, orientation, role)

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role == Qt.DisplayRole:
            return QVariant(self.tableData[index.row()][index.column()])
        elif role == Qt.TextAlignmentRole:
            return QVariant(Qt.AlignCenter | Qt.AlignVCenter)
        return QVariant()

class ListModel(QAbstractListModel):
    def __init__(self, dataIn, parent=None, *args):
        QAbstractListModel.__init__(self, parent, *args)
        self.listData = dataIn

    def rowCount(self, parent=QModelIndex()):
        return len(self.listData)

    def data(self, index, role):
        if index.isValid() and role == Qt.DisplayRole:
            return QVariant(self.listData[index.row()])
        else:
            return QVariant()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PLS_Form()
    sys.exit(app.exec())