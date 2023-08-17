############## NO-CHEAT ##############
######## By: Arman Hajmohammadi ########
# importing the dependencies
from no_cheat_module import CompareScript
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtGui import QIcon


class PDFComparisonApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("No CHEAT")
        self.setGeometry(100, 100, 400, 300)
        self.setWindowIcon(QIcon("icon.ico"))

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.folder_label = QLabel("Choose a folder:")
        layout.addWidget(self.folder_label)

        self.folder_entry = QLineEdit()
        layout.addWidget(self.folder_entry)

        self.browse_button = QPushButton("Browse")
        self.browse_button.clicked.connect(self.choose_folder)
        layout.addWidget(self.browse_button)

        self.run_button = QPushButton("Run")
        self.run_button.clicked.connect(self.run_comparison)
        layout.addWidget(self.run_button)

        self.result_text = QTextEdit()
        self.result_text.setPlaceholderText("The result will be shown here.")
        layout.addWidget(self.result_text)

        self.central_widget.setLayout(layout)

    def choose_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        self.folder_entry.setText(folder)

    def run_comparison(self):
        folder_path = self.folder_entry.text()
        # Perform your comparison logic here and update the result_text
        self.result_text.setPlainText("Running comparison...\n")
        self.run_button.setText("Running...")
        self.run_button.setEnabled(False)
        self.browse_button.setEnabled(False)
        self.folder_entry.setEnabled(False)
        self.result_text.setPlainText(CompareScript(folder_path))
        self.run_button.setStyleSheet(
            "background-color: #197741; color: white; font-weight: bold;")
        self.run_button.setText("DONE!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PDFComparisonApp()
    window.show()
    sys.exit(app.exec_())
