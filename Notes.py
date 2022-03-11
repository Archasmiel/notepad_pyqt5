import sys
import time
from PyQt5 import QtWidgets, uic

UIfile = 'ui/app.ui'


class MainUI(QtWidgets.QMainWindow):

    def update_window_name(self, new):
        self.setWindowTitle(f'{self.start_win_title} - {new}')

    def info(self):
        # new window
        pass

    def new_file(self):
        self.textEdit.setPlainText(f'')

    def save(self):
        filename = str(QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')[0])
        if filename:
            self.update_window_name(filename)
            with open(filename, 'w', encoding='utf-8') as f:
                contents = self.textEdit.toPlainText()
                f.write(contents)
                self.statusBar().showMessage(f'Saved - {time.strftime(f"%m/%d/%Y, %H:%M:%S", time.localtime())}')

    def open(self):
        filename = str(QtWidgets.QFileDialog.getOpenFileName(self, 'Load File')[0])
        self.update_window_name(filename)
        with open(filename, 'r', encoding='utf-8') as f:
            contents = f.read()
            self.textEdit.setPlainText(contents)
            self.statusBar().showMessage(f'Loaded - {time.strftime(f"%m/%d/%Y, %H:%M:%S", time.localtime())}')

    def init_menu(self):

        bar = self.menuBar()

        ####
        file = bar.addMenu('File')
        file_menu = [file.addAction('New file'), file.addAction('Open'), file.addAction('Save')]
        file_menu_actions = [self.new_file, self.open, self.save]
        file_menu_shortcuts = ['Ctrl+A', 'Ctrl+O', 'Ctrl+S']

        for n, m in enumerate(file_menu):
            m.triggered.connect(file_menu_actions[n])
            m.setShortcut(file_menu_shortcuts[n])

        ####
        about = bar.addMenu('About')
        about_menu = [about.addAction('Info')]
        about_menu_actions = [self.info]

        for n, m in enumerate(about_menu):
            m.triggered.connect(about_menu_actions[n])

    def __init__(self):
        super(MainUI, self).__init__()
        uic.loadUi(UIfile, self)

        self.start_win_title = self.windowTitle().title()
        self.saved_last = f''

        self.setWindowTitle(f'{self.start_win_title} - unnamed')
        self.init_menu()

        self.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = MainUI()
    app.exec_()


if __name__ == "__main__":
    main()
