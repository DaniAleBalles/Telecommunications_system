#Codificacion Hamming de Daniel Ballesteros y Kevin Niño
from collections import Counter
from tkinter import Entry, Frame, Image, IntVar, Label, LabelFrame, Radiobutton, Tk,Text,Button,StringVar,PhotoImage,Canvas, Toplevel
import math
import re
import operator
from collections import OrderedDict
import numpy

Ventana_principal=Tk()

Ventana_principal.title("Codigo Hamming")
Texto=StringVar()
TituloVentana_principal=Label(Ventana_principal, text="Codificación Hamming", bd=10, fg='black',bg=("cyan"), font="sans")
TituloVentana_principal.grid(row=0, column=2,padx=10,pady=10)
LabelTrama=Label(Ventana_principal, text="Digite una trama de minimo 25 bits",font=("sans",14))
LabelTrama.grid(row=1,column=2)
EntryTrama=Entry(Ventana_principal, textvariable=Texto, width=50)
EntryTrama.grid(row=2, column=2, padx=20, pady=20)

 

def click_boton():
    def BitsRedundantes(Lentrama):
        for i in range(Lentrama):
            if(2**i >= Lentrama + i + 1):
             return i

    def ListaBits(Trama, Bits):
        count = 0
        countres = 1
        Lentrama = len(Trama)
        Listresult = ''

        for i in range(1, Lentrama + Bits+1):
            if(i == 2**count):
                Listresult = Listresult + '0'
                count=count+ 1
            else:
                Listresult = Listresult + Trama[-1 * countres]
                countres=countres+1
        return Listresult[::-1]
 
    def BitsParidad(Trama, Bits):
        Lentrama = len(Trama)
        for i in range(Bits):
            dato = 0
            for j in range(1, Lentrama+1):

                if(j & pow(2,i) == pow(2,i)):
                    dato = dato^ int(Trama[-1*j])
            Trama = Trama[:Lentrama-(2**i)] + str(dato)+Trama[Lentrama-(2**i)+1:]
        return Trama
 
    Trama=Texto.get()
    lentrama=len(Trama)
    columnas=0
    filas=0
    digito=0
    if(lentrama<25):
        LabelTrama.configure(text="Su Trama es de menos de 25 caracteres")
    else:
        for i in range(len(Trama)):
            if(Trama[i]=="1" or Trama[i]=="0"):
                c=0
            else:
                c=1
        if (c==1):
            LabelTrama.configure(text="Su Trama no posee todos sus bits binarios")
        else:
            LabelTrama.configure(text="Su Trama es Apta para la codificacion")
            ventana_matriz=Toplevel()
            ventana_matriz.attributes("-fullscreen", True)
            frameMatriz=Frame(ventana_matriz)
            frameMatriz.place(relwidth=0.9,relheight=0.9)
            matriztk=None
            columnas=lentrama
            digitolist=[]
            for i in range(len(Trama)):
                digito= digito + 1
                digitolist.append(digito)
            elevado=0
            for i in range(0,len(Trama)):
                if digitolist[i]==pow(2,elevado):
                    columnas=columnas+1
                    filas=filas+1
                    elevado=elevado+1
            digitodeflist=[]
            digitodef=0
            for i in range(0,columnas):
                digitodef=digitodef+1
                digitodeflist.append(digitodef)
            count=(filas+1,columnas+1)
            fp='fp'
            fplist=[]
            fpnumero=0
            elevado=0
            for i in range(0,columnas):
                if digitodeflist[i]==pow(2,elevado):
                    fpnumero=digitodeflist[i]
                    fp=fp+str(fpnumero)
                    fplist.append(fp)
                    fp='fp'
                    elevado=elevado+1
            p='p'
            plist=[]
            pnumero=0
            dnumero=0
            elevado=0
            for i in range(0,columnas):
                if digitodeflist[i]==pow(2,elevado):
                    pnumero=pnumero+1
                    p=p+str(pnumero)
                    elevado=elevado+1
                else:
                    dnumero=dnumero+1
                    p='d'
                    p=p+str(dnumero)
                plist.append(p)
                p='p'
            matriz=[]
            for i in range(filas+1):
                matriz.append(['-']*(columnas+1))
            matriz[0][0]='ham'
            for i in range(0,filas):
                matriz[i+1][0]=fplist[i]
            for i in range(0,columnas):
                matriz[0][i+1]=plist[i]
            

            Bits = BitsRedundantes(lentrama)
            
            Trama = ListaBits(Trama, Bits)
            
            Trama = BitsParidad(Trama, Bits)
            print(Trama)
            tramalist=[]
            tramadato=0
            for i in range(len(Trama)):
                tramadato=Trama[i]
                tramalist.append(tramadato)
            
            print(tramalist)

            for i in range(1,filas+1):
                primerapos=pow(2,i-1)
                count=0
                countsalto=0
                salto=pow(2,i-1)
                count=0
                if primerapos==1:  
                    counttrama=0
                if primerapos==2:
                    counttrama=1 
                if primerapos==4:
                    counttrama=3
                if primerapos==8:
                    counttrama=7
                if primerapos==16:
                    counttrama=15
                if primerapos==32:
                    counttrama=31
        
                while primerapos<columnas+1:

                    if count!=salto:

                        matriz[i][primerapos]=tramalist[counttrama]
                        count=count+1
                        primerapos=primerapos+1
                        counttrama=counttrama+1

                    if count==salto:
                        if countsalto!=salto:
                            if primerapos!=1 or primerapos!=2 or primerapos!=4 or primerapos!=8 or primerapos!=16:
                                counttrama=counttrama+1
                            matriz[i][primerapos]='-'
                            countsalto=countsalto+1
                            primerapos=primerapos+1
                        if countsalto==salto:
                            count=0
                            countsalto=0

            for i in range(0,columnas+1):
                for j in range(0,filas+1):
                    matriztk=Label(frameMatriz, text=matriz[j][i])
                    matriztk.place(relx=0.03*i,rely=0.03*j)
            labeltramaresultante=Label(ventana_matriz, text='Su trama resultante es: '+ Trama)
            labeltramaresultante.place(x=60,y=200)



BotonCodificar=Button(Ventana_principal, text="codificacion", width=20, command=lambda : click_boton())
BotonCodificar.grid(row=3, column=2)
Ventana_principal.mainloop()