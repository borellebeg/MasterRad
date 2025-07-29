CREATE TABLE `CLAN` (
    `SIFC` integer  NOT NULL ,
    `IME` varchar(50)  NOT NULL ,
    `PREZIME` varchar(50)  NOT NULL ,
    `ADRESA` varchar(50)  NOT NULL ,
    `KONTAKT` varchar(15)  NOT NULL ,
    PRIMARY KEY (`SIFC`)
);

CREATE TABLE `AUTOR` (
    `SIFA` integer  NOT NULL ,
    `IME` varchar(50)  NOT NULL ,
    `PREZIME` varchar(50)  NOT NULL ,
    PRIMARY KEY (`SIFA`)
);

CREATE TABLE `OBLAST` (
    `SIFO` varchar(2)  NOT NULL ,
    `NAZIV` varchar(30)  NOT NULL ,
    PRIMARY KEY (`SIFO`)
);

CREATE TABLE `NASLOV` (
    `SIFN` varchar(4)  NOT NULL ,
    `NAZIV` varchar(300)  NOT NULL ,
    `SIFO` varchar(2)  NOT NULL ,
    PRIMARY KEY (`SIFN`),
    FOREIGN KEY (`SIFO`) REFERENCES `OBLAST` (`SIFO`)
);

CREATE TABLE `IZDAVAC` (
    `SIFI` integer  NOT NULL ,
    `NAZIV` varchar(30)  NOT NULL ,
    `ZEMLJA` varchar(30)  NOT NULL ,
    PRIMARY KEY (`SIFI`)
);

CREATE TABLE `IZDANJE` (
    `SIFIZ` integer  NOT NULL ,
    `ISBN` varchar(13)  NOT NULL ,
    `SIFI` integer  NOT NULL ,
    `BR_STRANICA` integer  NOT NULL ,
    `GODINA` integer  NOT NULL ,
    PRIMARY KEY (`SIFIZ`),
    FOREIGN KEY(`SIFI`) REFERENCES `IZDAVAC` (`SIFI`)
);

CREATE TABLE `KNJIGA` (
    `SIFK` integer  NOT NULL ,
    `SIFN` varchar(4)  NOT NULL ,
    `SIFIZ` integer  NOT NULL ,
    `POLICA` integer  NOT NULL ,
    PRIMARY KEY (`SIFK`),
    FOREIGN KEY(`SIFN`) REFERENCES `NASLOV` (`SIFN`),
    FOREIGN KEY(`SIFIZ`) REFERENCES `IZDANJE` (`SIFIZ`)

);

CREATE TABLE `POZAJMICA` (
    `SIFP` integer  NOT NULL ,
    `SIFC` integer  NOT NULL ,
    `SIFK` integer  NOT NULL ,
    `DANA` integer  NOT NULL ,
    PRIMARY KEY (`SIFP`),
    FOREIGN KEY(`SIFC`) REFERENCES `CLAN` (`SIFC`),
    FOREIGN KEY(`SIFK`) REFERENCES `KNJIGA` (`SIFK`)
);

CREATE TABLE `JE_AUTOR` (
    `SIFA` integer  NOT NULL ,
    `SIFN` varchar(4)  NOT NULL ,
    `REDNI_BROJ` integer  NOT NULL ,
    PRIMARY KEY (`SIFA`,`SIFN`),
    FOREIGN KEY(`SIFA`) REFERENCES `AUTOR` (`SIFA`),
    FOREIGN KEY(`SIFN`) REFERENCES `NASLOV` (`SIFN`)
);

CREATE TABLE `DRZI` (
    `SIFK` integer  NOT NULL ,
    `SIFC` integer  NOT NULL ,
    `DATUM_POZAJMICE` date  NOT NULL ,
    `TRAJANJE` integer NOT NULL, 
    PRIMARY KEY (`SIFK`),
    FOREIGN KEY(`SIFK`) REFERENCES `KNJIGA` (`SIFK`),
    FOREIGN KEY(`SIFC`) REFERENCES `CLAN` (`SIFC`)
);









