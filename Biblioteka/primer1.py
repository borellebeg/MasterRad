import mysql.connector
from mysql.connector import errorcode

def povezivanje_sa_bazom(hname, uname, upass, dbname):
    bp = mysql.connector.connect(
        host = hname,
        user = uname,
        password = upass,
        database = dbname)
    return bp

try:
    veza=povezivanje_sa_bazom("localhost", "root", "", "biblioteka")
    kursor = veza.cursor()
    sql="""CREATE TABLE IF NOT EXISTS `CLAN` (
            `SIFC` integer  NOT NULL ,
            `IME` varchar(50)  NOT NULL ,
            `PREZIME` varchar(50)  NOT NULL ,
            `ADRESA` varchar(50)  NOT NULL ,
            `KONTAKT` varchar(15)  NOT NULL ,
            PRIMARY KEY (`SIFC`)
        )"""
    kursor.execute(sql)
    veza.commit()
    kursor.close()
    veza.close()
except mysql.connector.Error as e:
    if e.errno == errorcode.ER_TABLE_EXISTS_ERROR:
        print("Neuspeh! Tabela postoji.")
    else:
        print("SQL greška:", e)
except Exception as e:
    print("Došlo je do greške:", e)
else:
    print("Tabela je napravljena.")


