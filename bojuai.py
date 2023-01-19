from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QLabel, QPushButton, QLineEdit
import sys

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def showondisplay():
    freshlyentered = entertext.toPlainText()
    displaytext.setText(freshlyentered)

def encrypt(input_text, encyrption_key, direction):
    output_text = ""
    for char in input_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + encyrption_key
            end_text += alphabet[new_position]
        else:
            end_text += char


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(900, 900)
    w.setWindowTitle('BojuAI')

    displaytext = QTextEdit(w)
    displaytext.resize(800, 300)
    displaytext.move(50, 50)
    displaytext.setReadOnly(True)
    displaytext.setStyleSheet('background-color: black; font-size: 20; color: yellow')
    # displaytext.setPlaceholderText('Do not type here...')

    entertext = QTextEdit(w)
    entertext.resize(800, 300)
    entertext.move(50, 550)
    entertext.setReadOnly(False)
    entertext.setStyleSheet('background-color: white; font-size: 20; color: black')
    entertext.textChanged.connect(showondisplay)

    encrypt_button = QPushButton(w)
    encrypt_button.setText('Encrypt')
    encrypt_button. move(50, 860)

    label = QLabel(w)
    label.setText('Encryption Number: ')
    label. move(50, 500)

    labeledit = QLineEdit(w)
    labeledit.setPlaceholderText('Enter your encryption Number')
    labeledit. move(170, 495)


    w.show()
    sys.exit(app.exec())