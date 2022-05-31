#importing PySide Modules 
from configparser import Error
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtPrintSupport import *
#---------------------------------------

#importing the json module
import json

#importing time,sys an os module
import time,sys,os

#importing sql modules
import mysql.connector as mc
import sqlite3
#-------------------------------

#importing UI FILES CONVERTED TO PYTHON FILES
from Menu import Ui_MainWindow
from register import Ui_Form
from consultation import Ui_Consulation
from patientsaved import Ui_PatientSaved
from Modify import Ui_Modify
from recapitulatif import Ui_Recapitulatif
from carnets import Ui_Carnet
from parametre import Ui_Parametre
from apropos import Ui_Apropos
from nsconfig import Ui_NsConfig

#importing the DB CLASS

from NsDataBase import *

#--------------------------------------------------------

#--------PATH-------------------------------------
DATABASE_PATH = '.DB/' if sys.platform == 'linux' else 'DB/'
print(DATABASE_PATH)
HTML_PATH = 'HTML/' #if sys.platform == 'linux' else 'HTML/'
LOG_PATH = '.LOG/' if sys.platform == 'linux' else 'LOG/'
NASPITOO_PATH_CONFIG_FILE = ".Naspitoo-Conifg/" if sys.platform == 'linux' else 'Naspitoo-Conifg/'

def hideFile(folder:str):
    if os.path.exists(folder):
        if sys.platform == 'win32':
            os.system('attrib +H '+folder)

#Function To Create Folder
def CreateFolder(folder:str) -> bool:
    if os.path.exists(folder):
        return False
    else:
        os.system('mkdir '+folder)
        return True

CreateFolder(HTML_PATH)
CreateFolder(LOG_PATH)
CreateFolder(NASPITOO_PATH_CONFIG_FILE)
CreateFolder(DATABASE_PATH)


#-------------------------------------------------

#NvData Class To Get Day,Time and year
class NvDate(object):
    import time

    '''
        %H : Hour (24-hour clock) as a decimal number [00,23]
        %M : Minute as a decimal number [00,59].
        %S : Second as a decimal number [00,61].
        %Y : Year with century as a decimal number.
        %d : Day of the month as a decimal number [01,31].
        %m : Month as a decimal number [01,12].
        %a : Locale's abbreviated weekday name.
        %A : Locale's full weekday name.
        %b : Locale's abbreviated month name.
        %B : Locale's full month name.
        %c : Locale's appropriate date and time representation.
        %I : Hour (12-hour clock) as a decimal number [01,12].
        %p : Locale's equivalent of either AM or PM.
    '''

    def __init__(self):
        super().__init__()

        self.time = time

    def getTime(self) -> str:
        return str(self.time.strftime("%H:%M:%S"))

    def getYear(self) -> str:
        return str(self.time.strftime("%Y"))

    def getDay(self) -> str:
        return str(self.time.strftime("%d-%m-%B %Y"))

    def getDayTime(self) -> str:
        return str(self.time.strftime("%H:%M:%S %p  %b,%d %B %Y "))
    
    def getWknm(self):
        return self.time.strftime("%A")

#---------------------------------------------------------------

#---------------------JSON CLASS--------------------

jsonstring = str

class NvJson(object):
    def __init__(self):
        global NASPITOO_PATH_CONFIG_FILE
        super().__init__()
        self._file_to_json = NASPITOO_PATH_CONFIG_FILE+"config.json"
        self.createJsonFileConfig()
    
    def createJsonFileConfig(self,reset=False):
        if not os.path.exists(self._file_to_json) or reset==True:
            jsontext = '''
                        {
                            "VILLE":[
                                "Yaounde",
                                "Douala",
                                "Tonga",
                                "Autre"
                            ],
                            "PROFESSION":[
                                "Cultivateur/Cultivatrice",
                                "Fonctionaire",
                                "Éleve",
                                "Commerçant(e)",
                                "Autre",
                                "Ménagère"
                            ],
                            "LANGUAGE":[
                                {
                                    "french" : true,
                                    "english":false
                                }
                            ],
                            "INTERVENTION":[
                                "EXTRACTION",
                                "SOINS CONSERVATEUR",
                                "ORDONNANCE",
                                "CONSEIL (IHBD)",
                                "RÉFÉRENCE + ORDONNANCE",
                                "DECAPUCHONNAGE",
                                "DÉTARTRAGE",
                                "RAS"

                            ],
                            "LASTYEAR":
                            [
                                2016,
                                2017,
                                2018,
                                2019,
                                2020,
                                2021
                            ],
                            "mysql" : false,
                            "sqlite" : true,
                            "DATABASETYPE": "sqlite",
                            "SQLITEDATABASENAME" : "Hospital.db",
                            "PATHTOSQLITEDATABASE":".DB/",
                            "MySQl":
                            {
                                "host":"127.0.0.1",
                                "username" : "root",
                                "database" : "",
                                "port" : 3306,
                                "password" : ""
                            }
                            
                        }
                        '''

            data = json.loads(jsontext)
            #print(data)
            newdata = json.dumps(data,indent=4,ensure_ascii=False,sort_keys=True)
            #print(newdata)

            with open(self._file_to_json,"w") as f:
                f.write(newdata)
                #json.dumps(newdata,f,indent=4,ensure_ascii=False,sort_keys=True)

    def readJson(self) -> jsonstring:
        with open(self._file_to_json) as f:
            data = json.load(f)

        return data

    def writeJson(self,jsontext:str):
        if jsontext:
            with open(self._file_to_json,"w") as f:
                json.dump(jsontext,f,indent=4,ensure_ascii=False,sort_keys=True)

    def changeLanguage(self,lang:str='french'):
        if lang == 'french':
            pass

        elif lang == 'english':
            pass

    def getDbType(self):
        data = self.readJson()['mysql'],self.readJson()['sqlite']

        if data[0] == True:
            return 'mysql'
        else:
            return 'sqlite'

    def setDbType(self,dbtype:str):
        if dbtype:
            data = self.readJson()
            if dbtype == 'sqlite':
                data['sqlite'] = True
                data['mysql'] = False

            elif dbtype == 'mysql':
                data['mysql'] = True
                data['sqlite'] = False

            self.writeJson(data)

    def getSqlDbName(self) -> str:
        return self.readJson()['SQLITEDATABASENAME']


    def getSqlDbPath(self) ->str:
        return self.readJson()['PATHTOSQLITEDATABASE']

    def getMysqlInfo(self):
        return self.readJson()['MySQl']

    def getIntervention(self) -> list:
        return self.readJson()["INTERVENTION"]

    def getLastYear(self) -> list:
        return self.readJson()['LASTYEAR']

    def getTown(self) -> list:
        return self.readJson()['VILLE']

    def getProff(self) -> list:
        return self.readJson()['PROFESSION']

    def addIntervention(self,intervention:str):
        data = self.readJson()
        if intervention:
            if isinstance(intervention, str):
                if intervention not in data['INTERVENTION']:
                    data['INTERVENTION'].append(intervention.upper())
                    self.writeJson(data)
                    return True
                else:
                    return f"{intervention} type must be a string"
    
    def addYear(self,year):
        data = self.readJson()
        if year:
            if isinstance(year,int):
                if year not in data['LASTYEAR']:
                    data['LASTYEAR'].append(year)
                    self.writeJson(data)
            else:
                return f"Year must be an integer but found {type(year)}"

    def addProff(self,profession:str):
        data = self.readJson()
        if profession:
            if isinstance(profession,str):
                if profession not in data['PROFESSION']:
                    data['PROFESSION'].append(profession.capitalize())
                    self.writeJson(data)
            else:
                return f"Profession must be of type string but {type(profession)} found"
            
    def addTown(self,town:str):
        data = self.readJson()
        if town:
            if isinstance(town,str):
                if town not in data['VILLE']:
                    data['VILLE'].append(town.capitalize())
                    self.writeJson(data)
                    return True
            else:
                return f"Town must be of type string but {type(town)} found"

#-------------------------END-----------------------

NvJson().addYear(int(NvDate().getYear()))
#NvJson().createJsonFileConfig(reset=True)
year = int(NvDate().getYear())
#print(NvJson().getLastYear())
count = 0


#Class Logs which helps alot in case of a problem
class Logs(object):
    """docstring for Logs"""
    def __init__(self):
        super(Logs, self).__init__()
        self._line = "="*130 + '\n'

    def write(self,text):
        with open(LOG_PATH+"log.txt","a") as f:
            f.write(text+"\n"+self._line)

class NsConfig(QWidget,Ui_NsConfig):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)

        self.setupUi(self)
        
        self.fillTables()
        self._enable = False
        self._disable = True
        self._enableville = False
        self._disableville = True
        self._enablepro = False
        self._disablepro = True
        self._enableint = False
        self._disableint = True
        self._enableyr = False
        self._disableyr = True

        self.databasetype = 'sqlite'
        self.databaseName = None

        self.radiomysql.toggled.connect(self.onSelected)
        self.radiosqlite.toggled.connect(self.onSelected)


        self.btnsaveconfig.clicked.connect(self.SaveConfigurations)
        self.btnreset.clicked.connect(self.reset)

        self.btnconnectmysql.clicked.connect(self.trymysqlconnection)


        #diabling all the tables
        
        self.villetable.setEnabled(False)
        self.frame_9.setEnabled(False)
        self.professiontable.setEnabled(False)
        self.interventiontable.setEnabled(False)
        self.anneetable.setEnabled(False)
        #-------------------------------------------

        #-------------------------------------------------------------------

        self.checkBox.clicked.connect(self.disable)
        self.activateville.clicked.connect(self.disableville)
        self.activateint.clicked.connect(self.disableint)
        self.activateprof.clicked.connect(self.disablepro)
        self.activateyear.clicked.connect(self.disableyr)

        #------------------------------------------------------

        #----------------adding / removing cell in tables
        self.btnaddpro.clicked.connect(self.add)
        self.btnremovepro.clicked.connect(self.rem)

        self.btnaddville.clicked.connect(lambda : self.Add(self.villetable))
        self.btnremoveville.clicked.connect(lambda : self.Rem(self.villetable))

        self.btnaddinter.clicked.connect(lambda : self.Add(self.interventiontable))
        self.btnremoveinter.clicked.connect(lambda : self.Rem(self.interventiontable))

        self.btnaddyear.clicked.connect(lambda : self.Add(self.anneetable))
        self.btnremoveyear.clicked.connect(lambda : self.Rem(self.anneetable))

        #--------------------------------------------------------

    def add(self):
        if self.professiontable.isEnabled():
            row = self.professiontable.rowCount()
            self.professiontable.setRowCount(row)
            self.professiontable.insertRow(row)
            self.professiontable.setItem(row,0,QTableWidgetItem(str(row)))
            self.professiontable.selectRow(row)

    def rem(self):
        if self.professiontable.isEnabled():
            row = self.professiontable.selectionModel().selectedRows()
            for i in row:
                self.professiontable.removeRow(i.row())
            try:
                self.professiontable.selectRow(self.professiontable.rowCount()-1)
            except:
                pass
    
    def Add(self,widget):
        if widget.isEnabled():
            row = widget.rowCount()
            widget.setRowCount(row)
            widget.insertRow(row)
            widget.setItem(row,0,QTableWidgetItem(str('')))
            widget.selectRow(row)

    def Rem(self,widget):
        if widget.isEnabled():
            row = widget.selectionModel().selectedRows()
            for i in row:
                widget.removeRow(i.row())
            try:
                widget.selectRow(widget.rowCount()-1)
            except:
                pass


    def disable(self):
        if self._enable == False and self._disable == True:
            self.frame_9.setEnabled(True)
            self._enable = True
            self._disable = False
        else:
            self.frame_9.setEnabled(False)
            self._enable = False
            self._disable = True

    def disableville(self):
        if self._enableville == False and self._disableville == True:
            self.villetable.setEnabled(True)
            self._enableville = True
            self._disableville = False
        else:
            self.villetable.setEnabled(False)
            self._enableville = False
            self._disableville = True

    def disablepro(self):
        if self._enablepro == False and self._disablepro == True:
            self.professiontable.setEnabled(True)
            self._enablepro = True
            self._disablepro = False
        else:
            self.professiontable.setEnabled(False)
            self._enablepro = False
            self._disablepro = True 

    def disableint(self):
        if self._enableint == False and self._disableint == True:
            self.interventiontable.setEnabled(True)
            self._enableint = True
            self._disableint = False
        else:
            self.interventiontable.setEnabled(False)
            self._enableint = False
            self._disableint = True

    def trymysqlconnection(self):
        host = self.host.text()
        user = self.username.text()
        database = self.database.text()
        port = self.port.text()
        password = self.password.text()

        try:
            con = mc.connect(host=host,user=user,passwd=password,database=database,port=port)
            if con:
                QMessageBox.information(self,"Connection Successfull",f"Connected successfully to database {database} on {host} ",QMessageBox.Ok)
        except Exception as e:
            QMessageBox.warning(self,"Error",f"{e}",QMessageBox.Ok)

    def reset(self):
        reply = QMessageBox.information(self,"Confirmer","Voulez vous vraiment reninialiser les parametre ?",QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            NvJson().createJsonFileConfig(reset=True)
            self.fillTables()

    def SaveConfigurations(self):
        ville = []
        prof = []
        inter = []
        year = []

        for i in range(self.villetable.rowCount()):
            val = self.villetable.item(i,0).text()
            if val:
                ville.append(val)

        for i in range(self.professiontable.rowCount()):
            val = self.professiontable.item(i,0).text()
            if val:
                prof.append(val)

        for i in range(self.interventiontable.rowCount()):
            val = self.interventiontable.item(i,0).text()
            if val:
                inter.append(val)
        
        for i in range(self.anneetable.rowCount()):
            val = self.anneetable.item(i,0).text()
            try:
                val = int(val)
                year.append(val)
            except:
                pass

        ville.sort()
        prof.sort()
        inter.sort()
        year.sort()

        #clearing the json file

        data = NvJson().readJson()

        #clearing ville
        data['VILLE'].clear()

        #clearing profession
        data['PROFESSION'].clear()

        #clearing intervention
        data['INTERVENTION'].clear()

        #clearing years
        data['LASTYEAR'].clear()

        
        
        if self.databasetype == 'sqlite':
            print(self.sqlitedatabasepath.text())
            if sqlite3.connect(self.sqlitedatabasepath.text()):
                QMessageBox.information(self,"Connextion Successfull",f"Connected successfully to database {QFileInfo(self.sqlitedatabasepath.text()).fileName()}")
                NvJson().setDbType('sqlite')
                data['PATHTOSQLITEDATABASE'] = os.path.dirname(self.sqlitedatabasepath.text())+"/"
                data['SQLITEDATABASENAME'] = QFileInfo(self.sqlitedatabasepath.text()).fileName()
            else:
                QMessageBox.information(self,"SQLite Connection Error","Le Chemin entrez est incorrect")
                path = '.DB/'
                databasename = 'Hospital.db'
                data['PATHTOSQLITEDATABASE'] = path
                data['SQLITEDATABASENAME'] = databasename
        
        elif self.databasetype == 'mysql':
            host = self.host.text()
            user = self.username.text()
            database = self.database.text()
            port = self.port.text()
            password = self.password.text()

            try:
                con = mc.connect(host=host,user=user,passwd=password,database=database,port=port)
                if con:
                    QMessageBox.information(self,"Connection Successfull",f"Connected successfully to database {database} on {host} ",QMessageBox.Ok)
                    data['MySQl']['database'] = database if database != '' else 'Hospital'
                    data['MySQl']['host'] = host
                    data['MySQl']['password'] = password
                    data['MySQl']['port'] = port
                    data['MySQl']['username'] = user
            except Exception as e:
                    QMessageBox.warning(self,"Error",f"{e}",QMessageBox.Ok)
        
        NvJson().writeJson(data)

        #Saving the data collected from the tables

        #print(ville)
        #print(prof)
        #print(inter)
        #print(year)

        if self.databasetype == 'mysql':
            NvJson().setDbType('mysql')
        elif self.databasetype == 'sqlite':
            NvJson().setDbType('sqlite')

        for i in ville:
            NvJson().addTown(i)

        for i in prof:
            NvJson().addProff(i)

        for i in inter:
            NvJson().addIntervention(i)

        for i in year:
            NvJson().addYear(i)

        self.fillTables()

        

    def disableyr(self):
        if self._enableyr == False and self._disableyr == True:
            self.anneetable.setEnabled(True)
            self._enableyr = True
            self._disableyr = False
        else:
            self.anneetable.setEnabled(False)
            self._enableyr = False
            self._disableyr = True           
    
    def loadMySQlDbConfig(self):
        data = NvJson().readJson()['MySQl']
        if NvJson().getDbType() == 'mysql':
            self.host.setText(data['host'])
            self.username.setText(data['username'])
            self.database.setText(data['database'])
            self.port.setText(str(data['port']))
            self.password.setText(data['password'])


    def fillTables(self):
        self.loadProfession()
        self.loadYear()
        self.loadInt()
        self.loadTown()
        self.loadMySQlDbConfig()

        databasetype = NvJson().getDbType()
        if databasetype == 'mysql':
            self.radiomysql.setChecked(True)
            self.radiosqlite.setChecked(False)
            self.tab_2.setEnabled(False)
            self.tab.setEnabled(True)
            self.databasetype = 'mysql'
        else:
            self.radiosqlite.setChecked(True)
            self.radiomysql.setChecked(False)
            self.tab.setEnabled(False)
            self.tab_2.setEnabled(True)
            self.databasetype = 'sqlite'
            path = NvJson().getSqlDbPath() + NvJson().getSqlDbName()
            self.sqlitedatabasepath.setText(path)

    def onSelected(self):
        radio = self.sender()

        if radio.isChecked():
            if radio.text() == 'Mysql':
                self.tab_2.setEnabled(False)
                self.tab.setEnabled(True)
                self.databasetype = 'mysql'
            else:
                self.tab.setEnabled(False)
                self.tab_2.setEnabled(True)
                self.databasetype = 'sqlite'
    
    def loadProfession(self):
        
        profession = NvJson().getProff()
        profession.sort()
        self.professiontable.setRowCount(len(profession))
        for i,pro in enumerate(profession):
            self.professiontable.setItem(i,0,QTableWidgetItem(pro))
        
    def loadYear(self):

        years = NvJson().getLastYear()
        years.sort()

        self.anneetable.setRowCount(len(years))
        for i,yr in enumerate(years):
            self.anneetable.setItem(i,0,QTableWidgetItem(str(yr)))

    def loadInt(self):
        inter = NvJson().getIntervention()
        inter.sort()

        self.interventiontable.setRowCount(len(inter))

        for i,it in enumerate(inter):
            self.interventiontable.setItem(i,0,QTableWidgetItem(it))

    def loadTown(self):
        ville = NvJson().getTown()
        ville.sort()

        self.villetable.setRowCount(len(ville))

        for i,vl in enumerate(ville):
            self.villetable.setItem(i,0,QTableWidgetItem(vl))

class Apropos(QWidget,Ui_Apropos):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)

        self.setupUi(self)
        f = QFile(HTML_PATH+'about.html')
        if not f.open(QFile.ReadOnly):
            print("Can't Open")
        data = f.readAll()
        text = data.data().decode('utf8')
        file_url = QUrl(HTML_PATH+'about.html') #if f[0] == ':' else QUrl.fromLocalFile(f)
        options = QUrl.FormattingOptions(QUrl.RemoveFilename)
        self.textEdit.document().setBaseUrl(file_url.adjusted(options))
        self.textEdit.setStyleSheet("QTextEdit{"
                                    "background:transparent;"
                                    "color:black;"
                                    "padding: 12px 12px;"
                                    "/*margin:30px auto;*/"
                                    "border:0.1px solid rgb(171,171,171);"
                                    "border-radius:1px;}"
                                    )
        self.textEdit.setHtml(text)
        self.textEdit.setReadOnly(True)

class Parametre(QWidget,Ui_Parametre):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)

        self.setupUi(self)

        self.btnAide.clicked.connect(self.animate)
        self.slidedown.clicked.connect(self.animate)

    def animate(self):
        height = self.slidehelp.height()

        if height == 0:
            newHeight = 700
        else:
            newHeight = 0

        self.anim1 = QPropertyAnimation(self.slidehelp,b"maximumHeight")
        self.anim1.setStartValue(height)
        self.anim1.setEndValue(newHeight)
        self.anim1.setDuration(1000)
        self.anim1.setEasingCurve(QEasingCurve.OutSine)
        self.anim1.start()

class Carnets(QWidget,Ui_Carnet):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)

        self.setupUi(self)
        self.tables.currentTextChanged.connect(self.fill)
        self.tableWidget.itemSelectionChanged.connect(self.get)

        self.fillTables()

    def fillTables(self):
        db = DataBase()

        tables = db.getTables()
        self.tables.addItems(tables)
        self.fill(self.tables.currentText())

    def fill(self,txt):
        db = DataBase()

        row,data = db.getPatients(txt)

        col = db.getColumn(txt)
        #print('col ',col)

        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(len(col))

        self.tableWidget.setHorizontalHeaderLabels(col)

        for i,dt in enumerate(data):
            for j,dy in enumerate(dt):
                self.tableWidget.setItem(i,j,QTableWidgetItem(str(dy)))


    def get(self):

        itm = self.tableWidget.selectedItems()
        #print([i.text() for i in itm])
        try:
            self.textEdit.setText(itm[0].text())
            self.textEdit.selectAll()
        except:
            pass

STYLES = ["Standard", "Bullet List (Disc)", "Bullet List (Circle)",
          "Bullet List (Square)", "Task List (Unchecked)",
          "Task List (Checked)", "Ordered List (Decimal)",
          "Ordered List (Alpha lower)", "Ordered List (Alpha upper)",
          "Ordered List (Roman lower)", "Ordered List (Roman upper)",
          "Heading 1", "Heading 2", "Heading 3", "Heading 4", "Heading 5",
          "Heading 6"]

class Recapitulatif(QWidget,Ui_Recapitulatif):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.setupUi(self)
        self.modifier.clicked.connect(self.animateright)
        self.SEX = None
        self.AGE = None
        self.PROF = None
        self.TOWN = None
        self.INTER = None
        self.CAO = None
        self.fillTables()

        self.btncut.clicked.connect(self.textEdit.cut)
        self.btncut.setShortcut(QKeySequence.Cut)
        self.btncopy.clicked.connect(self.textEdit.copy)
        self.btncopy.setShortcut(QKeySequence.Copy)
        self.btnpaste.clicked.connect(self.textEdit.paste)
        self.btnpaste.setShortcut(QKeySequence.Paste)

        doc = self.textEdit.document()
        doc.modificationChanged.connect(self.setWindowModified)
        doc.undoAvailable.connect(self.btnundo.setEnabled)
        doc.redoAvailable.connect(self.btnredo.setEnabled)
        self.setWindowModified(doc.isModified())

        self.btnredo.setEnabled(doc.isRedoAvailable())
        self.btnundo.setEnabled(doc.isUndoRedoEnabled())
        self.btnundo.setShortcut(QKeySequence.Undo)
        self.btnundo.clicked.connect(self.textEdit.undo)
        self.btnredo.setShortcut(QKeySequence.Redo)
        self.btnredo.clicked.connect(self.textEdit.redo)

        self.btnbold.toggled.connect(self.text_bold)
        bold = QFont()
        bold.setBold(True)
        self.btnbold.setFont(bold)

        self.btnitalic.toggled.connect(self.text_italic)

        self.btnunderline.toggled.connect(self.text_underline)
        
        self.btnleft.setShortcut("Ctrl+L")
        self.btncenter.setShortcut("Ctrl+E")
        self.btnright.setShortcut("Ctrl+R")
        self.btnjustify.setShortcut("Ctrl+J")

        self.fontComboBox.textActivated.connect(self.text_family)

        standard_sizes = QFontDatabase.standardSizes()
        for size in standard_sizes:
            self.fontSize.addItem(str(size))
        index = standard_sizes.index(QApplication.font().pointSize())
        self.fontSize.setCurrentIndex(index)

        self.fontSize.textActivated.connect(self.text_size)

        self.combostyle.addItems(STYLES)
        self.combostyle.activated.connect(self.text_style)

        self.btncolor.clicked.connect(self.text_color)
        self.btnundercolor.clicked.connect(self.underline_color)

        self.btnleft.toggled.connect(self.text_align_left)
        self.btnright.toggled.connect(self.text_align_right)
        self.btncenter.toggled.connect(self.text_align_center)
        self.btnjustify.toggled.connect(self.text_align_justify)

        self.textEdit.currentCharFormatChanged.connect(self.current_char_format_changed)

        self.font_changed(self.textEdit.font())
        self.color_change(self.textEdit.textColor())

        self.btnindent.clicked.connect(self.indent)
        self.btnunindent.clicked.connect(self.unindent)

        self.alignment_changed(self.textEdit.alignment())

        self.textEdit.setEnabled(True)

        self.textEdit.setTabStopDistance(8.0)
        self.toolBarLayout.deleteLater()

        self.toolBarWidget.deleteLater()

    def fillTables(self):
        prof = NvJson().getProff()
        town = NvJson().getTown()
        inter = NvJson().getIntervention()
        inter.remove('RAS')

        self.professiontable.setRowCount(0)
        self.professiontable.setRowCount(len(prof))
        self.professiontable.setVerticalHeaderLabels(prof)

        self.residencetable.setRowCount(0)
        self.residencetable.setRowCount(len(town))
        self.residencetable.setVerticalHeaderLabels(town)

        self.interventiontable.setRowCount(0)
        self.interventiontable.setRowCount(len(inter))
        self.interventiontable.setVerticalHeaderLabels(inter)

        self.fillValues()

    def animateright(self):
        width = self.slideframe.width()

        if width == 0:
            newWidth = 700
        else:
            newWidth = 0
        
        self.anim1 = QPropertyAnimation(self.slideframe,b"maximumWidth")
        self.anim1.setStartValue(width)
        self.anim1.setEndValue(newWidth)
        self.anim1.setDuration(1000)
        self.anim1.setEasingCurve(QEasingCurve.OutSine)
        self.anim1.start()
        self.setReca()

    def fillValues(self):
        db = DataBase()

        sex =  []

        sex.append(db.count("SEX","SEX = 'M' "))
        sex.append(db.count("SEX","SEX = 'F' "))

        for i,s in enumerate(sex):
            self.sextable.setItem(0,i,QTableWidgetItem(str(s)))

        age = []

        age.append(db.count("AGE","AGE >= 0 AND AGE <= 5"))
        age.append(db.count("AGE","AGE >= 6 AND AGE <= 17"))
        age.append(db.count("AGE","AGE >= 18 AND AGE <= 35"))
        age.append(db.count("AGE","AGE >= 36 AND AGE <= 45"))
        age.append(db.count("AGE","AGE >= 45"))

        for i,a in enumerate(age):
            self.agetable.setItem(0,i,QTableWidgetItem(str(a)))

        prof = []
        _prof = NvJson().getProff()

        for i in _prof:
            prof.append(db.count("PROFESSION","PROFESSION = '{}'".format(i)))
        for i,p in enumerate(prof):
            self.professiontable.setItem(0,i,QTableWidgetItem(str(p)))

        town = []
        _town = NvJson().getTown()

        for i in _town:
            town.append(db.count("TOWN","TOWN = '{}'".format(i)))

        for i,t in enumerate(town):
            self.residencetable.setItem(0,i,QTableWidgetItem(str(t)))

        inter = []
        _inter = NvJson().getIntervention()

        for i in _inter:
            if databaseType() == 'sqlite':
                one,two,three = db.count("INT1","INT1 = '{}'".format(i)),db.count("INT2","INT2 = '{}'".format(i)),db.count("INT3","INT3 = '{}'".format(i))
                inter.append(one+two+three)
            else:
                one,two,three = db.count("INTER1","INTER1 = '{}'".format(i)),db.count("INTER2","INTER2 = '{}'".format(i)),db.count("INTER3","INTER3 = '{}'".format(i))
                inter.append(one+two+three)

        for i,it in enumerate(inter):
            self.interventiontable.setItem(0,i,QTableWidgetItem(str(it)))

        cao = []
        _cao = ['C','A','O','Autre']

        for i in _cao:
            cao.append(db.sum('{}'.format(i)))

        for i,c in enumerate(cao):
            self.caotable.setItem(0,i,QTableWidgetItem(str(c)))

        self.SEX = sex
        self.AGE = age
        self.PROF = prof
        self.TOWN = town
        self.INTER = inter
        self.CAO = cao

    def setReca(self):
        
        style = '''
                p{
                    white-space:pre-wrap;
                }
                h4{
                    text-align:center;
                    font-family:'ubuntu condense';
                }
                h5{
                    text-align:center;
                    font-family:'arial';
                    font-weight:100px;

                }
                h6{
                    font-size:13pt;
                    font-weight:300px;

                }
                .div1{
                    #border:1 solid rgba(0,255,0,50);
                    text-align:center;
                    padding : 0 40 0 40;
                    margin 100px auto;
                }
                .nv{
                    margin:0px 90px;
                    padding :1 1;
                }
                section{
                    padding:10 0;
                    text-align:left;
                    margin:100px auto;
                }
                .one{
                    text-align:left;
                }
                th,td{
                    text-align: left;
                }   
                '''
        dt = "{} : VOLET DENTAIRE.".format(NvDate().getDay())

        r = '''
            <strong style="font-size:12pt;">RESUME</strong>
            
            '''

        t = '''
            <strong style="font-size:12pt;text-decoration:underline;">INTRODUCTION</strong>
            
            '''

        q = ['0-5','6-17','18-35','36-45','+45']

        k = '''
            '''

        p = '''
            '''

        v = '''
            '''

        it = '''
             '''

        cao = '''
              '''

        for i in list(zip(q,self.AGE)):
            k += '''
                    <tr>
                        <td>
                            {}
                        </td>

                        <td>
                            {}
                        </td>
                    </tr>
                 '''.format(i[0],i[1])

        for i in list(zip(NvJson().getProff(),self.PROF)):
            p += '''
                    <tr>
                        <td>
                            {}
                        </td>

                        <td>
                            {}
                        </td>
                    </tr>
                 '''.format(i[0],i[1])

        l = '''
                <strong>N.B:</strong>
                <ul>
                    <li>
                        Fonctionnaire: personnels de santé, enseignant(e)s.
                    </li>
                    <li>
                        Autres: chef traditionnel, couturières, coiffeuses.
                    </li>
                </ul>
            '''

        for i in list(zip(NvJson().getTown(),self.TOWN)):
            v += '''
                    <tr>
                        <td>
                            {}
                        </td>

                        <td>
                            {}
                        </td>
                    </tr>
                 '''.format(i[0],i[1])
        te = NvJson().getIntervention()
        te.remove('RAS')
        for i in list(zip(te,self.INTER)):
            it += '''
                    <tr>
                        <td>
                            {}
                        </td>

                        <td>
                            {}
                        </td>
                    </tr>
                 '''.format(i[0],i[1])

        for i in list(zip(['C','A','O','Autre'],self.CAO)):
            cao += '''
                    <tr>
                        <td>
                            {}
                        </td>

                        <td>
                            {}
                        </td>
                    </tr>
                 '''.format(i[0],i[1])

        html = f'''
                <!DOCTYPE html>
                <html>
                <head>
                <meta name = "qrichtext" content="0">
                <meta http-equiv="Content-Type" content="text/html" charset="UTF-8">

                <title>
                    Récapitulatif
                </title>
                <style>
                    {style}
                </style>
                </head>
                <body>
                    <section class="nv">
                        <div class = "div1">
                            <br/>
                            <h4>RAPPORT DE LA CAMPAGNE DE SANTE DE TONGA</h4>
                            <h5>{dt}</h5>
                        </div>
                        <div align = "left">
                            <!-- <p style="font-size:12pt;font-weight:300;font-family:'ubuntu Mono';">RESUME</p> -->
                            <p align="left" style="padding:0 0;display:inline block;width:90%;">
                                {r}
                                {t}
                            </p>
                        </div>
                        <div>
                            <ol>
                                <li>
                                    <span style="font-weight: bold;text-align: left;">Données démographiques</span>
                                    <table border="1" width="90%" cellspacing="0" cellpadding="1">
                                        <tr style="padding:0px 0px 5px 0px">
                                            <th align="left" style="font-size:13pt;font-weight:400">
                                                SEXE
                                            </th>
                                            <th align="left" style="font-size:13pt;font-weight:400">
                                                Masculin
                                            </th>
                                            <th align="left" style="font-size:13pt;font-weight:400">
                                                Féminin
                                            </th>
                                        </tr>
                                        <tr>
                                            <td>
                                                EFFECTIF
                                            </td>
                                            <td>

                                                {self.SEX[0]}
                                            </td>
                                            <td>
                                                {self.SEX[1]}
                                            </td>
                                        </tr>
                                    </table>
                                    <br/>
                                </li>
                                <li>
                                    <span style="font-weight: bold;text-align: left;">Age</span>
                                    <table border="1" width="90%" cellspacing="0" cellpadding="1">
                                        <tr>
                                            <th align="left" style="font-size:13pt;font-weight:400">
                                                TRANCHE D’AGE (ANNEES)
                                            </th>
                                            <th align="left" style="font-size:13pt;font-weight:400">
                                                EFFECTIF
                                            </th>
                                        </tr>
                                        {k}
                                    </table>
                                    <br/>
                                </li>
                                <li>
                                    <span style="font-weight: bold;text-align: left;">Activité professionnelle</span>
                                    <table border="1" width="90%" cellspacing="0" cellpadding="1">
                                        <tr>
                                            <th align="left" style="font-size:13pt;font-weight:400">
                                                PROFESSION
                                            </th>
                                            <th align="left" style="font-size:13pt;font-weight:400">
                                                EFFECTIF
                                            </th>
                                        </tr>
                                        {p}
                                    </table>
                                    <br/>
                                        <div>
                                            {l}
                                        </div>
                                    <br/>
                                </li>
                                <li>
                                    <span style="font-weight: bold;text-align: left;">Lieu de résidence</span>
                                    <table border="1" width="90%" cellspacing="0" cellpadding="1">
                                        <tr>
                                            <th align="left" style="font-size:13pt;font-weight:400">
                                                LIEU DE RESIDENCE
                                            </th>
                                            <th align="left" style="font-size:13pt;font-weight:400">
                                                EFFECTIF
                                            </th>
                                        </tr>
                                        {v}
                                    </table>
                                    <br/>
                                </li>
                                <li>
                                    <span style="font-weight: bold;text-align: left;">Mode d’information sur la campagne</span>
                                    <table border="1" width="90%" cellspacing="0" cellpadding="1">
                                        <tr>
                                            <th align="left" style="font-size:13pt;font-weight:400">
                                                NATURE DE L’ACTE
                                            </th>
                                            <th align="left" style="font-size:13pt;font-weight:400">
                                                EFFECTIF (No PATIENTS)
                                            </th>
                                        </tr>
                                        {it}
                                    </table>
                                    <br/>
                                </li>
                                <li>
                                    <span style="font-weight: bold;text-align: left;">INDICE CAO</span>
                                    <table border="1" width="90%" cellspacing="0" cellpadding="1">
                                        {cao}
                                    </table>
                                    <br/>
                                </li>
                            </ol>
                        </div>


                    </section>
                </body>
                </html>
               '''
        self.textEdit.setHtml(html)

    @Slot()
    def text_bold(self):
        fmt = QTextCharFormat()
        weight = QFont.Bold if self.btnbold.isChecked() else QFont.Normal
        fmt.setFontWeight(weight)
        self.merge_format_on_word_of_selection(fmt)

    @Slot()
    def text_italic(self):
        fmt = QTextCharFormat()
        fmt.setFontItalic(self.btnitalic.isChecked())
        self.merge_format_on_word_of_selection(fmt)
    
    @Slot()
    def text_underline(self):
        fmt = QTextCharFormat()
        fmt.setFontUnderline(self.btnunderline.isChecked())
        self.merge_format_on_word_of_selection(fmt)

    @Slot(str)
    def text_family(self,f):
        fmt = QTextCharFormat()
        fmt.setFontFamilies({f})
        self.merge_format_on_word_of_selection(fmt)

    @Slot(str)
    def text_size(self,p):
        point_size = float(p)
        if point_size > 0:
            fmt = QTextCharFormat()
            fmt.setFontPointSize(point_size)
            self.merge_format_on_word_of_selection(fmt)
    
    @Slot(int)
    def text_style(self,styleIndex):
        cursor = self.textEdit.textCursor()
        style = QTextListFormat.ListStyleUndefined
        marker = QTextBlockFormat.MarkerType.NoMarker

        if styleIndex == 1:
            style = QTextListFormat.ListDisc
        elif styleIndex == 2:
            style = QTextListFormat.ListCircle
        elif styleIndex == 3:
            style = QTextListFormat.ListSquare
        elif styleIndex == 4:
            if cursor.currentList():
                style = cursor.currentList().format().style()
            else:
                style = QTextListFormat.ListDisc
            marker = QTextBlockFormat.MarkerType.Unchecked
        elif styleIndex == 5:
            if cursor.currentList():
                style = cursor.currentList().format().style()
            else:
                style = QTextListFormat.ListDisc
            marker = QTextBlockFormat.MarkerType.Checked
        elif styleIndex == 6:
            style = QTextListFormat.ListDecimal
        elif styleIndex == 7:
            style = QTextListFormat.ListLowerAlpha
        elif styleIndex == 8:
            style = QTextListFormat.ListUpperAlpha
        elif styleIndex == 9:
            style = QTextListFormat.ListLowerRoman
        elif styleIndex == 10:
            style = QTextListFormat.ListUpperRoman

        cursor.beginEditBlock()

        block_fmt = cursor.blockFormat()

        if style == QTextListFormat.ListStyleUndefined:
            block_fmt.setObjectIndex(-1)
            # H1 to H6, or Standard
            heading_level = styleIndex - 11 + 1 if styleIndex >= 11 else 0
            block_fmt.setHeadingLevel(heading_level)
            cursor.setBlockFormat(block_fmt)

            # H1 to H6: +3 to -2
            size_adjustment = 4 - heading_level if heading_level != 0 else 0
            fmt = QTextCharFormat()
            fmt.setFontWeight(QFont.Bold if heading_level else QFont.Normal)
            fmt.setProperty(QTextFormat.FontSizeAdjustment, size_adjustment)
            cursor.select(QTextCursor.LineUnderCursor)
            cursor.mergeCharFormat(fmt)
            self.textEdit.mergeCurrentCharFormat(fmt)
        else:
            block_fmt.setMarker(marker)
            cursor.setBlockFormat(block_fmt)
            list_fmt = QTextListFormat()
            if cursor.currentList():
                list_fmt = cursor.currentList().format()
            else:
                list_fmt.setIndent(block_fmt.indent() + 1)
                block_fmt.setIndent(0)
                cursor.setBlockFormat(block_fmt)
            list_fmt.setStyle(style)
            cursor.createList(list_fmt)
        cursor.endEditBlock()
    
    @Slot()
    def text_color(self):
        col = QColorDialog.getColor(self.textEdit.textColor(),self)
        if not col.isValid():
            return
        fmt = QTextCharFormat()
        fmt.setForeground(col)
        self.merge_format_on_word_of_selection(fmt)
        self.color_change(col)

    @Slot()
    def underline_color(self):
        col = QColorDialog().getColor(Qt.black,self)
        if not col.isValid():
            return
        
        fmt = QTextCharFormat()
        fmt.setUnderlineColor(col)
        self.merge_format_on_word_of_selection(fmt)
        self.color_change(col)

    @Slot()
    def text_align_left(self):
        self.textEdit.setAlignment(Qt.AlignLeft | Qt.AlignAbsolute)

    @Slot()
    def text_align_center(self):
        self.textEdit.setAlignment(Qt.AlignHCenter)

    @Slot()
    def text_align_right(self):
        self.textEdit.setAlignment(Qt.AlignRight | Qt.AlignAbsolute)

    @Slot()
    def text_align_justify(self):
        self.textEdit.setAlignment(Qt.AlignJustify)
    
    @Slot(QTextCharFormat)
    def current_char_format_changed(self,format):
        self.font_changed(format.font())
        self.color_change(format.foreground().color())

    @Slot()
    def indent(self):
        self.modify_indentation(1)
    
    @Slot()
    def unindent(self):
        self.modify_indentation(-1)

    @Slot()
    def cursor_position_changed(self):
        self.alignment_changed(self.textEdit.alignment())
        list = self.textEdit.textCursor().currentList()
        if list:
            style = list.format().style()
            if style == QTextListFormat.ListDisc:
                self.combostyle.setCurrentIndex(1)
            elif style == QTextListFormat.ListCircle:
                self.combostyle.setCurrentIndex(2)
            elif style == QTextListFormat.ListSquare:
                self.combostyle.setCurrentIndex(3)
            elif style == QTextListFormat.ListDecimal:
                self.combostyle.setCurrentIndex(6)
            elif style == QTextListFormat.ListLowerAlpha:
                self.combostyle.setCurrentIndex(7)
            elif style == QTextListFormat.ListUpperAlpha:
                self.combostyle.setCurrentIndex(8)
            elif style == QTextListFormat.ListLowerRoman:
                self.combostyle.setCurrentIndex(9)
            elif style == QTextListFormat.ListUpperRoman:
                self.combostyle.setCurrentIndex(10)
            else:
                self.combostyle.setCurrentIndex(-1)
            marker = self.textEdit.textCursor().block().blockFormat().marker()
            #if marker == QTextBlockFormat.MarkerType.NoMarker:
            #    self._action_toggle_check_state.setChecked(False)
            #elif marker == QTextBlockFormat.MarkerType.Unchecked:
            #    self.combostyle.setCurrentIndex(4)
            #    self._action_toggle_check_state.setChecked(False)
            #elif marker == QTextBlockFormat.MarkerType.Checked:
            #    self.combostyle.setCurrentIndex(5)
            #    self._action_toggle_check_state.setChecked(True)
        else:
            heading_level = self.textEdit.textCursor().blockFormat().headingLevel()
            new_level = heading_level + 10 if heading_level != 0 else 0
            self.combostyle.setCurrentIndex(new_level)

    def alignment_changed(self,a):
        if a & Qt.AlignLeft:
            self.btnleft.setChecked(True)
            self.btncenter.setChecked(False)
            self.btnright.setChecked(False)
            self.btnjustify.setChecked(False)
        elif a & Qt.AlignHCenter:
            self.btnleft.setChecked(False)
            self.btncenter.setChecked(True)
            self.btnright.setChecked(False)
            self.btnjustify.setChecked(False)
        elif a & Qt.AlignRight:
            self.btnleft.setChecked()
            self.btncenter.setChecked(False)
            self.btnright.setChecked(True)
            self.btnjustify.setChecked(False)
        elif a & Qt.AlignJustify:
            self.btnleft.setChecked(False)
            self.btncenter.setChecked(False)
            self.btnjustify.setChecked(True)
            self.btnright.setChecked(False)

    def modify_indentation(self,amount):
        cursor = self.textEdit.textCursor()
        cursor.beginEditBlock()
        if cursor.currentList():
            list_fmt = cursor.currentList().format()
            above = QTextCursor(cursor)
            above.movePosition(QTextCursor.Up)
            if (above.currentList() and list_fmt.indent() + amount == above.currentList().format().indent()):
                above.currentList().add(cursor.block())
            
            else:
                list_fmt.setIndent(list_fmt.indent() + amount)
                cursor.createList(list_fmt)
        else:
            block_fmt = cursor.blockFormat()
            block_fmt.setIndent(block_fmt.indent() + amount)
            cursor.setBlockFormat(block_fmt)
        cursor.endEditBlock()
                
    def font_changed(self,f):
        index = self.fontComboBox.findText(QFontInfo(f).family())
        self.fontComboBox.setCurrentIndex(index)
        index = self.fontSize.findText(str(f.pointSize()))
        self.fontSize.setCurrentIndex(index)
        self.btnbold.setChecked(f.bold())
        self.btnitalic.setChecked(f.italic())
        self.btnunderline.setChecked(f.underline())

    def color_change(self,c):
        p = QPixmap(10,10)
        p.fill(c)
        self.btncolor.setIcon(p)    

    def merge_format_on_word_of_selection(self,format):
        cursor = self.textEdit.textCursor()
        if not cursor.hasSelection():
            cursor.select(QTextCursor.WordUnderCursor)

        cursor.mergeCharFormat(format)
        self.textEdit.mergeCurrentCharFormat(format)

class Modify(QWidget,Ui_Modify):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self._id = None
        self._sex = None
        self.setupUi(self)
        self.populate()
        self.hey()
        self.tohide.hide()
        self.tableWidget.setFocus()
        self.tableWidget.itemSelectionChanged.connect(self.get)
        self.lineEdit.returnPressed.connect(self.search)
        self.pushButton.clicked.connect(self.search)
        self.btnsupprimer.clicked.connect(self.delete)
        self.btnmodifier.clicked.connect(self.modif)
        self.male.toggled.connect(self.setSex)
        self.female.toggled.connect(self.setSex)

    def setSex(self):
        s = self.sender()

        if s.isChecked():
            self._sex = s.text()

    def animmodify(self,msg):
        height = self.slideframe.height()
        if height == 0:
            newHeight = 50
        else:
            newHeight = 0
        self.msg.setStyleSheet("color:green")
        self.msg.setText(msg)
        
        self.yanim = QPropertyAnimation(self.slideframe,b"maximumHeight")
        self.yanim.setStartValue(height)
        self.yanim.setEndValue(newHeight)
        self.yanim.setDuration(250)
        self.yanim.setEasingCurve(QEasingCurve.InOutSine)
        self.yanim.start()

        self.timer = QTimer()
        self.timer.start(10)
        self.timer.timeout.connect(lambda:self.kk(msg))

    def kk(self,msg):
        global count
        #print('count = ',count)

        if count == 200:
            self.animmodify(msg)
            count = 0
            self.timer.stop()
            del self.timer

        count += 1

    def modif(self):
        #print(self._id,self._sex)
        if self._id and self._sex:
            rep = QMessageBox.information(self,"Confirmer",f"Voulez vous vraiment modifier le patient {self.nom.text()} {self.prenom.text()}",QMessageBox.Yes | QMessageBox.No)
            if rep == QMessageBox.No:
                return
            ncin = self.ncin.text()
            nom = self.nom.text()
            pre = self.prenom.text()
            age = self.age.text()
            res = self.quartier.currentText()
            pro = self.profession.currentText()

            self.animmodify("Patient {} {} has been modify successfully".format(nom,pre))
            db = DataBase()
            db.updatePatient(self._id,ncin,nom,pre,int(age),self._sex,res,pro)
            self.populate()
            #self.animmodify("Patient {} {} has been modify successfully".format(nom,pre))
         
    def delete(self):
        if self._id != None:
            rep = QMessageBox.information(self,"Confirmer",f"Voulez vous vraiment supprimer le patient {self.nom.text()} {self.prenom.text()}",QMessageBox.Yes | QMessageBox.No)
            if rep == QMessageBox.No:
                return
            db = DataBase()
            db.removePatient(self._id)

            self.ncin.setText('')
            self.nom.setText('')
            self.prenom.setText('')
            self.age.setText('')
            self._sex = None
            self._id = None
            self.tohide.setChecked(True)
            self.quartier.clear()
            self.profession.clear()
            self.hey()
            self.populate()
    
    def hey(self):
        twn = NvJson().getTown()
        prf = NvJson().getProff()

        self.quartier.addItems(twn)
        self.profession.addItems(prf)

    def get(self):
        data = self.tableWidget.selectedItems()
        dt = [x.text() for x in data]
        try:
            self._id = int(dt[0])
            #print(self._id)
            self.ncin.setText(dt[1])
            self.nom.setText(dt[2])
            self.prenom.setText(dt[3])
            self.age.setText(dt[4])
            if dt[5] == 'M':
                self.male.setChecked(True)
                self._sex = 'M'
            else:
                self._sex = 'F'
                self.female.setChecked(True)
            self.quartier.setCurrentText(dt[6])
            self.profession.setCurrentText(dt[7])
        except:pass

    def search(self):
        c = self.lineEdit.text()
        db = DataBase()
        data = db.getPatientM(c)
        #self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setRowCount(len(data))

        for i,dt in enumerate(data):
            for j,dy in enumerate(dt):
                self.tableWidget.setItem(i,j,QTableWidgetItem(str(dy)))
        
        self.tableWidget.selectRow(0)
        self.tableWidget.setFocus()

    def populate(self):

        header = self.tableWidget.horizontalHeader()
        
        db = DataBase()
        data = db.getSaved()
        row = data[0]
        col = data[1]
        pat = data[2]
        self.tableWidget.setColumnCount(len(col))
        self.tableWidget.setRowCount(row)
        self.tableWidget.setHorizontalHeaderLabels(col)

        for i in range(len(col)):
            header.setSectionResizeMode(i,QHeaderView.Stretch)

        for i,dt in enumerate(pat):
            for j,dy in enumerate(dt):
                self.tableWidget.setItem(i,j,QTableWidgetItem(str(dy)))

class PatientSaved(QWidget,Ui_PatientSaved):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)

        self.setupUi(self)
        self.populate()

    def populate(self):

        header = self.tableWidget.horizontalHeader()
        
        db = DataBase()
        data = db.getSaved()
        row = data[0]
        col = data[1]
        pat = data[2]
        self.tableWidget.setColumnCount(len(col))
        self.tableWidget.setRowCount(row)
        self.tableWidget.setHorizontalHeaderLabels(col)

        for i in range(len(col)):
            header.setSectionResizeMode(i,QHeaderView.Stretch)

        for i,dt in enumerate(pat):
            for j,dy in enumerate(dt):
                self.tableWidget.setItem(i,j,QTableWidgetItem(str(dy)))

class Consultation(QWidget,Ui_Consulation):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)

        self.setupUi(self)
        self.seeconsultation.setShortcut("Ctrl+K")
        self.age.setValidator(QIntValidator())
        self.loadComboValues()
        self.animation1 = False
        self.animation2 = False
        self.animation3 = False
        self.toh.hide()

        self._sex = None

        self.seeconsultation.clicked.connect(self.animateright)
        self.btnslide.clicked.connect(self.animateup)
        self.btnslide.setShortcut("shift+s")
        self.searchbox.returnPressed.connect(self.animatesearch)
        self.searchpatient.clicked.connect(self.animatesearch)
        self.clearinputs.clicked.connect(self.clear)
        self.saveconsultation.clicked.connect(self.save)
        self.saveconsultation.setShortcut("Ctrl+S")
        self.printconsultation.clicked.connect(self.printB)
        self.printconsultation.setShortcut("Ctrl+p")
        self.btngeneratecarnet.clicked.connect(self.display)
        self.btngeneratecarnet.setShortcut("Ctrl+a")

        #self.profession.setCurrentText("Fonctionaire")

        
        self.tableWidget.itemSelectionChanged.connect(self.get)
        self.Male.toggled.connect(self.chooseSex)
        self.Female.toggled.connect(self.chooseSex)
    
    def chooseSex(self):
        s = self.sender()
        if s.isChecked():
            self._sex = s.text()

    def printB(self):
        printer = QPrinter(QPrinter.HighResolution)
        #dlg = QPrintDialog(printer,self)
        prev = QPrintPreviewDialog(printer,self)
        prev.paintRequested.connect(self.consulation.print_)
        prev.exec()

    def animatesearch(self):
        width = self.searchframeslide.width()

        db = DataBase() 
        data = db.getPatient(self.searchbox.text())

        tb = db.getColumn(db.currentTable)

        if self.searchbox.text() == '':
            self.patienterrornotfound.setText("Svp entrez un mot mot ou nom pour chercher un patient")
            self.patienterrornotfound.setStyleSheet("color:green")
            #tb = ['ID','NCIN','NAME','SURNAME','AGE','SEX']
            self.tableWidget.setColumnCount(len(tb))
            self.tableWidget.setRowCount(len(data))

            self.tableWidget.setHorizontalHeaderLabels(tb)

            

            #print(data)

            for i,ele in enumerate(data):
                for j,c in enumerate(ele):
                    self.tableWidget.setItem(i,j,QTableWidgetItem(str(c)))
            self.tableWidget.setFocus()

        elif data == []:
            self.patienterrornotfound.setText("Aucun patient trouver avec {}".format(self.searchbox.text()))
            self.patienterrornotfound.setStyleSheet("color:red")
            #tb = ['ID','NCIN','NAME','SURNAME','AGE','SEX']
            
            self.tableWidget.setColumnCount(len(tb))
            self.tableWidget.setRowCount(len(data))

            self.tableWidget.setHorizontalHeaderLabels(tb)

            

            #print(data)

            for i,ele in enumerate(data):
                for j,c in enumerate(ele):
                    self.tableWidget.setItem(i,j,QTableWidgetItem(str(c)))

        elif data != []:
            self.patienterrornotfound.setText("Les patient trouves avec '{}' sont : ".format(self.searchbox.text()))
            self.patienterrornotfound.setStyleSheet("color:green")

            #tb = ['ID','NCIN','NAME','SURNAME','AGE','SEX']
            
            self.tableWidget.setColumnCount(len(tb))
            self.tableWidget.setRowCount(len(data))

            self.tableWidget.setHorizontalHeaderLabels(tb)

            

            #print(data)

            for i,ele in enumerate(data):
                for j,c in enumerate(ele):
                    self.tableWidget.setItem(i,j,QTableWidgetItem(str(c)))

        

        if width == 0:
            newWidth = 700
            self.animation1 = True
            if self.animation2:
                self.animateright()
        else:
            newWidth = 0
            self.animation1 = False

        self.animx = QPropertyAnimation(self.searchframeslide,b"maximumWidth")
        self.animx.setStartValue(width)
        self.animx.setEndValue(newWidth)
        self.animx.setDuration(1000)
        self.animx.setEasingCurve(QEasingCurve.OutInQuart)
        self.animx.start()


    def animateup(self):
        height = self.slideframe.height()

        if height == 0:
            newHeight = 50
            self.searchbox.setFocus()
            self.animation3 = True
            self.btnslide.setIcon(QIcon(":/images/images/arrow-up.svg"))
        else:
            self.animation3 = False
            newHeight =0
            
            self.btnslide.setIcon(QIcon(":/images/images/arrow-down.svg"))

        self.anim1  = QPropertyAnimation(self.slideframe,b"maximumHeight")
        self.anim1.setStartValue(height)
        self.anim1.setEndValue(newHeight)
        self.anim1.setDuration(1000)
        self.anim1.setEasingCurve(QEasingCurve.InOutBounce)
        self.anim1.start()

        if (newHeight == 0) and (self.animation1 == True):
            self.animatesearch()

    def animateright(self):
        width = self.slideFrameConsult.width()

        if width == 0:
            newWidth = 700
            self.animation2 = True
            if self.animation1:
                self.animatesearch()
        else:
            newWidth = 0
            self.animation2 = False

        self.anim = QPropertyAnimation(self.slideFrameConsult,b"maximumWidth")
        self.anim.setStartValue(width)
        self.anim.setEndValue(newWidth)
        self.anim.setDuration(1000)
        self.anim.setEasingCurve(QEasingCurve.InSine)
        self.anim.start()


        if self.nom.text() == '':
            pass
        else:
            self.NvBooklet()
            #self.consulation.setHtml(self.html)
            self.consulation.setReadOnly(True)
    
    def save(self):
        #print(1)
        if self.ncin.text():
            nci = self.ncin.text()
        if self.nom.text():
            nom = self.nom.text()
            self.NvBooklet()
            self.display()
        else:
            self.__error__("Le nom est obligatoire!")
            return
        if self.prenom.text():
            pre = self.prenom.text()
        if self.age.text():
            age = self.age.text()
            self.NvBooklet()
            self.display()
        else:
            self.__error__("L'age est obligatoire!")
            return
        if self._sex:
            sex = self._sex
        else:
            self.__error__("Le sex est obligatoire!")
            return
        if self.town.currentText():
            town = self.town.currentText()
            self.NvBooklet()
            self.display()
        else:
            self.__error__("La ville est obligatoire!")
            return
        if self.prof.currentText():
            pro = self.prof.currentText()
            self.NvBooklet()
            self.display()
        else:
            self.__error__("La profession est obligatoire!")
            return
        if self.lastyear.currentText():
            lst = self.lastyear.currentText()
        else:
            self.__error__("La dernnier annéee de participation est obligatoire!")
            return
        c = self.indiceC.value()
    
        a = self.indiceA.value()
    
        o = self.indiceO.value()
    
        aut = self.indeiceAutre.value()
        #print('currentText2',self.intervention2.currentText(),self.intervention2.currentText()=='')
        if self.intervention1.currentText()!='':   
            int1 = self.intervention1.currentText()
        else:
            self.intervention1.setCurrentText("RAS")
            self.NvBooklet()
            self.display()

        if self.intervention2.currentText()!='':
            int2 = self.intervention2.currentText()
        else:
            self.intervention2.setCurrentText("RAS")
            self.NvBooklet()
            self.display()
        
        if self.intervention3.currentText()!='':
            int3 = self.intervention3.currentText()
        else:
            self.intervention3.setCurrentText("RAS")
            self.NvBooklet()
            self.display()

        if self.diagnostic.toPlainText():
            diag = self.diagnostic.toPlainText()
        else:
            self.__error__("Le diagnostic est obligatoire!")
            return
        self.NvBooklet()
        self.display()
        if self.consulation.toHtml():
            with open('C:\\Users\\Ivan Tom\\Desktop\\g.html','w') as f:
                f.write(self.consulation.toHtml())
            car = self.consulation.toHtml()

        db = DataBase()
        #db.cur2.execute("ALTER TABLE DENTIST_2021 DROP COLUMN CONSULTATION ")
        #db.con2.commit()
        if db.addConsultation(nci,nom,pre,age,sex,town,pro,lst,c,a,o,aut,int1,int2,int3,diag,car) == True:
            QMessageBox.information(self,"Success","Patient {} {} successfully saved".format(nom,pre),QMessageBox.Ok)

    def __error__(self,msg):
        QMessageBox.information(self,"Error",msg,QMessageBox.Ok)

    def NvBooklet(self):
        nci = self.ncin.text()
        nom = self.nom.text()
        pre = self.prenom.text()
        age = self.age.text()
        sex = self._sex
        town = self.town.currentText()
        pro = self.prof.currentText()
        lst = self.lastyear.currentText()
        c = self.indiceC.value()
        a = self.indiceA.value()
        o = self.indiceO.value()
        aut = self.indeiceAutre.value()
        int1 = self.intervention1.currentText()
        int2 = self.intervention2.currentText()
        int3 = self.intervention3.currentText()
        diag = self.diagnostic.toPlainText()

        title = "<strong>Campaign bucco-dentaire de Tonga</strong>".center(60," ")
        style = '''
                header{
                    text-align:center;
                    padding:60 20 20 20;
                }
                strong{
                    font-size:16px;
                    font-weight:600px;
                }
                p{
                    text-align:center;
                    padding 0 20 0 20;
                }
                #p{
                    text-align:left;
                }
                section{
                    padding:40px 0;
                    text-align:left;
                    margin:100px auto;
                }
                hr{
                    color:red;
                }
                .one{
                    text-align:left;
                    padding : 0 40 0 40;
                    margin 100px auto;
                }
                span,h2{
                    white-space:pre-wrap;
                }
                .nv{
                    margin:0px 90px;
                    padding :1 1;
                }
                b,h6{
                    font-weight: 100;
                }
                h4{
                    font-size:12px;
                }
                '''
        dttm = f'''
                Tonga le {NvDate().getWknm()} {NvDate().getDay()} à {NvDate().getTime()}'''
        ln = "<hr/>"
        self.html='''<!DOCTYPE html>
                <html>
                <head>
                <meta name="viewport" content="width=device-width,initial-scale=1.0">
                <meta name="qrichtext" content="0">
                <meta http-equiv="Content-Type" content="text/html" charset="UTF-8">
                <title>
                    Naspitoo Consultation 
                </title>
                <style type="text/css">
                {0}
                </style>
                </head>
                <body>
                <section class="nv">
                    <header>
                        <br>
                        <h2 style="font-size:12pt;">{1}</h2>
                        <h6 style="font-size:9pt;">{2}</h6>
                        {3}
                    </header>
                    <section>
                        <div class="one">
                            <b>Ncin</b> : {4}<br/>
                            <b>Nom</b> : {5}<br/>
                            <b>Prénom</b> : {6}<br/>
                            <b>Age</b> :{7} <span align="rigth">        <b>Sex</b> :{8} </span><br>
                            <b>Lieux de résidence</b> : {9} <span align="rigth">  <b>Profession</b> : {10} </span><br/>
                            <b>Année de la dernier participation</b> : {11}
                        </div>
                        <p style="margin:0 0;"><strong><h4>INDICE CAO</h4></strong></p>
                        {3}
                        <div class="one">
                            <b>C</b> : {12} <br/>
                            <b>A</b> : {13} <br/>
                            <b>O</b> : {14} <br/>
                            <b>Autre</b> : {15}
                        </div>
                        <p id="p"><strong><h4>INTERVENTION</h4></strong></p>
                        {3}
                        <div class="one">
                            <b>1:</b> {16} <br/>
                            <b>2:</b> {17} <br/>
                            <b>3:</b> {18}
                        </div>
                        <p><strong><h4>DIAGNOSTIC</h4></strong></p>
                        {3}
                        <div>
                            <p style="text-align:left">
                                {19}
                            </p>
                        </div>
                    </section>
                </section>
                </body>
                </html>
               '''.format(style,title,dttm,ln,nci,nom,pre,age,sex,town,pro,lst,c,a,o,aut,int1,int2,int3,diag)
        with open("C:\\Users\\Ivan Tom\\Desktop\\g.html",'w') as f:
            f.write(self.html)

    def display(self):
        self.NvBooklet()
        self.consulation.setHtml(self.html)

    def load(self,widget,val):
        widget.addItems(val)

    def loadComboValues(self):
        profession = NvJson().getProff()
        ville = NvJson().getTown()
        yrs = NvJson().getLastYear()

        inter = NvJson().getIntervention()
        #for i in ville:
        self.town.addItems(ville)

        #for i in profession:
        self.prof.addItems(profession)

        #for i in yrs:
        self.lastyear.addItems([str(i) for i in yrs])

        self.load(self.intervention1,inter)
        self.load(self.intervention2,inter)
        self.load(self.intervention3,inter)

    def get(self):
        val = self.tableWidget.selectedItems()
        dat = [x.text() for x in val]

        if dat == []:return
        #print(dat)
        self.ncin.setText(dat[1])
        self.nom.setText(dat[2])
        self.prenom.setText(dat[3])
        self.age.setText(dat[4])
        if dat[5] == 'M':
            self.Male.setChecked(True)
            #self.Female.setChecked(False)
            self._sex = 'M'
        else:
            self._sex = 'F'
            self.Female.setChecked(True)
            #self.Male.setChecked(False)

        self.town.setCurrentText(dat[6])
        self.prof.setCurrentText(dat[7])
        self.lastyear.setCurrentText(str(dat[8]))
        self.indiceC.setValue(int(dat[9]))
        self.indiceA.setValue(int(dat[10]))
        self.indiceO.setValue(int(dat[11]))
        self.indeiceAutre.setValue(int(dat[12]))
        self.intervention1.setCurrentText(str(dat[13]))
        self.intervention2.setCurrentText(str(dat[14]))
        self.intervention3.setCurrentText(str(dat[15]))
        self.diagnostic.setText(dat[16])

    def clear(self):
        self.ncin.setText('')
        self.nom.setText('')
        self.prenom.setText('')
        self.age.setText('')
        self.toh.setChecked(True)
        self._sex = None
        self.town.clear()
        self.prof.clear()
        self.lastyear.clear()
        self.indiceC.setValue(0)
        self.indiceA.setValue(0)
        self.indiceO.setValue(0)
        self.indeiceAutre.setValue(0)
        self.intervention1.clear()
        self.intervention2.clear()
        self.intervention3.clear()
        self.diagnostic.setText('')
        self.loadComboValues()
        self.Male.setCheckable(True)
        self.Female.setCheckable(True)
        self.consulation.setText('')

class Register(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()

        self.nci = None
        self.name = None
        self.surname = None
        self.age = None
        self.sex = None
        self.town = None
        self.prof = None

        self.setupUi(self)
        self.toh.hide()
        self.savepatient.clicked.connect(self.ifError)
        #self.savepatient.clicked.connect(self.d)
        self.errFrame.setStyleSheet("QFrame{border :1px solid rgb(171, 171, 171);border-radius:10px;}")
        self.populateEntries()
        self.patientage.setValidator(QIntValidator(0,120,self.patientage))
        self.btndelete.clicked.connect(self.clrs)

        self.sexfemal.toggled.connect(self.onSex)
        self.sexmale.toggled.connect(self.onSex)

    def animate(self,msg="",ok=False):
        height = self.errFrame.height()
        if height == 0:
            newHeight = 200
        else:
            newHeight = 0
        if not ok:
            self.erromsg.setStyleSheet("QLabel{color:red;font-size:20px;border:none;}")
        else:
            self.erromsg.setStyleSheet("QLabel{color:green;font-size:20px;border:none;}")
        self.erromsg.setText(msg)
        self.anim1 = QPropertyAnimation(self.errFrame,b"maximumHeight")
        self.anim1.setStartValue(height)
        self.anim1.setEndValue(newHeight)
        self.anim1.setDuration(1000)
        self.anim1.setEasingCurve(QEasingCurve.InOutSine)
        self.anim1.start()
        
        self.timer = QTimer()
        self.timer.start(10)
        self.timer.timeout.connect(lambda:self.clr(msg,ok))
        
    def clr(self,msg,ok):
        global count
        if count == 200:
            self.animate(msg,ok)
            self.timer.stop()
            count = 0
            del self.timer
        #print('running' ,count)
        count += 1

    def ifError(self):
        self.nci = self.ncin.text()
        if self.patientname.text() == '':
            self.animate("User Name Require !")
            self.patientname.setFocus()
            return
        else:
            self.name = self.patientname.text()

        self.surname = self.patientsurname.text()

        if self.patientage.text() == '':
            self.animate("Patient Age Require !")
            self.patientage.setFocus()
            return
        else:
            self.age = self.patientage.text()

        if self.sex == None:
            self.animate("Patient Sex Require !")
            return    
        if self.comboBox.currentText() == '':
            self.animate("Patient Town Require !")
            self.comboBox.setFocus()
            return
        else:
            self.town = self.comboBox.currentText()
        
        if self.comboBox_2.currentText() == '':
            self.comboBox_2.setFocus()
            self.animate("Patient Profession Require !")
            return
        else:
            self.comboBox_2.currentText()

        
        db = DataBase()
        ok = db.addPatient(self.nci,self.name,self.surname,self.age,self.sex,self.comboBox.currentText(),self.comboBox_2.currentText())
        
        if ok == True:
            self.animate("Patient Saved successfully !",True)
        else:
            self.animate("Error Patient Could Not Saved successfully !")

    def clrs(self):
        self.comboBox.clear()
        self.comboBox_2.clear()
        self.ncin.setText('')
        self.patientname.setText('')
        self.patientsurname.setText('')
        self.patientage.setText('')
        self.sex = None
        self.toh.setChecked(True)
        self.sexmale.setChecked(False)
        self.sexfemal.setChecked(False)
        self.populateEntries()

    def populateEntries(self):
        profession = NvJson().getProff()
        ville = NvJson().getTown()
        for i in ville:
            self.comboBox.addItem(i)

        for i in profession:
            self.comboBox_2.addItem(i)

    def onSex(self):
        sex = self.sender()

        if sex.isChecked():
            self.sex = sex.text()
            #print("SEX = ",self.sex)
            #print("PROFESSION",self.comboBox.currentText())

class Main(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        #self.setWindowFlags(Qt.FramelessWindowHint)
        #self.setAttribute(Qt.WA_TranslucentBackground)
        self.globalWidget = QVBoxLayout()
        self.mainframe.setLayout(self.globalWidget)
        self.globalWidget.setContentsMargins(0,0,0,0)

        self.menubtn.clicked.connect(self.showMenu)
        self.quitbtn.clicked.connect(self.close)
        self.btnsavepatient.clicked.connect(self.toRegisterPatien)
        self.btnconsult.clicked.connect(self.toConsult)
        self.btnsavedpatient.clicked.connect(self.toPatienSaved)
        self.btnmodify.clicked.connect(self.toModify)
        self.btnrecap.clicked.connect(self.toRecapitulatif)
        self.btnseebooklet.clicked.connect(self.toBooklet)
        self.btnparametre.clicked.connect(self.toParametre)
        self.btncredit.clicked.connect(self.toApropos)
        #self.settingsbtn.clicked.connect(lambda : print(self.mainframe.height()))
        self.settingsbtn.clicked.connect(self.toConfig)
        self.menubtn.animateClick()
        self.setWindowTitle("Naspitoo")
    
    def clear(self):
        while self.globalWidget.count():
            child = self.globalWidget.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            else:
                self.clear()

    def animateWidget(self,widget):
        widget.setMaximumHeight(0)
        self.anim = QPropertyAnimation(widget,b"maximumHeight")
        height = 0
        newheight = self.mainframe.height()

        self.anim.setStartValue(height)
        self.anim.setEndValue(newheight)
        self.anim.setDuration(800)
        self.anim.setEasingCurve(QEasingCurve.InSine)
        self.anim.start()

    def toConfig(self):
        self.clear()
        self.config = NsConfig()
        self.globalWidget.addWidget(self.config)
        self.mainframe.setLayout(self.globalWidget)
        self.config.setMaximumHeight(0)
        height = 0
        newheight = self.mainframe.height() - 2
        self.anim1 = QPropertyAnimation(self.config,b"maximumHeight")
        self.anim1.setStartValue(height)
        self.anim1.setEndValue(newheight)
        self.anim1.setDuration(2000)
        self.anim1.setEasingCurve(QEasingCurve.InOutSine)
        self.anim1.start()

    def toApropos(self):
        self.clear()
        self.apropos = Apropos()
        self.globalWidget.addWidget(self.apropos)
        self.mainframe.setLayout(self.globalWidget)
        self.animateWidget(self.apropos)
        self.showMenu()

    def toParametre(self):
        self.clear()
        self.para = Parametre()
        self.globalWidget.addWidget(self.para)
        self.mainframe.setLayout(self.globalWidget)
        self.animateWidget(self.para)
        self.showMenu()

    def toBooklet(self):
        self.clear()
        self.car = Carnets()
        self.globalWidget.addWidget(self.car)
        self.mainframe.setLayout(self.globalWidget)
        self.animateWidget(self.car)
        self.showMenu()

    def toConsult(self):
        self.clear()
        self.consult = Consultation()
        self.globalWidget.addWidget(self.consult)
        self.mainframe.setLayout(self.globalWidget)
        self.animateWidget(self.consult)
        self.showMenu()

    def toModify(self):
        self.clear()
        self.mod = Modify()
        self.globalWidget.addWidget(self.mod)
        self.mainframe.setLayout(self.globalWidget)
        self.animateWidget(self.mod)
        self.showMenu()

    def toRecapitulatif(self):
        self.clear()
        self.rec = Recapitulatif()
        self.globalWidget.addWidget(self.rec)
        self.mainframe.setLayout(self.globalWidget)
        self.animateWidget(self.rec)
        self.showMenu()

    def toRegisterPatien(self):
        self.clear()
        self.reg = Register()
        self.globalWidget.addWidget(self.reg)
        self.mainframe.setLayout(self.globalWidget)
        self.animateWidget(self.reg)
        self.showMenu()

    def toPatienSaved(self):
        self.clear()
        self.pat = PatientSaved()
        self.globalWidget.addWidget(self.pat)
        self.mainframe.setLayout(self.globalWidget)
        self.animateWidget(self.pat)
        self.showMenu()

    def closeEvent(self, event):
        reply = QMessageBox.information(self,"Confirm Quit","Voulez vous vraiment quitter l'application ?",QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def showMenu(self):
        css = """
                QToolButton{
                /*border-radius:17px;*/
                image: url(:/images/images/format-justify-fill.svg);
                border:1px solid rgb(171, 171, 171);
                }

                QToolButton::pressed{
                    background: rgba(171, 171, 171,60);
                }

                /*QToolButton::hover{
                    background : rgba(171, 171, 171,100);
                }
                */
            """
        css1 = """
                QToolButton{
                /*border-radius:17px;*/
                image: url(:/images/images/arrow-left.svg);
                border:1px solid rgb(171, 171, 171);
                }

                QToolButton::pressed{
                    background: rgba(171, 171, 171,60);
                }

                /*QToolButton::hover{
                    background : rgba(171, 171, 171,100);
                }
                */
                
            """
        width = self.slideframe.width()

        if width == 0:
            newWidth = 300
            self.menubtn.setStyleSheet(css1)
        else:
            newWidth =0
            self.menubtn.setStyleSheet(css)

        self.anim1 = QPropertyAnimation(self.slideframe,b"maximumWidth")
        self.anim1.setStartValue(width)
        self.anim1.setEndValue(newWidth)
        self.anim1.setDuration(1000)
        #self.anim1.setEasingCurve(QEasingCurve.OutBounce)
        self.anim1.setEasingCurve(QEasingCurve.OutSine)
        #self.anim1.setEasingCurve(QEasingCurve.InOutSine)
        self.anim1.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Main()
    if sys.platform == 'win32':
        win.setStyleSheet('''
                QFrame{
                    border:1px solid rgb(171,171,171)
                }
                QLabel{
                    border:none;
                }
            ''')
    win.showMaximized()
    sys.exit(app.exec())
    