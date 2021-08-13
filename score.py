# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'score.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(586, 528)
        self.cb0 = QtWidgets.QComboBox(Dialog)
        self.cb0.setGeometry(QtCore.QRect(140, 20, 101, 21))
        self.cb0.setObjectName("cb0")
        import sqlite3
        conn = sqlite3.connect('Fantasygame.db')
        sql = "select team_name from teams"
        cur = conn.execute(sql)
        teams=[]
        for row in cur:
            self.cb0.addItem(row[0])
        conn.close()
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 94, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(330, 20, 97, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.cb1 = QtWidgets.QComboBox(Dialog)
        self.cb1.setGeometry(QtCore.QRect(430, 20, 101, 22))
        self.cb1.setObjectName("cb1")
        self.cb1.addItem("Season2020")
        self.cb1.addItem("Season2021")
        self.cb1.addItem("")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(20, 50, 521, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(110, 70, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(400, 70, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(20, 90, 521, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lw1 = QtWidgets.QListWidget(Dialog)
        self.lw1.setGeometry(QtCore.QRect(20, 110, 256, 301))
        self.lw1.setObjectName("lw1")
        self.lw2 = QtWidgets.QListWidget(Dialog)
        self.lw2.setGeometry(QtCore.QRect(290, 110, 256, 301))
        self.lw2.setObjectName("lw2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(230, 420, 121, 28))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calculate)
        self.scoreline = QtWidgets.QLineEdit(Dialog)
        self.scoreline.setGeometry(QtCore.QRect(300, 460, 61, 22))
        self.scoreline.setObjectName("scoreline")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(240, 460, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def calculate(self):
        import sqlite3
        conn = sqlite3.connect('Fantasygame.db')
        team=self.cb0.currentText()
        self.lw1.clear()
        sql1="SELECT team_players, team_value from teams where team_name='"+team+"'"
        cur=conn.execute(sql1)
        row=cur.fetchone()
        selected = row[0].split(',')
        self.lw1.addItems(selected)
        teamttl=0
        self.lw2.clear()
        match=self.cb1.currentText()
        count = self.lw1.count()-1
        for i in range(count):
            ttl=0
            batscore=0
            bowlscore=0
            fieldscore=0
            nm=self.lw1.item(i).text()
            cursor=conn.execute("SELECT * from "+ match +" where player='"+nm+"'")
            row=cursor.fetchone()
            if row[1]==0:
                ttl=2
            else:
                batscore=int(row[2]/2)
                if row[2]>=50: batscore+=5
                if row[2]>=100: batscore+=10
                if row[2]>0:
                    sr=int(row[2]/row[3])
                    if sr>=80 and sr<100: batscore+=2
                    if sr>=100:batscore+=4
                batscore=batscore+row[4]
                batscore=batscore+2*row[5]
                bowlscore=row[9]*10
                if row[7]>=0: bowlscore=bowlscore+(row[7]*3)
                if row[7]>0:
                    er=int(6*row[8]/row[6])
                    if er<=2: bowlscore=bowlscore+10
                    if er>2 and er<=3.5: bowlscore=bowlscore+7
                    if er>3.5 and er<=4.5: bowlscore=bowlscore+4
                fieldscore=(row[10]+row[11])*10            
                ttl=int((batscore+bowlscore+fieldscore)/row[1])+2
            self.lw2.addItem(str(ttl))
            teamttl=teamttl+ttl
        self.scoreline.setText(str(teamttl))


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Choose Team :"))
        self.label_2.setText(_translate("Dialog", "Choose Season :"))
        self.label_3.setText(_translate("Dialog", "Players"))
        self.label_4.setText(_translate("Dialog", "Score"))
        self.pushButton.setText(_translate("Dialog", "Calculate Score"))
        self.label_5.setText(_translate("Dialog", "Total :"))
        self.scoreline.setText(_translate("Dialog", "00"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
