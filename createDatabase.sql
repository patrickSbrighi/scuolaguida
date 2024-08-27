-- *********************************************
-- * SQL MySQL generation                      
-- *--------------------------------------------
-- * DB-MAIN version: 11.0.2              
-- * Generator date: Sep 14 2021              
-- * Generation date: Wed Jul 31 15:32:42 2024 
-- * LUN file: C:\Users\Utente\Downloads\Progetto_basi_2.lun 
-- * Schema: SCUOLA GUIDA/progLogica 
-- ********************************************* 


-- Database Section
-- ________________ 

create database SCUOLAGUIDA;
use SCUOLAGUIDA;


-- Tables Section
-- _____________ 

create table ACQUISTI (
     idAcquisto int not null auto_increment,
     numeroFattura int not null,
     costoTotale float(5) not null,
     idStudente int not null,
     constraint IDACQUISTO primary key (idAcquisto),
     constraint FKemissione_ID unique (numeroFattura));

create table ADMIN (
     username  char(100) not null,
     password char(100) not null,
     constraint IDADMIN primary key (username ));

create table ESAMIPRATICI (
     idEsame int not null auto_increment,
     data date not null,
     costo float(5) not null,
     esito char not null,
     idStudente int not null,
     CFEsaminatore char(100) not null,
     idAcquisto int not null,
     constraint IDESAME primary key (idEsame));

create table ESAMITEORICI (
     idEsame int not null auto_increment,
     data date not null,
     costo float(5) not null,
     esito char not null,
     numErrori int not null,
     idStudente int not null,
     idAcquisto int not null,
     constraint IDESAME primary key (idEsame));

create table ESAMINATORI (
     CFEsaminatore char(100) not null,
     nome char(100) not null,
     cognome char(100) not null,
     indirzzo char(100) not null,
     recapito char(100) not null,
     dataNascita date not null,
     constraint IDESAMINATORE primary key (CFEsaminatore));

create table FATTURE (
     numeroFattura int not null auto_increment,
     importoLordo float(5) not null,
     IVA float(5) not null,
     constraint IDFATTURA_ID primary key (numeroFattura));

create table GUIDE (
     idGuida int not null auto_increment,
     data date not null,
     ora int not null,
     IdPacchetto int not null,
     targa char(100) not null,
     CFIstruttorePratico char(100) not null,
     constraint IDGUIDA primary key (idGuida));

create table ISCRIZIONI (
     idStudente int not null auto_increment,
     dataInizio date not null,
     CFStudente char(100) not null,
     idTipologia int not null,
     idAcquisto int,
     costo float(5) not null,
     chiusa char not null,
     CFIstruttoreTeorico char(100) not null,
     CFIstruttorePratico char(100) not null,
     constraint IDISCRIZIONE primary key (idStudente),
     constraint IDISCRIZIONE_1 unique (CFStudente, idTipologia, dataInizio));

create table ISTRUTTORIPRATICI  (
     CFIstruttorePratico char(100) not null,
     nome char(100) not null,
     cognome char(100) not null,
     indirzzo char(100) not null,
     recapito char(100) not null,
     dataNascita date not null,
     constraint IDISTRUTTOREPRATICO  primary key (CFIstruttorePratico));

create table ISTRUTTORITEORICI  (
     CFIstruttoreTeorico char(100) not null,
     nome char(100) not null,
     cognome char(100) not null,
     indirzzo char(100) not null,
     recapito char(100) not null,
     dataNascita date not null,
     constraint IDISTRUTTORETEORICO  primary key (CFIstruttoreTeorico));

create table LEZIONI (
     idLezione int not null auto_increment,
     data date not null,
     ora int not null,
     CFIstruttoreTeorico char(100) not null,
     constraint IDLEZIONE primary key (idLezione));

create table PACCHETTI (
     IdPacchetto int not null auto_increment,
     prezzo float(5) not null,
     tipo int not null,
     idAcquisto int not null,
     constraint IDPACCHETTO primary key (IdPacchetto));

create table STUDENTI (
     CFStudente char(100) not null,
     nome char(100) not null,
     cognome char(100) not null,
     indirzzo char(100) not null,
     recapito char(100) not null,
     dataNascita date not null,
     constraint IDCLIENTE primary key (CFStudente));

create table TIPOLOGIEPATENTE (
     idTipologia int not null auto_increment,
     nome char(100) not null,
     eta int not null,
     constraint IDTIPOLOGIAPATENTE primary key (idTipologia));

create table VEICOLI (
     targa char(100) not null,
     modello char(100) not null,
     constraint IDVEICOLO primary key (targa));


-- Constraints Section
-- ___________________ 

alter table ACQUISTI add constraint FKappartenenza
     foreign key (idStudente)
     references ISCRIZIONI (idStudente);

alter table ACQUISTI add constraint FKemissione_FK
     foreign key (numeroFattura)
     references FATTURE (numeroFattura);

alter table ESAMIPRATICI add constraint FKsostienePratico
     foreign key (idStudente)
     references ISCRIZIONI (idStudente);

alter table ESAMIPRATICI add constraint FKesamina
     foreign key (CFEsaminatore)
     references ESAMINATORI (CFEsaminatore);

alter table ESAMIPRATICI add constraint FKacquisizione
     foreign key (idAcquisto)
     references ACQUISTI (idAcquisto);

alter table ESAMITEORICI add constraint FKsostieneTeorico
     foreign key (idStudente)
     references ISCRIZIONI (idStudente);

alter table ESAMITEORICI add constraint FKacqusizione
     foreign key (idAcquisto)
     references ACQUISTI (idAcquisto);

-- Not implemented
-- alter table FATTURE add constraint IDFATTURA_CHK
--     check(exists(select * from ACQUISTI
--                  where ACQUISTI.numeroFattura = numeroFattura)); 

alter table GUIDE add constraint FKcomposizione
     foreign key (IdPacchetto)
     references PACCHETTI (IdPacchetto);

alter table GUIDE add constraint FKmezzo
     foreign key (targa)
     references VEICOLI (targa);

alter table GUIDE add constraint FKsegue
     foreign key (CFIstruttorePratico)
     references ISTRUTTORIPRATICI  (CFIstruttorePratico);

alter table ISCRIZIONI add constraint FKassisteTeorico
     foreign key (CFIstruttoreTeorico)
     references ISTRUTTORITEORICI  (CFIstruttoreTeorico);

alter table ISCRIZIONI add constraint FKassistePratico
     foreign key (CFIstruttorePratico)
     references ISTRUTTORIPRATICI  (CFIstruttorePratico);

alter table ISCRIZIONI add constraint FKeffettuazione
     foreign key (CFStudente)
     references STUDENTI (CFStudente);

alter table ISCRIZIONI add constraint FKtipologia
     foreign key (idTipologia)
     references TIPOLOGIEPATENTE (idTipologia);

alter table LEZIONI add constraint FKspiegazione
     foreign key (CFIstruttoreTeorico)
     references ISTRUTTORITEORICI  (CFIstruttoreTeorico);

alter table PACCHETTI add constraint FKcomprende
     foreign key (idAcquisto)
     references ACQUISTI (idAcquisto);


-- Index Section
-- _____________ 

