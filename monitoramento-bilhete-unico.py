import psutil
from time import sleep
import mysql.connector
from datetime import datetime
import pandas as pd

infobd = mysql.connector.connect( 
 host = 'localhost',
 user = 'urubu100',
 password = 'urubu100',
 database = 'bilheteUnico'
)


chamarbd = infobd.cursor()
horarioRegistro = datetime.now()





def mostrarUso(quantidadeTupla = 3):

    capturarDados()

    while True:
        
        chamarbd.execute("Select * from viewCliente")
        listaUsoMaquina = chamarbd.fetchall()


        for x in range(0,quantidadeTupla):
                
                mydataset = {
                    'Servidor': [listaUsoMaquina[x][0]],
                    'Maquina': [listaUsoMaquina[x][1]],
                    'CPU': [listaUsoMaquina[x][2]],
                    'RAM': [listaUsoMaquina[x][3]],
                    'Disco': [listaUsoMaquina[x][4]],
                    'Unidade': [listaUsoMaquina[x][5]],
                    'Horário': [listaUsoMaquina[x][6]]
                }

                myvar = pd.DataFrame(mydataset)
                print(myvar)

        escolhaOpcao = opcaoMenu()

        if escolhaOpcao == 1:
            quantidadeTupla = int(input("Informe o número de registro desejável: "))
        elif escolhaOpcao == 2:
            mostrarUso(quantidadeTupla)
        elif escolhaOpcao == 3:
            monitorarMaquina()
        else:
            opcaoMenu()

            




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

    enviarBancoMem(registroMem1, registroMem2, registroMem3)
    enviarBancoDisco(registroDisco1, registroDisco2, registroDisco3)
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






def opcaoMenu():
    print(
            """
            Aperte:
            
            1 - Ver mais registro
            2 - continuar com o programa 
            3 - Voltar
            """
        )
    return int(input())






def mostrarMaquinaUm(quantidadeTupla = 1):
     capturarDados()
     while True:
        
        chamarbd.execute("Select * from viewClienteMaquinaUm")
        listaUsoMaquina = chamarbd.fetchall()


        for x in range(0,quantidadeTupla):
                
                mydataset = {
                    'Servidor': [listaUsoMaquina[x][0]],
                    'Maquina': [listaUsoMaquina[x][1]],
                    'CPU': [listaUsoMaquina[x][2]],
                    'RAM': [listaUsoMaquina[x][3]],
                    'Disco': [listaUsoMaquina[x][4]],
                    'Unidade': [listaUsoMaquina[x][5]],
                    'Horário': [listaUsoMaquina[x][6]]
                }

                myvar = pd.DataFrame(mydataset)
                print(myvar)

        escolhaOpcao = opcaoMenu()
        
        if escolhaOpcao == 0:
            Login()
        elif escolhaOpcao == 1:
            quantidadeTupla = int(input("Informe o número de registro desejável: "))
        elif escolhaOpcao == 2:
            mostrarMaquinaUm(quantidadeTupla)
        elif escolhaOpcao == 3:
            monitorarMaquina()
        else:
            opcaoMenu()






def mostrarMaquinaDois(quantidadeTupla = 1):
     capturarDados()
     while True:
        
        chamarbd.execute("Select * from viewClienteMaquinaDois")
        listaUsoMaquina = chamarbd.fetchall()


        for x in range(0,quantidadeTupla):
                
                mydataset = {
                    'Servidor': [listaUsoMaquina[x][0]],
                    'Maquina': [listaUsoMaquina[x][1]],
                    'CPU': [listaUsoMaquina[x][2]],
                    'RAM': [listaUsoMaquina[x][3]],
                    'Disco': [listaUsoMaquina[x][4]],
                    'Unidade': [listaUsoMaquina[x][5]],
                    'Horário': [listaUsoMaquina[x][6]]
                }

                myvar = pd.DataFrame(mydataset)
                print(myvar)

        escolhaOpcao = opcaoMenu()

        if escolhaOpcao == 1:
            quantidadeTupla = int(input("Informe o número de registro desejável: "))
        elif escolhaOpcao == 2:
            mostrarMaquinaDois(quantidadeTupla)





def mostrarMaquinaTres(quantidadeTupla = 1):
     capturarDados()
     while True:
        
        chamarbd.execute("Select * from viewClienteMaquinaTres")
        listaUsoMaquina = chamarbd.fetchall()


        for x in range(0,quantidadeTupla):
                
                mydataset = {
                    'Servidor': [listaUsoMaquina[x][0]],
                    'Maquina': [listaUsoMaquina[x][1]],
                    'CPU': [listaUsoMaquina[x][2]],
                    'RAM': [listaUsoMaquina[x][3]],
                    'Disco': [listaUsoMaquina[x][4]],
                    'Unidade': [listaUsoMaquina[x][5]],
                    'Horário': [listaUsoMaquina[x][6]]
                }

                myvar = pd.DataFrame(mydataset)
                print(myvar)

        escolhaOpcao = opcaoMenu()

        if escolhaOpcao == 1:
            quantidadeTupla = int(input("Informe o número de registro desejável: "))
        elif escolhaOpcao == 2:
            mostrarMaquinaTres(quantidadeTupla)
        elif escolhaOpcao == 3:
            monitorarMaquina()
        else :
            opcaoMenu()



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

    if escolhaOpcao == 1:
        mostrarMaquinaUm()
    elif escolhaOpcao == 2:
        mostrarMaquinaDois()
    elif escolhaOpcao == 3:
        mostrarMaquinaTres()
    elif escolhaOpcao == 4:
        mostrarUso()
    else:
        monitorarMaquina()


def situacaoServidor():

    chamarbd.execute("Select * from Servidor")
    chamarbd.fetchall()
    
    print(
        """
        Servidor está conectado com o banco !

        Aperte 1 para voltar
        """)
    escolhaOpcao = int(input())

    if escolhaOpcao == 1:
        mostrarServidores()
    else :
        situacaoServidor()






def mostrarServidores():
    print(
        """
        Login Realizado com sucesso!

        Estes são os seus servidores disponiveis:
        1 - BU1109

        Para sair, aperte 0
        """
    )
    escolhaOpcao = int(input("Servidor escolhido: "))
    
    if  escolhaOpcao == 0:
        Login()
    elif escolhaOpcao == 1:
        menuGeral()


def menuGeral():

    print(
        """
        O que deseja fazer?
        0 - Sair
        1 - Ver situação do servidor
        2 - Monitorar máquinas 
        3 - Voltar
        """
    )
    escolhaOpcao = int(input("Opção escolhida: "))
    
    if escolhaOpcao == 0:
        Login()
    elif escolhaOpcao == 1:
        situacaoServidor()
    elif escolhaOpcao == 2:
        monitorarMaquina()
    elif escolhaOpcao == 3:
        mostrarServidores()
    else:
        menuGeral()



def Login():

    validacaoLogin = False

    chamarbd.execute("Select email, senha from Funcionario")

    listaUsuario = chamarbd.fetchall()

    while validacaoLogin == False:

        email = input("Email: ")
        senha = input("Senha: ")
        
        for x in listaUsuario:
            
            if email == (x[0]) and senha == (x[1]):
                validacaoLogin = True
        
        if validacaoLogin == False:
            print("Erro ao realizar o login!")

    mostrarServidores()
    











