#Codificacion DPCM de Daniel Ballesteros y Kevin Niño
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
seleccion=IntVar()
a=(10,10)
arreglo=numpy.zeros(a,dtype=int)
matriz=None
frameMatriz=Frame(Ventana_principal)
frameMatriz.place(relwidth=0.8,relheight=0.8,y=200)


for i in range(0,10):
    for j in range(0,10):
        matriz=Label(frameMatriz, text=arreglo[j][i])
        matriz.place(relx=0.09*i,rely=0.08*j,width=100,height=10)


Ventana_principal.title("Codigo DPCM")
TituloVentana_principal=Label(Ventana_principal, text="Codificación DPCM", bd=10, fg='black',bg=("cyan"), font="sans")
TituloVentana_principal.grid(row=0, column=2,padx=10,pady=10)
Labelseleccion=Label(Ventana_principal, text="Seleccione como quiere que se lea la matriz",font=("sans",14))
Labelseleccion.grid(row=1,column=2)
LabelUsuario=Label(Ventana_principal, text="",bg="red")
LabelUsuario.grid(row=3,column=2)
labelBinario=Label(Ventana_principal, text="")
labeltramatotal_res=Label(Ventana_principal,text="")
labeltramatotal_res.grid(row=15,column=3)

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


def Boton_Aleatorio():
    global a
    ventanatrama=Toplevel()
    ventanatrama.geometry("855x680")
    arreglosecundario=numpy.zeros(a,dtype=int)
    frameMatrizsec=Frame(ventanatrama)
    frameMatrizsec.place(relwidth=0.8,relheight=0.8,y=50)
    labelMatrizsec=Label(ventanatrama,text="Matriz Secundaria",bg="red")
    labelMatrizsec.grid(row=0,column=0)
   

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
                    matriz.pack_forget()
                    matriz2=Label(frameMatriz, text=arreglo[j][i])
                    matriz2.place(relx=0.09*i,rely=0.08*j,width=100,height=10)
        if lectura==2:    
            for i in range(0,10):
                for j in range(0,10):
                    matriz.pack_forget()
                    matriz2=Label(frameMatriz, text=arreglo[i][j])
                    matriz2.place(relx=0.09*i,rely=0.08*j,width=100,height=10) 
        if lectura==3:
            matriz.pack_forget()
            alto=10
            ancho=10
            MatrizSolucion=[[] for i in range(ancho+alto-1)]
            for i in range(ancho):
                for j in range(alto):
                    sum=i+j
                    if(sum%2 ==0):
                        MatrizSolucion[sum].insert(0,arreglo[i][j])
                    else:
                        MatrizSolucion[sum].append(arreglo[i][j])		
            lista=list()
            for i in MatrizSolucion:
                for j in i:
                        lista.append(j)

            for i in range(0,10):
                for j in range(0,10):
                    matriz2=Label(frameMatriz, text=arreglo[j][i])
                    matriz2.place(relx=0.09*i,rely=0.08*j,width=100,height=10) 
            zigzag=numpy.array(lista).reshape(10,10)

        if lectura==2:
            numero=0
            caracter=int(arreglo[0,0])
            datomatriz=numpy.zeros(a,dtype=int)
            count=0
            for i in range(0,10):
                if count>1:
                    numero=int(arreglo[i][0])-int(arreglo[i-1][9])
                    datomatriz[i,0]=numero
                for j in range(1,10):
                    if count<1:
                        datomatriz[0][0]=arreglo[0][0]
                        numero=int(arreglo[i][j])-int(arreglo[i][j-1])
                        datomatriz[i,j]=numero
                        count=count+2
                    else:
                        numero=int(arreglo[i][j])-int(arreglo[i][j-1])
                        datomatriz[i,j]=numero
        
            for i in range(0,10):
                for j in range(0,10):
                    matrizsec=Label(frameMatrizsec, text=datomatriz[j][i])
                    matrizsec.place(relx=0.09*i,rely=0.08*j)
            labelMatrizsec.config(bg="green")

            matrizpositiva=numpy.zeros(a,dtype=int)
            for i in range(0,10):
                for j in range(0,10):
                    if int(datomatriz[i][j])<0:
                        matrizpositiva[i][j]=-1*datomatriz[i][j]
                    else:
                        matrizpositiva[i][j]=datomatriz[i][j]
            #print(matrizpositiva)

 
            mayor=matrizpositiva[0][0]
            mayor2=matrizpositiva[0][0]
            for fila in matrizpositiva:
                for valor in fila:
                    if valor > mayor:
                        mayor = valor
                        mayor2=valor
            listcharmax=''
            while mayor != 0:
                modulo=mayor%2
                cociente=mayor//2
                listcharmax=str(modulo)+listcharmax
                mayor=cociente
            bitsuma=len(listcharmax)
            bitband=len(listcharmax)+1
            #print(bitband)

        
            trama=[]
            for i in range(0,10):
                    for j in range(0,10):
                        caracter=int(matrizpositiva[i][j])
                        trama.append(caracter)

            tramaneg=[]
            for i in range(0,10):
                    for j in range(0,10):
                        caracter=int(datomatriz[i][j])
                        tramaneg.append(caracter)

            numerosbin=[]
            listbin=''
            for i in range(0,len(trama)):
                if trama[i]==0:
                    listbin='0'
                    while len(listbin)<bitband:
                        listbin='0'+listbin
                else:
                    while trama[i] !=0:
                        modulo=trama[i]%2
                        cociente=trama[i]//2
                        listbin=str(modulo)+listbin
                        trama[i]=cociente
                    while len(listbin)<bitsuma:
                        listbin='0'+listbin
                    if tramaneg[i]<0:
                        listbin='1'+listbin
                    else:
                        listbin='0'+listbin
                numerosbin.append(listbin)
                listbin=''

            labelbitschar=Label(ventanatrama, text="el numero mayor es: ")
            labelbitschar.place(x=650,y=20)
            labelbitschar_res=Label(ventanatrama, text=mayor2)
            labelbitschar_res.place(x=800,y=20)
            labelmayor=Label(ventanatrama, text="el numero total de bits es: ")
            labelmayor.place(x=650,y=60)
            labelmayor_res=Label(ventanatrama, text=bitband)
            labelmayor_res.place(x=800,y=60)
            labeltramada=Label(Ventana_principal, text="Trama resultante ")
            labeltramada.grid(row=4,column=3)
            contador=0
            fila=5
            i=0
            while contador <= 20: 
                labelCodificacion_res=Label(Ventana_principal,text=numerosbin[i:i+5])
                i=i+5
                labelCodificacion_res.grid(row=fila,column=3)
                fila= fila+1
                contador=contador+1
                
            totalstr=""
            for i in range(0, len(numerosbin)):
                totalstr=totalstr+str(numerosbin[i])
                
            totalstr2=""
            for i in range(0, 25):
                totalstr2=totalstr2+totalstr[i]
            jamin(totalstr2)

        if lectura==1:
            numero=0
            caracter=int(arreglo[0,0])
            datomatriz=numpy.zeros(a,dtype=int)
            count=0
            for i in range(0,10):
                if count>1:
                    numero=int(arreglo[i][0])-int(arreglo[i-1][9])
                    datomatriz[i,0]=numero
                for j in range(1,10):
                    if count<1:
                        datomatriz[0][0]=arreglo[0][0]
                        numero=int(arreglo[i][j])-int(arreglo[i][j-1])
                        datomatriz[i,j]=numero
                        count=count+2
                    else:
                        numero=int(arreglo[i][j])-int(arreglo[i][j-1])
                        datomatriz[i,j]=numero
        
            for i in range(0,10):
                for j in range(0,10):
                    matrizsec=Label(frameMatrizsec, text=datomatriz[j][i])
                    matrizsec.place(relx=0.09*i,rely=0.08*j)
            labelMatrizsec.config(bg="green")

            matrizpositiva=numpy.zeros(a,dtype=int)
            for i in range(0,10):
                for j in range(0,10):
                    if int(datomatriz[i][j])<0:
                        matrizpositiva[i][j]=-1*datomatriz[i][j]
                    else:
                        matrizpositiva[i][j]=datomatriz[i][j]
            #print(matrizpositiva)

 
            mayor=matrizpositiva[0][0]
            mayor2=matrizpositiva[0][0]
            for fila in matrizpositiva:
                for valor in fila:
                    if valor > mayor:
                        mayor = valor
                        mayor2=valor
            listcharmax=''
            while mayor != 0:
                modulo=mayor%2
                cociente=mayor//2
                listcharmax=str(modulo)+listcharmax
                mayor=cociente
            bitsuma=len(listcharmax)
            bitband=len(listcharmax)+1
            #print(bitband)

        
            trama=[]
            for i in range(0,10):
                    for j in range(0,10):
                        caracter=int(matrizpositiva[i][j])
                        trama.append(caracter)
            print(trama)

            tramaneg=[]
            for i in range(0,10):
                    for j in range(0,10):
                        caracter=int(datomatriz[i][j])
                        tramaneg.append(caracter)
            print(tramaneg)

            numerosbin=[]
            listbin=''
            for i in range(0,len(trama)):
                if trama[i]==0:
                    listbin='0'
                    while len(listbin)<bitband:
                        listbin='0'+listbin
                else:
                    while trama[i] !=0:
                        modulo=trama[i]%2
                        cociente=trama[i]//2
                        listbin=str(modulo)+listbin
                        trama[i]=cociente
                    while len(listbin)<bitsuma:
                        listbin='0'+listbin
                    if tramaneg[i]<0:
                        listbin='1'+listbin
                    else:
                        listbin='0'+listbin
                numerosbin.append(listbin)
                listbin=''
            print(numerosbin)
            print(mayor)
            labelbitschar=Label(ventanatrama, text="el numero mayor es: ")
            labelbitschar.place(x=650,y=20)
            labelbitschar_res=Label(ventanatrama, text=mayor2)
            labelbitschar_res.place(x=800,y=20)
            labelmayor=Label(ventanatrama, text="el numero total de bits es: ")
            labelmayor.place(x=650,y=60)
            labelmayor_res=Label(ventanatrama, text=bitband)
            labelmayor_res.place(x=800,y=60)
            labeltramada=Label(Ventana_principal, text="Trama resultante ")
            labeltramada.grid(row=4,column=3)
            contador=0
            fila=5
            i=0
            while contador <= 20: 
                labelCodificacion_res=Label(Ventana_principal,text=numerosbin[i:i+5])
                i=i+5
                labelCodificacion_res.grid(row=fila,column=3)
                fila= fila+1
                contador=contador+1

            totalstr=""
            for i in range(0, len(numerosbin)):
                totalstr=totalstr+str(numerosbin[i])
                
            totalstr2=""
            for i in range(0, 25):
                totalstr2=totalstr2+totalstr[i]
            jamin(totalstr2)


        if lectura==3:
            numero=0
            caracter=int(zigzag[0,0])
            datomatriz=numpy.zeros(a,dtype=int)
            count=0
            for i in range(0,10):
                if count>1:
                    numero=int(zigzag[i][0])-int(zigzag[i-1][9])
                    datomatriz[i,0]=numero
                for j in range(1,10):
                    if count<1:
                        datomatriz[0][0]=zigzag[0][0]
                        numero=int(zigzag[i][j])-int(zigzag[i][j-1])
                        datomatriz[i,j]=numero
                        count=count+2
                    else:
                        numero=int(zigzag[i][j])-int(zigzag[i][j-1])
                        datomatriz[i,j]=numero
        
            for i in range(0,10):
                for j in range(0,10):
                    matrizsec=Label(frameMatrizsec, text=datomatriz[j][i])
                    matrizsec.place(relx=0.09*i,rely=0.08*j)
            labelMatrizsec.config(bg="green")

            matrizpositiva=numpy.zeros(a,dtype=int)
            for i in range(0,10):
                for j in range(0,10):
                    if int(datomatriz[i][j])<0:
                        matrizpositiva[i][j]=-1*datomatriz[i][j]
                    else:
                        matrizpositiva[i][j]=datomatriz[i][j]

 
            mayor=matrizpositiva[0][0]
            mayor2=matrizpositiva[0][0]
            for fila in matrizpositiva:
                for valor in fila:
                    if valor > mayor:
                        mayor = valor
                        mayor2=valor
            listcharmax=''
            while mayor != 0:
                modulo=mayor%2
                cociente=mayor//2
                listcharmax=str(modulo)+listcharmax
                mayor=cociente
            bitsuma=len(listcharmax)
            bitband=len(listcharmax)+1

        
            trama=[]
            for i in range(0,10):
                    for j in range(0,10):
                        caracter=int(matrizpositiva[i][j])
                        trama.append(caracter)

            tramaneg=[]
            for i in range(0,10):
                    for j in range(0,10):
                        caracter=int(datomatriz[i][j])
                        tramaneg.append(caracter)

            numerosbin=[]
            listbin=''
            for i in range(0,len(trama)):
                if trama[i]==0:
                    listbin='0'
                    while len(listbin)<bitband:
                        listbin='0'+listbin
                else:
                    while trama[i] !=0:
                        modulo=trama[i]%2
                        cociente=trama[i]//2
                        listbin=str(modulo)+listbin
                        trama[i]=cociente
                    while len(listbin)<bitsuma:
                        listbin='0'+listbin
                    if tramaneg[i]<0:
                        listbin='1'+listbin
                    else:
                        listbin='0'+listbin
                numerosbin.append(listbin)
                listbin=''
            labelbitschar=Label(ventanatrama, text="el numero mayor es: ")
            labelbitschar.place(x=650,y=20)
            labelbitschar_res=Label(ventanatrama, text=mayor2)
            labelbitschar_res.place(x=800,y=20)
            labelmayor=Label(ventanatrama, text="el numero total de bits es: ")
            labelmayor.place(x=650,y=60)
            labelmayor_res=Label(ventanatrama, text=bitband)
            labelmayor_res.place(x=800,y=60)
            labeltramada=Label(Ventana_principal, text="Trama resultante ")
            labeltramada.grid(row=4,column=3)
            contador=0
            fila=5
            i=0
            while contador <= 20: 
                labelCodificacion_res=Label(Ventana_principal,text=numerosbin[i:i+5])
                i=i+5
                labelCodificacion_res.grid(row=fila,column=3)
                fila= fila+1
                contador=contador+1
            print(numerosbin)
            totalstr=""
            for i in range(0, len(numerosbin)):
                totalstr=totalstr+str(numerosbin[i])

            totalstr2=""
            for i in range(0, 25):
                totalstr2=totalstr2+totalstr[i]
            jamin(totalstr2)



             
BotonAleatorio=Button(Ventana_principal, text="Llenar matriz y codificar",width=20, command=lambda : Boton_Aleatorio())
BotonAleatorio.grid(row=4,column=1,padx=10,pady=20)
Boton_horizontal=Radiobutton(Ventana_principal, text="Horizontal", variable=seleccion, value=1, command=Boton_radio)
Boton_horizontal.grid(row=2,column=0)
Boton_vertical=Radiobutton(Ventana_principal, text="Vertical", variable=seleccion, value=2,command=Boton_radio)
Boton_vertical.grid(row=2,column=2)
Boton_zigzag=Radiobutton(Ventana_principal, text="ZigZag", variable=seleccion, value=3,command=Boton_radio)
Boton_zigzag.grid(row=2,column=4)
Ventana_principal.mainloop()