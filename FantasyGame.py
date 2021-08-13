# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FantasyGame.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(738, 577)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 101, 16))
        self.label.setObjectName("label")
        self.batle = QtWidgets.QLabel(self.centralwidget)
        self.batle.setGeometry(QtCore.QRect(30, 70, 111, 16))
        self.batle.setObjectName("batle")
        self.bated = QtWidgets.QLineEdit(self.centralwidget)
        self.bated.setGeometry(QtCore.QRect(140, 70, 21, 22))
        self.bated.setText("")
        self.bated.setObjectName("bated")
        self.bwlle = QtWidgets.QLabel(self.centralwidget)
        self.bwlle.setGeometry(QtCore.QRect(200, 70, 101, 16))
        self.bwlle.setObjectName("bwlle")
        self.bwled = QtWidgets.QLineEdit(self.centralwidget)
        self.bwled.setGeometry(QtCore.QRect(310, 70, 21, 22))
        self.bwled.setObjectName("bwled")
        self.wkle = QtWidgets.QLabel(self.centralwidget)
        self.wkle.setGeometry(QtCore.QRect(370, 70, 141, 16))
        self.wkle.setObjectName("wkle")
        self.wked = QtWidgets.QLineEdit(self.centralwidget)
        self.wked.setGeometry(QtCore.QRect(510, 70, 21, 22))
        self.wked.setObjectName("wked")
        self.arle = QtWidgets.QLabel(self.centralwidget)
        self.arle.setGeometry(QtCore.QRect(570, 70, 131, 16))
        self.arle.setObjectName("arle")
        self.ared = QtWidgets.QLineEdit(self.centralwidget)
        self.ared.setGeometry(QtCore.QRect(700, 70, 21, 22))
        self.ared.setObjectName("ared")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 120, 121, 16))
        self.label_6.setObjectName("label_6")
        self.paed = QtWidgets.QLineEdit(self.centralwidget)
        self.paed.setGeometry(QtCore.QRect(150, 120, 41, 22))
        self.paed.setText("")
        self.paed.setObjectName("paed")
        self.rbtn1 = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn1.setGeometry(QtCore.QRect(30, 150, 61, 20))
        self.rbtn1.setObjectName("rbtn1")
        self.rbtn2 = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn2.setGeometry(QtCore.QRect(90, 150, 51, 20))
        self.rbtn2.setObjectName("rbtn2")
        self.rbtn3 = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn3.setGeometry(QtCore.QRect(150, 150, 41, 20))
        self.rbtn3.setObjectName("rbtn3")
        self.rbtn4 = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn4.setGeometry(QtCore.QRect(200, 150, 51, 20))
        self.rbtn4.setObjectName("rbtn4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(580, 120, 91, 20))
        self.label_7.setObjectName("label_7")
        self.pued = QtWidgets.QLineEdit(self.centralwidget)
        self.pued.setGeometry(QtCore.QRect(680, 120, 41, 22))
        self.pued.setText("")
        self.pued.setObjectName("pued")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(270, 120, 91, 16))
        self.label_8.setObjectName("label_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(360, 120, 141, 22))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.exitbtn = QtWidgets.QPushButton(self.centralwidget)
        self.exitbtn.setGeometry(QtCore.QRect(300, 490, 93, 28))
        self.exitbtn.setObjectName("exitbtn")
        self.list1 = QtWidgets.QListWidget(self.centralwidget)
        self.list1.setGeometry(QtCore.QRect(30, 190, 256, 281))
        self.list1.setObjectName("list1")
        self.list2 = QtWidgets.QListWidget(self.centralwidget)
        self.list2.setGeometry(QtCore.QRect(380, 190, 256, 281))
        self.list2.setObjectName("list2")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 738, 28))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")

        self.menuManage_Team = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.menuManage_Team.setFont(font)
        self.menuManage_Team.setObjectName("menuManage_Team")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionNEW = QtWidgets.QAction(MainWindow)
        self.actionNEW.setObjectName("actionNEW")
        self.actionOPEN = QtWidgets.QAction(MainWindow)
        self.actionOPEN.setObjectName("actionOPEN")
        self.actionSAVE = QtWidgets.QAction(MainWindow)
        self.actionSAVE.setObjectName("actionSAVE")
        self.actionEVALUATE = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE.setObjectName("actionEVALUATE")
        self.menuManage_Team.addAction(self.actionNEW)
        self.menuManage_Team.addSeparator()
        self.menuManage_Team.addAction(self.actionOPEN)
        self.menuManage_Team.addSeparator()
        self.menuManage_Team.addAction(self.actionSAVE)
        self.menuManage_Team.addSeparator()
        self.menuManage_Team.addAction(self.actionEVALUATE)
        self.menubar.addAction(self.menuManage_Team.menuAction())

        self.list1.itemDoubleClicked.connect(self.removelist1)
        self.list2.itemDoubleClicked.connect(self.removelist2)

        self.rbtn1.toggled.connect(self.ctg)
        self.rbtn2.toggled.connect(self.ctg)
        self.rbtn3.toggled.connect(self.ctg)
        self.rbtn4.toggled.connect(self.ctg)

        self.menuManage_Team.triggered[QtWidgets.QAction].connect(self.menu)

        self.bat = 0
        self.bwl = 0 
        self.ar = 0
        self.wk = 0
        self.avl = 1100
        self.used = 0

        self.retranslateUi(MainWindow)
        self.exitbtn.clicked.connect(self.exit)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Your Selection"))
        self.batle.setText(_translate("MainWindow", "Batsman (BAT) :"))
        self.bwlle.setText(_translate("MainWindow", "Bowler (BWL) :"))
        self.wkle.setText(_translate("MainWindow", "Wicketkeeper (WK) :"))
        self.arle.setText(_translate("MainWindow", "All Rounders (AR) :"))
        self.label_6.setText(_translate("MainWindow", "Points Available :"))
        self.rbtn1.setText(_translate("MainWindow", "BAT"))
        self.rbtn2.setText(_translate("MainWindow", "BWL"))
        self.rbtn3.setText(_translate("MainWindow", "AR"))
        self.rbtn4.setText(_translate("MainWindow", "WK"))
        self.label_7.setText(_translate("MainWindow", "Points Used :"))
        self.label_8.setText(_translate("MainWindow", "Team Name :"))
        self.exitbtn.setText(_translate("MainWindow", "EXIT"))
        self.menuManage_Team.setTitle(_translate("MainWindow", "Manage Team"))
        self.actionNEW.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE.setText(_translate("MainWindow", "EVALUATE Team"))


    def exit(self):
        import sys
        self.showdlg("THANK YOU....Hope you enjoyed !!")
        sys.exit()

    def menu(self,action):
        txt = (action.text())
        
        if txt == 'NEW Team':
            self.bat = 0
            self.bwl = 0
            self.ar = 0
            self.wk = 0
            self.avl = 1100
            self.used = 0
            self.list1.clear()
            self.list2.clear()

            text, ok=QtWidgets.QInputDialog.getText(MainWindow, "Team", "Enter name of team:")
            if ok:
                self.lineEdit_7.setText(str(text))
            self.show()

        if txt == 'SAVE Team':
            count = self.list2.count()
            selected = ""
            for i in range(count):
                selected += self.list2.item(i).text()
                if i < count:
                    selected += ","
            self.saveteam(self.lineEdit_7.text(),selected,self.used)
                
        if txt == 'OPEN Team':
            self.bat = 0
            self.bwl = 0
            self.ar = 0
            self.wk = 0
            self.avl = 1000
            self.used = 0
            self.list1.clear()
            self.list2.clear()
            self.show()
            self.openteam()

        if txt == 'EVALUATE Team' :
            from score import Ui_Dialog
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog)
            ret=Dialog.exec()

    def show(self):
        self.bated.setText(str(self.bat))
        self.bwled.setText(str(self.bwl))
        self.wked.setText(str(self.wk))
        self.ared.setText(str(self.ar))
        self.paed.setText(str(self.avl))
        self.pued.setText(str(self.used))

    def criteria(self,ctgr,item):
        msg = ''
        if ctgr=="BAT" and self.bat>=5:msg="Batsmen not more than 5"
        if ctgr=="BWL" and self.bwl>=5:msg="bowlers not more than 5"
        if ctgr=="AR" and self.ar>=3:msg="Allrounders not more than 3"
        if ctgr=="WK" and self.wk>=2:msg="Wicketkeepers not more than 2"
        if msg!='':
            self.showdlg(msg)
            return False

        if self.avl<=85:
            msg="You Have Exhausted your Points"
            self.showdlg(msg)
            return False
        
        if ctgr=="BAT":self.bat+=1
        if ctgr=="BWL":self.bwl+=1
        if ctgr=="AR":self.ar+=1
        if ctgr=="WK":self.wk+=1

        sql = "select value from stats where player = '"+item.text()+"'"
        cur = conn.execute(sql)
        row = cur.fetchone()
        self.avl -= int(row[0])
        self.used += int(row[0])
        return True

    def removelist1(self,item):
        ctgr = ''
        if self.rbtn1.isChecked()==True:ctgr='BAT'
        if self.rbtn2.isChecked()==True:ctgr='BWL'
        if self.rbtn3.isChecked()==True:ctgr='AR'
        if self.rbtn4.isChecked()==True:ctgr='WK'
        ret = self.criteria(ctgr,item)
        
        if ret==True:
            self.list1.takeItem(self.list1.row(item))
            
            self.list2.addItem(item.text())
            self.show()

    def ctg(self):
        ctgr = ''
        if self.rbtn1.isChecked()==True:ctgr='BAT'
        if self.rbtn2.isChecked()==True:ctgr='BWL'
        if self.rbtn3.isChecked()==True:ctgr='AR'
        if self.rbtn4.isChecked()==True:ctgr='WK'
       	
        self.fillList(ctgr)

    def removelist2(self,item):
        self.list2.takeItem(self.list2.row(item))
        cursor = conn.execute("select player, value, ctg from stats where player ='"+item.text()+"'")
        row=cursor.fetchone()
        self.avl=self.avl+int(row[1])
        self.used=self.used-int(row[1])
        ctgr=row[2]
        if ctgr=="BAT":
            self.bat-=1
            if self.rbtn1.isChecked()==True:
                self.list1.addItem(item.text())
        if ctgr=="BWL":
            self.bwl-=1
            if self.rbtn2.isChecked()==True:
                self.list1.addItem(item.text())
        if ctgr=="AR":
            self.ar-=1
            if self.rbtn3.isChecked()==True:
                self.list1.addItem(item.text())
        if ctgr=="WK":
            self.wk-=1
            if self.rbtn4.isChecked()==True:
                self.list1.addItem(item.text())
        self.show()

    def fillList(self,ctgr):
        if self.lineEdit_7.text()=='':
            self.showdlg("Enter name fo the team")
            return
        self.list1.clear()
        sql = "select player from players where ctg='"+ctgr+"';"
        cur = conn.execute(sql)
        for row in cur:
            selected=[]
            for i in range(self.list2.count()):
                selected.append(self.list2.item(i).text())
            if row[0] not in selected:
                self.list1.addItem(row[0])

    def openteam(self):
        sql = "select team_name from teams;"
        cur = conn.execute(sql)
        teams = []
        for row in cur:
            teams.append(row[0])
        team, ok=QtWidgets.QInputDialog.getItem(MainWindow,"Dream","Choose A Team",teams,0,False)
        if ok and team:
            self.lineEdit_7.setText(team)

        sql = "select team_players,team_value from teams where team_name='"+team+"';"
        cur = conn.execute(sql)
        row = cur.fetchone()
        selected = row[0].split(',')
        self.list2.addItems(selected)
        self.used = row[1]

        self.avl = 1100 - row[1]
        count = self.list2.count()

        for i in range(count-1):
            ply = self.list2.item(i).text()
            sql = "select ctg from stats where player='"+ply+"';"

            cur = conn.execute(sql)
            row = cur.fetchone()
            ctgr = row[0]
            if ctgr=="BAT":self.bat+=1
            if ctgr=="BWL":self.bwl+=1
            if ctgr=="AR":self.ar+=1
            if ctgr=="WK":self.wk+=1

        self.show()

    def saveteam(self,nm,ply,val):
        if self.bat+self.bwl+self.ar+self.wk!=11:
            self.showdlg("Insufficient players")
            return
        sql = "INSERT INTO teams (team_name, team_players, team_value) VALUES ('"+nm+"','"+ply+"','"+str(val)+"');"
        try:
            cur = conn.execute(sql)
            self.showdlg("Team Saved Successfully")
            conn.commit()
        except:
            self.showdlg("Error in Operation")
            conn.rollback()

    def showdlg(self,msg):
        Dialog=QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("Fantasy Team selector")
        ret=Dialog.exec()



if __name__ == "__main__":
    import sqlite3
    conn = sqlite3.connect('Fantasygame.db')
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
