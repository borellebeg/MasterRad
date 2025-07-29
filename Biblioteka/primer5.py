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
        "with pom as ( "
            "SELECT SIFC , SIFK FROM drzi "
            "UNION "
            "SELECT SIFC , SIFK FROM pozajmica "
         ") SELECT SIFC , COUNT(SIFK) "
         "FROM pom "
         "GROUP BY SIFC "
        "ORDER BY 2 DESC "
    )
    kursor.execute(sql)
    rezultati=kursor.fetchmany(size=3)
    i=1
    if(len(rezultati)>0):
        for r in rezultati:
            print(str(i)+".", r[0],r[1])
            i+=1
    rezultati=kursor.fetchall()
    if(len(rezultati)>0):
        for r in rezultati:
            print(r[0], end=" ")
        print("")
    kursor.close()
    veza.close()
except mysql.connector.Error as sql_err:
    print("SQL greška:", sql_err)

except Exception as e:
    print("Došlo je do greške:", e)


