import mysql.connector
import zlib
import sys
import glob

def povezivanje_sa_bazom(imehosta, korisnicko_ime, lozinka, imebaze):
    baza = mysql.connector.connect(
        host=imehosta,
        user=korisnicko_ime,
        password=lozinka,
        database = imebaze,
        charset='utf8')
    return baza
def kreiranje_tabela(baza):
    kursor = baza.cursor()
    sql_naredbe = [
        """CREATE TABLE IF NOT EXISTS `CLAN` (
            `SIFC` integer  NOT NULL ,
            `IME` varchar(50)  NOT NULL ,
            `PREZIME` varchar(50)  NOT NULL ,
            `ADRESA` varchar(50)  NOT NULL ,
            `KONTAKT` varchar(15)  NOT NULL ,
            PRIMARY KEY (`SIFC`)
        )""",
    
        """CREATE TABLE IF NOT EXISTS `AUTOR` (
            `SIFA` integer  NOT NULL ,
            `IME` varchar(50)  NOT NULL ,
            `PREZIME` varchar(50)  NOT NULL ,
            PRIMARY KEY (`SIFA`)
        )""",
    
        """CREATE TABLE IF NOT EXISTS `OBLAST` (
            `SIFO` varchar(2)  NOT NULL ,
            `NAZIV` varchar(30)  NOT NULL ,
            PRIMARY KEY (`SIFO`)
        )""",
    
        """CREATE TABLE IF NOT EXISTS `NASLOV` (
            `SIFN` varchar(4)  NOT NULL ,
            `NAZIV` varchar(300)  NOT NULL ,
            `SIFO` varchar(2)  NOT NULL ,
            PRIMARY KEY (`SIFN`),
            FOREIGN KEY (`SIFO`) REFERENCES `OBLAST` (`SIFO`)
        )""",
    
        """CREATE TABLE IF NOT EXISTS `IZDAVAC` (
            `SIFI` integer  NOT NULL ,
            `NAZIV` varchar(30)  NOT NULL ,
            `ZEMLJA` varchar(30)  NOT NULL ,
            PRIMARY KEY (`SIFI`)
        )""",
    
        """CREATE TABLE IF NOT EXISTS `IZDANJE` (
            `SIFIZ` integer  NOT NULL ,
            `ISBN` varchar(13)  NOT NULL ,
            `SIFI` integer  NOT NULL ,
            `BR_STRANICA` integer  NOT NULL ,
            `GODINA` integer  NOT NULL ,
            PRIMARY KEY (`SIFIZ`),
            FOREIGN KEY(`SIFI`) REFERENCES `IZDAVAC` (`SIFI`)
        )""",
    
        """CREATE TABLE IF NOT EXISTS `KNJIGA` (
            `SIFK` integer  NOT NULL ,
            `SIFN` varchar(4)  NOT NULL ,
            `SIFIZ` integer  NOT NULL ,
            `POLICA` integer  NOT NULL ,
            PRIMARY KEY (`SIFK`),
            FOREIGN KEY(`SIFN`) REFERENCES `NASLOV` (`SIFN`),
            FOREIGN KEY(`SIFIZ`) REFERENCES `IZDANJE` (`SIFIZ`)
        )""",
    
        """CREATE TABLE IF NOT EXISTS `POZAJMICA` (
            `SIFP` integer  NOT NULL ,
            `SIFC` integer  NOT NULL ,
            `SIFK` integer  NOT NULL ,
            `DANA` integer  NOT NULL ,
            PRIMARY KEY (`SIFP`),
            FOREIGN KEY(`SIFC`) REFERENCES `CLAN` (`SIFC`),
            FOREIGN KEY(`SIFK`) REFERENCES `KNJIGA` (`SIFK`)
        )""",
    
        """CREATE TABLE IF NOT EXISTS `JE_AUTOR` (
            `SIFA` integer  NOT NULL ,
            `SIFN` varchar(4)  NOT NULL ,
            `REDNI_BROJ` integer  NOT NULL ,
            PRIMARY KEY (`SIFA`,`SIFN`),
            FOREIGN KEY(`SIFA`) REFERENCES `AUTOR` (`SIFA`),
            FOREIGN KEY(`SIFN`) REFERENCES `NASLOV` (`SIFN`)
        )""",
    
        """CREATE TABLE IF NOT EXISTS `DRZI` (
            `SIFK` integer  NOT NULL ,
            `SIFC` integer  NOT NULL ,
            `DATUM_POZAJMICE` date  NOT NULL ,
            `TRAJANJE` integer NOT NULL, 
            PRIMARY KEY (`SIFK`),
            FOREIGN KEY(`SIFK`) REFERENCES `KNJIGA` (`SIFK`),
            FOREIGN KEY(`SIFC`) REFERENCES `CLAN` (`SIFC`)
        )"""
    ]
    for sql in sql_naredbe:
        kursor.execute(sql)
    
    baza.commit()
    kursor.close()

try:
    baza=povezivanje_sa_bazom("localhost", "root", "", "biblioteka")
    kreiranje_tabela(baza)
    baza.close()
except mysql.connector.Error as sql_err:
    print("SQL greška:", sql_err)

except Exception as e:
    print("Došlo je do greške:", e)
