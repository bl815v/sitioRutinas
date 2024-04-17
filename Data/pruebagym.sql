CREATE DATABASE pruebagym;
USE pruebagym;

CREATE TABLE usuarios (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    documento VARCHAR(20) NOT NULL,
    celular VARCHAR(20) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    altura FLOAT NOT NULL,
    peso FLOAT NOT NULL,
    dias TEXT NOT NULL,
    objetivo VARCHAR(100) NOT NULL
);
