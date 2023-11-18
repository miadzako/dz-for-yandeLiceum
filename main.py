import sys

from PyQt5 import uic, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
import sqlite3


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.load_coffes()
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)

    def load_coffes(self):
        connection = sqlite3.connect('coffee.sqlite')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM coffee")
        data = cursor.fetchall()

        row_count = len(data)
        col_count = len(data[0]) if data else 0
        self.tableWidget.setRowCount(row_count)
        self.tableWidget.setColumnCount(col_count - 1)

        for row in range(row_count):
            for col in range(col_count):
                item = QTableWidgetItem(str(data[row][col]))
                self.tableWidget.setItem(row, col, item)

        connection.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())