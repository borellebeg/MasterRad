
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
    sql = "SHOW TABLES"
    kursor.execute(sql)
    rezultati=kursor.fetchall()
    if(len(rezultati)==0):
        print("Nema tabela u bazi podataka")
    else:
        print("Tabele u bazi Biblioteka su: ")
        for r in rezultati:
            print(r[0], end=" ")
        print("")
    kursor.close()
    veza.close()
except mysql.connector.Error as sql_err:
    print("SQL greška:", sql_err)

except Exception as e:
    print("Došlo je do greške:", e)


