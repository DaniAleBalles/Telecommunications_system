#Trabajo final Sistemas de Telecomunicaciones II de Daniel Ballesteros y Kevin Niño

from collections import Counter
from tkinter import Entry, Frame, Image, IntVar, Label, LabelFrame, Radiobutton, Tk,Text,Button,StringVar,PhotoImage,Canvas, Toplevel
import math
import re
import operator
from collections import OrderedDict
import numpy
import subprocess




Ventana_principal=Tk()

Ventana_principal.title("Trabajo Final")
Texto=StringVar()
TituloVentana_principal=Label(Ventana_principal, text="---Trabajo Final---", bd=10, fg='black',bg=("cyan"), font=("sans",20))
TituloVentana_principal.grid(row=0, column=2,padx=10,pady=10)
LabelTrama=Label(Ventana_principal, text="Estes es nuestro Trabajo Final, aca podras elegir los distintos tipos de codificacion tocados en este semestre.",font=("sans",14))
LabelTrama.grid(row=1,column=2)

def Hammingp():
    subprocess.call("Hamming.py", shell=True)
      
def Aritmetciap():
    subprocess.call("Aritmetica.py", shell=True)

def Huffmanp():
    subprocess.call("Huffman.py", shell=True)

def Shannonp():
    subprocess.call("Shannon.py", shell=True)

def Algoritmicap():
    subprocess.call("Algoritmica.py", shell=True)

def RLEP():
    subprocess.call("RLE.py", shell=True)

def DPCMP():
    subprocess.call("DPCM.py", shell=True)
    
BotonCodificar=Button(Ventana_principal, text="Huffman", width=20, command=lambda : Huffmanp() )
BotonCodificar.grid(row=2, column=0,padx=20,pady=20)
BotonCodificar=Button(Ventana_principal, text="Shannon Fano", width=20, command=lambda : Shannonp())
BotonCodificar.grid(row=2, column=3,padx=20,pady=20)
BotonCodificar=Button(Ventana_principal, text="Aritmetica", width=20, command=lambda : Aritmetciap())
BotonCodificar.grid(row=3, column=0,padx=20,pady=20)
BotonCodificar=Button(Ventana_principal, text="Algoritmica Modificada", width=20, command=lambda : Algoritmicap() )
BotonCodificar.grid(row=3, column=3,padx=20,pady=20)
BotonCodificar=Button(Ventana_principal, text="RLE", width=20, command=lambda : RLEP() )
BotonCodificar.grid(row=4, column=0,padx=20,pady=20)
BotonCodificar=Button(Ventana_principal, text="DPCM", width=20, command=lambda : DPCMP() )
BotonCodificar.grid(row=4, column=3,padx=20,pady=20)
BotonCodificar=Button(Ventana_principal, text="Hamming", width=20, command=lambda : Hammingp())
BotonCodificar.grid(row=5, column=2,padx=20,pady=20)
Ventana_principal.mainloop()