CREATE DATABASE AGENDAAI;

USE AGENDAAI;

-- CREATE TABLE (
 --   CONSTRAINT pk_Tabela_campo PRIMARY KEY(id),
 --   CONSTRAINT fk_Tabela_Tabela_FK_ID FOREIGN KEY(id) REFERENCES [nome_tabela](id_tabela_fk)
--)

CREATE TABLE users (
    id INT NOT NULL IDENTITY(1,1),
    email VARCHAR(60) NOT NULL UNIQUE,
    senha VARCHAR(250) NOT NULL,
    nome  VARCHAR(250) NOT NULL,
    apelido VARCHAR(250) NOT NULL,
    token VARCHAR(254) NULL,
    active BIT DEFAULT(1),
    CONSTRAINT PK_users_id PRIMARY KEY(id)
);