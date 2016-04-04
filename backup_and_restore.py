import os
import time
import datetime
from subprocess import Popen, PIPE


DATABASE = raw_input("""
which database you want to access ?
1.Mysql
2.Mongodb
"""
)

OPERATION = raw_input("""
What operation you want to do ?
1.Backup
2.Restore
"""
)

if DATABASE == '1':
	DATABASE_HOST = raw_input("Enter your host name :")
	USER_NAME = raw_input("Enter your mysql username :")
	USER_PASSWORD = raw_input("Enter your mysql password :")
	DATABASE_NAME = raw_input("Enter your mysql database name :")

	if OPERATION == '1':
		BACKUP_PATH = raw_input("Enter your backuppath :")
	    
	    	DATETIME = time.strftime('%m-%d-%Y-%H:%M:%S')

		CURRENTDAYPATH = BACKUP_PATH + DATETIME

		# Checking if backup folder already exists or not. If not exists will create it.
		print "creating backup folder"
		if not os.path.exists(CURRENTDAYPATH):
		    os.makedirs(CURRENTDAYPATH)

		# Code for checking if you want to take single database backup or assinged multiple backups in DB_NAME.
		print "checking for databases names file."
		if os.path.exists(DATABASE_NAME):
		    file1 = open(DATABASE_NAME)
		    multi = 1
		    print "Databases file found..."
		    print "Starting backup of all dbs listed in file " + DATABASE_NAME
		else:
		    print "Databases file not found..."
		    print "Starting backup of database " + DATABASE_NAME
		    multi = 0

		# Starting actual database backup process.
		if multi:
		   print "came here at multi is that okay for you "
		   in_file = open(DATABASE_NAME,"r")
		   flength = len(in_file.readlines())
		   in_file.close()
		   p = 1
		   dbfile = open(DATABASE_NAME,"r")

		   while p <= flength:

		       db = dbfile.readline()   # reading database name from file
		       db = db[:-1]         # deletes extra line
		       dumpcommand = "mysqldump -u " + USER_NAME + " -p" + USER_PASSWORD + " " + db + " > " + CURRENTDAYPATH + "/" + db + ".sql"
		       os.system(dumpcommand)
		       p = p + 1
		   dbfile.close()
		else:
		   db = DATABASE_NAME
		   dumpcommand = "mysqldump -u " + USER_NAME + " -p" + USER_PASSWORD + " " + db + " > " + CURRENTDAYPATH + "/" + db + ".sql"
		   os.system(dumpcommand)

		print "Backup script completed"
		print "Your backups has been created in '" + CURRENTDAYPATH + "' directory"

	elif OPERATION == '2':
		DB_BACKUP_FILE = raw_input("Enter your database backup path and filename(without extension) :")
		print "Data restoring is started ....."	
		restorecommand = "mysql -u " + USER_NAME + " -p"+USER_PASSWORD + " " + DATABASE_NAME + " " + " < " + DB_BACKUP_FILE + ".sql"
		os.system(restorecommand)
		print "Data Restoring done"
else:
	MONGO_HOST = raw_input("Enter your mongo host :")
	MONGO_PORT = raw_input("Enter Your mongodb port :")
	MONGO_DATABASE_NAME = raw_input("Enter Your Database Name :")

	if OPERATION == '1':
		MONGODUMP_PATH = raw_input("Enter the path for dumping :")
		DATETIME = time.strftime('%m-%d-%Y-%H:%M:%S')
		CURRENTDAYPATH = MONGODUMP_PATH + DATETIME

		if not os.path.exists(CURRENTDAYPATH):
			os.makedirs(CURRENTDAYPATH)

		print "checking for databases names file."
		if os.path.exists(MONGO_DATABASE_NAME):
		    file1 = open(MONGO_DATABASE_NAME)
		    multi = 1
		    print "Databases file found..."
		    print "Starting backup of all dbs listed in file " + MONGO_DATABASE_NAME
		else:
		    print "Databases file not found..."
		    print "Starting backup of database " + MONGO_DATABASE_NAME
		    multi = 0
		    
		if multi:
		   in_file = open(MONGO_DATABASE_NAME,"r")
		   flength = len(in_file.readlines())
		   in_file.close()
		   p = 1
		   dbfile = open(MONGO_DATABASE_NAME,"r")

		   while p <= flength:
		       dumpcommand = "mongodump --db " + " " + MONGO_DATABASE_NAME + " " + "--out" + " " +  CURRENTDAYPATH 
		       print dumpcommand
		       os.system(dumpcommand)
		       p = p + 1
		   dbfile.close()
		else:
		   db = MONGO_DATABASE_NAME
		   dumpcommand = "mongodump --db" + " " + MONGO_DATABASE_NAME + " " + "--out" + " " +  CURRENTDAYPATH 
		   os.system(dumpcommand)

		print "Backup script completed"
		print "Your backups has been created in '" + CURRENTDAYPATH + "' directory"    	
		print 'data backup'

	elif OPERATION == '2':
		BACKUP_PATH_FILE = raw_input("Enter your bson backup file path: ") 
		restorecommand = "mongorestore --db" + " " + MONGO_DATABASE_NAME + " " + BACKUP_PATH_FILE 
		#print restorecommand
		os.system(restorecommand)
		print 'data restoring done'


