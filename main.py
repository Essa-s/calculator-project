# main_script.py

from PyQt5.QtWidgets import QApplication, QMainWindow
from window import Ui_MainWindow  # Import the generated window file
import re
from PyQt5.QtCore import Qt
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.bind()
    def bind(self):
        # Connect buttons to functions
            self.ui.btn_0.clicked.connect(self.pressed_btn_0)
            self.ui.btn_1.clicked.connect(self.pressed_btn_1)
            self.ui.btn_2.clicked.connect(self.pressed_btn_2)
            self.ui.btn_3.clicked.connect(self.pressed_btn_3)
            self.ui.btn_4.clicked.connect(self.pressed_btn_4)
            self.ui.btn_5.clicked.connect(self.pressed_btn_5)
            self.ui.btn_6.clicked.connect(self.pressed_btn_6)
            self.ui.btn_7.clicked.connect(self.pressed_btn_7)
            self.ui.btn_8.clicked.connect(self.pressed_btn_8)
            self.ui.btn_9.clicked.connect(self.pressed_btn_9)
            self.ui.btn_add.clicked.connect(self.pressed_btn_add)
            self.ui.btn_sub.clicked.connect(self.pressed_btn_sub)
            self.ui.btn_multi.clicked.connect(self.pressed_btn_multi)
            self.ui.btn_div.clicked.connect(self.pressed_btn_div)
            self.ui.btn_module.clicked.connect(self.pressed_btn_module)
            self.ui.btn_del.clicked.connect(self.pressed_btn_del)
            self.ui.btn_divfloor.clicked.connect(self.pressed_btn_divfloor)
            self.ui.btn_dot.clicked.connect(self.pressed_btn_dot)
            self.ui.btn_result.clicked.connect(self.pressed_btn_result)
    def keyPressEvent(self, event):
        key = event.key()

        # Map Qt key constants to their respective characters
        key_mapping = {
            Qt.Key_0: '0',
            Qt.Key_1: '1',
            Qt.Key_2: '2',
            Qt.Key_3: '3',
            Qt.Key_4: '4',
            Qt.Key_5: '5',
            Qt.Key_6: '6',
            Qt.Key_7: '7',
            Qt.Key_8: '8',
            Qt.Key_9: '9',
            Qt.Key_Plus: '+',
            Qt.Key_Minus: '-',
            Qt.Key_Asterisk: '*',
            Qt.Key_Slash: '/',
            Qt.Key_Percent: '%',
            Qt.Key_Backspace: 'backspace',
            Qt.Key_Period: '.',
            Qt.Key_Enter: 'enter',
        }

        # Convert the key to its corresponding character
        key_char = key_mapping.get(key, None)

        if key_char is not None:
            if key_char == 'enter':
                self.pressed_btn_result()
            elif key_char == 'backspace':
                self.ui.lineEdit.backspace()
            else:
                text_to_insert = key_char
                self.ui.lineEdit.insert(text_to_insert)
     
    def pressed_btn_0(self):
        text_to_insert = "0"
        self.ui.lineEdit.insert(text_to_insert)

    def pressed_btn_1(self):
        text_to_insert = "1"
        self.ui.lineEdit.insert(text_to_insert)
    
    def pressed_btn_2(self):
        text_to_insert = "2"
        self.ui.lineEdit.insert(text_to_insert)
        
    def pressed_btn_3(self):
        text_to_insert = "3"
        self.ui.lineEdit.insert(text_to_insert)
    def pressed_btn_4(self):
        text_to_insert = "4"
        self.ui.lineEdit.insert(text_to_insert)
    def pressed_btn_5(self):
        text_to_insert = "5"
        self.ui.lineEdit.insert(text_to_insert)
    def pressed_btn_6(self):
        text_to_insert = "6"
        self.ui.lineEdit.insert(text_to_insert)
    def pressed_btn_7(self):
        text_to_insert = "7"
        self.ui.lineEdit.insert(text_to_insert)
    def pressed_btn_8(self):
        text_to_insert = "8"
        self.ui.lineEdit.insert(text_to_insert)
    def pressed_btn_9(self):
        text_to_insert = "9"
        self.ui.lineEdit.insert(text_to_insert)
    def pressed_btn_add(self):
        text_to_insert = "+"
        self.ui.lineEdit.insert(text_to_insert)
    def pressed_btn_sub(self):
        text_to_insert = "-"
        self.ui.lineEdit.insert(text_to_insert)
    def pressed_btn_multi(self):
        text_to_insert = "*"
        self.ui.lineEdit.insert(text_to_insert)
    def pressed_btn_div(self):
        text_to_insert = "/"
        self.ui.lineEdit.insert(text_to_insert)
    def pressed_btn_module(self):
        text_to_insert = "%"
        self.ui.lineEdit.insert(text_to_insert)
    def pressed_btn_divfloor(self):
        text_to_insert = "//"
        self.ui.lineEdit.insert(text_to_insert)
    def pressed_btn_dot(self):
        text_to_insert = "."
        self.ui.lineEdit.insert(text_to_insert)
    def pressed_btn_del(self):
        self.ui.lineEdit.clear()
    def pressed_btn_result(self):
        current_text = self.ui.lineEdit.text()

        # Regular expression patterns
        operand_pattern = r'\d+'
        operator_pattern = r'[-+*/%//]'

        # Find all operands
        operands = [int(operand) for operand in re.findall(operand_pattern, current_text)]
        print(operands)
        # Find all operators
        operators = re.findall(operator_pattern, current_text)
        print(operators)
        # Check if there are enough operands and operators
        if len(operands) < 2 or len(operators) != len(operands) - 1:
            self.ui.lineEdit.clear()
            return

        # Perform calculations
        result = operands[0]
        for i in range(len(operators)):
            if operators[i] == '+':
                result += operands[i + 1]
            elif operators[i] == '-':
                result -= operands[i + 1]
            elif operators[i] == '*':
                result *= operands[i + 1]
            elif operators[i] == '/':
                try:
                    result /= operands[i + 1]
                except ZeroDivisionError:
                    self.ui.lineEdit.clear()
                    return
            elif operators[i] == '//':
                result //= operands[i + 1]
            elif operators[i] == '%':
                result %= operands[i + 1]
            else:
                self.ui.lineEdit.clear()
                return

        self.ui.lineEdit.setText(str(result))

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = MyWindow()
    mainWindow.show()
    sys.exit(app.exec_())
