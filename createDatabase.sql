-- ***************
-- * SQL MySQL generation                      
-- *--------------------------------------------
-- * DB-MAIN version: 11.0.2              
-- * Generator date: Sep 14 2021              
-- * Generation date: Fri Aug 30 23:11:07 2024 
-- * LUN file: C:\Users\Utente\OneDrive\Desktop\università\base di dati\Progetto_basi.lun 
-- * Schema: SCUOLA GUIDA/progLogica 
-- *************** 

-- Database Section
-- ______ 
CREATE DATABASE SCUOLAGUIDA;
USE SCUOLAGUIDA;

-- Tables Section
-- _____ 

CREATE TABLE Acquisti (
     idAcquisto INT NOT NULL AUTO_INCREMENT,
     costoTotale FLOAT NOT NULL,
     idStudente INT NOT NULL,
     CONSTRAINT PK_Acquisti PRIMARY KEY (idAcquisto)
);

CREATE TABLE Admins (
     username VARCHAR(50) NOT NULL,
     password VARCHAR(50) NOT NULL,
     CONSTRAINT PK_Admins PRIMARY KEY (username)
);

CREATE TABLE EsamiPratici (
     idEsame INT NOT NULL AUTO_INCREMENT,
     data DATE NULL,
     costo FLOAT NOT NULL,
     esito CHAR(1) NULL,
     idStudente INT NOT NULL,
     CFEsaminatore VARCHAR(20) NOT NULL,
     idAcquisto INT NOT NULL,
     CONSTRAINT PK_EsamiPratici PRIMARY KEY (idEsame)
);

CREATE TABLE EsamiTeorici (
     idEsame INT NOT NULL AUTO_INCREMENT,
     data DATE NULL,
     costo FLOAT NOT NULL,
     esito CHAR(1) NULL,
     numErrori INT NULL,
     idStudente INT NOT NULL,
     idAcquisto INT NOT NULL,
     CONSTRAINT PK_EsamiTeorici PRIMARY KEY (idEsame)
);

CREATE TABLE Esaminatori (
     CFEsaminatore VARCHAR(20) NOT NULL,
     nome VARCHAR(50) NOT NULL,
     cognome VARCHAR(50) NOT NULL,
     indirizzo VARCHAR(100) NOT NULL,
     recapito VARCHAR(20) NOT NULL,
     dataNascita DATE NOT NULL,
     CONSTRAINT PK_Esaminatori PRIMARY KEY (CFEsaminatore)
);

CREATE TABLE Fatture (
     numeroFattura INT NOT NULL AUTO_INCREMENT,
     importoLordo DECIMAL(10,2) NOT NULL,
     IVA DECIMAL(5,2) NOT NULL,
     importoNetto DECIMAL(10,2) NOT NULL,
     idAcquisto INT NOT NULL,
     CONSTRAINT PK_Fatture PRIMARY KEY (numeroFattura)
);

CREATE TABLE Guide (
     idGuida INT NOT NULL AUTO_INCREMENT,
     data DATE NOT NULL,
     ora TIME NOT NULL,
     idPacchetto INT NOT NULL,
     targa VARCHAR(20) NOT NULL,
     CFIstruttorePratico VARCHAR(20) NOT NULL,
     CONSTRAINT PK_Guide PRIMARY KEY (idGuida)
);

CREATE TABLE Iscrizioni (
     idStudente INT NOT NULL AUTO_INCREMENT,
     dataInizio DATE NOT NULL,
     CFStudente VARCHAR(20) NOT NULL,
     idTipologia INT NOT NULL,
     costo INT NOT NULL,
     chiusa CHAR(1) NOT NULL,
     CFIstruttoreTeorico VARCHAR(20) NOT NULL,
     CFIstruttorePratico VARCHAR(20) NOT NULL,
     CONSTRAINT PK_Iscrizioni PRIMARY KEY (idStudente),
     CONSTRAINT UK_Iscrizioni UNIQUE (CFStudente, idTipologia, dataInizio)
);

CREATE TABLE IstruttoriPratici (
     CFIstruttorePratico VARCHAR(20) NOT NULL,
     nome VARCHAR(50) NOT NULL,
     cognome VARCHAR(50) NOT NULL,
     indirizzo VARCHAR(100) NOT NULL,
     recapito VARCHAR(20) NOT NULL,
     dataNascita DATE NOT NULL,
     CONSTRAINT PK_IstruttoriPratici PRIMARY KEY (CFIstruttorePratico)
);

CREATE TABLE IstruttoriTeorici (
     CFIstruttoreTeorico VARCHAR(20) NOT NULL,
     nome VARCHAR(50) NOT NULL,
     cognome VARCHAR(50) NOT NULL,
     indirizzo VARCHAR(100) NOT NULL,
     recapito VARCHAR(20) NOT NULL,
     dataNascita DATE NOT NULL,
     CONSTRAINT PK_IstruttoriTeorici PRIMARY KEY (CFIstruttoreTeorico)
);

CREATE TABLE Lezioni (
     idLezione INT NOT NULL AUTO_INCREMENT,
     data DATE NOT NULL,
     ora TIME NOT NULL,
     CFIstruttoreTeorico VARCHAR(20) NOT NULL,
     CONSTRAINT PK_Lezioni PRIMARY KEY (idLezione)
);

CREATE TABLE Pacchetti (
     idPacchetto INT NOT NULL AUTO_INCREMENT,
     prezzo FLOAT NOT NULL,
     tipo INT NOT NULL,
     finito CHAR(1) NOT NULL,
     idAcquisto INT NOT NULL,
     CONSTRAINT PK_Pacchetti PRIMARY KEY (idPacchetto)
);

CREATE TABLE Studenti (
     CFStudente VARCHAR(20) NOT NULL,
     nome VARCHAR(50) NOT NULL,
     cognome VARCHAR(50) NOT NULL,
     indirizzo VARCHAR(100) NOT NULL,
     recapito VARCHAR(20) NOT NULL,
     dataNascita DATE NOT NULL,
     CONSTRAINT PK_Studenti PRIMARY KEY (CFStudente)
);

CREATE TABLE TipologiePatenti (
     idTipologia INT NOT NULL AUTO_INCREMENT,
     nome VARCHAR(50) NOT NULL,
     eta INT NOT NULL,
     CONSTRAINT PK_TipologiePatenti PRIMARY KEY (idTipologia)
);

CREATE TABLE Veicoli (
     targa VARCHAR(20) NOT NULL,
     modello VARCHAR(50) NOT NULL,
     CONSTRAINT PK_Veicoli PRIMARY KEY (targa)
);

-- Constraints Section
-- _______ 

ALTER TABLE Acquisti ADD CONSTRAINT FK_Appartenenza
     FOREIGN KEY (idStudente)
     REFERENCES Iscrizioni (idStudente);

ALTER TABLE EsamiPratici ADD CONSTRAINT FK_SostienePratico
     FOREIGN KEY (idStudente)
     REFERENCES Iscrizioni (idStudente);

ALTER TABLE EsamiPratici ADD CONSTRAINT FK_Esamina
     FOREIGN KEY (CFEsaminatore)
     REFERENCES Esaminatori (CFEsaminatore);

ALTER TABLE EsamiPratici ADD CONSTRAINT FK_AcquisizionePratico
     FOREIGN KEY (idAcquisto)
     REFERENCES Acquisti (idAcquisto);

ALTER TABLE EsamiTeorici ADD CONSTRAINT FK_SostieneTeorico
     FOREIGN KEY (idStudente)
     REFERENCES Iscrizioni (idStudente);

ALTER TABLE EsamiTeorici ADD CONSTRAINT FK_AcquisizioneTeorico
     FOREIGN KEY (idAcquisto)
     REFERENCES Acquisti (idAcquisto);

ALTER TABLE Fatture ADD CONSTRAINT FK_FatturaAcquisto
     FOREIGN KEY (idAcquisto)
     REFERENCES Acquisti (idAcquisto);

ALTER TABLE Guide ADD CONSTRAINT FK_Composizione
     FOREIGN KEY (idPacchetto)
     REFERENCES Pacchetti (idPacchetto);

ALTER TABLE Guide ADD CONSTRAINT FK_Mezzo
     FOREIGN KEY (targa)
     REFERENCES Veicoli (targa);

ALTER TABLE Guide ADD CONSTRAINT FK_Segue
     FOREIGN KEY (CFIstruttorePratico)
     REFERENCES IstruttoriPratici (CFIstruttorePratico);

ALTER TABLE Iscrizioni ADD CONSTRAINT FK_AssisteTeorico 
     FOREIGN KEY (CFIstruttoreTeorico)
     REFERENCES IstruttoriTeorici (CFIstruttoreTeorico);

ALTER TABLE Iscrizioni ADD CONSTRAINT FK_AssistePratico
     FOREIGN KEY (CFIstruttorePratico)
     REFERENCES IstruttoriPratici (CFIstruttorePratico);

ALTER TABLE Iscrizioni ADD CONSTRAINT FK_Effettuazione
     FOREIGN KEY (CFStudente)
     REFERENCES Studenti (CFStudente);

ALTER TABLE Iscrizioni ADD CONSTRAINT FK_Tipologia
     FOREIGN KEY (idTipologia)
     REFERENCES TipologiePatenti (idTipologia);

ALTER TABLE Lezioni ADD CONSTRAINT FK_Spiegazione
     FOREIGN KEY (CFIstruttoreTeorico)
     REFERENCES IstruttoriTeorici (CFIstruttoreTeorico);

ALTER TABLE Pacchetti ADD CONSTRAINT FK_Comprende
     FOREIGN KEY (idAcquisto)
     REFERENCES Acquisti (idAcquisto);

INSERT INTO `scuolaguida`.`admins` (`username`, `password`) VALUES ('admin', 'admin');