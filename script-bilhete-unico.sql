drop database bilheteUnico;
create database bilheteUnico;

use bilheteUnico;

create table Funcionario (
idFuncionario INT  PRIMARY KEY AUTO_INCREMENT,
Email VARCHAR(45),
Senha VARCHAR(45)
)AUTO_INCREMENT = 100;

create table Servidor(
idServidor INT PRIMARY KEY AUTO_INCREMENT,
descricao VARCHAR(250)		
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
descricao VARCHAR(250),
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
valor DECIMAL(5,2),
horario DATETIME,
fkMaquina INT,
fkMetrica INT,
FOREIGN KEY(fkMaquina) REFERENCES Maquina(idMaquina),
FOREIGN KEY(fkMetrica) REFERENCES Metrica(idMetrica)
) AUTO_INCREMENT = 1;


INSERT INTO Metrica values(null, '%');
INSERT INTO Servidor values(null, 'servidor das máquinas da estação Vila Prudente');
INSERT INTO Maquina value(null,'primeira máquina',100);
INSERT INTO Maquina value(null,'Segunda máquina',100);
INSERT INTO Maquina value(null,'Terceira máquina',100);

select * from Registro;
-- Pegar servidor e máquina
CREATE VIEW servidorRegistro as select idServidor as Servidor, idMaquina as Maquina from Servidor join Maquina on fkServidor = idServidor;

-- Dados cpu
CREATE VIEW dadosCpu as select tipo as Categoria, valor as Registro, unidadeMedida as 'Unidade de Medida', horario as 'Horário' from Registro join Metrica 
	on fkMetrica = idMetrica and tipo = 'cpu' and unidadeMedida = '%';

-- Dados ram
select tipo as Categoria, unidadeMedida as 'Unidade de Medida' from Registro join Metrica 
	on fkMetrica = idMetrica and tipo = 'ram' and unidadeMedida = '%';
    
-- Dados cpu
select tipo as Categoria, unidadeMedida as 'Unidade de Medida' from Registro join Metrica 
	on fkMetrica = idMetrica and tipo = 'disco' and unidadeMedida = '%';
    
  drop view viewCliente;
 CREATE VIEW viewCliente as select * from servidorRegistro join dadosCpu order by 'Horário';
 
 select * from viewCliente;
