# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ServiceWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from choosefood_gui import Ui_ChooseFoodWindow
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
from Cart_selenium import Ui_CartWindow
class Ui_ServiceWindow(QMainWindow):



    def opencartwindow(self,information):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CartWindow()
        self.ui.setupUi(self.window)
        date = str(self.calendarWidget.selectedDate().toPyDate())
        date = date.split('-')
        self.ui.read_inforamtion_file_ordeer(information)
        self.ui.initialize_information(self.user_name, date)
        self.window.show()



    def set_user_name(self, user_name):
        self.user_name = user_name


    def showLoginWindow(self, LoginWindow, ServiceWindow):
        LoginWindow.show()
        self.hidesecend(ServiceWindow)

    def hidesecend(self, secend_w):
        secend_w.hide()

    def open_choosefood(self):
        self.window = QtWidgets.QMainWindow()
        ui = Ui_ChooseFoodWindow()
        ui.setupUi(self.window)
        ui.set_user_name(self.user_name)
        self.window.show()


    def setupUi(self, ServiceWindow, LoginWindow):
        ServiceWindow.setObjectName("ServiceWindow")
        ServiceWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ServiceWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buyfood_commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget, clicked = lambda : self.open_choosefood())
        self.buyfood_commandLinkButton.setGeometry(QtCore.QRect(300, 280, 250, 80))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.buyfood_commandLinkButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/burger.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buyfood_commandLinkButton.setIcon(icon)
        self.buyfood_commandLinkButton.setIconSize(QtCore.QSize(60, 60))
        self.buyfood_commandLinkButton.setObjectName("buyfood_commandLinkButton")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget, clicked = lambda : self.opent_addcommnet())
        self.commandLinkButton.setGeometry(QtCore.QRect(300, 370, 250, 80))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/icons8-comment-58.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon1)
        self.commandLinkButton.setIconSize(QtCore.QSize(60, 60))
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.profile_label = QtWidgets.QLabel(self.centralwidget)
        self.profile_label.setGeometry(QtCore.QRect(570, 20, 150, 150))
        self.profile_label.setFrameShape(QtWidgets.QFrame.Box)
        self.profile_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.profile_label.setAlignment(QtCore.Qt.AlignCenter)
        self.profile_label.setObjectName("profile_label")
        self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_4.setGeometry(QtCore.QRect(300, 480, 250, 80))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_4.setIcon(icon3)
        self.commandLinkButton_4.setIconSize(QtCore.QSize(60, 60))
        self.commandLinkButton_4.setObjectName("commandLinkButton_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(300, 30, 180, 35))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(290, 20, 180, 35))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(290, 30, 180, 35))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(290, 80, 180, 35))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(290, 120, 180, 35))
        self.label_9.setObjectName("label_9")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget, clicked = lambda : self.showLoginWindow(LoginWindow, ServiceWindow))
        self.commandLinkButton_2.setGeometry(QtCore.QRect(20, 480, 80, 80))
        self.commandLinkButton_2.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_2.setIcon(icon4)
        self.commandLinkButton_2.setIconSize(QtCore.QSize(60, 60))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        ServiceWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ServiceWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        ServiceWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ServiceWindow)
        self.statusbar.setObjectName("statusbar")
        ServiceWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ServiceWindow)
        QtCore.QMetaObject.connectSlotsByName(ServiceWindow)

    def retranslateUi(self, ServiceWindow):
        _translate = QtCore.QCoreApplication.translate
        ServiceWindow.setWindowTitle(_translate("ServiceWindow", "ServiceWindow"))
        self.buyfood_commandLinkButton.setText(_translate("ServiceWindow", "Buy Food"))
        self.commandLinkButton.setText(_translate("ServiceWindow", "Add Comment"))
        self.label.setText(_translate("ServiceWindow", "Name :"))
        self.label_2.setText(_translate("ServiceWindow", "Phone Number:"))
        self.label_3.setText(_translate("ServiceWindow", "Email : "))
        self.profile_label.setText(_translate("ServiceWindow", "Profile Photo"))
        self.commandLinkButton_4.setText(_translate("ServiceWindow", "Edit Profole"))
        self.label_7.setText(_translate("ServiceWindow", "..."))
        self.label_8.setText(_translate("ServiceWindow", "..."))
        self.label_9.setText(_translate("ServiceWindow", "..."))

    def set_information_profile(self, user_name):
        import json
        with open(f"F:\\project_ap_99472068\\Users_information\\customer\\{user_name}.json") as outfile:
            data = json.load(outfile)

        self.prof_address = data['Profile']
        self.name = data["first_name"] + ' ' +data["last_name"]
        self.label_7.setText(self.name)
        self.label_8.setText(data["phone_number"])
        self.label_9.setText(data["Email"])


        pixmap = QPixmap(f"F:\\project_ap_99472068\\Users_information\\photo\\{user_name}")
        pixmap = pixmap.scaled(150, 150)
        self.profile_label.setPixmap(pixmap)

    def opent_addcommnet(self):
        from addcommnet import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.ui.setuser_name(self.user_name)
        self.window.show()
        self.ui.show_error("Please select the desired date!", QtWidgets.QMessageBox.Information, self.user_name)







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ServiceWindow = QtWidgets.QMainWindow()
    ui = Ui_ServiceWindow()
    ui.setupUi(ServiceWindow)
    ServiceWindow.show()
    sys.exit(app.exec_())
