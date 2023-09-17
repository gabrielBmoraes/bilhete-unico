create database bilheteUnico;
use bilheteUnico;

create table Funcionario (
idFuncionario INT  PRIMARY KEY AUTO_INCREMENT,
Email VARCHAR(45),
Senha VARCHAR(45)
)AUTO_INCREMENT = 100;

create table Servidor(
idServidor INT PRIMARY KEY AUTO_INCREMENT,
descricao VARCHAR(45)		
) AUTO_INCREMENT = 100;


create table FuncionarioServidor(
fkFuncionario INT,
fkServidor INT,
fOREIGN KEY(fkFuncionario) REFERENCES Funcionario(idFuncionario),
fOREIGN KEY(fkServidor) REFERENCES Servidor(idServidor),
PRIMARY KEY(fkFuncionario, fkServidor) 
);



create table Maquina (
idMaquina INT PRIMARY KEY AUTO_INCREMENT,
descricao VARCHAR(45),
fkServidor INT,
FOREIGN KEY(fkServidor) REFERENCES Servidor(idServidor)
)AUTO_INCREMENT = 10;

create table Metrica(
idMetrica INT PRIMARY KEY auto_increment,
unidadeMedida VARCHAR(45)
)auto_increment = 1;

create table Registro(
idRegistro INT PRIMARY KEY AUTO_INCREMENT,
tipo VARCHAR(45),
fkMaquina INT,
fkMetrica INT,
FOREIGN KEY(fkMaquina) REFERENCES Maquina(idMaquina),
FOREIGN KEY(fkMetrica) REFERENCES Metrica(idMetrica)
) AUTO_INCREMENT = 1;

-- Pegar servidor e máquina
select idServidor as Servidor, idMaquina as Maquina from Servidor join Maquina on fkServidor = idServidor;

-- Dados cpu
select tipo as Categoria, unidadeMedida as 'Unidade de Medida' from Registro join Metrica 
	on fkMetrica = idMetrica and tipo = 'cpu' and unidadeMedida = '%';
    
-- Dados ram
select tipo as Categoria, unidadeMedida as 'Unidade de Medida' from Registro join Metrica 
	on fkMetrica = idMetrica and tipo = 'ram' and unidadeMedida = '%';
    
-- Dados cpu
select tipo as Categoria, unidadeMedida as 'Unidade de Medida' from Registro join Metrica 
	on fkMetrica = idMetrica and tipo = 'disco' and unidadeMedida = '%';
