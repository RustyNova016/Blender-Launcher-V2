from enum import Enum

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow

from modules.settings import *
from ui.dialog_window_design import Ui_DialogWindow
from windows.base_window import BaseWindow


class DialogIcon(Enum):
    WARNING = 1
    INFO = 2


class DialogWindow(QMainWindow, BaseWindow, Ui_DialogWindow):
    accepted = pyqtSignal()
    cancelled = pyqtSignal()

    def __init__(self, parent, title="Warning", text="Dialog Window", accept_text="Accept", cancel_text="Cancel", icon=DialogIcon.WARNING):
        super().__init__()
        self.parent = parent
        self.setupUi(self)

        self.setWindowTitle(title)
        self.InfoLabel.setText(text)
        self.IconButton.setProperty("Icon", True)
        self.AcceptButton.setText(accept_text)

        if cancel_text is None:
            self.CancelButton.hide()
        else:
            self.CancelButton.setText(cancel_text)

        if self.AcceptButton.sizeHint().width() > self.CancelButton.sizeHint().width():
            width = self.AcceptButton.sizeHint().width()
        else:
            width = self.CancelButton.sizeHint().width()

        self.AcceptButton.setFixedWidth(width + 16)
        self.CancelButton.setFixedWidth(width + 16)

        self.AcceptButton.clicked.connect(self.accept)
        self.CancelButton.clicked.connect(self.cancel)

        self.show()

    def accept(self):
        self.accepted.emit()
        self.close()

    def cancel(self):
        self.cancelled.emit()
        self.close()