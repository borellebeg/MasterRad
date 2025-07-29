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
    print("Unesite podatke o osobi u formatu IME, PREZIME, ADRESA, KONTAKT razdvojene zarezom")

    ulaz = input().split(",")
    podaci = (2307, ulaz[0].strip(), ulaz[1].strip(), ulaz[2].strip(), ulaz[3].strip())

    kursor.execute(sql, podaci)
    veza.commit()
    kursor.close()
    veza.close()
except mysql.connector.Error as sql_err:
    print("SQL greška:", sql_err)

except Exception as e:
    print("Došlo je do greške:", e)
else:
    print("Unos je uspesan!")


