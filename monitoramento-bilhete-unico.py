import psutil
from time import sleep
import mysql.connector


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



cpu1 = 20
mem1 = 30
disco1 = 56

cpu2 = 20*1.1 
mem2 = 30*1.15
disco2 = 56*0.95


cpu3 = cpu2*1.05
mem3 = mem2*1.05
disco3 = disco2*3

print(cpu3,mem3,disco3)


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

print(psutil.virtual_memory()[2])