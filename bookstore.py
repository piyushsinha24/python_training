# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bookstore.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3
mylibrary=sqlite3.connect('mylibrary.db')
print("OPENEND DATABASE")



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(16, 70, 81, 20))
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 67, 17))
        self.label_2.setObjectName("label_2")
        self.t1 = QtWidgets.QLineEdit(Form)
        self.t1.setGeometry(QtCore.QRect(120, 70, 113, 25))
        self.t1.setObjectName("t1")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 67, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 81, 20))
        self.label_4.setObjectName("label_4")
        self.t2 = QtWidgets.QLineEdit(Form)
        self.t2.setGeometry(QtCore.QRect(120, 150, 113, 25))
        self.t2.setObjectName("t2")
        self.pricebtn = QtWidgets.QPushButton(Form)
        self.pricebtn.setGeometry(QtCore.QRect(280, 70, 89, 25))
        self.pricebtn.setObjectName("pricebtn")
        self.amtbtn = QtWidgets.QPushButton(Form)
        self.amtbtn.setGeometry(QtCore.QRect(280, 150, 89, 25))
        self.amtbtn.setObjectName("amtbtn")
        self.l1 = QtWidgets.QLabel(Form)
        self.l1.setGeometry(QtCore.QRect(120, 110, 67, 17))
        self.l1.setText("")
        self.l1.setObjectName("l1")
        self.l2 = QtWidgets.QLabel(Form)
        self.l2.setGeometry(QtCore.QRect(120, 200, 67, 17))
        self.l2.setText("")
        self.l2.setObjectName("l2")
        self.pricebtn.clicked.connect(self.findprice)
        self.amtbtn.clicked.connect(self.findamt)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Book Title :"))
        self.label_2.setText(_translate("Form", "Price :"))
        self.label_3.setText(_translate("Form", "Quantity :"))
        self.label_4.setText(_translate("Form", "Total :"))
        self.pricebtn.setText(_translate("Form", "Find Price"))
        self.amtbtn.setText(_translate("Form", "Find Total"))

    def findprice(self):
        title=self.t1.text()
        cur=mylibrary.cursor()
        x=cur.execute('''SELECT * FROM BOOKS WHERE NAME == {} '''.format(title))
        for row in x:
            price=row[3]
        self.l1.setText(str(price))
        
        

    def findamt(self):
        n=self.t2.text()
        prc=self.l1.text()
        amount=int(n)*float(prc)
        self.l2.setText(str(amount))
        
        
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    
mylibrary.close()
