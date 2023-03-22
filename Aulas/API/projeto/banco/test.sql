-- Active: 1669074719164@@127.0.0.1@3306@gama
CREATE DATABASE IF NOT EXISTS teste;
USE teste;
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
INSERT INTO alunos VALUES (1, 'teste', 0, 0, 'AA', 2, '');