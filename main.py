from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QGraphicsScene
import new


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.value_ = ""
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(1149, 775)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(0,0,0)")
        self.gridLayout_8 = QtWidgets.QGridLayout(MainWindow)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(MainWindow)
        self.frame.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setStyleSheet("background-color: rgb(171, 171, 171);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setStyleSheet("background-color: rgb(171, 171, 171);\\n")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet("background-color: rgb(171, 171, 171);\\n")
        self.gridLayout_3.addWidget(self.pushButton_5, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame_3, 1, 1, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet("background-color: rgb(171, 171, 171);\\n")
        self.gridLayout_11.addWidget(self.pushButton_4, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_11.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(75, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_11.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_7.setStyleSheet("background-color: rgb(171, 171, 171);\\n")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_11.addWidget(self.pushButton_7, 2, 2, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_11.addWidget(self.comboBox_2, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_11.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_11.addWidget(self.comboBox, 2, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("background-color: rgb(171, 171, 171);\\n")
        self.gridLayout_11.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(75, 0))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_11.addWidget(self.lineEdit_4, 2, 1, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_11, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame_5, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setWhatsThis("")
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("font: 18pt \"Arial\";\n"
"color: rgb(64, 64, 64);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.label_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_7.setLineWidth(1)
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(False)
        self.label_7.setObjectName("label_7")
        self.gridLayout_9.addWidget(self.label_7, 0, 0, 1, 3)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_6.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.graphicsView.setFont(font)
        self.graphicsView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graphicsView.setLineWidth(0)
        self.graphicsView.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_6.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_6, 3, 0, 1, 3)
        self.gridLayout_21 = QtWidgets.QGridLayout()
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setStyleSheet("background-color: rgb(171, 171, 171);\\n")
        self.gridLayout_21.addWidget(self.pushButton_6, 2, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setStyleSheet("background-color: rgb(171, 171, 171);\\n")
        self.gridLayout_21.addWidget(self.pushButton_8, 1, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setStyleSheet("background-color: rgb(171, 171, 171);\\n")
        self.gridLayout_21.addWidget(self.pushButton_9, 0, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_21, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_2.clicked.connect(self.browser_key)
        self.pushButton_7.clicked.connect(self.browser_file)

        self.pushButton.clicked.connect(self.encrypt)
        self.pushButton_3.clicked.connect(self.decrypt)

        self.pushButton_4.clicked.connect(self.hash)

        self.pushButton_8.clicked.connect(self.clear)
    #     pushButton_9
        self.pushButton_9.clicked.connect(self._save_image)
        self.pushButton_5.clicked.connect(self.generate)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Encryptor"))
        self.pushButton.setToolTip(_translate("MainWindow", "Upload memory dump"))
        self.pushButton.setText(_translate("MainWindow", "Encrypt"))
        self.pushButton_3.setToolTip(_translate("MainWindow", "Confirm action"))
        self.pushButton_3.setText(_translate("MainWindow", "Decrypt"))
        self.pushButton_5.setText(_translate("MainWindow", "Generate Key"))
        self.pushButton_4.setText(_translate("MainWindow", "Calculate"))
        self.label.setText(_translate("MainWindow", "Hash"))
        self.pushButton_7.setText(_translate("MainWindow", "Search"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Key"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Password"))
        self.comboBox.setItemText(0, _translate("MainWindow", "File"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Folder"))
        self.pushButton_2.setText(_translate("MainWindow", "Select"))
        self.label_7.setText(_translate("MainWindow", "Encryptor (Developer: Masrik Dahir)"))
        self.pushButton_6.setText(_translate("MainWindow", "@$$"))
        self.pushButton_8.setText(_translate("MainWindow", "Clear"))
        self.pushButton_9.setText(_translate("MainWindow", "Save"))

    def browser_file(self):
        if str(self.comboBox.currentText()) == "File":
            path = QFileDialog.getOpenFileName()[0]
            self.lineEdit_4.setText(str(path))
        else:
            dir_ = QFileDialog.getExistingDirectory(None, 'Select a folder:', '')
            self.lineEdit_4.setText(str(dir_))

    def browser_key(self):
        if str(self.comboBox_2.currentText()) == "Key":
            path = QFileDialog.getOpenFileName()[0]
            self.lineEdit_2.setText(str(path))

    def encrypt(self):
        # print(self.lineEdit_4.text())
        if str(self.comboBox.currentText()) == "File":
            if str(self.comboBox_2.currentText()) == "Key":
                self.value_ += new.encrypt(str(self.lineEdit_4.text()), str(self.lineEdit_2.text())) + "\n\n"
                scene = QGraphicsScene()
                scene.addText(self.value_)
                self.graphicsView.setScene(scene)
            else:
                self.value_ += new.encrypt_by_password(str(self.lineEdit_4.text()), str(self.lineEdit_2.text())) + "\n\n"
                scene = QGraphicsScene()
                scene.addText(self.value_)
                self.graphicsView.setScene(scene)
        else:
            if str(self.comboBox_2.currentText()) == "Key":
                self.value_ += str(new.encrypt_max(str(self.lineEdit_4.text()), str(self.lineEdit_2.text()))) + "\n\n"
                scene = QGraphicsScene()
                scene.addText(self.value_)
                self.graphicsView.setScene(scene)
            else:
                self.value_ += new.password_encrypt_max(str(self.lineEdit_4.text()), str(self.lineEdit_2.text())) + "\n\n"
                scene = QGraphicsScene()
                scene.addText(self.value_)
                self.graphicsView.setScene(scene)

    def decrypt(self):
        # print(self.lineEdit_4.text())
        if str(self.comboBox.currentText()) == "File":
            if str(self.comboBox_2.currentText()) == "Key":
                self.value_ += new.decrypt(str(self.lineEdit_4.text()), str(self.lineEdit_2.text())) + "\n\n"
                scene = QGraphicsScene()
                scene.addText(self.value_)
                self.graphicsView.setScene(scene)
            else:
                self.value_ += new.decrypt_by_password(str(self.lineEdit_4.text()), str(self.lineEdit_2.text())) + "\n\n"
                scene = QGraphicsScene()
                scene.addText(self.value_)
                self.graphicsView.setScene(scene)
        else:
            if str(self.comboBox_2.currentText()) == "Key":
                self.value_ += new.decrypt_max(str(self.lineEdit_4.text()), str(self.lineEdit_2.text())) + "\n\n"
                scene = QGraphicsScene()
                scene.addText(self.value_)
                self.graphicsView.setScene(scene)
            else:
                self.value_ += new.password_decrypt_max(str(self.lineEdit_4.text()), str(self.lineEdit_2.text())) + "\n\n"
                scene = QGraphicsScene()
                scene.addText(self.value_)
                self.graphicsView.setScene(scene)

    def hash(self):
        path = QFileDialog.getOpenFileName()[0]
        self.lineEdit.setText(str(path))

        self.value_ += "Name: " + str(path) + "\nDate: " + str(datetime.now()) + "\n" + new.hash(self.lineEdit.text()) + "\n\n"
        scene = QGraphicsScene()
        scene.addText(self.value_)
        self.graphicsView.setScene(scene)

    def clear(self):
        self.value_ = ""
        scene = QGraphicsScene()
        scene.addText(self.value_)
        self.graphicsView.setScene(scene)

    def _save_image(self):
        f = open(str(datetime.now()).replace("-","_").replace(":","_")+".txt", "a")
        f.write(str(self.value_))
        f.close()

    def generate(self):
        name = QFileDialog.getSaveFileName()[0]
        new.create_key(str(name))

# main
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
