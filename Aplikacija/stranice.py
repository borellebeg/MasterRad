import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from PIL import ImageTk,Image
from database import *

class f1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        l1 = Label(self, text="Odaberite način poređenja: ")
        l1.place(x=20,y=10)
        self.int1 = tk.IntVar()
        self.rb1 = Radiobutton(self, text="uzorci iz baze", variable = self.int1, value=1)
        self.rb2 = Radiobutton(self, text="uzorci iz datoteka", variable = self.int1, value=2)
        self.rb3 = Radiobutton(self, text="unos uzoraka", variable = self.int1, value=3)
        self.rb1.select()
        self.rb2.deselect()
        self.rb3.deselect()
        self.rb1.place(x=20, y=25)
        self.rb2.place(x=120, y=25)
        self.rb3.place(x=240, y=25)
        
        
        self.tekst1 = scrolledtext.ScrolledText(self, height = 6, width = 60, wrap="none")
        self.tekst1.place(x=25,y=50)

        l2 = Label(self, text="Poređenje sa: (opciono)")
        l2.place(x=20, y=170)
        self.ktekst1 = Entry(self, width = 80)
        self.ktekst1.place(x=25, y=190)
        f1dugme1 = tk.Button(self, text="Započni", command=lambda: controller.zapocni())
        f1dugme1.place(x=455, y=220)
        self.f1labelg = Label(self, text="", fg='red')
        self.f1labelg.place(x=25, y=240)

class f2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        parent
        f2l1 = Label(self, text="Putanja ka konfiguraciji:")
        f2l1.place(x=20, y=170)
        self.ktekst1 = Entry(self, width = 80)
        self.ktekst1.place(x=25, y=190)
        f2dugme1 = tk.Button(self, text="Otvori", command=lambda: controller.otvorikonf())
        f2dugme1.place(x=455, y=220)
        self.f2labelg = Label(self, text="MILOS", fg='red')
        self.f2labelg.place(x=25, y=220)

class f3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        f3l1 = Label(self, text="Putanja ka konfiguraciji i ime fajla:")
        f3l1.place(x=20, y=170)
        self.ktekst1 = Entry(self, width = 80)
        self.ktekst1.place(x=25, y=190)
        f3dugme1 = tk.Button(self, text="Sačuvaj", command=lambda: controller.sacuvajkonf())
        f3dugme1.place(x=455, y=220)
        self.f3labelg = Label(self, text="MILOS", fg='red')
        self.f3labelg.place(x=25, y=220)
	
class f4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        f4l1 = Label(self, text="Putanja ka izveštaju i ime fajla:")
        f4l1.place(x=20, y=170)
        self.ktekst1 = Entry(self, width = 80)
        self.ktekst1.place(x=25, y=190)
        f4dugme1 = tk.Button(self, text="Otvori", command=lambda: controller.otvorirez())
        f4dugme1.place(x=455, y=220)
        self.f4labelg = Label(self, text="MILOS", fg='red')
        self.f4labelg.place(x=25, y=220)
        
        
class f5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #stranica za promenu radnog direktorijuma (za sledece verzije programa)
	
class f6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.kolone = ["pango", "who", "gisaid",
                  "nextstrain","zemlja_prvog_uzorkovanja",
                  "kontinent_prvog_uzorkovanja",
                  "mesec_prvog_uzorkovanja",
                  "godina_prvog_uzorkovanja",
                  "datum_oznacavanja"]
        self.f6entry = []
        for i, naziv in enumerate(self.kolone):
            lbl = tk.Label(self, text=naziv + ":", anchor="w")
            lbl.grid(row=i, column=0, sticky="w", padx=4, pady=2)
            entry = tk.Entry(self, width=40)
            entry.grid(row=i, column=1, padx=4, pady=2)
            self.f6entry.append(entry)
        self.f6labelg = tk.Label(self, text="",fg='red')
        self.f6labelg.grid(row=9, column=0, pady=2)
        f6dugme1 = tk.Button(self, text="Unesi", command=lambda: controller.unesiSoj())
        f6dugme1.grid(row=10, column=3, pady=2)

class f7(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.kolone = ["pristupni_id", "pango",
                       "vlasnik", "opis", "duzina",
                       "lokacija_uzorkovanja", "datum_uzorkovanja",
                       "kompletnost_sekvence", "sekvenca (putanja)"]
        self.f7entry = []
        for i, naziv in enumerate(self.kolone):
            lbl = tk.Label(self, text=naziv + ":", anchor="w")
            lbl.grid(row=i, column=0, sticky="w", padx=4, pady=2)
            entry = tk.Entry(self, width=40)
            entry.grid(row=i, column=1, padx=4, pady=2)
            self.f7entry.append(entry)
        self.f7labelg = tk.Label(self, text="",fg='red')
        self.f7labelg.grid(row=9, column=0, pady=2)
        f7dugme1 = tk.Button(self, text="Unesi", command=lambda: controller.unesiUzorak())
        f7dugme1.grid(row=10, column=3, pady=2)
	
class f8(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.kolone = ["pango", "who", "gisaid",
                  "nextstrain","zemlja_prvog_uzorkovanja",
                  "kontinent_prvog_uzorkovanja",
                  "mesec_prvog_uzorkovanja",
                  "godina_prvog_uzorkovanja",
                  "datum_oznacavanja"]
        self.f8entry = []
        for i, naziv in enumerate(self.kolone):
            lbl = tk.Label(self, text=naziv + ":", anchor="w")
            lbl.grid(row=i, column=0, sticky="w", padx=4, pady=2)
            entry = tk.Entry(self, width=40)
            entry.grid(row=i, column=1, padx=4, pady=2)
            self.f8entry.append(entry)
        self.f8labelg = tk.Label(self, text="",fg='red')
        self.f8labelg.grid(row=9, column=0, pady=2)
        f8dugme1 = tk.Button(self, text="Unesi", command=lambda: controller.azurirajSoj())
        f8dugme1.grid(row=10, column=3, pady=2)

class f9(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.kolone = ["pristupni_id", "pango",
                       "vlasnik", "opis", "duzina",
                       "lokacija_uzorkovanja", "datum_uzorkovanja",
                       "kompletnost_sekvence", "sekvenca (putanja)"]
        self.f9entry = []
        for i, naziv in enumerate(self.kolone):
            lbl = tk.Label(self, text=naziv + ":", anchor="w")
            lbl.grid(row=i, column=0, sticky="w", padx=4, pady=2)
            entry = tk.Entry(self, width=40)
            entry.grid(row=i, column=1, padx=4, pady=2)
            self.f9entry.append(entry)
        self.f9labelg = tk.Label(self, text="",fg='red')
        self.f9labelg.grid(row=9, column=0, pady=2)
        f9dugme1 = tk.Button(self, text="Ažuriraj", command=lambda: controller.azurirajUzorak())
        f9dugme1.grid(row=10, column=3, pady=2)
	
class f10(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller        

        lbl1 = tk.Label(self, text="Unesite pangolin za soj virusa:")
        lbl1.grid(row=0, column=0, sticky="w", columnspan=2, pady=(0, 10))

        lbl2 = tk.Label(self, text="pangolin: ")
        lbl2.grid(row=1, column=0, sticky="w", padx=(0, 10), pady=(0, 15))

        self.epango = tk.Entry(self, width=40)
        self.epango.grid(row=1, column=1, sticky="w", pady=(0, 15))

        f10napomena = tk.Label(
            self,
            text="Napomena: Brisanjem soja virusa iz baze podataka brišu se i svi uzorci tog soja virusa.",
            wraplength=550,
            justify="left",
            font=("Arial", 10)
        )
        f10napomena.grid(row=2, column=0, columnspan=2, sticky="w", pady=(0, 15))

        self.f10labelg = tk.Label(self, text="", fg="red", font=("Arial", 10, "bold"))
        self.f10labelg.grid(row=3, column=0, sticky="w")

        f10dugme1 = tk.Button(self, text="Obriši", command=lambda: controller.obrisiSoj())
        f10dugme1.grid(row=4, column=1, sticky="e")

class f11(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller        

        lbl1 = tk.Label(self, text="Unesite oznaku uzorka virusa:")
        lbl1.grid(row=0, column=0, sticky="w", columnspan=2, pady=(0, 10))

        lbl2 = tk.Label(self, text="oznaka uzorka virusa: ")
        lbl2.grid(row=1, column=0, sticky="w", padx=(0, 10), pady=(0, 15))

        self.epristupni = tk.Entry(self, width=40)
        self.epristupni.grid(row=1, column=1, sticky="w", pady=(0, 15))

        f11napomena = tk.Label(
            self,
            text="Napomena: Klikom na dugme Obriši uzorak će biti uklonjen iz baze podataka.",
            wraplength=550,
            justify="left",
            font=("Arial", 10)
        )
        f11napomena.grid(row=2, column=0, columnspan=2, sticky="w", pady=(0, 15))

        self.f11labelg = tk.Label(self, text="", fg="red", font=("Arial", 10, "bold"))
        self.f11labelg.grid(row=3, column=0, sticky="w")

        f11dugme1 = tk.Button(self, text="Obriši", command=lambda: controller.obrisiUzorak())
        f11dugme1.grid(row=4, column=1, sticky="e")
	
class f12(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.kolone = ["pango", "who", "gisaid",
                  "nextstrain","zemlja_prvog_uzorkovanja",
                  "kontinent_prvog_uzorkovanja",
                  "mesec_prvog_uzorkovanja",
                  "godina_prvog_uzorkovanja",
                  "datum_oznacavanja"]
        self.f12entry = []
        for i, naziv in enumerate(self.kolone):
            lbl = tk.Label(self, text=naziv + ":", anchor="w")
            lbl.grid(row=i, column=0, sticky="w", padx=4, pady=2)
            entry = tk.Entry(self, width=40)
            entry.grid(row=i, column=1, padx=4, pady=2)
            self.f12entry.append(entry)
        self.f12labelg = tk.Label(self, text="",fg='red')
        self.f12labelg.grid(row=9, column=0, pady=2)
        f12dugme1 = tk.Button(self, text="Pretraži", command=lambda: controller.pretraziSoj())
        f12dugme1.grid(row=10, column=3, pady=2)
	
class f13(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.kolone = ["pristupni_id", "pango",
                       "vlasnik", "opis", "duzina",
                       "lokacija_uzorkovanja", "datum_uzorkovanja",
                       "kompletnost_sekvence"]
        self.f13entry = []
        for i, naziv in enumerate(self.kolone):
            lbl = tk.Label(self, text=naziv + ":", anchor="w")
            lbl.grid(row=i, column=0, sticky="w", padx=4, pady=2)
            entry = tk.Entry(self, width=40)
            entry.grid(row=i, column=1, padx=4, pady=2)
            self.f13entry.append(entry)
        self.f13labelg = tk.Label(self, text="",fg='red')
        self.f13labelg.grid(row=9, column=0, pady=2)
        f13dugme1 = tk.Button(self, text="Pretraži", command=lambda: controller.pretraziUzorak())
        f13dugme1.grid(row=10, column=3, pady=2)

class f14(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        l14 = Label(self, text="Unesite SQL upit za pretragu: ")
        l14.place(x=20, y=15)
        self.t1 = tk.scrolledtext.ScrolledText(self, height = 6, width = 60, wrap="none")
        self.t1.place(x=25,y=40)
        self.f14labelg = tk.Label(self, text="",fg='red')
        self.f14labelg.place(x=25, y=140)
        f14dugme1 = tk.Button(self, text="Pretraži", command=lambda: controller.pretraziNapredno())
        f14dugme1.place(x=460, y=160)

class f15(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        text = scrolledtext.ScrolledText(self, height = 12, width = 60, wrap="none")
        text.place(x=25,y=25)
        
        dpdugme1 = tk.Button(self, text="Povratak", command=lambda: controller.pocetna())
        dpdugme1.place(x=455, y=240)
        labelg = tk.Label(self, text="",fg='red')
        labelg.place(x=25, y=230)

        try:
            f=open("pomoc.txt", "r", encoding="utf-8")
            p = f.read()
            text.insert(INSERT, p)
            text.config(state="disabled")
            f.close()
        except FileNotFoundError:
            labelg.config(text="Greška: fajl 'pomoc.txt' nije pronađen.")
        except Exception as e:
            labelg.config(text=f"Greška pri učitavanju: {e}")        
	
class f16(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = Canvas(self, width=530, height=280)
        canvas.pack()
        f16logo = Image.open("matf.png").resize((180, 200))  
        f16logoimg = ImageTk.PhotoImage(f16logo)  
        canvas.create_image(135, 100, anchor="center", image=f16logoimg)
        canvas.image = f16logoimg  

        label = tk.Label(self, text="Univerzitet u Beogradu\nMatematički fakultet\nAutor: Miloš Arsić\nMentor: prof. dr Vesna Marinković",
                 font=("Arial", 12), justify="center")
        label.place(x=265, y=240, anchor="center")
