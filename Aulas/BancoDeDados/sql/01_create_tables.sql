CREATE DATABASE filmes;
USE filmes;

CREATE TABLE `filmes` (
	`id` INT NOT NULL,
	`filme` varchar(100) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `usuarios` (
	`id` INT NOT NULL,
	`usuario` varchar(50) NOT NULL,
	`sexo` varchar(1) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `avaliacoes` (
	`id` INT NOT NULL,
	`filme` INT NOT NULL,
	`usuario` INT NOT NULL,
	`nota` FLOAT,
	PRIMARY KEY (`id`)
);

ALTER TABLE `avaliacoes` ADD CONSTRAINT `avaliacoes_fk0` FOREIGN KEY (`filme`) REFERENCES `filmes`(`id`);

ALTER TABLE `avaliacoes` ADD CONSTRAINT `avaliacoes_fk1` FOREIGN KEY (`usuario`) REFERENCES `usuarios`(`id`);




