from PyQt5 import QtCore, QtGui, QtWidgets

a = ["ф", "б", "f", "g", "h",  "m", "n", "!", "в", "г", "9", "а", "е", "р", "4", "2", "ё", "и", "6", "-", "о",
     "у", "д", "ж", "з", "й", "к", "t", "z", "r", "л", "?", "i", "j", "k", "l", "7", "м", "3", "н", "v", "p", "w",
     "п", "0", "х", "ч", "ц", "5", "ш", ":", "щ", " ", "8", "ы",  "ь", "1", "ъ", ",", "с", ".", "т", "a", "b", "c",
     "d", "e", "o", "э", "ю", "я", "q",  "u", "x", "y", "s"]


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1040, 760)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 30, 1000, 250))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 460, 1000, 250))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(520, 300, 160, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 330, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(590, 330, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(650, 330, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget, value=1)
        self.spinBox.setGeometry(QtCore.QRect(520, 370, 35, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox.setFont(font)
        self.spinBox.setRange(1, 9)
        self.spinBox.setObjectName("spinBox")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(570, 420, 100, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(820, 300, 160, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(880, 420, 140, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 310, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)

        self.pushButton.setObjectName("pushButton")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 390, 450, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget, value=2)
        self.spinBox_2.setGeometry(QtCore.QRect(580, 370, 35, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setRange(1, 9)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget, value=3)
        self.spinBox_3.setGeometry(QtCore.QRect(640, 370, 35, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_3.setFont(font)
        self.spinBox_3.setRange(1, 9)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_4.setGeometry(QtCore.QRect(930, 340, 60, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_4.setFont(font)
        self.spinBox_4.setObjectName("spinBox_4")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 0, 60, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1040, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "шифр."))
        self.label.setText(_translate("MainWindow", "доп. «ключи»:"))
        self.label_2.setText(_translate("MainWindow", "x"))
        self.label_3.setText(_translate("MainWindow", "y"))
        self.label_4.setText(_translate("MainWindow", "z"))
        self.label_5.setText(_translate("MainWindow", "(от 1 до 9)"))
        self.label_6.setText(_translate("MainWindow", "главный \nотступ: "))
        self.label_7.setText(_translate("MainWindow", "разработчик: Тарасов Д.Л."))
        self.pushButton.setText(_translate("MainWindow", "делать. "))
        self.label_8.setText(_translate("MainWindow", "*тех. строка*****************************************"
                                                      "\n*******************************************************"))
        self.label_9.setText(_translate("MainWindow", "сюда:"))


def knopka():
    'кнопка'
    o = ""
    x = ui.spinBox.value()
    y = ui.spinBox_2.value()
    z = ui.spinBox_3.value()
    t = ui.textEdit.toPlainText()
    w = ui.spinBox_4.value()
    if len(t) < 5:
        o = "текст слишком короткий. (надо минимум 5 знаков)"
    elif w > len(t) * 3:
        o = "главный отступ слишком велик."
    elif x == y and x == z:
        o = 'значения доп. "ключей",\nдолжны быть НЕравными'
    if len(o) > 0:
        ui.label_8.setText(o)
        return False

    if ui.textEdit.toPlainText().isdigit():
        de_hifr()
    else:
        hifr()

def hifr():
    'шифровка тескта'
    ui.label_8.setText("")
    x = ui.spinBox.value()
    y = ui.spinBox_2.value()
    z = ui.spinBox_3.value()
    t = ui.textEdit.toPlainText()
    w = ui.spinBox_4.value()

    t1, t2 = "", ""

    b = [(i + x if i % 4 == 0 else i * x) if i % 2 == 0 else i * z * y + 1
         for i in range(len(a) * 3) if (i + 1) % 2 == 0]

    for i, n in enumerate(b):
        b[i] = str(n)
    for i, n in enumerate(b):
        if int(n) % 2 == 0:
            b[i] = b[i].rjust(4, str(x))
        elif int(n) % 3 == 0:
            b[i] = b[i].ljust(4, str(y))
        else:
            b[i] = b[i].rjust(4, str(z))
    b1 = []
    while len(b1) != len(a):
        for n in b:
            if not (n in b1) and len(b1) != len(a):
                b1.append(n)
    try:
        c = [[a[i], b1[i]] for i in range(len(a))]
        eni = dict(c)
        t = t.lower()
        for n in t:
            if n in eni:
                t1 += eni[n]
        j = 0
        for n in t1:
            j += 1
            if j == w + 1:
                t2 += str(x)
            elif j == w + 8:
                t2 += str(y)
            elif j == w + 10:
                t2 += str(z)
            t2 += n
        ui.label_8.setText("\nвот:")
        ui.textBrowser.setText(t2)
    except:
        pass

def de_hifr():
    'дешифровка текста'
    ui.label_8.setText("")
    t = ui.textEdit.toPlainText()
    t = list(t)
    w = ui.spinBox_4.value()
    t1, t3 = [], []

    x = int(t[w])
    y = int(t[w + 8])
    z = int(t[w + 11])
    del t[w]
    del t[w + 7]
    del t[w + 9]

    b = [(i + x if i % 4 == 0 else i * x) if i % 2 == 0 else i * z * y + 1
         for i in range(len(a) * 3) if (i + 1) % 2 == 0]

    for i, n in enumerate(b):
        b[i] = str(n)
    for i, n in enumerate(b):
        if int(n) % 2 == 0:
            b[i] = b[i].rjust(4, str(x))
        elif int(n) % 3 == 0:
            b[i] = b[i].ljust(4, str(y))
        else:
            b[i] = b[i].rjust(4, str(z))

    b1 = []
    while len(b1) != len(a):
        for n in b:
            if not (n in b1) and len(b1) != len(a):
                b1.append(n)
    try:
        c = [[b1[i], a[i]] for i in range(len(a))]
        eni = dict(c)
        for i, n in enumerate(t):
            t1 += n
            if (i + 1) % 4 == 0:
                t1 += " "

        t2 = "".join(t1)
        t2 = t2.split(" ")
        for n in t2:
            if n in eni:
                t3 += eni[n]
        t3 = "".join(t3)
        ui.label_8.setText("\nвот:")
        ui.textBrowser.setText(t3)
    except:
        pass



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.label_8.setText("")
    ui.pushButton.clicked.connect(knopka)

    sys.exit(app.exec_())
