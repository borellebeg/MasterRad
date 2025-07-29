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
    sql = "DROP TABLE uzorak"
    kursor.execute(sql)
    sql = "DROP TABLE soj_virusa"
    kursor.execute(sql)
    sql = "CREATE TABLE soj_virusa ("
    sql+= "pango VARCHAR(30) NOT NULL,"
    sql+= "who VARCHAR(30),"
    sql+= "gisaid VARCHAR(30),"
    sql+= "nextstrain VARCHAR(30),"
    sql+= "zemlja_prvog_uzorkovanja VARCHAR(50),"
    sql+= "kontinent_prvog_uzorkovanja VARCHAR(100) NOT NULL,"
    sql+= "mesec_prvog_uzorkovanja INT,"
    sql+= "godina_prvog_uzorkovanja INT,"
    sql+= "datum_oznacavanja DATE,"
    sql+= "PRIMARY KEY (pango)"
    sql+= ") ENGINE=InnoDB"
    kursor.execute(sql)
    sql = "CREATE TABLE uzorak ("
    sql+= "pristupni_id VARCHAR(30) NOT NULL,"
    sql+= "pango VARCHAR(30) NOT NULL,"
    sql+= "vlasnik VARCHAR(100),"
    sql+= "opis VARCHAR(1000),"
    sql+= "duzina INT,"
    sql+= "lokacija_uzorkovanja VARCHAR(30),"
    sql+= "datum_uzorkovanja DATE,"
    sql+= "kompletnost_sekvence VARCHAR(11),"
    sql+= "sekvenca VARBINARY(10000) NOT NULL,"
    sql+= "PRIMARY KEY (pristupni_id),"
    sql+= "FOREIGN KEY (pango) REFERENCES soj_virusa(pango)"
    sql+= ") ENGINE=InnoDB"
    kursor.execute(sql)
def ucitavanje_datoteka(direktorijum):
    datoteke = []
    for datoteka in glob.glob(direktorijum+ "/*.fasta"):
        datoteke.append(datoteka)
    return datoteke
def unos_podataka(baza, direktorijum, infodat, infouzor):
    info = open(infodat, "r")
    infou = open(infouzor, "r")
    varijante = info.read().split("\n")
    uzorci = infou.read().split("\n")
    datoteke = ucitavanje_datoteka(direktorijum)
    
    kursor = baza.cursor()
    for v in varijante: 
        l= v.split(";")
        d=l[8].split(".")
        l[8] = d[2]+"-"+d[1]+"-"+d[0]
        sql = "INSERT INTO soj_virusa (pango, who, gisaid, nextstrain, zemlja_prvog_uzorkovanja, kontinent_prvog_uzorkovanja, mesec_prvog_uzorkovanja, godina_prvog_uzorkovanja, datum_oznacavanja) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (l[0].strip(), l[1].strip(), l[2].strip(), l[3].strip(), l[4].strip(), l[5].strip(), l[6].strip(), l[7].strip(), l[8].strip())
        kursor.execute(sql, val)
        baza.commit()
        for datoteka in datoteke:
            print(datoteke)
            datotekapom = datoteka.split("\\")[-1]
            if datotekapom==(l[0].strip()+".fasta"):
                f = open(datoteka, "r")
                seq = f.read()
                imeuzorka = seq[1:seq.find(" ")]
                seq = seq[seq.find('\n'):]
                seq = seq.replace('\n', '')
                seq1= seq.encode()
                compressed = zlib.compress(seq1)
                for u in uzorci:
                    lu= u.split(";")
                    d=lu[6].split(".")
                    lu[6] = d[2]+"-"+d[1]+"-"+d[0]
                    if lu[1].strip()==l[0].strip():
                        sql = "INSERT INTO uzorak (pristupni_id, pango, vlasnik, opis, duzina, lokacija_uzorkovanja, datum_uzorkovanja, kompletnost_sekvence, sekvenca) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        val = (lu[0].strip(), lu[1].strip(), lu[2].strip(), lu[3].strip(), lu[4].strip(), lu[5].strip(), lu[6].strip(), lu[7].strip(), compressed)
                        kursor.execute(sql, val)
    baza.commit()    
def izlistaj(baza):
    kursor = baza.cursor()
    sql = "select v.pango, u.pristupni_id, sekvenca from soj_virusa v join uzorak u on v.pango = u.pango"
    kursor.execute(sql)
    myresult = kursor.fetchall()
    
    for x in myresult:
        seqC = zlib.decompress(x[2])
        seqC = seqC.decode()
        print(x[0]+" "+x[1]+ " "+str(len(seqC)))
try:
    baza=povezivanje_sa_bazom("localhost", "root", "", "baza")
    kreiranje_tabela(baza)
    unos_podataka(baza, "./UZORCI", "./varijante_virusa.txt", "./uzorak.txt")
    izlistaj(baza)
except mysql.connector.Error as sql_err:
    print("SQL greška:", sql_err)

except Exception as e:
    print("Došlo je do greške:", e)










