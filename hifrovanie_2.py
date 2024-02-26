from PyQt5 import QtCore, QtGui, QtWidgets
import sys

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

        font_1, font_2, font_3, font_4, font_5, font_6 = QtGui.QFont(), QtGui.QFont(), QtGui.QFont(), QtGui.QFont(),\
            QtGui.QFont(), QtGui.QFont()
        self.spisok_font = [[font_1, 12, False, 50, "Segoe UI"], [font_2, 16, True, 75, "Segoe Print"],
                            [font_3, 14, True, 75, "Segoe Print"], [font_4, 12, False, 50, "Segoe Print"],
                            [font_5, 7, True, 75, "Segoe Print"], [font_6, 12, True, 75, "Segoe Print"]]
        for i in self.spisok_font:
            i[0].setFamily(i[4])
            i[0].setPointSize(i[1])
            i[0].setBold(i[2])
            i[0].setWeight(i[3])

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 30, 1000, 250))
        self.textEdit.setFont(font_1)

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 460, 1000, 250))
        self.textBrowser.setFont(font_1)

        self.label, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6, self.label_7, self.label_8,\
            self.label_9 = QtWidgets.QLabel(self.centralwidget), QtWidgets.QLabel(self.centralwidget),\
            QtWidgets.QLabel(self.centralwidget), QtWidgets.QLabel(self.centralwidget),\
            QtWidgets.QLabel(self.centralwidget), QtWidgets.QLabel(self.centralwidget),\
            QtWidgets.QLabel(self.centralwidget), QtWidgets.QLabel(self.centralwidget),\
            QtWidgets.QLabel(self.centralwidget)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)

        self.spisok_l = [[self.label, 520, 300, 160, 25, font_2, 'доп. «ключи»:'],
                         [self.label_2, 530, 330, 30, 30, font_2, 'x'], [self.label_3, 590, 330, 30, 30, font_2, 'y'],
                         [self.label_4, 650, 330, 30, 30, font_2, 'z'], [self.label_5, 550, 415, 100, 25, font_4, '(от 1 до 9)'],
                         [self.label_6, 820, 300, 160, 70, font_2, 'главный \nотступ: '],
                         [self.label_7, 880, 420, 140, 25, font_5, 'разработчик: Тарасов Д.Л.'],
                         [self.label_8, 30, 390, 450, 55, font_4, ''], [self.label_9, 20, 0, 60, 25, font_6, 'сюда:'],
                         [self.pushButton, 170, 310, 200, 50, font_2, "делать. "]]
        for i in self.spisok_l:
            i[0].setGeometry(QtCore.QRect(i[1], i[2], i[3], i[4]))
            i[0].setFont(i[5])

        self.spinBox = QtWidgets.QSpinBox(self.centralwidget, value=1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget, value=2)
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget, value=3)
        self.spinBox_4 = QtWidgets.QSpinBox(self.centralwidget)

        self.spisok_spinB = [[self.spinBox, 520, 370, 35, 1, 9], [self.spinBox_2, 580, 370, 35, 1, 9],\
                             [self.spinBox_3, 640, 370, 35, 1, 9], [self.spinBox_4, 930, 340, 60, 0, 25]]
        for i in self.spisok_spinB:
            i[0].setGeometry(QtCore.QRect(i[1], i[2], i[3], 35))
            i[0].setFont(font_3)
            i[0].setRange(i[4], i[5])

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
        for i in self.spisok_l:
            i[0].setText(_translate("MainWindow", i[6]))



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
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.label_8.setText('')
    ui.pushButton.clicked.connect(knopka)
    sys.exit(app.exec_())
