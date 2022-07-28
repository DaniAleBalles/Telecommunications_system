#Codificacion Huffman de Daniel Ballesteros Y Kevin Niño
from tkinter import Entry, Image, Label, LabelFrame, Tk,Text,Button,StringVar,PhotoImage,Canvas,Toplevel,Frame
from time import sleep
from tkinter.constants import INSERT
import math

ventana_principal=Tk()
trama=StringVar()
ventana_principal.title('Codigo huffman')
label=Label(text='ingrese la trama para el codigo huffman sin espacios: ')
label.grid(row=0,column=1,columnspan=5,padx=20,pady=5,)
pantalla=Entry(ventana_principal,textvariable=trama, state='normal',width=40,background='white',foreground='black')
pantalla.grid(row=1,column=1,columnspan=5,padx=20,pady=20)


def click_boton():

    if len(trama.get())>15:
        label3=Label(text='digite una trama menor de 15 digitos')
        label3.grid(row=3,column=5,columnspan=5,padx=20,pady=5)
    else:
        if len(trama.get())<10:
            label2=Label(text='digite una trama mayor de 10 digitos')
            label2.grid(row=3,column=5,columnspan=5,padx=20,pady=5)
        else:
            class ordenamiento(object):
                def __init__(self, izquierda=None, derecha=None):
                    self.izquierda = izquierda
                    self.derecha = derecha
                def ramificacion(self):
                    return (self.izquierda, self.derecha)

            def huffman(var, izquierda=True, binString=''):
                if type(var) is str:
                    return {var: binString}
                (menor, mayor) = var.ramificacion()
                diccionario = dict()
                diccionario.update(huffman(menor, True, binString + '1'))
                diccionario.update(huffman(mayor, False, binString + '0'))
                return diccionario

            frecuencia = {}
            for i in trama.get():
                if i in frecuencia:
                    frecuencia[i] = frecuencia[i]+1
                else:
                    frecuencia[i] = 1

            probabilidades={}
            for i in trama.get():
                 probabilidades[i] = frecuencia[i]/float(len(trama.get()))

            entropia=0
            for i in probabilidades:
                 entropia= entropia + (-1*(probabilidades[i])*math.log2(probabilidades[i]))

            frecuencia = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)

            nodo = frecuencia

            while len(nodo) > 1:
                (var1, i1) = nodo[-1]
                (var2, i2) = nodo[-2]
                nodo = nodo[:-2]
                var = ordenamiento(var1, var2)
                nodo.append((var, i1 + i2))
                nodo = sorted(nodo, key=lambda x: x[1], reverse=True)

            Codigohuffman = huffman(nodo[0][0])

            longitudp=0
            for i in probabilidades:
                 longitudp=longitudp+(probabilidades[i]*len(Codigohuffman[i]))
            eficiencia=entropia/longitudp
            cou=len(set(trama.get()))
            tasa=(math.log(cou,2)/longitudp)
            cartel=Label(text='Codificacion huffman')
            cartel.grid(row=3,column=1,columnspan=5,padx=20,pady=5)
            cartel2=Label(text=Codigohuffman)
            cartel2.grid(row=4,column=1,columnspan=5,padx=20,pady=5)
            cartel3=Label(text='FRECUENCIAS')
            cartel3.grid(row=5,column=1,columnspan=5,padx=20,pady=5)
            cartel4=Label(text=frecuencia)
            cartel4.grid(row=6,column=1,columnspan=5,padx=20,pady=5)
            cartel5=Label(text='PROBABILIDADES')
            cartel5.grid(row=7,column=1,columnspan=5,padx=20,pady=5)
            cartel6=Label(text=probabilidades)
            cartel6.grid(row=8,column=1,columnspan=5,padx=20,pady=5)
            cartel7=Label(text='ENTROPIA')
            cartel7.grid(row=9,column=1,columnspan=5,padx=20,pady=5)
            cartel8=Label(text=entropia)
            cartel8.grid(row=10,column=1,columnspan=5,padx=20,pady=5)
            cartel9=Label(text='FRECUENCIAS')
            cartel9.grid(row=11,column=1,columnspan=5,padx=20,pady=5)
            cartel10=Label(text=frecuencia)
            cartel10.grid(row=12,column=1,columnspan=5,padx=20,pady=5)
            cartel11=Label(text='LONGITUD PROMEDIO')
            cartel11.grid(row=13,column=1,columnspan=5,padx=20,pady=5)
            cartel12=Label(text=longitudp)
            cartel12.grid(row=14,column=1,columnspan=5,padx=20,pady=5)
            cartel13=Label(text='EFICIENCIA')
            cartel13.grid(row=15,column=1,columnspan=5,padx=20,pady=5)
            cartel14=Label(text=eficiencia)
            cartel14.grid(row=16,column=1,columnspan=5,padx=20,pady=5)
            cartel15=Label(text='TASA DE COMPRESION')
            cartel15.grid(row=17,column=1,columnspan=5,padx=20,pady=5)
            cartel16=Label(text=tasa)
            cartel16.grid(row=18,column=1,columnspan=5,padx=20,pady=5)
            tramafinal=list(Codigohuffman.values())
            totalstr=""
            for i in range(0, len(tramafinal)):
                totalstr=totalstr+tramafinal[i]
            print(totalstr)

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

            Trama=totalstr
            lentrama=len(Trama)
            columnas=0
            filas=0
            digito=0
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
            tramalist=[]
            tramadato=0
            for i in range(len(Trama)):
                tramadato=Trama[i]
                tramalist.append(tramadato)


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
                if primerapos==64:
                    counttrama=63
                if primerapos==128:
                    counttrama=127
                if primerapos==256:
                    counttrama=255
                if primerapos==512:
                    counttrama=511  

                while primerapos<columnas:

                    if count!=salto:

                        matriz[i][primerapos]=tramalist[counttrama]
                        count=count+1
                        primerapos=primerapos+1
                        counttrama=counttrama+1

                    if count==salto:
                        if countsalto!=salto:
                            if primerapos!=1 or primerapos!=2 or primerapos!=4 or primerapos!=8 or primerapos!=16 or primerapos!=32 or primerapos==64 or primerapos==128 or primerapos==256 or primerapos==512:
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
            labeltramaresultante=Label(ventana_matriz, text='Su trama resultante en Hamming: '+ Trama)
            labeltramaresultante.place(x=60,y=200)
            print (Trama)
            
      
                 
                
boton1=Button(ventana_principal, text='codificacion',width=9,height=1,command=click_boton)
boton1.grid(row=2,column=1,columnspan=5,padx=20,pady=1)
ventana_principal.mainloop()





























