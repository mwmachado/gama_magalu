-- Active: 1667845254722@@127.0.0.1@3306@gama
CREATE DATABASE IF NOT EXISTS gama;
USE gama;
DROP TABLE IF EXISTS alunos;
CREATE TABLE alunos(
  id INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(100) NOT NULL,
  idade INTEGER NOT NULL,
  filhos INTEGER NOT NULL,
  estado VARCHAR(3) NOT NULL,
  altura DECIMAL(3,2) NOT NULL,
  formacao VARCHAR(100)
);

INSERT INTO alunos(nome, idade, filhos, estado, altura, formacao) VALUES
('Anderson',40,0,'SP',1.9,'Superior Incompleto (ADS)'),
('Ettore Mitsueda',29,2,'SP',1.72,'Ensino Médio Completo'),
('Bruna',28,0,'MG',1.62,'Superior completo'),
('clara',19,0,'RJ',1.63,'superior incompleto (ADS)'),
('João Paulo',27,0,'DF',1.5,'Superior completo'),
('Fernando A',32,1,'SP',1.74,'Mestrado completo/Doutorado incompleto'),
('José Vitor',24,0,'PB',1.78,'superior incompleto'),
('Raissa',32,2,'GO',1.68,'Superior'),
('George',38,0,'CE',1.8,'Superior'),
('Bruno Coelho',30,0,'SP',1.7,'Superior'),
('Fernando Oliveira',41,0,'SP',1.79,'Superior'),
('Edson',26,0,'PR',1.8,'Superior Incompleto'),
('Eron',32,1,'SP',1.76,'Ensino Médio Completo'),
('Fernando',23,0,'RN',1.7,'Ensino Médio'),
('Wagner',30,0,'CE',2,'Superior Completo'),
('Gabrielle',25,0,'RJ',1.56,'Superior Completo'),
('Larissa',28,0,'RJ',1.74,'Ensino Superior Completo'),
('Câmara',58,1,'RJ',1.8,'Superior Completo'),
('William Ferrari',40,3,'SP',1.73,'Superior incompleto'),
('Erick',26,0,'SP',1.7,'Ensino Superior Completo'),
('lucas',26,0,'SP',1.7,'superior'),
('Willian Caetano',37,1,'pa',1.75,'superior'),
('Divino',24,0,'SP',1.69,'Superior'),
('Natalia',25,0,'SSA',1.59,'Ensino Médio Completo'),
('julia',30,0,'pa',1.59,'superior completo'),
('Gabriel Silva',27,0,'SP',1.8,'superior incompleto'),
('Bruno Fernandes',25,0,'SC',1.9,'Superior incompleto'),
('Josivaldo',35,8,'SP',1.8,'Ensino medio Completo'),
('BRUNO LIMA',32,0,'pr',1.8,'Pós graduado'),
('Sandro Santos Marra',38,0,'DF',1.83,'Ensino Superior Inc'),
('Gabriel Queiroz',23,0,'MG',1.78,'Superior Completo');

SELECT * FROM alunos;