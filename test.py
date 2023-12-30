from PyQt5.QtWidgets import QApplication, QMainWindow
from window import Ui_MainWindow
from PyQt5.QtCore import Qt
import re

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.bind()

    def bind(self):
        # Connect buttons to functions
        for i in range(10):
            getattr(self.ui, f"btn_{i}").clicked.connect(lambda num=i: self.ui.lineEdit.insert(str(num)))

        operators = ['add', 'sub', 'multi', 'div', 'module', 'divfloor', 'dot']
        operator_symbols = ['+', '-', '*', '/', '%', '//', '.']
        for operator, symbol in zip(operators, operator_symbols):
            getattr(self.ui, f'btn_{operator}').clicked.connect(lambda s=symbol: self.ui.lineEdit.insert(s))

        self.ui.btn_del.clicked.connect(self.ui.lineEdit.clear)
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
                self.ui.lineEdit.insert(str(key_char))
    def pressed_btn_result(self):
        current_text = self.ui.lineEdit.text()

        # Regular expression patterns
        operand_pattern = r'\d+'
        operator_pattern = r'[-+*/%//.]'

        # Find all operands and operators
        operands = [int(operand) if operand.isdigit() else operand for operand in re.findall(operand_pattern, current_text)]
        
        # Check if there are enough operands and operators
        if len(operands) < 2 or len(operands) - 1 != current_text.count('enter'):
            self.ui.lineEdit.clear()
            return

        try:
            result = eval(''.join(map(str, operands)))
            self.ui.lineEdit.setText(str(result))
        except Exception as e:
            print(f"Error: {e}")
            self.ui.lineEdit.clear()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = MyWindow()
    mainWindow.show()
    sys.exit(app.exec_())
