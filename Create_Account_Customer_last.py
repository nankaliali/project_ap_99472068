# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Create_Account_Customer_last.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from create_account_customer import CreateAccountCustomer

class ReadOnly(QtWidgets.QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        return

class Ui_CreateAccountCustomerWindow(object):
    def setupUi(self, CreateAccountCustomerWindow):
        CreateAccountCustomerWindow.setObjectName("CreateAccountCustomerWindow")
        CreateAccountCustomerWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(CreateAccountCustomerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 370, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 471, 270))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget, clicked = lambda : self.membership())
        self.commandLinkButton_2.setGeometry(QtCore.QRect(520, 470, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.commandLinkButton_2.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/icons8-membership-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_2.setIcon(icon)
        self.commandLinkButton_2.setIconSize(QtCore.QSize(60, 60))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(190, 310, 150, 150))
        self.plainTextEdit.setObjectName("plainTextEdit")
        CreateAccountCustomerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CreateAccountCustomerWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        CreateAccountCustomerWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CreateAccountCustomerWindow)
        self.statusbar.setObjectName("statusbar")
        CreateAccountCustomerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CreateAccountCustomerWindow)
        QtCore.QMetaObject.connectSlotsByName(CreateAccountCustomerWindow)



    def retranslateUi(self, CreateAccountCustomerWindow):
        _translate = QtCore.QCoreApplication.translate
        CreateAccountCustomerWindow.setWindowTitle(_translate("CreateAccountCustomerWindow", "Create Account Customer"))
        self.label_6.setText(_translate("CreateAccountCustomerWindow", "Profile:"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("CreateAccountCustomerWindow", "First Name"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("CreateAccountCustomerWindow", "Last Name"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("CreateAccountCustomerWindow", "User Name"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("CreateAccountCustomerWindow", "Phone Number"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("CreateAccountCustomerWindow", "Email"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("CreateAccountCustomerWindow", "Password"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("CreateAccountCustomerWindow", "Status"))
        self.commandLinkButton_2.setText(_translate("CreateAccountCustomerWindow", "Membership"))
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 250)
        self.tableWidget.setColumnWidth(2, 230)
        item = QtWidgets.QTableWidgetItem(f"")
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem(f"")
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem(f"")
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem(f"")
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem(f"")
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem(f"")
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 5, item)





    @staticmethod
    def show_error(message, type_mesasge):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(type_mesasge)
        msg.setText(f"Hello")
        msg.setInformativeText(message)
        msg.setWindowTitle("Message")
        msg.exec_()

    def membership(self):
        x = 0
        list_information = []

        try:
            while x < 6:
                if self.tableWidget.item(x,0).text() == '':
                    raise Exception(f"{self.tableWidget.verticalHeaderItem(x).text()} filed is empty !")

                list_information.append(self.tableWidget.item(x,0).text())
                x+=1

            list_information.append(self.plainTextEdit.toPlainText())

            try:
                creatacccustomer = CreateAccountCustomer(*list_information)
                creatacccustomer.save_information_json_file()
                self.show_error("Your registration was successful !", QtWidgets.QMessageBox.Information)


            except Exception as exc:
                self.show_error(str(exc), QtWidgets.QMessageBox.Warning)
        except Exception as exc:
            self.show_error(str(exc), QtWidgets.QMessageBox.Warning)


        item = QtWidgets.QTableWidgetItem(f"")
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem(f"")
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem(f"")
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem(f"")
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem(f"")
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem(f"")
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 5, item)
        self.plainTextEdit.setPlainText('')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateAccountCustomerWindow = QtWidgets.QMainWindow()
    ui = Ui_CreateAccountCustomerWindow()
    ui.setupUi(CreateAccountCustomerWindow)
    CreateAccountCustomerWindow.show()
    sys.exit(app.exec_())
