import psutil
from time import sleep
import mysql.connector
from datetime import datetime

infobd = mysql.connector.connect( 
 host = 'localhost',
 user = 'urubu100',
 password = 'urubu100',
 database = 'bilheteUnico'
)



chamarbd = infobd.cursor()
horarioRegistro = datetime.now()

# idServidor = [1]

# email = input("Email: ")
# senha = input("Senha: ")



# print(
#     """
#     Bem-vindo a Grey Cloud Transactions

#     Estes são os seus servidores disponíveis no momento:
    
#     id
#     """
# )


# print(
#     """
#     Deseja Monitorar qual máquina:
#     1 - Primeira Máquina
#     2 - Segunda Máquina
#     3 - Terceira Máquina
#     4 - voltar
#     """
# )




cpu1 = 100
# mem1 = 30
# disco1 = 56

cpu2 = cpu1*1.1 
# mem2 = 30*1.15
# disco2 = 56*0.95


cpu3 = cpu2*1.05
# mem3 = mem2*1.05
# disco3 = disco2*3


registroCpu1 = min(100,cpu1)
registroCpu2 = min(100,cpu2)
registroCpu3 = min(100,cpu3)


chamarbd.execute("INSERT INTO Registro values" + 
                 f"(null,'cpu',{registroCpu1},'{horarioRegistro}',10,1),"  + 
                 f"(null,'cpu',{registroCpu2},'{horarioRegistro}',11,1),"  +
                 f"(null,'cpu',{registroCpu3},'{horarioRegistro}',12,1)")

infobd.commit()

# cpu1 = psutil.cpu_count
# mem1 = psutil.virtual_memory()[2]
# disco1 = psutil.disk_usage('C:').percent

# cpu2 = float(cpu1)*1.1 
# mem2 = float(mem1)*1.15
# disco2 = float(disco1)*0.95 

# cpu3 = float(cpu2)*1.05
# mem3 = float(mem2)*1.05
# disco3 = float(disco2)*3




# print(cpu1,mem1,disco1,cpu2,mem2,disco2)

# formulaCpuDois = ((maquinaUm["cpuPorcent"])*1.5)*100
# formulaDiscoDois = ((maquinaUm["discoPorcent"])*1.5)*100
# formulaMemoriaDois = ((maquinaUm["memoriaPorcent"])*0.95)*100


# maquinaDois = {"cpuPorcent":formulaCpuDois, "discoPorcent": formulaDiscoDois, "memoriaPorcent": formulaMemoriaDois}
# #maquinaTres = {"cpuPorcent":0, "discoPorcent": 0, "memoriaPorcent": 0}

# print(maquinaUm, maquinaDois)

# print(psutil.virtual_memory()[2])