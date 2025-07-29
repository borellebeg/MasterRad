import mysql.connector
from mysql.connector import errorcode

def povezivanje_sa_bazom(hname, uname, upass, dbname):
    bp = mysql.connector.connect(
        host = hname,
        user = uname,
        password = upass,
        database = dbname)
    return bp

def slobodna_sifc(kursor):
    sql = (
            "SELECT MAX(SIFC) "
            "FROM clan "
    )
    try:
        kursor.execute(sql)
        rezultati=kursor.fetchall()
        return int(rezultati[0][0]) +1
    except mysql.connector.Error as e:
        print(e.msg)
try:
    
    veza=povezivanje_sa_bazom("localhost", "root", "", "biblioteka")
    kursor = veza.cursor()
    print(slobodna_sifc(kursor))
    kursor.close()
    veza.close()
except mysql.connector.Error as sql_err:
    print("SQL greška:", sql_err)

except Exception as e:
    print("Došlo je do greške:", e)


