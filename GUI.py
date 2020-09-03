import sys
from PyQt5.QtWidgets import *
import execution


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.urlLabel = QLabel("URL:", self)
        self.urlLE = QLineEdit(self)
        self.urlLE.setPlaceholderText("https://www.example.com/")

        self.keywordLabel = QLabel("Keyword:", self)
        self.keywordLE = QLineEdit(self)

        self.depthLabel = QLabel('Depth: (MAX: 100)')
        self.depthSpinbox = QSpinBox()
        self.depthSpinbox.setRange(1, 100)
        self.depthSpinbox.setSingleStep(1)

        self.optionsLabel = QLabel('Options:')
        self.options = QComboBox(self)
        self.options.addItem('All Words')
        self.options.addItem('Text Ranking')

        self.outputOption1 = QCheckBox('Found words', self)
        self.outputOption1.toggle()

        self.outputOption2 = QCheckBox('Wordcloud', self)

        self.btn = QPushButton("Execute", self)

        self.initUI()

    def initUI(self):
        inputLayout = QGridLayout()
        inputLayout.addWidget(self.urlLabel, 0, 0)
        inputLayout.addWidget(self.urlLE, 0, 1)
        inputLayout.addWidget(self.keywordLabel, 1, 0)
        inputLayout.addWidget(self.keywordLE, 1, 1)

        optionsLayout = QGridLayout()
        optionsLayout.addWidget(self.depthLabel, 0, 0)
        optionsLayout.addWidget(self.depthSpinbox, 1, 0)
        optionsLayout.addWidget(self.optionsLabel, 0, 1)
        optionsLayout.addWidget(self.options, 1, 1)
        optionsLayout.addWidget(self.outputOption1, 0, 2)
        optionsLayout.addWidget(self.outputOption2, 1, 2)

        containerLayout = QVBoxLayout()
        containerLayout.addLayout(inputLayout)
        containerLayout.addLayout(optionsLayout)
        containerLayout.addWidget(self.btn)

        self.setLayout(containerLayout)
        self.btn.clicked.connect(self.execute)

        self.setWindowTitle('wordpy')
        self.setGeometry(300, 300, 500, 150)
        self.show()

    def execute(self):
        url = self.urlLE.text()
        keyword = self.keywordLE.text()
        depth = self.depthSpinbox.value()
        option = self.options.currentIndex()
        outputOption = [self.outputOption1.isChecked(), self.outputOption2.isChecked()]
        execution.execute(url, depth, keyword, option, outputOption)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())