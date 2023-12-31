drop database bilheteUnico;
create database bilheteUnico;
-- GRANT all privileges on bilheteunico.* to urubu100;
-- flush privileges;

use bilheteUnico;

create table Funcionario (
idFuncionario INT  PRIMARY KEY AUTO_INCREMENT,
Email VARCHAR(45),
Senha VARCHAR(45)
)AUTO_INCREMENT = 100;

create table Servidor(
idServidor INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(50),
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
INSERT INTO Servidor values(null,'GD3948', 'servidor das máquinas da estação Vila Prudente');
INSERT INTO Maquina value(null,'primeira máquina',100);
INSERT INTO Maquina value(null,'Segunda máquina',100);
INSERT INTO Maquina value(null,'Terceira máquina',100);
Insert into Funcionario values (null,'cliente@gmail.com', '12345');


select * from Registro;

-- Pegar servidor e máquina
CREATE VIEW servidorRegistro as select idServidor as Servidor, idMaquina as Maquina from Servidor join Maquina on fkServidor = idServidor;
select * from servidorRegistro;

-- Dados cpu
-- drop view dadosCpu;
CREATE VIEW dadosCpu as select tipo as Categoria, valor as Registro, unidadeMedida, horario from Registro join Metrica 
	on fkMetrica = idMetrica and tipo = 'cpu' and unidadeMedida = '%' where Registro.fkMaquina = 10;
select * from dadosCpu;

-- drop view dadosCpuMaquinaDois;
CREATE VIEW dadosCpuMaquinaDois as select tipo as Categoria, valor as Registro, unidadeMedida, horario from Registro join Metrica 
	on fkMetrica = idMetrica and tipo = 'cpu' and unidadeMedida = '%' where Registro.fkMaquina = 11;
select * from dadosCpuMaquinaDois;

-- drop view dadosCpuMaquinaTres;
CREATE VIEW dadosCpuMaquinaTres as select tipo as Categoria, valor as Registro, unidadeMedida, horario from Registro join Metrica 
	on fkMetrica = idMetrica and tipo = 'cpu' and unidadeMedida = '%' where Registro.fkMaquina = 12;
select * from dadosCpuMaquinaTres;

-- Dados ram
CREATE VIEW dadosRam as select tipo as Categoria, valor as Registro, unidadeMedida as 'Unidade de Medida', horario as 'Horário' from Registro join Metrica 
	on fkMetrica = idMetrica and tipo = 'ram' and unidadeMedida = '%';
select * from dadosRam;
    
-- Dados disco
CREATE VIEW dadosDisco as select tipo as Categoria, valor as Registro, unidadeMedida as 'Unidade de Medida' from Registro join Metrica 
	on fkMetrica = idMetrica and tipo = 'disco' and unidadeMedida = '%';
select * from dadosDisco;

-- drop view viewCliente;
CREATE VIEW viewCliente as select servidorRegistro.*, dadosCpu.Registro as 'CPU', dadosRam.Registro as 'RAM', dadosDisco.Registro as 'Disco',
	dadosCpu.unidadeMedida as 'Unidade de Medida', dadosCpu.horario as 'Horário' 
	from servidorRegistro join dadosCpu join dadosRam join dadosDisco order by 'Horário' and 'Maquina'; 
select * from viewCliente;

-- drop view viewClienteMaquinaUm;
CREATE VIEW viewClienteMaquinaUm as select servidorRegistro.*, dadosCpu.Registro as 'CPU', dadosRam.Registro as 'RAM', dadosDisco.Registro as 'Disco',
	dadosCpu.unidadeMedida as 'Unidade de Medida', dadosCpu.horario as 'Horário' 
	from servidorRegistro join dadosCpu join dadosRam join dadosDisco where servidorRegistro.maquina = 10 order by dadosCpu.horario desc; 
select * from viewClienteMaquinaUm;

-- drop view viewClienteMaquinaDois;
CREATE VIEW viewClienteMaquinaDois as select servidorRegistro.*, dadosCpu.Registro as 'CPU', dadosRam.Registro as 'RAM', dadosDisco.Registro as 'Disco',
	dadosCpu.unidadeMedida as 'Unidade de Medida', dadosCpu.horario as 'Horário' 
	from servidorRegistro join dadosCpu join dadosRam join dadosDisco where servidorRegistro.maquina = 11 order by dadosCpu.horario desc; 
select * from viewClienteMaquinaDois;

-- drop view viewClienteMaquinaTres;
CREATE VIEW viewClienteMaquinaTres as select servidorRegistro.*, dadosCpu.Registro as 'CPU', dadosRam.Registro as 'RAM', dadosDisco.Registro as 'Disco',
	dadosCpu.unidadeMedida as 'Unidade de Medida', dadosCpu.horario as 'Horário' 
	from servidorRegistro join dadosCpu join dadosRam join dadosDisco where servidorRegistro.maquina = 12 order by dadosCpu.horario desc; 
select * from viewClienteMaquinaTres;
