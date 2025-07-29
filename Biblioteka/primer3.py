
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
    sql = (
      "INSERT INTO clan (SIFC, IME, PREZIME, ADRESA, KONTAKT) "
      "VALUES (%s, %s, %s, %s, %s)"
    )
    podaci = []
    i = 2308
    with open('podaci.txt', 'r', encoding='utf-8') as fajl:
        for linija in fajl:
            linija= str(i)+","+linija
            elementi = [l.strip()
                        for l in linija.strip().split(',')]
            if len(elementi) == 5:
                i+=1
                podaci.append(tuple(elementi))
    kursor.executemany(sql, podaci)
    veza.commit()
    kursor.close()
    veza.close()
except mysql.connector.Error as sql_err:
    print("SQL greška:", sql_err)

except Exception as e:
    print("Došlo je do greške:", e)




