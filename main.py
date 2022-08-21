from tokenize import Octnumber
import requests
import json
import sys
from PyQt6 import QtWidgets
from PyQt6 import QtGui
from PyQt6.QtWidgets import QDialog, QApplication, QFileDialog
import mainUI
import time


stylesheet = """
    MainWindow {
        background-image: url("background.jpeg"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""

names = []
result = {}
counter = 0
top_result = []


class MainWindow(QtWidgets.QMainWindow, mainUI.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('logo.png'))

        self.OpenCurrentDir.clicked.connect(self.browsefile)
        self.start_btn.clicked.connect(self.main)
        

    def browsefile(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', './')
        self.choseFileLine.setText(fname[0])


        with open(fname[0], 'r') as file:
            ips = file.readlines()

        for country in ips:
            resp = requests.get('http://api.sypexgeo.net/json/' + country)
            data = json.loads(resp.text)
            names.append(data['country']['name_en'])

        sorted_names = str(set(names))

        self.countriesLine.setText(sorted_names)


    def main(self, fname):

        fname = self.choseFileLine.text()

        with open(fname, 'r') as file:
            f = file.readlines()
            countries = self.countriesLine.text()
            country_names = []

            for country in f:
                resp = requests.get('http://api.sypexgeo.net/json/' + country)
                data = json.loads(resp.text)
                # print(data['ip'] + data['country']['name_en'])
                country_names.append(data['country']['name_en'])

            huyna = ["{", ", ", " ,", "}"]
            coun = countries.split("'")
            for elem in coun:
                if elem in huyna:
                    coun.remove(elem)
            print(coun)
            file.close()
            

        with open(fname, 'r+') as newfile:
            nf = newfile.readlines()
            for current_ip in nf:
                r = requests.get('http://api.sypexgeo.net/json/' + current_ip)
                data = json.loads(r.text)
                if data['country']['name_en'] in coun:
                    top_result.append(data['ip'])
            print(top_result)
            newfile.close()

        with open('result.txt' + time.strftime('%m_%d_(%H:%M)'), 'w') as result_file:
            for element in top_result:
                result_file.write(element + '\n')
        result_file.close()
                
app = QApplication([])
app.setStyleSheet(stylesheet)  
window = MainWindow()
window.show()
app.exec()