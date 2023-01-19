from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QGridLayout, QMessageBox, QPushButton
from PyQt5.QtCore import Qt
import math
import sys
import os 

def calculate():
        # Get the values of a, b, and c from the input fields
        a = float(a_field.text())
        b = float(b_field.text())
        c = float(c_field.text())

        # Calculate the discriminant
        discriminant = b ** 2 - 4 * a * c

        # Calculate the roots
        mbox = QMessageBox()
        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            mbox.setIcon(QMessageBox.Information)
            mbox.setText(f'Roots: {root1}, {root2}')
            mbox.exec_()
        elif discriminant == 0:
            root = -b / (2 * a)
            mbox.setIcon(QMessageBox.Information)
            mbox.setText(f'Root: {root}')
            mbox.exec_()
        else:
            mbox.setIcon(QMessageBox.Information)
            mbox.setText('No real roots')
            mbox.exec_()


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle('Quadratic Equation Calculator')
    w.setGeometry(300, 300, 300, 100)

    a_label = QLabel(w)
    a_label.setText('a:')
    a_field = QLineEdit(w)

    b_label = QLabel(w)
    b_label.setText('b:')
    b_field = QLineEdit(w)

    c_label = QLabel(w)
    c_label.setText('c:')
    c_field = QLineEdit(w)

    calculate_button = QPushButton(w)
    calculate_button.setText('Calculate')
    calculate_button.clicked.connect(calculate)

    grid = QGridLayout(w)
    grid.addWidget(a_label, 0, 0)
    grid.addWidget(a_field, 0, 1)
    grid.addWidget(b_label, 1, 0)
    grid.addWidget(b_field, 1, 1)
    grid.addWidget(c_label, 2, 0)
    grid.addWidget(c_field, 2, 1)
    grid.addWidget(calculate_button, 3, 0, 1, 2)
    w.setLayout(grid)

    w.show()
    sys.exit(app.exec())