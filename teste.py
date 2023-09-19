import psutil
import mysql.connector
import pandas as pd 

# cpu_porcent = psutil.cpu_count()

infobd = mysql.connector.connect( 
 host = 'localhost',
 user = 'urubu100',
 password = 'urubu100',
 database = 'bilheteUnico'
)

chamarbd = infobd.cursor()

chamarbd.execute("Select * from Registro")

myresult = chamarbd.fetchall() 

print (myresult[0][3])

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2], 
#   'airplanes': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2],
#   'humans': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# myvar = pd.DataFrame(mydataset)

# print(myvar)

