import psutil
import mysql.connector

cpu_porcent = psutil.cpu_count()

infobd = mysql.connector.connect( 
 host = 'localhost',
 user = 'urubu100',
 password = 'urubu100',
 database = 'bilheteUnico'
)

chamarbd = infobd.cursor()

chamarbd.execute("Select * from Registro")

myresult = chamarbd.fetchall() 




for x in myresult:
    print (x[0])
