import os
import zlib
import sys
import glob
import re
import pylab
import math as mat
import matplotlib.pyplot as plt
import mysql.connector


import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from PIL import ImageTk,Image

from Bio.Align.Applications import ClustalOmegaCommandline
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor, DistanceCalculator
from Bio import AlignIO

from scrollableimage import ScrollableImage #ubaceno dodatno

def povezivanje_sa_bazom(hostname, username, ipassword, databasename):
    mydb = mysql.connector.connect(
        host=hostname,
        user=username,
        password=ipassword,
        database = databasename)
    return mydb
def get_sequences_filenames(directory):
    files = []
    for file in glob.glob(directory+ "/*.fasta"):
        files.append(file)
    return files
def import_sequences(hostname, username, ipassword, databasename, directory):
    mydb = connect_to_database(hostname, username, ipassword, databasename)
    files = get_sequences_filenames(directory)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE sample( `ID` VARCHAR(20) NOT NULL , `SEQUENCE` VARBINARY(10000) NOT NULL , PRIMARY KEY (`ID`(20))) ENGINE = InnoDB")
    mycursor.execute("TRUNCATE TABLE uzorak")
    for filename in files:
        f = open(filename, "r")
        seq = f.read()
        seq = seq[seq.find('\n'):]
        seq = seq.replace('\n', '')
        #print(len(seq))
        seq1= seq.encode()
        compressed = zlib.compress(seq1)
        
        #decompressed=zlib.decompress(compressed)
        #seq2 = decompressed.decode()
        print(len(compressed))
        
        filename = filename.split("\\")[-1]
        filename = filename[0:-6]
        print(filename)
        sql = "INSERT INTO sample (ID, SEQUENCE) VALUES (%s, %s)"
        val = (filename, compressed)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
def check_if_correct(hostname, username, ipassword, databasename, directory):
    mydb = connect_to_database(hostname, username, ipassword, databasename)
    files = get_sequences_filenames(directory)
    mycursor = mydb.cursor()
    for filename in files:
        f = open(filename, "r")
        seq = f.read()
        seq = seq[seq.find('\n'):]
        seq = seq.replace('\n', '')
        filename = filename.split("\\")[-1]
        filename = filename[0:-6]
        print(filename)
        sql = "SELECT * FROM sample where ID = '" + filename + "'"
        res = mycursor.execute(sql)
        compressed = (mycursor.fetchall()[0])[1]
        decompressed=zlib.decompress(compressed)
        seq2 = decompressed.decode()
        print(len(seq2))
        if seq==seq2:
            print("DA")
        else:
            print("NE")
