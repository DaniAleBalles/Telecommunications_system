#Codificacion RLE de Daniel Ballesteros y Kevin Niño
from collections import Counter
from tkinter import Entry, Frame, Image, IntVar, Label, LabelFrame, Radiobutton, Tk,Text,Button,StringVar,PhotoImage,Canvas, Toplevel
import math
import re
import operator
from collections import OrderedDict
import numpy

Ventana_principal=Tk()
Ventana_principal.geometry("855x680")

lectura=0
tecnicas=0
seleccion=IntVar()
selecciontecnicas=IntVar()
a=(10,10)
arreglo=numpy.zeros(a,dtype=int)
matriz=None
frameMatriz=Frame(Ventana_principal)
frameMatriz.place(relwidth=0.8,relheight=0.8,y=200)


for i in range(0,10):
    for j in range(0,10):
        matriz=Label(frameMatriz, text=arreglo[j][i])
        matriz.place(relx=0.09*i,rely=0.08*j,width=100,height=10)


Ventana_principal.title("Codigo RLE")
TituloVentana_principal=Label(Ventana_principal, text="Codificación RLE", bd=10, fg='black',bg=("cyan"), font="sans")
TituloVentana_principal.grid(row=0, column=2,padx=10,pady=10)
Labelseleccion=Label(Ventana_principal, text="Seleccione como quiere que se lea la matriz",font=("sans",14))
Labelseleccion.grid(row=1,column=2)
LabelUsuario=Label(Ventana_principal, text="",bg="red")
LabelUsuario.grid(row=3,column=2)
labelCodificacion=Label(Ventana_principal, text=" Codificacion ", bg="red")
labelCodificacion.grid(row=4,column=3)
labelBinario=Label(Ventana_principal, text="")
labeltramatotal_res=Label(Ventana_principal,text="")
labeltramatotal_res.grid(row=15,column=3)
labelTasa=Label(Ventana_principal,text="Tasa de compresion",bg="red")
labelTasa.grid(row=16,column=3)
labelTasa_res=Label(Ventana_principal,text="")
labelTasa_res.grid(row=17,column=3)

def jamin(totalstr):

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

        while primerapos<columnas+1:

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
    labeltramaresultante=Label(ventana_matriz, text='Su trama resultante es: '+ Trama)
    labeltramaresultante.place(x=60,y=200)
    print (Trama)



def Boton_radio():
    global lectura
    lectura=seleccion.get()

def Boton_tecnicas():
    global tecnicas
    tecnicas=selecciontecnicas.get()

def Boton_Aleatorio():
    ventanatrama=Toplevel()
    labeltramaresultante=Label(ventanatrama,text="Trama resultante",bg="red")
    labeltramaresultante.grid(row=0,column=0)
    global a
    if(lectura!=1 and lectura!=2 and lectura!=3):
        LabelUsuario.configure(text="Porfavor seleccione una de las formas de lectura antes de continuar")
        arreglo=numpy.zeros(a,dtype=int)
        for i in range(0,10):
            for j in range(0,10):
                matriz.pack_forget()
                matriz2=Label(frameMatriz, text=arreglo[i][j])
                matriz2.place(relx=0.09*i,rely=0.08*j,width=100,height=10)  
    else:
        LabelUsuario.configure(text="Su matriz es apta para la codificacion", bg="green")
        arreglo=numpy.random.randint(1,20,size=(10,10))
        if lectura==1:
            for i in range(0,10):
                for j in range(0,10):
                    pasada=arreglo[i,j-1]
                    antepasada=arreglo[i,j-2]
                    if(pasada!=arreglo[i,j]):
                        if(pasada!=antepasada):
                            arreglo[i,j]=pasada
                    matriz.pack_forget()
                    matriz2=Label(frameMatriz, text=arreglo[i][j])
                    matriz2.place(relx=0.09*i,rely=0.08*j,width=100,height=10)
        if lectura==2:    
            for i in range(0,10):
                for j in range(0,10):
                    pasada=arreglo[j,i-1]
                    antepasada=arreglo[j,i-2]
                    if(pasada!=arreglo[j,i]):
                        if(pasada!=antepasada):
                            arreglo[j,i]=pasada
                    matriz.pack_forget()
                    matriz2=Label(frameMatriz, text=arreglo[j][i])
                    matriz2.place(relx=0.09*i,rely=0.08*j,width=100,height=10)      
        if lectura==1:
            codificacion=[]
            maximo=[]
            numeros=[]
            caracter=str(arreglo[0,0])
            count=0
            for i in range(0,10):
                for j in range(0,10):
                    if str(arreglo[i,j])==caracter:
                        count= count+1
                    else:
                        codificacion.append([caracter,count])
                        maximo.append(count)
                        numeros.append(caracter)
                        caracter=str(arreglo[i,j])
                        count=1
            codificacion.append([caracter,count])
            maximo.append(count)
            numeros.append(caracter)
            listacod=codificacion
            labelCodificacion.config(bg="green")
            labeltramaresultante.config(bg="green")
            contador=0
            fila=5
            i=0
            
            while contador <= 7: 
                labelCodificacion_res=Label(Ventana_principal,text=listacod[i:i+8])
                i=i+8
                labelCodificacion_res.grid(row=fila,column=3)
                fila= fila+1
                contador=contador+1
            mayor=maximo[0]
            for i in range(1, len(maximo)):
                if maximo[i] >mayor:
                    mayor= maximo[i]
            listcharmax=""
            
            while mayor != 0:
                modulo=mayor%2
                cociente=mayor//2
                listcharmax=str(modulo)+listcharmax
                mayor=cociente
            bitsuma=len(listcharmax)+1
            numero=list(map(int, numeros))
            mayorcaracter=numero[0]
            
            for i in range(1, len(numero)):
                if numero[i] >mayorcaracter:
                    mayorcaracter= numero[i]
            listchar=""
            
            while mayorcaracter != 0:
                modulo=mayorcaracter%2
                cociente=mayorcaracter//2
                listchar=str(modulo)+listchar
                mayorcaracter=cociente
            bitsuma2=len(listchar)+1
            repbin=[]
            listcharmax2=""
            for i in range(0,len(maximo)):
                while maximo[i] != 0:
                    modulo=maximo[i]%2
                    cociente=maximo[i]//2
                    listcharmax2=str(modulo)+listcharmax2
                    maximo[i]=cociente
                while len(listcharmax2)<bitsuma:
                    listcharmax2="0"+listcharmax2
                repbin.append(listcharmax2)
                listcharmax2=""
            numerosbin=[]
            listcharmax3=""
            for i in range(0,len(numero)):
                while numero[i] != 0:
                    modulo=numero[i]%2
                    cociente=numero[i]//2
                    listcharmax3=str(modulo)+listcharmax3
                    numero[i]=cociente
                while len(listcharmax3)<bitsuma2:
                    listcharmax3="0"+listcharmax3
                numerosbin.append(listcharmax3)
                listcharmax3=""
            tramaresultante=list()
            for i in range(0,len(maximo)):
                tramaresultante.append([numerosbin[i],repbin[i]])

            contador=0
            fila=1
            i=0 
            while contador <= 15: 
                labelCodificacion_res=Label(ventanatrama,text=tramaresultante[i:i+10])
                i=i+3
                labelCodificacion_res.grid(row=fila,column=3)
                fila= fila+1
                contador=contador+1
            totalbits=800
            totalstr=""
            for i in range(0, len(tramaresultante)):
                totalstr=totalstr+tramaresultante[i][0]
                totalstr=totalstr+tramaresultante[i][1]
            bitsresultantes=len(totalstr)
            tasadecompresion=(totalbits-bitsresultantes)*100/totalbits
            labelTasa.config(bg="green")
            labelTasa_res.config(text=tasadecompresion)
            labelbitschar=Label(ventanatrama, text="el numero total de bits de informacion es: ")
            labelbitschar.grid(row=18,column=3)
            labelbitschar_res=Label(ventanatrama, text=bitsuma2)
            labelbitschar_res.grid(row=19,column=3)
            labelbitsrep=Label(ventanatrama, text="el numero total de bits de repeticion es: ")
            labelbitsrep.grid(row=20,column=3)
            labelbitsrep_res=Label(ventanatrama, text=bitsuma)
            labelbitsrep_res.grid(row=21,column=3)
            labelbittrama=Label(ventanatrama, text="el numero total de bits de la trama es: ")
            labelbittrama.grid(row=22, column=3)
            labelbittrama_Res=Label(ventanatrama, text=bitsresultantes)
            labelbittrama_Res.grid(row=23, column=3)
            totalstr2=""
            for i in range(0, 25):
                totalstr2=totalstr2+totalstr[i]
            jamin(totalstr2)

            
            if tecnicas==1:
                maximo=[]
                numeros=[]
                caracter=str(arreglo[0,0])
                count=0
                for i in range(0,10):
                    for j in range(0,10):
                        if str(arreglo[i,j])==caracter:
                            count= count+1
                        else:
                            codificacion.append([caracter,count])
                            maximo.append(count)
                            numeros.append(caracter)
                            caracter=str(arreglo[i,j])
                            count=1
                codificacion.append([caracter,count])
                maximo.append(count)
                numeros.append(caracter)
                repbin=[]
                listcharmax2=""
                for i in range(0,len(maximo)):
                    while maximo[i] != 0:
                        modulo=maximo[i]%2
                        cociente=maximo[i]//2
                        listcharmax2=str(modulo)+listcharmax2
                        maximo[i]=cociente
                    while len(listcharmax2)<bitsuma:
                        listcharmax2="0"+listcharmax2
                    listcharmax2="1"+listcharmax2
                    repbin.append(listcharmax2)
                    listcharmax2=""
                numero=list(map(int, numeros))
                numerosbin=[]
                listcharmax3=""
                for i in range(0,len(numero)):
                    while numero[i] != 0:
                        modulo=numero[i]%2
                        cociente=numero[i]//2
                        listcharmax3=str(modulo)+listcharmax3
                        numero[i]=cociente
                    while len(listcharmax3)<bitsuma2:
                        listcharmax3="0"+listcharmax3
                    listcharmax3="0"+listcharmax3
                    numerosbin.append(listcharmax3)
                    listcharmax3=""
                tramaresultante=list()
                for i in range(0,len(maximo)):
                    tramaresultante.append([numerosbin[i],repbin[i]])
                contador=0
                fila=1
                i=0 
                while contador <= 15: 
                    labelCodificacion_res=Label(ventanatrama,text=tramaresultante[i:i+10])
                    i=i+3
                    labelCodificacion_res.grid(row=fila,column=3)
                    fila= fila+1
                    contador=contador+1

            if tecnicas==2:
                maximo=[]
                numeros=[]
                caracter=str(arreglo[0,0])
                count=0
                for i in range(0,10):
                    for j in range(0,10):
                        if str(arreglo[i,j])==caracter:
                            count= count+1
                        else:
                            codificacion.append([caracter,count])
                            maximo.append(count)
                            numeros.append(caracter)
                            caracter=str(arreglo[i,j])
                            count=1
                codificacion.append([caracter,count])
                maximo.append(count)
                numeros.append(caracter)
                repbin=[]
                listcharmax2=""
                for i in range(0,len(maximo)):
                    while maximo[i] != 0:
                        modulo=maximo[i]%2
                        cociente=maximo[i]//2
                        listcharmax2=str(modulo)+listcharmax2
                        maximo[i]=cociente
                    while len(listcharmax2)<bitsuma:
                        listcharmax2="0"+listcharmax2
                    listcharmax2=" "+listcharmax2
                    repeticionbyte=1
                    while repeticionbyte<=bitsuma:
                        listcharmax2="1"+listcharmax2
                        repeticionbyte= repeticionbyte+1
                    repbin.append(listcharmax2)
                    listcharmax2=""

                tramaresultante=list()
                for i in range(0,len(maximo)):
                    tramaresultante.append([numerosbin[i],repbin[i]])
                contador=0
                fila=1
                i=0 
                while contador <= 15: 
                    labelCodificacion_res=Label(ventanatrama,text=tramaresultante[i:i+10])
                    i=i+3
                    labelCodificacion_res.grid(row=fila,column=3)
                    fila= fila+1
                    contador=contador+1

            if tecnicas==3:
                contadormaestro=0
                maximo=[]
                numeros=[]
                caracter=str(arreglo[0,0])
                count=0
                for i in range(0,10):
                    for j in range(0,10):
                        if str(arreglo[i,j])==caracter:
                            count= count+1
                        else:
                            codificacion.append([caracter,count])
                            maximo.append(count)
                            numeros.append(caracter)
                            caracter=str(arreglo[i,j])
                            count=1
                codificacion.append([caracter,count])
                maximo.append(count)
                numeros.append(caracter)
                anticipado="0"
                b=0
                bitanticipado=0
                tramaresultante=list()
                if bitsuma<bitsuma2:
                    bitanticipado=bitsuma2
                else:
                    bitanticipado=bitsuma
                while b<bitanticipado-1:
                    if anticipado[-1]=="0":
                        anticipado=anticipado+"1"
                    elif anticipado[-1]=="1":
                        anticipado=anticipado+"0"
                    b=b+1
                tramaresultante.append(anticipado)
                repbin=[]
                listcharmax2=""
                for i in range(0,len(maximo)):
                    while maximo[i] != 0:
                        modulo=maximo[i]%2
                        cociente=maximo[i]//2
                        listcharmax2=str(modulo)+listcharmax2
                        maximo[i]=cociente
                    while len(listcharmax2)<bitsuma:
                        listcharmax2="0"+listcharmax2
                    repbin.append(listcharmax2)
                    listcharmax2=""
                numero=list(map(int, numeros))
                numerosbin=[]
                listcharmax3=""
                for i in range(0,len(numero)):
                    while numero[i] != 0:
                        modulo=numero[i]%2
                        cociente=numero[i]//2
                        listcharmax3=str(modulo)+listcharmax3
                        numero[i]=cociente
                    while len(listcharmax3)<bitsuma2:
                        listcharmax3="0"+listcharmax3
                    numerosbin.append(listcharmax3)
                    listcharmax3=""
                for i in range(0,len(maximo)):
                    tramaresultante.append([numerosbin[i],repbin[i]])
                    contadormaestro=contadormaestro+2
                    if contadormaestro==bitanticipado:
                        tramaresultante.append(anticipado)
                        contadormaestro=0
                contador=0
                fila=1
                i=0 
                while contador <= 20: 
                    labelCodificacion_res=Label(ventanatrama,text=tramaresultante[i:i+20])
                    i=i+3
                    labelCodificacion_res.grid(row=fila,column=3)
                    fila= fila+1
                    contador=contador+1


            






            
        if lectura==2:
            codificacion=[]
            maximo=[]
            numeros=[]
            caracter=str(arreglo[0,0])
            count=0
            for i in range(0,10):
                for j in range(0,10):
                    if str(arreglo[i,j])==caracter:
                        count= count+1
                    else:
                        codificacion.append([caracter,count])
                        maximo.append(count)
                        numeros.append(caracter)
                        caracter=str(arreglo[i,j])
                        count=1
            codificacion.append([caracter,count])
            maximo.append(count)
            numeros.append(caracter)
            listacod=codificacion
            labelCodificacion.config(bg="green")
            labeltramaresultante.config(bg="green")
            contador=0
            fila=5
            i=0
            
            while contador <= 7: 
                labelCodificacion_res=Label(Ventana_principal,text=listacod[i:i+8])
                i=i+8
                labelCodificacion_res.grid(row=fila,column=3)
                fila= fila+1
                contador=contador+1
            mayor=maximo[0]
            for i in range(1, len(maximo)):
                if maximo[i] >mayor:
                    mayor= maximo[i]
            listcharmax=""
            
            while mayor != 0:
                modulo=mayor%2
                cociente=mayor//2
                listcharmax=str(modulo)+listcharmax
                mayor=cociente
            bitsuma=len(listcharmax)+1
            numero=list(map(int, numeros))
            mayorcaracter=numero[0]
            
            for i in range(1, len(numero)):
                if numero[i] >mayorcaracter:
                    mayorcaracter= numero[i]
            listchar=""
            while mayorcaracter != 0:
                modulo=mayorcaracter%2
                cociente=mayorcaracter//2
                listchar=str(modulo)+listchar
                mayorcaracter=cociente
            bitsuma2=len(listchar)+1
            repbin=[]
            listcharmax2=""
            for i in range(0,len(maximo)):
                while maximo[i] != 0:
                    modulo=maximo[i]%2
                    cociente=maximo[i]//2
                    listcharmax2=str(modulo)+listcharmax2
                    maximo[i]=cociente
                while len(listcharmax2)<bitsuma:
                    listcharmax2="0"+listcharmax2
                repbin.append(listcharmax2)
                listcharmax2=""
            numerosbin=[]
            listcharmax3=""

            for i in range(0,len(numero)):
                while numero[i] != 0:
                    modulo=numero[i]%2
                    cociente=numero[i]//2
                    listcharmax3=str(modulo)+listcharmax3
                    numero[i]=cociente
                while len(listcharmax3)<bitsuma2:
                    listcharmax3="0"+listcharmax3
                numerosbin.append(listcharmax3)
                listcharmax3=""
            tramaresultante=list()
            for i in range(0,len(maximo)):
                tramaresultante.append([numerosbin[i],repbin[i]])

            contador=0
            fila=1
            i=0 
            while contador <= 15: 
                labelCodificacion_res=Label(ventanatrama,text=tramaresultante[i:i+10])
                i=i+3
                labelCodificacion_res.grid(row=fila,column=3)
                fila= fila+1
                contador=contador+1
            totalbits=800
            totalstr=""
            print(tramaresultante)
            for i in range(0, len(tramaresultante)):
                totalstr=totalstr+tramaresultante[i][0]
                totalstr=totalstr+tramaresultante[i][1]
            print(totalstr)
            bitsresultantes=len(totalstr)
            tasadecompresion=(totalbits-bitsresultantes)*100/totalbits
            labelTasa.config(bg="green")
            labelTasa_res.config(text=tasadecompresion)
            labelbitschar=Label(ventanatrama, text="el numero total de bits de informacion es: ")
            labelbitschar.grid(row=18,column=3)
            labelbitschar_res=Label(ventanatrama, text=bitsuma2)
            labelbitschar_res.grid(row=19,column=3)
            labelbitsrep=Label(ventanatrama, text="el numero total de bits de repeticion es: ")
            labelbitsrep.grid(row=20,column=3)
            labelbitsrep_res=Label(ventanatrama, text=bitsuma)
            labelbitsrep_res.grid(row=21,column=3)
            labelbittrama=Label(ventanatrama, text="el numero de bits de la trama es de: ")
            labelbittrama.grid(row=22, column=3)
            labelbittrama_Res=Label(ventanatrama, text=bitsresultantes)
            labelbittrama_Res.grid(row=23, column=3)
            totalstr2=""
            for i in range(0, 25):
                totalstr2=totalstr2+totalstr[i]
            jamin(totalstr2)


            if tecnicas==1:
                maximo=[]
                numeros=[]
                caracter=str(arreglo[0,0])
                count=0
                for i in range(0,10):
                    for j in range(0,10):
                        if str(arreglo[i,j])==caracter:
                            count= count+1
                        else:
                            codificacion.append([caracter,count])
                            maximo.append(count)
                            numeros.append(caracter)
                            caracter=str(arreglo[i,j])
                            count=1
                codificacion.append([caracter,count])
                maximo.append(count)
                numeros.append(caracter)
                repbin=[]
                listcharmax2=""
                for i in range(0,len(maximo)):
                    while maximo[i] != 0:
                        modulo=maximo[i]%2
                        cociente=maximo[i]//2
                        listcharmax2=str(modulo)+listcharmax2
                        maximo[i]=cociente
                    while len(listcharmax2)<bitsuma:
                        listcharmax2="0"+listcharmax2
                    listcharmax2="1"+listcharmax2
                    repbin.append(listcharmax2)
                    listcharmax2=""
                numero=list(map(int, numeros))
                numerosbin=[]
                listcharmax3=""
                for i in range(0,len(numero)):
                    while numero[i] != 0:
                        modulo=numero[i]%2
                        cociente=numero[i]//2
                        listcharmax3=str(modulo)+listcharmax3
                        numero[i]=cociente
                    while len(listcharmax3)<bitsuma2:
                        listcharmax3="0"+listcharmax3
                    listcharmax3="0"+listcharmax3
                    numerosbin.append(listcharmax3)
                    listcharmax3=""
                tramaresultante=list()
                for i in range(0,len(maximo)):
                    tramaresultante.append([numerosbin[i],repbin[i]])
                contador=0
                fila=1
                i=0 
                while contador <= 15: 
                    labelCodificacion_res=Label(ventanatrama,text=tramaresultante[i:i+10])
                    i=i+3
                    labelCodificacion_res.grid(row=fila,column=3)
                    fila= fila+1
                    contador=contador+1

            if tecnicas==2:
                maximo=[]
                numeros=[]
                caracter=str(arreglo[0,0])
                count=0
                for i in range(0,10):
                    for j in range(0,10):
                        if str(arreglo[i,j])==caracter:
                            count= count+1
                        else:
                            codificacion.append([caracter,count])
                            maximo.append(count)
                            numeros.append(caracter)
                            caracter=str(arreglo[i,j])
                            count=1
                codificacion.append([caracter,count])
                maximo.append(count)
                numeros.append(caracter)
                repbin=[]
                listcharmax2=""
                for i in range(0,len(maximo)):
                    while maximo[i] != 0:
                        modulo=maximo[i]%2
                        cociente=maximo[i]//2
                        listcharmax2=str(modulo)+listcharmax2
                        maximo[i]=cociente
                    while len(listcharmax2)<bitsuma:
                        listcharmax2="0"+listcharmax2
                    listcharmax2=" "+listcharmax2
                    repeticionbyte=1
                    while repeticionbyte<=bitsuma:
                        listcharmax2="1"+listcharmax2
                        repeticionbyte= repeticionbyte+1
                    repbin.append(listcharmax2)
                    listcharmax2=""

                tramaresultante=list()
                for i in range(0,len(maximo)):
                    tramaresultante.append([numerosbin[i],repbin[i]])
                contador=0
                fila=1
                i=0 
                while contador <= 15: 
                    labelCodificacion_res=Label(ventanatrama,text=tramaresultante[i:i+10])
                    i=i+3
                    labelCodificacion_res.grid(row=fila,column=3)
                    fila= fila+1
                    contador=contador+1

            if tecnicas==3:
                contadormaestro=0
                maximo=[]
                numeros=[]
                caracter=str(arreglo[0,0])
                count=0
                for i in range(0,10):
                    for j in range(0,10):
                        if str(arreglo[i,j])==caracter:
                            count= count+1
                        else:
                            codificacion.append([caracter,count])
                            maximo.append(count)
                            numeros.append(caracter)
                            caracter=str(arreglo[i,j])
                            count=1
                codificacion.append([caracter,count])
                maximo.append(count)
                numeros.append(caracter)
                anticipado="0"
                b=0
                bitanticipado=0
                tramaresultante=list()
                if bitsuma<bitsuma2:
                    bitanticipado=bitsuma2
                else:
                    bitanticipado=bitsuma
                while b<bitanticipado-1:
                    if anticipado[-1]=="0":
                        anticipado=anticipado+"1"
                    elif anticipado[-1]=="1":
                        anticipado=anticipado+"0"
                    b=b+1
                tramaresultante.append(anticipado)
                repbin=[]
                listcharmax2=""
                for i in range(0,len(maximo)):
                    while maximo[i] != 0:
                        modulo=maximo[i]%2
                        cociente=maximo[i]//2
                        listcharmax2=str(modulo)+listcharmax2
                        maximo[i]=cociente
                    while len(listcharmax2)<bitsuma:
                        listcharmax2="0"+listcharmax2
                    repbin.append(listcharmax2)
                    listcharmax2=""
                numero=list(map(int, numeros))
                numerosbin=[]
                listcharmax3=""
                for i in range(0,len(numero)):
                    while numero[i] != 0:
                        modulo=numero[i]%2
                        cociente=numero[i]//2
                        listcharmax3=str(modulo)+listcharmax3
                        numero[i]=cociente
                    while len(listcharmax3)<bitsuma2:
                        listcharmax3="0"+listcharmax3
                    numerosbin.append(listcharmax3)
                    listcharmax3=""
                for i in range(0,len(maximo)):
                    tramaresultante.append([numerosbin[i],repbin[i]])
                    contadormaestro=contadormaestro+2
                    if contadormaestro==bitanticipado:
                        tramaresultante.append(anticipado)
                        contadormaestro=0
                contador=0
                fila=1
                i=0 
                while contador <= 20: 
                    labelCodificacion_res=Label(ventanatrama,text=tramaresultante[i:i+20])
                    i=i+3
                    labelCodificacion_res.grid(row=fila,column=3)
                    fila= fila+1
                    contador=contador+1
                print(totalstr)





             
BotonAleatorio=Button(Ventana_principal, text="Llenar matriz y codificar",width=20, command=lambda : Boton_Aleatorio())
BotonAleatorio.grid(row=4,column=1,padx=10,pady=20)
Boton_horizontal=Radiobutton(Ventana_principal, text="Vertical", variable=seleccion, value=1, command=Boton_radio)
Boton_horizontal.grid(row=2,column=0)
Boton_vertical=Radiobutton(Ventana_principal, text="Horizontal", variable=seleccion, value=2,command=Boton_radio)
Boton_vertical.grid(row=2,column=2)
Boton_zigzag=Radiobutton(Ventana_principal, text="ZigZag", variable=seleccion, value=3,command=Boton_radio)
Boton_zigzag.grid(row=2,column=4)
Label_Tecnicas=Label(Ventana_principal, text="seleccione la tecnica para mostrar la trama")
Label_Tecnicas.grid(row=18,column=3)
Boton_bandera=Radiobutton(Ventana_principal, text="Bit bandera", width=20,variable=selecciontecnicas, value=1, command=lambda : Boton_tecnicas())
Boton_bandera.grid(row=19,column=3,padx=10,pady=20)
Boton_Byteband=Radiobutton(Ventana_principal, text="Byte bandera", width=20,variable=selecciontecnicas, value=2, command=lambda : Boton_tecnicas())
Boton_Byteband.grid(row=20,column=3,padx=10,pady=20)
Boton_anticipado=Radiobutton(Ventana_principal, text="Byte anticipado", width=20,variable=selecciontecnicas, value=3, command=lambda : Boton_tecnicas())
Boton_anticipado.grid(row=21,column=3,padx=10,pady=20)
Ventana_principal.mainloop()

