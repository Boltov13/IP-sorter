# Form implementation generated from reading ui file 'sorter.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 180)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(250, 110, 113, 41))
        self.start_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.start_btn.setObjectName("start_btn")
        self.OpenCurrentDir = QtWidgets.QPushButton(self.centralwidget)
        self.OpenCurrentDir.setGeometry(QtCore.QRect(250, 10, 113, 41))
        self.OpenCurrentDir.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.OpenCurrentDir.setObjectName("OpenCurrentDir")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 450, 481, 23))
        self.progressBar.setProperty("value", 78)
        self.progressBar.setObjectName("progressBar")
        self.choseFileLine = QtWidgets.QLineEdit(self.centralwidget)
        self.choseFileLine.setGeometry(QtCore.QRect(20, 15, 201, 31))
        self.choseFileLine.setObjectName("choseFileLine")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 241, 21))
        self.label.setObjectName("label")
        self.countriesLine = QtWidgets.QLineEdit(self.centralwidget)
        self.countriesLine.setGeometry(QtCore.QRect(20, 110, 201, 31))
        self.countriesLine.setObjectName("countriesLine")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IP Sorter by @boltov"))
        self.start_btn.setText(_translate("MainWindow", "Start"))
        self.OpenCurrentDir.setText(_translate("MainWindow", "Browse"))
        self.choseFileLine.setPlaceholderText(_translate("MainWindow", "Chose file to sort"))
        self.label.setText(_translate("MainWindow", "Countries to stay in file"))
