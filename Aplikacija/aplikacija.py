import tkinter as tk
import subprocess
from tkinter import *
from datetime import *
from stranice import *

class Aplikacija(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        window = tk.Frame(self)
        window.pack()
        self.geometry('+%d+%d'%(20,20))
        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)
        
        self.frames = {}
        for s in (f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16):
            frame = s(window, self)
            self.frames[s] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(f1)
        self.title("Analizator sekvenci")

    
        meni = Menu(self.master)
        self.config(menu=meni)
        
        datMeni = Menu(meni)
        datMeni.add_command(label="Novo poređenje", command=self.novoPoredjenje)
        datMeni.add_command(label="Otvori konfiguraciju", command=self.otvori)
        datMeni.add_command(label="Sačuvaj konfiguraciju", command=self.sacuvajKonfiguraciju)
        datMeni.add_command(label="Otvori izveštaj", command=self.otvoriIzvestaj)
        meni.add_cascade(label="Datoteka", menu=datMeni)

        bazaMeni = Menu(meni)
        bazaMeni.add_command(label="Unos soja virusa", command=self.unosSoja)
        bazaMeni.add_command(label="Unos uzorka", command=self.unosUzorka)
        bazaMeni.add_command(label="Ažuriranje soja virusa", command=self.azuriranjeSoja)
        bazaMeni.add_command(label="Ažuriranje uzorka", command=self.azuriranjeUzorka)
        bazaMeni.add_command(label="Brisanje soja virusa", command=self.brisanjeSoja)
        bazaMeni.add_command(label="Brisanje uzorka", command=self.brisanjeUzorka)
        meni.add_cascade(label="Baza", menu=bazaMeni)

        pretragaMeni = Menu(meni)
        pretragaMeni.add_command(label="Pretraga sojeva", command=self.pretragaSojeva)
        pretragaMeni.add_command(label="Pretraga uzoraka", command=self.pretragaUzoraka)
        pretragaMeni.add_command(label="Napredna pretraga", command=self.naprednaPretraga)
        meni.add_cascade(label="Pretraga", menu=pretragaMeni)

        pomocMeni = Menu(meni)
        pomocMeni.add_command(label="O aplikaciji", command=self.oAplikaciji)
        pomocMeni.add_command(label="Pomoć", command=self.pomoc)
        meni.add_cascade(label="Pomoć", menu=pomocMeni)
    def pocetna(self):
        self.show_frame(f1)   
    def novoPoredjenje(self):
        self.show_frame(f1)
        opcija = 1
        self.title("Novo poređenje")
        #resetuje sve elemente prvog frejma
        f=self.frames[f1]
        if len(f.ktekst1.get())!=0:
            f.ktekst1.delete("0","end")
        if len(f.tekst1.get("1.0","end-1c"))!=0:
            f.tekst1.delete("1.0","end-1c")
        f.f1labelg.config(text = "")
        f.rb1.select()
        f.rb2.deselect()
        f.rb3.deselect()
        
    def otvori(self):
        #prikazuje konfiguraciju sacuvanu u fajlu ka kome se putanja unosi.
        self.show_frame(f2)
        self.title("Otvori konfiguraciju")
        
    def otvorikonf(self):
        f=self.frames[f2]
        adresa=f.ktekst1.get()
        u = open(adresa, "r")
        ulaz = u.read()
        u.close()
        l=ulaz.split(";")
        self.novoPoredjenje()
        opcija=int(l[0])
        f=self.frames[f1]
        f.tekst1.insert(INSERT, l[1][1:])
        f.ktekst1.insert(INSERT,l[2][1:])
        if opcija==1:
            f.rb1.select()
        elif opcija==2:
            f.rb2.select()
        else:
            f.rb3.select()
            
    def sacuvajKonfiguraciju(self):
        self.show_frame(f3)
        self.title("Sačuvaj konfiguraciju")
        
    def sacuvajkonf(self):
        #cuva konfiguraciju na zadatoj adresi
        f=self.frames[f3]
        adresa=f.ktekst1.get()
        i = open(adresa, "w")
        opc=self.frames[f1].int1.get()
        if opc==1:
            i.write("1;\n")
        elif opc==2:
            i.write("2;\n")
        else:
            i.write("3;\n")
        i.write(self.frames[f1].tekst1.get("1.0","end-1c")+";\n")
        i.write(self.frames[f1].ktekst1.get())
        i.close()
        self.show_frame(f1)
        self.frames[f1].f1labelg.config(text = "Konfiguracija je uspešno sačuvana.")
    def sacuvajrez(self,adresa):
        if len(adresa)==0:
            self.frames[f1].f1labelg.config(text = "Nije navedeno ime za čuvanje rezultata.")
        else:
            i = open(adresa, "w")
            t1 = open("aligned.fasta", "r")
            t2 = open("output.distmat", "r")
            t3 = open("stablo.nwk", "r")
            i.write("Poravnanje: \n"+t1.read()+";\nMatrica slicnosti: \n"+t2.read()+";\nFilogenetsko stablo:\n"+t3.read())
            t1.close()
            t2.close()
            t3.close()
            i.close()
            self.frames[f1].f1labelg.config(text = "Rezultat je uspešno sačuvan.")
    def otvoriIzvestaj(self):
        self.show_frame(f4)
    def otvorirez(self):
        f=self.frames[f4]
        adresa=f.ktekst1.get()
        u = open(adresa, "r")
        ulaz = u.read()
        u.close()
        l=ulaz.split(";")
        p='\n'.join(((l[0].split("\n"))[1:]))
        q='\n'.join(((l[1].split("\n"))[2:]))
        r='\n'.join(((l[2].split("\n"))[2:]))
        self.novoPoredjenje()
        rez = tk.Toplevel(self)
        rez.minsize(550, 650)
        rez.title("Rezultat poravnanja i poređenja")
        rez.geometry("+%d+%d" % (570, 20))
        l1 = Label(rez, text="Poravnanje sekvenci: (format fasta)")
        l1.place(x=20, y=15)
        t1 = tk.scrolledtext.ScrolledText(rez, height = 6, width = 60, wrap="none")
        t1.place(x=25,y=40)
        t1.insert(INSERT, p)
        t1.config(state='disabled')
        l2 = Label(rez, text="Matrica sličnosti (%): ")
        l2.place(x=20, y=145)
        t2 = tk.scrolledtext.ScrolledText(rez, height = 6, width = 60, wrap="none")
        t2.place(x=25,y=170)
        t2.insert(INSERT, q)
        t2.config(state='disabled')
        i = open("phylopom.nwk", "w")
        i.write(r+";")
        i.close()
        tree = Phylo.read("phylopom.nwk", "newick")
        fig = plt.figure(figsize=(5,5), dpi=100)
        axes = fig.add_subplot(1,1,1)
        
        Phylo.draw(tree, axes=axes,do_show=False)
        axes.set_xlabel("evolutivna udaljenost")
        axes.set_ylabel("uzorci")
        plt.savefig('filor.png')
        img = tk.PhotoImage(file="./filor.png")
        l3 = Label(rez, text="Filogenetsko stablo: ")
        l3.place(x=20, y=275)
        image_window = ScrollableImage(rez, image=img, scrollbarwidth=6, width=500, height=300)
        image_window.place(x=25,y=300)
        rezdugme1 = tk.Button(rez, text="Zatvori", command=rez.destroy)
        rezdugme1.place(x=480, y=610)
    def unosSoja(self):
        f=self.frames[f6]
        f.f6labelg.config(text="")
        self.title("Unos soja virusa")
        self.show_frame(f6)
        
    def unesiSoj(self):
        f=self.frames[f6]
        f.f6labelg.config(text="")
        kolone = f.kolone
        unos = [e.get().strip() for e in f.f6entry]
        
        if not unos[0]:
            f.f6labelg.config(text="Greška: polje 'pango' je obavezno.")
            return None
        vrednosti = []

        for i, t in enumerate(unos):
            kolona = kolone[i]
            
            if not t:
                vrednosti.append("NULL")
                continue

            if kolona == "mesec_prvog_uzorkovanja":
                try:
                    mesec = int(t)
                    if not (1 <= mesec and mesec <= 12):
                        f.f6labelg.config(text="Greška: mesec mora biti između 1 i 12")
                        return None
                    vrednosti.append(str(mesec))
                except ValueError:
                    f.f6labelg.config(text="Greška: mesec mora biti broj")
                    return None

            elif kolona == "godina_prvog_uzorkovanja":
                try:
                    godina = int(t)
                    if godina < 2019:
                        f.f6labelg.config(text="Greška: godina mora biti 2019. ili kasnije.")
                        return None
                    vrednosti.append(str(godina))
                except ValueError:
                    f.f6labelg.config(text="Greška: godina mora biti broj.")
                    return None

            elif kolona == "datum_oznacavanja":
                try:
                    datum = datetime.strptime(t, "%d.%m.%Y")
                    vrednosti.append(f"'{datum.strftime('%Y-%m-%d')}'")
                except ValueError:
                    f.f6labelg.config(text="Greška: datum mora biti u formatu dd.mm.yyyy.")
                    return None

            else:
                vrednosti.append(f"'{t}'")

        kolone_sql = ", ".join(kolone)
        vrednosti_sql = ", ".join(vrednosti)
        upit = f"INSERT INTO soj_virusa ({kolone_sql}) VALUES ({vrednosti_sql});"
        try:
            baza = povezivanje_sa_bazom("localhost", "root", "", "baza")
            kursor = baza.cursor()
            kursor.execute(upit)
            baza.commit()
            f.f6labelg.config(text=f"Unos soja virusa je uspešan.")
        except mysql.connector.Error as err:
            f.f6labelg.config(text=err)
        except Exception as e:
            f.f6labelg.config(text=e)
    def unosUzorka(self):
        f=self.frames[f7]
        self.title("Unos uzorka virusa")
        f.f7labelg.config(text="")
        self.show_frame(f7)
    
    def unesiUzorak(self):
        f=self.frames[f7]
        f.f7labelg.config(text="")
        kolone = f.kolone
        unosi = [e.get().strip() for e in f.f7entry]

        kompresovano=""
        sql_kolone = [k if "(" not in k else "sekvenca" for k in kolone]
        vrednosti = []
        for i, vrednost in enumerate(unosi):
            naziv_kolone = sql_kolone[i]
            if naziv_kolone in ["pristupni_id", "pango", "sekvenca"]:
                if not vrednost:
                    f.f7labelg.config(text=f"Polje '{naziv_kolone}' je obavezno.")
                    return None
                elif naziv_kolone == "sekvenca":
                    ulaz = open(vrednost, "r")
                    seq = ulaz.read()
                    seq = seq[seq.find('\n'):]
                    seq = seq.replace('\n', '')
                    seq1= seq.encode()
                    kompresovano = zlib.compress(seq1)
                else:
                    vrednosti.append(f"{vrednost}")
            else:
                if not vrednost:
                    vrednosti.append("NULL")
                elif naziv_kolone == "duzina" and int(vrednost)<0:
                    f.f7labelg.config(text=f"Dužina mora biti prirodan broj")
                    return None
                elif naziv_kolone == "datum_uzorkovanja":
                    try:
                        datum = datetime.strptime(vrednost, "%d.%m.%Y").strftime("%Y-%m-%d")
                    except ValueError:
                        f.f7labelg.config(text="Datum mora biti u formatu dd.mm.gggg")
                        return None
                    vrednosti.append(f"{datum}")
                else:
                    vrednosti.append(f"{vrednost}")

        sql = "INSERT INTO uzorak (pristupni_id, pango, vlasnik, opis, duzina, lokacija_uzorkovanja, datum_uzorkovanja, kompletnost_sekvence, sekvenca) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (vrednosti[0].strip(), vrednosti[1].strip(), vrednosti[2].strip(), vrednosti[3].strip(), vrednosti[4].strip(), vrednosti[5].strip(), vrednosti[6].strip(), vrednosti[7].strip(), kompresovano)
        
        try:
           baza = povezivanje_sa_bazom("localhost", "root", "", "baza")
           kursor = baza.cursor()
           kursor.execute(sql, val)
           baza.commit()
           f.f7labelg.config(text=f"Unos uzorka je uspešan.")
        except mysql.connector.Error as err:
            f.f7labelg.config(text=err)
        except Exception as e:
            f.f7labelg.config(text=e)

    def azuriranjeSoja(self):
        self.title("Ažuriranje soja virusa")
        f=self.frames[f8]
        f.f8labelg.config(text="")
        self.show_frame(f8)
        
    def azurirajSoj(self):
        f = self.frames[f8]
        f.f8labelg.config(text="")
        kolone = f.kolone
        unos = [e.get().strip() for e in f.f8entry]

        if not unos[0]:
            f.f8labelg.config(text="Greška: polje 'pango' je obavezno.")
            return None

        vrednosti = []
        pango_vrednost = unos[0]

        for i, t in enumerate(unos):
            kolona = kolone[i]

            if t:
                if kolona == "mesec_prvog_uzorkovanja":
                    try:
                        mesec = int(t)
                        if not (1 <= mesec <= 12):
                            f.f8labelg.config(text="Greška: mesec mora biti između 1 i 12")
                            return None
                        vrednosti.append(f"{kolona}={mesec}")
                    except ValueError:
                        f.f8labelg.config(text="Greška: mesec mora biti broj")
                        return None

                elif kolona == "godina_prvog_uzorkovanja":
                    try:
                        godina = int(t)
                        if godina < 2019:
                            f.f8labelg.config(text="Greška: godina mora biti 2019. ili kasnije.")
                            return None
                        vrednosti.append(f"{kolona}={godina}")
                    except ValueError:
                        f.f8labelg.config(text="Greška: godina mora biti broj.")
                        return None

                elif kolona == "datum_oznacavanja":
                    try:
                        datum = datetime.strptime(t, "%d.%m.%Y")
                        vrednosti.append(f"{kolona}='{datum.strftime('%Y-%m-%d')}'")
                    except ValueError:
                        f.f8labelg.config(text="Greška: datum mora biti u formatu dd.mm.yyyy.")
                        return None

                else:
                    vrednosti.append(f"{kolona}='{t}'")

        set_sql = ", ".join(vrednosti)
        upit = f"UPDATE soj_virusa SET {set_sql} WHERE pango='{pango_vrednost}';"
        
        try:
            baza = povezivanje_sa_bazom("localhost", "root", "", "baza")
            kursor = baza.cursor()
            kursor.execute(upit)
            baza.commit()
            if kursor.rowcount == 0:
                f.f8labelg.config(text="Nijedan red nije ažuriran (pango ne postoji?).")
            else:
                f.f8labelg.config(text="Ažuriranje soja virusa je uspešno.")
        except mysql.connector.Error as err:
            f.f8labelg.config(text=err)
        except Exception as e:
            f.f8labelg.config(text=e)

        
        
    def azuriranjeUzorka(self):
        self.title("Ažuriranje uzorka virusa")
        self.show_frame(f9)
        
    def azurirajUzorak(self):
        f = self.frames[f9]
        f.f9labelg.config(text="")
        kolone = f.kolone
        unosi = [e.get().strip() for e in f.f9entry]

        kompresovano = None
        sql_kolone = [k if "(" not in k else "sekvenca" for k in kolone]
        vrednosti = {}
        
        if not unosi[0]:
            f.f9labelg.config(text="Polje 'pristupni_id' je obavezno.")
            return None
        pristupni_id = unosi[0]

        for i, vrednost in enumerate(unosi):
            naziv_kolone = sql_kolone[i]

            if vrednost:
                if naziv_kolone == "sekvenca":
                    try:
                        with open(vrednost, "r") as ulaz:
                            seq = ulaz.read()
                        seq = seq[seq.find('\n'):]
                        seq = seq.replace('\n', '')
                        seq1 = seq.encode()
                        kompresovano = zlib.compress(seq1)
                        vrednosti[naziv_kolone] = kompresovano
                    except Exception:
                        f.f9labelg.config(text="Greška pri čitanju sekvence.")
                        return None

                elif naziv_kolone == "duzina":
                    try:
                        duzina = int(vrednost)
                        if duzina < 0:
                            f.f9labelg.config(text="Dužina mora biti prirodan broj.")
                            return None
                        vrednosti[naziv_kolone] = duzina
                    except ValueError:
                        f.f9labelg.config(text="Dužina mora biti broj.")
                        return None

                elif naziv_kolone == "datum_uzorkovanja":
                    try:
                        datum = datetime.strptime(vrednost, "%d.%m.%Y").strftime("%Y-%m-%d")
                        vrednosti[naziv_kolone] = datum
                    except ValueError:
                        f.f9labelg.config(text="Datum mora biti u formatu dd.mm.gggg.")
                        return None

                else:
                    vrednosti[naziv_kolone] = vrednost
        
        set_delovi = [f"{kol}= %s" for kol in vrednosti if kol != "pristupni_id"]
        sql = f"UPDATE uzorak SET {', '.join(set_delovi)} WHERE pristupni_id = %s"

        val = tuple(vrednosti[k] for k in vrednosti if k != "pristupni_id") + (pristupni_id,)


        try:
            baza = povezivanje_sa_bazom("localhost", "root", "", "baza")
            kursor = baza.cursor()
            kursor.execute(sql, val)
            baza.commit()
            if kursor.rowcount == 0:
                f.f9labelg.config(text="Nijedan red nije ažuriran (pristupni_id ne postoji?).")
            else:
                f.f9labelg.config(text="Ažuriranje uzorka je uspešno.")
        except mysql.connector.Error as err:
            f.f9labelg.config(text=err)
        except Exception as e:
            f.f9labelg.config(text=e)


        
    def brisanjeSoja(self):
        self.title("Brisanje soja virusa")
        self.show_frame(f10)
        
    def obrisiSoj(self):
        f=self.frames[f10]
        f.f10labelg.config(text="")
        try:
            pango = f.epango.get()
            baza = povezivanje_sa_bazom("localhost", "root", "", "baza")
            kursor = baza.cursor()
            sql = "DELETE FROM uzorak WHERE pango = %s"
            kursor.execute(sql, (pango,))        
            sql = "DELETE FROM soj_virusa WHERE pango = %s"
            kursor.execute(sql, (pango,))
            baza.commit()
            if kursor.rowcount == 0:
                f.f10labelg.config(text=f"Nije obrisan soj virusa (pango ne postoji?)")
            else:
                f.f10labelg.config(text=f"Brisanje soja virusa je uspešno.")
            
        except mysql.connector.Error as err:
            f.f10labelg.config(text=f"SQL greška: {err}")
        except Exception as e:
            f.f10labelg.config(text=e)
        
    def brisanjeUzorka(self):
        self.title("Brisanje uzorka virusa")
        self.show_frame(f11)

    def obrisiUzorak(self):
        f=self.frames[f11]
        f.f11labelg.config(text="")
        pid = f.epristupni.get()
        try:
            baza = povezivanje_sa_bazom("localhost", "root", "", "baza")
            kursor = baza.cursor()
            sql = "DELETE FROM uzorak WHERE pristupni_id = %s"
            kursor.execute(sql, (pid,))        
            baza.commit()
            if kursor.rowcount == 0:
                f.f11labelg.config(text=f"Nije obrisan uzorak (pristupni_id ne postoji?)")
            else:
                f.f11labelg.config(text=f"Brisanje uzorka je uspešno.")
        except mysql.connector.Error as err:
            f.f11labelg.config(text=f"SQL greška: {err}")
        except Exception as e:
            f.f11labelg.config(text=e)

    def pretragaSojeva(self):
        self.title("Pretraga sojeva virusa")
        self.show_frame(f12)
        
    def pretraziSoj(self):
        f=self.frames[f12]
        f.f12labelg.config(text="")
        rez = tk.Toplevel(self)
        rez.minsize(550, 300)
        rez.title("Rezultat pretrage")
        rez.geometry("+%d+%d" % (570, 20))
        l1 = Label(rez, text="Rezultat pretrage: ")
        l1.place(x=20, y=15)
        t1 = tk.scrolledtext.ScrolledText(rez, height = 6, width = 60, wrap="none")
        t1.place(x=25,y=40)

        
        vrednosti = [e.get().strip() for e in f.f12entry]

        izbor_kolona = []
        uslovi = []

        for kolona, vrednost in zip(f.kolone, vrednosti):
            if vrednost == "*":
                izbor_kolona.append(kolona)  
            elif vrednost:
                izbor_kolona.append(kolona)
                if kolona == "datum_oznacavanja":
                    try:
                        datum = datetime.strptime(vrednost, "%d.%m.%Y").strftime("%Y-%m-%d")
                        uslovi.append(f"{kolona} = '{datum}'")
                    except ValueError:
                        f.f12labelg.config(text=f"Greška u formatu datuma: {vrednost}")
                        return
                elif kolona in ["mesec_prvog_uzorkovanja", "godina_prvog_uzorkovanja"]:
                    uslovi.append(f"{kolona} = {int(vrednost)}")
                else:
                    uslovi.append(f"{kolona} = '{vrednost}'")
        if not izbor_kolona:
            izbor_kolona.append("*")
        sql = f"SELECT {', '.join(izbor_kolona)} FROM soj_virusa"
        if uslovi:
            sql += " WHERE " + " AND ".join(uslovi)
        
        try:
            baza = povezivanje_sa_bazom("localhost", "root", "", "baza")
            kursor = baza.cursor()
            kursor.execute(sql)
            rezultat = kursor.fetchall()

            tekst = "\t".join([desc[0] for desc in kursor.description]) + "\n"

            for red in rezultat:
                tekst += "\t".join(str(vrednost) if vrednost is not None else "" for vrednost in red) + "\n"

            if not rezultat:
                tekst += "Nema rezultata\n"
            t1.insert(INSERT, tekst)

            

        except mysql.connector.Error as err:
            f.f12labelg.config(text=f"SQL greška: {err}")
        except Exception as e:
            f.f12labelg.config(text=e)
        
        t1.config(state='disabled')

    def pretragaUzoraka(self):
        self.title("Pretraga uzoraka virusa")
        self.show_frame(f13)
    def pretraziUzorak(self):
        f = self.frames[f13]
        f.f13labelg.config(text="")
        rez = tk.Toplevel(self)
        rez.minsize(550, 300)
        rez.title("Rezultat pretrage")
        rez.geometry("+%d+%d" % (570, 20))

        l1 = Label(rez, text="Rezultat pretrage: ")
        l1.place(x=20, y=15)
        t1 = tk.scrolledtext.ScrolledText(rez, height=6, width=60, wrap="none")
        t1.place(x=25, y=40)

        vrednosti = [e.get().strip() for e in f.f13entry]

        izbor_kolona = []
        uslovi = []

        for kolona, vrednost in zip(f.kolone, vrednosti):
            if vrednost == "*":
                izbor_kolona.append(kolona)
            elif vrednost:
                izbor_kolona.append(kolona)

                if kolona == "datum_uzorkovanja":
                    try:
                        datum = datetime.strptime(vrednost, "%d.%m.%Y").strftime("%Y-%m-%d")
                        uslovi.append(f"{kolona} = '{datum}'")
                    except ValueError:
                        f.f13labelg.config(text=f"Greška u formatu datuma: {vrednost}")
                        return None
                elif kolona == "duzina":
                    try:
                        duzina = int(vrednost)
                        if duzina < 0:
                            f.f13labelg.config(text="Dužina mora biti nenegativan broj.")
                            return None
                        uslovi.append(f"{kolona} = {duzina}")
                    except ValueError:
                        f.f13labelg.config(text="Greška: dužina mora biti broj.")
                        return None
                else:
                    uslovi.append(f"{kolona} = '{vrednost}'")

        if not izbor_kolona:
            izbor_kolona.append("*")

        sql = f"SELECT {', '.join(izbor_kolona)} FROM uzorak"
        if uslovi:
            sql += " WHERE " + " AND ".join(uslovi)

        try:
            baza = povezivanje_sa_bazom("localhost", "root", "", "baza")
            kursor = baza.cursor()
            kursor.execute(sql)
            rezultat = kursor.fetchall()

            tekst = "\t".join([desc[0] for desc in kursor.description]) + "\n"

            for red in rezultat:
                tekst += "\t".join(str(vrednost) if vrednost is not None else "" for vrednost in red) + "\n"

            if not rezultat:
                tekst += "Nema rezultata\n"

            t1.insert(INSERT, tekst)

        except mysql.connector.Error as err:
            f.f13labelg.config(text=f"SQL greška: {err}")
        except Exception as e:
            f.f13labelg.config(text=e)

        t1.config(state='disabled')

    
    def naprednaPretraga(self):
        self.title("Napredna pretraga")
        self.show_frame(f14)

    def pretraziNapredno(self):
        f=self.frames[f14]
        sql=f.t1.get("1.0","end-1c")
        f.f14labelg.config(text="")
        rez = tk.Toplevel(self)
        rez.minsize(550, 300)
        rez.title("Rezultat pretrage")
        rez.geometry("+%d+%d" % (570, 20))
        l1 = Label(rez, text="Rezultat pretrage: ")
        l1.place(x=20, y=15)
        t1 = tk.scrolledtext.ScrolledText(rez, height = 6, width = 60, wrap="none")
        t1.place(x=25,y=40)

        try:
            baza = povezivanje_sa_bazom("localhost", "root", "", "baza")
            kursor = baza.cursor()
            kursor.execute(sql)
            rezultat = kursor.fetchall()

            tekst = "\t".join([desc[0] for desc in kursor.description]) + "\n"
            for red in rezultat:
                tekst += "\t".join(str(vrednost) if vrednost is not None else "" for vrednost in red) + "\n"
            if not rezultat:
                tekst += "Nema rezultata\n"
            t1.insert(INSERT, tekst)

        except mysql.connector.Error as err:
            f.f14labelg.config(text=f"SQL greška: {err}")
        except Exception as e:
            f.f14labelg.config(text=e)

        
    def oAplikaciji(self):
        self.title("O aplikaciji")
        self.show_frame(f16)
    def pomoc(self):
        self.title("Pomoć")
        self.show_frame(f15)
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
    def izdvoji(self, t, s):
        linije = t.strip().splitlines()
        n = int(linije[0].strip())
        
        uzorci = []
        matrica = []
        
        for linija in linije[1:]:
            delovi = linija.split()
            uzorci.append(delovi[0])
            matrica.append(list(map(float, delovi[1:])))
        
        if s not in uzorci:
            return f"Uzorak {s} nije pronađen."
        i = uzorci.index(s)
        
        rezultat = [f"Uzorak {s}:"]
        for j, naziv in enumerate(uzorci):
            if j == i:
                continue
            procenat = matrica[i][j]
            rezultat.append(f"{procenat:.2f}% slicnosti sa uzorkom {naziv}")
        
        return "\n".join(rezultat)
    def zapocni(self):
        f=self.frames[f1]
        opc=f.int1.get()
        f.f1labelg.config(text = "")
        
        try:
            d1 = f.tekst1.get("1.0","end-1c").split("\n")
            d2 = f.ktekst1.get().split(" ")
            if opc==1:
                baza = povezivanje_sa_bazom("localhost", "root", "", "baza")
                kursor = baza.cursor()
                izlaz = open("unaligned.fasta", "w")
                if d2[0]!='':
                    d1+=d2
                if d1[0]=='' or len(d1)<3:
                    #ako nema dovoljno unetih oznaka uzoraka koriste se svi uzorci
                    #iz baze prvo vrsimo povezivanje sa bazom i citanje rezultata
                    sql = "SELECT pristupni_id, sekvenca FROM uzorak"
                    res = kursor.execute(sql)
                    podaci = kursor.fetchall()
                    konf=""
                    for p in podaci:
                        dec=zlib.decompress(p[1])
                        seq = dec.decode()
                        konf = konf + p[0]+"\n"
                        izlaz.write(">"+p[0]+"\n"+seq+"\n")
                    izlaz.close()
                    konf = konf[0:-1]
                    f.tekst1.insert(INSERT, konf)
                    
                else:
                    for u in d1:
                        sql = "SELECT pristupni_id, sekvenca FROM uzorak WHERE pristupni_id = '"+u+"'"
                        res = kursor.execute(sql)
                        uzorak = kursor.fetchall()
                        if uzorak:
                            dec=zlib.decompress(uzorak[0][1])
                            seq = dec.decode()
                            izlaz.write(">"+uzorak[0][0]+"\n"+seq+"\n")
                        else:
                            f.f1labelg.config(text = "Uzorak "+u+ " nije pronađen.\n Nakon provere pokušajte ponovo")
                            return -1
                izlaz.close()
            elif opc==2:
                #uzorci iz datoteka
                if len(d1)+len(d2)<3:
                    f.f1labelg.config(text = "Morate da unesete ime bar tri datoteke.")
                    return
                else:
                    izlaz = open("unaligned.fasta", "w")
                    if d2[0]!='':
                        seq = open(d2[1], "r").read()
                        seq = seq[seq.find('\n'):]
                        seq = seq.replace('\n', '')
                        izlaz.write(">"+d2[0]+"\n")
                        izlaz.write(seq+"\n")
                    for i in range(len(d1)):
                        if i%2==0:
                            izlaz.write(">"+d1[i]+"\n")
                        else:
                            seq = open(d1[i], "r").read()
                            seq = seq[seq.find('\n'):]
                            seq = seq.replace('\n', '')
                            izlaz.write(seq+"\n") 
                    izlaz.close()
            else:
                #unos uzoraka rucno linija po linija
                if (len(d1)+len(d2))/2>2:
                    izlaz = open("unaligned.fasta", "w")
                    if(len(d2)==2):
                        izlaz.write(">"+d2[0]+"\n"+d2[1]+"\n")
                    for i in range(len(d1)):
                        if i%2==0:
                            izlaz.write(">"+d1[i]+"\n")
                        else:
                            izlaz.write(d1[i]+"\n")
                    izlaz.close()
                else:
                    f.f1labelg.config(text = "Nema dovoljno uzoraka")
                    return
                
            in_file = "unaligned.fasta"
            out_file = "aligned.fasta"
            clustalomega_cline = ClustalOmegaCommandline(r"C:\Users\Mg\Desktop\FINALPROJEKAT\clustalo.exe", infile=in_file,  distmat_full=True, percentid=True, distmat_out="output.distmat", guidetree_out="filtree.dnd", verbose=True, outfmt="fasta", outfile=out_file, outputorder="tree-order", seqtype="rna", residuenumber=True, threads=12, force=True)
            stdout, stderr = clustalomega_cline()
            
            rez = tk.Toplevel(self)
            rez.minsize(550, 650)
            rez.title("Rezultat poravnanja i poređenja")
            rez.geometry("+%d+%d" % (570, 20))
            l1 = Label(rez, text="Poravnanje sekvenci: (format FASTA)")
            l1.place(x=20, y=15)
            t1 = tk.scrolledtext.ScrolledText(rez, height = 6, width = 60, wrap="none")
            
            t1.place(x=25,y=40)
            u = open("aligned.fasta", "r")
            t1.insert(INSERT, u.read())
            u.close()
            t1.config(state='disabled')
            l2 = Label(rez, text="Matrica sličnosti (%): ")
            l2.place(x=20, y=145)
            t2 = tk.scrolledtext.ScrolledText(rez, height = 6, width = 60, wrap="none")
            t2.place(x=25,y=170)
            u = open("output.distmat", "r")
            matrica_slicnosti=u.read()
            t2.insert(INSERT, matrica_slicnosti)
            
            u.close()
            t2.config(state='disabled')          


            output_tree = "stablo.nwk"
            try:
                subprocess.run(
                    ["FastTree", "-nt", "aligned.fasta"],
                    check=True,
                    stdout=open(output_tree, "w")
                )
            except FileNotFoundError:
                f.f1labelg.config(text = "FastTree nije pronađen.")
                return
            except subprocess.CalledProcessError as e:
                f.f1labelg.config(text = f"Greška pri pokretanju programa FastTree: {e}")
                return



	    
            tree = Phylo.read(output_tree, "newick")
            fig = plt.figure(figsize=(5,5), dpi=100)
            axes = fig.add_subplot(1,1,1)
            
            Phylo.draw(tree, axes=axes,do_show=False)
            axes.set_xlabel("evolutivna udaljenost")
            axes.set_ylabel("uzorci")
            
            plt.savefig('filo.png')
            img = tk.PhotoImage(file="./filo.png")
            l3 = Label(rez, text="Filogenetsko stablo: ")
            l3.place(x=20, y=275)
            image_window = ScrollableImage(rez, image=img, scrollbarwidth=6, width=500, height=300)
            image_window.place(x=25,y=300)
            ktekst1 = Entry(rez, width = 63)
            ktekst1.place(x=25, y=615)
            rezdugme1 = tk.Button(rez, text="Sačuvaj", command=lambda: self.sacuvajrez(ktekst1.get()))
            rezdugme1.place(x=420, y=610)
            rezdugme2 = tk.Button(rez, text="Poništi", command=rez.destroy)
            rezdugme2.place(x=480, y=610)
            if d2[0]!='':
                rez = tk.Toplevel(self)
                rez.minsize(530, 200)
                rez.title("Sličnost sa istaknutim uzorkom")
                rez.geometry("+%d+%d" % (20, 360))
                l1 = Label(rez, text="Podaci o sličnosti: ")
                l1.place(x=20, y=15)
                t1 = tk.scrolledtext.ScrolledText(rez, height = 6, width = 60, wrap="none")
                t1.place(x=25,y=40)
                t1.insert(INSERT, self.izdvoji(matrica_slicnosti, d2[0]))
                
        except Exception as e:             
            x=str(e).find("(")
            f.f1labelg.config(text = str(e)[:x]+"\n"+str(e)[x:mat.ceil((x+len(str(e)))/2)+1]+"\n"+str(e)[mat.ceil((x+len(str(e)))/2+1):])
