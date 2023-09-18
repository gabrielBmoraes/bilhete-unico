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

def enviarBancoCpu(registroCpu1, registroCpu2, registroCpu3):
    chamarbd.execute("INSERT INTO Registro values" + 
                 f"(null,'cpu',{registroCpu1},'{horarioRegistro}',10,1),"  + 
                 f"(null,'cpu',{registroCpu2},'{horarioRegistro}',11,1),"  +
                 f"(null,'cpu',{registroCpu3},'{horarioRegistro}',12,1)")
    infobd.commit()

def enviarBancoMem(registroMem1, registroMem2, registroMem3):
    chamarbd.execute("INSERT INTO Registro values" + 
                 f"(null,'ram',{registroMem1},'{horarioRegistro}',10,1),"  + 
                 f"(null,'ram',{registroMem2},'{horarioRegistro}',11,1),"  +
                 f"(null,'ram',{registroMem3},'{horarioRegistro}',12,1)")
infobd.commit()

def enviarBancoDisco(registroDisco1, registroDisco2, registroDisco3):
    chamarbd.execute("INSERT INTO Registro values" + 
                 f"(null,'disco',{registroDisco1},'{horarioRegistro}',10,1),"  + 
                 f"(null,'disco',{registroDisco2},'{horarioRegistro}',11,1),"  +
                 f"(null,'disco',{registroDisco3},'{horarioRegistro}',12,1)")
infobd.commit()


def dadosTratamento(cpu1, cpu2, cpu3, mem1, mem2, mem3, disco1, disco2, disco3):
    registroCpu1 = min(100,cpu1)
    registroCpu2 = min(100,cpu2)
    registroCpu3 = min(100,cpu3)


    registroMem1 = min(100,mem1)
    registroMem2 = min(100,mem2)
    registroMem3 = min(100,mem3)

    registroDisco1 = min(100,disco1)
    registroDisco2 = min(100,disco2)
    registroDisco3 = min(100,disco3)

    enviarBancoCpu(registroCpu1, registroCpu2, registroCpu3)




def capturarDados():
    cpu1 = psutil.cpu_percent()
    mem1 = psutil.virtual_memory().percent
    disco1 = psutil.disk_usage('C:').percent
    cpu2 = cpu1*1.1 
    mem2 = 30*1.15
    disco2 = 56*0.95
    cpu3 = cpu2*1.05
    mem3 = mem2*1.05
    disco3 = disco2*3
    
    dadosTratamento(cpu1,cpu2, cpu3, mem1, mem2, mem3, disco1, disco2, disco3)



def verTodasMaquinas():
    capturarDados()

def monitorarMaquina():
    print(
        """
        Deseja Monitorar qual máquina:
        1 - Primeira Máquina
        2 - Segunda Máquina
        3 - Terceira Máquina
        4 - Ver todas às máquinas
        5 - voltar
        """
    )
    escolhaOpcao = int(input("Opção selecionada: "))

    if escolhaOpcao == 4:
        capturarDados()



validacaoLogin = False

email = input("Email: ")
senha = input("Senha: ")

chamarbd.execute("Select email, senha from Funcionario")

listaUsuario = chamarbd.fetchall()


while validacaoLogin == False:

    for x in listaUsuario:
        
        if email == (x[0]) and senha == (x[1]):
            validacaoLogin = True
    
    if validacaoLogin == False:
        print("Erro ao realizar o login!")

print(
    """
    Login Realizado com sucesso!

    Estes são os seus servidores disponiveis:
    1 - SF0820
    """
)

escolhaServidor = int(input("Servidor escolhido: "))

print(
    """
    O que deseja fazer?
    1 - Ver situação do servidor
    2 - Monitorar máquinas 
    3 - Sair
    """
)

escolhaOpcao = int(input("Opção escolhida: "))
if escolhaOpcao == 2:
    monitorarMaquina()







