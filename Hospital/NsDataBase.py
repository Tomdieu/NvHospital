import sqlite3
import mysql.connector as mc

import json,time


def getSqlPath():
	with open('Naspitoo-Conifg/config.json') as f:
		data = json.load(f)

	if data['mysql'] == True:
		return data['MySQl']
	else:
		return data['PATHTOSQLITEDATABASE']+data['SQLITEDATABASENAME']

def databaseType():
	with open('Naspitoo-Conifg/config.json') as f:
		data = json.load(f)

	if data['mysql'] == True:
		return 'mysql'

	else:
		return 'sqlite'

def getYear():
	return time.strftime("%Y")

def setMySQlDbName(name):
	with open('Naspitoo-Conifg/config.json') as f:
		data = json.load(f)

	if name:
		data['MySQl']['database'] = name

	with open('Naspitoo-Conifg/config.json','w') as f:
		json.dump(data,f,indent=4,sort_keys=True,ensure_ascii=False) 

class DataBase:

	def __init__(self):

		self.host = ''
		self.user = ''
		self.database = ''
		self.port = 3306
		self.database = ''

		if databaseType() == 'sqlite':
			self.database = getSqlPath()
			self.con1 = sqlite3.connect(self.database)
			self.cur1 = self.con1.cursor()
		else:
			self.config = getSqlPath()

			if self.config['database'] != '':
				try:
					self.con2 = mc.connect(host=self.config['host'],
								   user = self.config['username'],
								   passwd = self.config['password'],
								   database = self.config['database'],
								   port = self.config['port']
								   )
					self.cur2 = self.con2.cursor()
				except:
					self.con2 = mc.connect(host=self.config['host'],
								   user = self.config['username'],
								   passwd = self.config['password'],
								   port = self.config['port']
								   )
					self.cur2 = self.con2.cursor()

			else:
				self.con2 = mc.connect(host=self.config['host'],
								   user = self.config['username'],
								   passwd = self.config['password'],
								   port = self.config['port']
								   )
				self.cur2 = self.con2.cursor()

		self.currentTable = "DENTIST_"+getYear()

		self.tables = {
					'DENTIST_SQLITE':"""
                                    CREATE TABLE IF NOT EXISTS DENTIST_{}
                                    (
                                        ID integer PRIMARY KEY,
                                        NCIN varchar(30) DEFAULT '',
                                        NAME varchar(30) NOT NULL,
                                        SURNAME varchar(30) DEFAULT '',
                                        AGE INT NOT NULL,
                                        SEX varchar(1) NOT NULL,
                                        TOWN varchar(30) NOT NULL,
                                        PROFESSION varchar(30) NOT NULL,
                                        LASTYEAR INTEGER(4) NOT NULL DEFAULT {},
                                        C INT DEFAULT 0,
                                        A INT DEFAULT 0,
                                        O INT DEFAULT 0,
                                        Autre INT DEFAULT 0,
                                        INT1 varchar(30) NOT NULL DEFAULT 'RAS',
                                        INT2 varchar(30) NOT NULL DEFAULT 'RAS',
                                        INT3 varchar(30) NOT NULL DEFAULT 'RAS',
                                        DIAGNOSTIC varchar(255) DEFAULT 'RAS',
                                        CONSULTATION TEXT DEFAULT ''
                                    )
                                  """.format(getYear(),getYear()),
                    'DENTIST_MYSQL':"""
                                    CREATE TABLE IF NOT EXISTS DENTIST_{}
                                    (
                                        ID INT PRIMARY KEY AUTO_INCREMENT,
                                        NCIN varchar(30) DEFAULT '',
                                        NAME varchar(30) NOT NULL,
                                        SURNAME varchar(30) DEFAULT '',
                                        AGE INT NOT NULL,
                                        SEX varchar(1) NOT NULL,
                                        TOWN varchar(30) NOT NULL,
                                        PROFESSION varchar(30) NOT NULL,
                                        LASTYEAR INT(4) NOT NULL DEFAULT {},
                                        C INT DEFAULT 0,
                                        A INT DEFAULT 0,
                                        O INT DEFAULT 0,
                                        Autre INT DEFAULT 0,
                                        INTER1 varchar(30) DEFAULT 'RAS',
                                        INTER2 varchar(30) DEFAULT 'RAS',
                                        INTER3 varchar(30) DEFAULT 'RAS',
                                        DIAGNOSTIC varchar(255) DEFAULT 'RAS',
                                        CONSULTATION TEXT DEFAULT ''
                                    )
                                  """.format(getYear(),getYear())
                        }

		self.createTables()

		
	def createTables(self):

		if databaseType() == 'sqlite':
			self.cur1.execute(self.tables['DENTIST_SQLITE'])
			self.con1.commit()

		else:
			if self.config['database'] == '':
				sql = 'CREATE DATABASE IF NOT EXISTS Hospital'

				self.cur2.execute(sql)
				self.con2.commit()
				self.con2.close()

				self.con2 = mc.connect(host=self.config['host'],
								   user = self.config['username'],
								   passwd = self.config['password'],
								   database = "Hospital",
								   port = self.config['port']
								   )
				setMySQlDbName("Hospital")
				self.cur2 = self.con2.cursor()
				self.cur2.execute(self.tables['DENTIST_MYSQL'])

				self.con2.commit()
			else:
				self.cur2 = self.con2.cursor()
				self.cur2.execute(self.tables['DENTIST_MYSQL'])

				self.con2.commit()

	def getId(self,name,surname):
		if databaseType() == 'sqlite':
			sql = "SELECT ID,NAME,SURNAME FROM {} WHERE NAME = ? AND SURNAME = ?".format(self.currentTable)
			self.cur1.execute(sql,(name,surname))
			data = self.cur1.fetchall()

			return data[0][0]

		elif databaseType() == 'mysql':
			sql = "SELECT ID,NAME,SURNAME FROM {} WHERE NAME = %s AND SURNAME = %s".format(self.currentTable)
			self.cur2.execute(sql,(name,surname))
			data = self.cur2.fetchall()

			return data[0][0]

	def present(self,name,surname):
		if databaseType() == 'sqlite':
			sql = "SELECT NAME,SURNAME FROM {} WHERE NAME = ? AND SURNAME = ?".format(self.currentTable)
			self.cur1.execute(sql,(name,surname))
			data = self.cur1.fetchall()

			print('data = ',data)
			if data == []:
				return False
			if data[0][0] == name and data[0][1] == surname:
				return True
			return False

		elif databaseType() == 'mysql':
			sql = "SELECT NAME,SURNAME FROM {} WHERE NAME = %s AND SURNAME = %s".format(self.currentTable)
			self.cur2.execute(sql,(name,surname))
			data = self.cur2.fetchall()

			print(data)
			if data == []:
				return False
			if data[0][0] == name and data[0][1] == surname:
				return True
			return False

	def removePatient(self,_id):
		if databaseType() == 'sqlite':
			sql = "DELETE FROM {} WHERE ID = {}".format(self.currentTable,_id)

			self.cur1.execute(sql)

			self.con1.commit() 

		elif databaseType() == 'mysql':
			sql = "DELETE FROM {} WHERE ID = {}".format(self.currentTable,_id)

			self.cur2.execute(sql)

			self.con2.commit()

	def addPatient(self,ncin,name,surname,age,sex,town,profession):
		if databaseType() == 'sqlite':
			if self.present(name,surname):
				return False

			sql = '''INSERT INTO {}(NCIN,NAME,SURNAME,AGE,SEX,TOWN,PROFESSION)
					 VALUES (?,?,?,?,?,?,?)
				  '''.format(self.currentTable)
			self.cur1.execute(sql,(ncin,name,surname,age,sex,town,profession))
			self.con1.commit()

			return True

		elif databaseType() == 'mysql':
			if self.present(name,surname):
				return False

			sql = '''INSERT INTO {}(NCIN,NAME,SURNAME,AGE,SEX,TOWN,PROFESSION)
					 VALUES (%s,%s,%s,%s,%s,%s,%s)
				  '''.format(self.currentTable)
			self.cur2.execute(sql,(ncin,name,surname,age,sex,town,profession))
			self.con2.commit()

			return True

	def updatePatient(self,_id,ncin,name,surname,age,sex,town,profession):
		if databaseType() == 'sqlite':
			sql = '''
				   UPDATE {}
				   SET
				   NCIN = ?,
				   NAME = ?,
				   SURNAME = ?,
				   AGE = ?,
				   SEX = ?,
				   TOWN = ?,
				   PROFESSION = ?
				   WHERE ID = ?
				  '''.format(self.currentTable)
			self.cur1.execute(sql,(ncin,name,surname,age,sex,town,profession,_id))
			self.con1.commit()

		elif databaseType() == 'mysql':
			sql = '''
				   UPDATE {}
				   SET
				   NCIN = %s,
				   NAME = %s,
				   SURNAME = %s,
				   AGE = %s,
				   SEX = %s,
				   TOWN = %s,
				   PROFESSION = %s
				   WHERE ID = %s
				  '''.format(self.currentTable)
			self.cur2.execute(sql,(ncin,name,surname,age,sex,town,profession,_id))
			self.con2.commit()

	def addConsultation(self,ncin,name,surname,age,sex,town,profession,last,c,a,o,aut,int1,int2,int3,diag,cons) -> bool:
		if databaseType() == 'sqlite':
			if self.present(name,surname):
				_id = self.getId(name,surname)

				sql = '''
						UPDATE {}
						SET 
						NCIN = ?,
						NAME = ?,
						SURNAME = ?,
						AGE = ?,
						SEX = ?,
						TOWN = ?,
						PROFESSION = ?,
						LASTYEAR = ?,
						C = ?,
						A = ?,
						O = ?,
						Autre = ?,
						INT1 = ?,
						INT2 = ?,
						INT3 = ?,
						DIAGNOSTIC = ?,
						CONSULTATION = ?

						WHERE ID = ?
					'''.format(self.currentTable)
				self.cur1.execute(sql,(ncin,name,surname,age,sex,town,profession,last,c,a,o,aut,int1,int2,int3,diag,cons,self.getId(name,surname)))
				self.con1.commit()
				return True

			else:
				sql = '''
					  INSERT INTO {}(NCIN,NAME,SURNAME,AGE,SEX,TOWN,PROFESSION,LASTYEAR,C,A,O,Autre,INT1,INT2,INT3,DIAGNOSTIC,CONSULTATION)
					  VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
					  '''
				self.cur1.execute(sql,(ncin,name,surname,age,sex,town,profession,last,c,a,o,aut,int1,int2,int3,diag,cons))
				self.con1.commit()

				return True

		elif databaseType() == 'mysql':
			if self.present(name,surname):
				sql = '''
						UPDATE {}
						SET 
						NCIN = %s,
						NAME = %s,
						SURNAME = %s,
						AGE = %s,
						SEX = %s,
						TOWN = %s,
						PROFESSION = %s,
						LASTYEAR = %s,
						C = %s,
						A = %s,
						O = %s,
						Autre = %s,
						INTER1 = %s,
						INTER2 = %s,
						INTER3 = %s,
						DIAGNOSTIC = %s,
						CONSULTATION = %s

						WHERE ID = %s
					'''.format(self.currentTable)
				self.cur2.execute(sql,(ncin,name,surname,age,sex,town,profession,last,c,a,o,aut,int1,int2,int3,diag,cons,self.getId(name,surname)))
				self.con2.commit()
				return True

			else:
				sql = '''
					  INSERT INTO {}(NCIN,NAME,SURNAME,AGE,SEX,TOWN,PROFESSION,LASTYEAR,C,A,O,Autre,INT1,INT2,INT3,DIAGNOSTIC,CONSULTATION)
					  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
					  '''
				self.cur2.execute(sql,(ncin,name,surname,age,sex,town,profession,last,c,a,o,aut,int1,int2,int3,diag,cons))
				self.con2.commit()
				return True

	def getPatientM(self,x):
		#v = ['ID','NCIN','NAME','SURNAME','AGE','SEX','TOWN','PROFESSION']
		if databaseType() == 'sqlite':
			sql = f"SELECT ID,NCIN,NAME,SURNAME,AGE,SEX,TOWN,PROFESSION FROM {self.currentTable} WHERE NCIN LIKE '%"+x+"%' OR NAME LIKE '%"+x+"%' OR SURNAME LIKE '%"+x+"%' "
			self.cur1.execute(sql)

			data = self.cur1.fetchall()
			return data

		elif databaseType() == 'mysql':
			sql = f"SELECT ID,NCIN,NAME,SURNAME,AGE,SEX,TOWN,PROFESSION FROM {self.currentTable} WHERE NCIN LIKE '%"+x+"%' OR NAME LIKE '%"+x+"%' OR SURNAME LIKE '%"+x+"%'"
			self.cur2.execute(sql)

			data = self.cur2.fetchall()
			return data

	def getSaved(self):
		if databaseType() == 'sqlite':
			tbl = ['ID','NCIN','NAME','SURNAME','AGE','SEX','TOWN','PROFESSION']
			sql = "SELECT ID,NCIN,NAME,SURNAME,AGE,SEX,TOWN,PROFESSION FROM {}".format(self.currentTable)
			self.cur1.execute(sql)
			data = self.cur1.fetchall()

			return len(data),tbl,data


		elif databaseType() == 'mysql':
			tbl = ['ID','NCIN','NAME','SURNAME','AGE','SEX','TOWN','PROFESSION']
			sql = "SELECT ID,NCIN,NAME,SURNAME,AGE,SEX,TOWN,PROFESSION FROM {}".format(self.currentTable)
			self.cur2.execute(sql)
			data = self.cur2.fetchall()

			return len(data),tbl,data
	
	def getPatient(self,x):
		if databaseType() == 'sqlite':
			sql = f"SELECT ID,NCIN,NAME,SURNAME,AGE,SEX,TOWN,PROFESSION,LASTYEAR,C,A,O,Autre,INT1,INT2,INT3,DIAGNOSTIC,CONSULTATION FROM {self.currentTable} WHERE NCIN LIKE '%"+x+"%' OR NAME LIKE '%"+x+"%' OR SURNAME LIKE '%"+x+"%' "
			self.cur1.execute(sql)

			data = self.cur1.fetchall()
			return data

		elif databaseType() == 'mysql':
			sql = f"SELECT ID,NCIN,NAME,SURNAME,AGE,SEX,TOWN,PROFESSION,LASTYEAR,C,A,O,Autre,INTER1,INTER2,INTER3,DIAGNOSTIC,CONSULTATION FROM {self.currentTable} WHERE NCIN LIKE '%"+x+"%' OR NAME LIKE '%"+x+"%' OR SURNAME LIKE '%"+x+"%'"
			self.cur2.execute(sql)

			data = self.cur2.fetchall()
			return data

	def getPatients(self,table):
		if databaseType() == "sqlite":
			sql = 'SELECT * FROM {}'.format(table)
			self.cur1.execute(sql)

			data = self.cur1.fetchall()

			return len(data),data

		elif databaseType() == 'mysql':
			sql = f'SELECT * FROM {table}'
			self.cur2.execute(sql)

			data = self.cur2.fetchall()

			return len(data),data

	def getTables(self):
		if databaseType() == 'sqlite':
			sql = "SELECT name FROM sqlite_master WHERE type='table'"
			self.cur1.execute(sql)

			data = self.cur1.fetchall()
			tab = [x[0] for x in data]
			return tab

		else:
			sql = "SHOW TABLES"
			self.cur2.execute(sql)
			data = self.cur2.fetchall()

			tab = [x[0] for x  in data]
			return tab

	def getColumn(self,table):
		if databaseType() == 'sqlite':
			sql = 'PRAGMA table_info({})'.format(table)
			self.cur1.execute(sql)
			column = self.cur1.fetchall()

			col = [x[1] for x in column]

			return col
		else:
			#sql = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = Database() AND TABLE_NAME = {}".format(table)
			sql = "DESCRIBE {}".format(table)
			self.cur2.execute(sql)
			data = self.cur2.fetchall()

			col = [x[0] for x  in data]

			return col

	def count(self,column,condition=''):
		if databaseType() == 'sqlite':
			if condition == '':
				sql = "SELECT {} FROM {}".format(column,self.currentTable)
				print(sql)
				self.cur1.execute(sql)

				data = self.cur1.fetchall()

				return len(data)
			else:

				sql = "SELECT {} FROM {} WHERE {}".format(column,self.currentTable,condition)
				print(sql)
				self.cur1.execute(sql)
				data = self.cur1.fetchall()

				return len(data)

		elif databaseType() == 'mysql':
			if condition == '':
				sql = "SELECT {} FROM {}".format(column,self.currentTable)
				self.cur2.execute(sql)

				data = self.cur2.fetchall()

				return len(data)
			else:
				sql = "SELECT {} FROM {} WHERE {}".format(column,self.currentTable,condition)
				self.cur2.execute(sql)
				data = self.cur2.fetchall()

				return len(data)
		
	def sum(self,column,condition=''):
		if databaseType() == 'sqlite':
			if condition == '':
				sql = "SELECT {} FROM {}".format(column,self.currentTable)
				self.cur1.execute(sql)

				data = self.cur1.fetchall()

				_x = [x[0] for x in data]

				return sum(_x)

			else:
				sql = "SELECT {} FROM {} WHERE {}".format(column,self.currentTable,condition)
				self.cur1.execute(sql)

				data = self.cur1.fetchall()

				_x = [x[0] for x in data]

				return sum(_x)

		elif databaseType() == 'mysql':
			if condition == '':
				sql = "SELECT {} FROM {}".format(column,self.currentTable)
				self.cur2.execute(sql)

				data = self.cur2.fetchall()

				_x = [x[0] for x in data]

				return sum(_x)

			else:
				sql = "SELECT {} FROM {} WHERE {}".format(column,self.currentTable,condition)
				self.cur2.execute(sql)

				data = self.cur2.fetchall()

				_x = [x[0] for x in data]

				return sum(_x)

if __name__ == '__main__':

	a = DataBase()
	for i in a.getTables():
		print(a.getPatient('to'))
		#print(a.getColumn(i))
	s = ''
	print(a.count("AGE","NAME LIKE '%a%'"))
	print(a.sum("AGE","AGE < 6"))

	a.addPatient('7106','navi','Tom',18,'M','Yaounde','students')

	print(a.getSaved())
