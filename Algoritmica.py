#Codificacion Algoritmica de Daniel Ballesteros y Kevin Niño
from collections import Counter
from tkinter import Entry, Image, Label, LabelFrame, Tk,Text,Button,StringVar,PhotoImage,Canvas, Toplevel,Frame
import math
import re
import operator




Ventana_principal=Tk()

Ventana_principal.title("Codigo Algoritmico")
TituloVentana_principal=Label(Ventana_principal, text="Codificación Algoritmica", bd=10, fg='black',bg=("cyan"), font=16)
TituloVentana_principal.grid(row=0, column=1,padx=20,pady=20)
label=Label(Ventana_principal, text="Porfavor seleccione la base que desea utilizar")
label.grid(row=1, column=1,padx=20,pady=20)

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
    labeltramaresultante=Label(ventana_matriz, text='Su trama resultante es: '+ Trama)
    labeltramaresultante.place(x=60,y=200)
    print (Trama)

def base_6():
    Ventana_base_6=Toplevel()
    Mensaje_base_6=StringVar()
    TituloVentana_base_6=Label(Ventana_base_6, text="Base 6", bd=10, fg='black', font=("sans",16))
    TituloVentana_base_6.grid(row=0, column=1,padx=20)
    Label_base6=Label(Ventana_base_6, text="Su Alfabeto para base 6 sera: ",bd=10, fg='black', font=("sans",12))
    Label_base6.grid(row=1,column=1)
    Label_Alfabeto6=Label(Ventana_base_6, text="a b c d e f ",bd=10, fg='black', bg="cyan", font=("sans",12))
    Label_Alfabeto6.grid(row=2,column=1)
    Label_texto6=Label(Ventana_base_6, text="Digite la trama entre 7 y 12 caracteres")
    Label_texto6.grid(row=3,column=1)
    Trama6=Entry(Ventana_base_6,textvariable=Mensaje_base_6, width=50)
    Trama6.grid(row=4,column=1,padx=10,pady=10)
    Label_Asignacion=Label(Ventana_base_6, text=" El mensaje en base 6 es ")
    Label_Asignacion.grid(row=6,column=1,padx=20,pady=20)
    Label_Asignacion_res=Label(Ventana_base_6, text="")
    Label_Asignacion_res.grid(row=7,column=1)
    Label_msj_6=Label(Ventana_base_6, text="el mensaje en decimal es: ")
    Label_msj_6.grid(row=8,column=1,padx=20,pady=20)
    Label_msj_6_res=Label(Ventana_base_6, text="")
    Label_msj_6_res.grid(row=9,column=1)
    Label_bin_6=Label(Ventana_base_6, text="Su mensaje en binario es :")
    Label_bin_6.grid(row=10,column=1,padx=20,pady=20)
    Label_bin_6_res=Label(Ventana_base_6, text="")
    Label_bin_6_res.grid(row=11,column=1)
    Label_redondeo_6=Label(Ventana_base_6, text="El numero que permitio el redondeo es :")
    Label_redondeo_6.grid(row=12,column=1,padx=20,pady=20)
    Label_redondeo_6_res=Label(Ventana_base_6, text="")
    Label_redondeo_6_res.grid(row=13,column=1)

    def boton_6():
        Trama=Mensaje_base_6.get()
        Len6=len(Trama)
        if (Len6<7):
            Label_texto6.configure(text="Su trama es menor de 7 caracteres")
            Label_Asignacion_res.configure(text="No se pudo obtener la asignacion a los caracteres")
            Label_msj_6_res.configure(text="no se pudo obtener el mensaje en base 6")
            Label_bin_6_res.configure(text="no se pudo obtener el mensaje en binario")
            Label_redondeo_6_res.configure(text="no se pudo obtener el numero que permitio el redondeo")
            a=1
        else:
            if(Len6>12):
                Label_texto6.configure(text="Su trama es mayor de 12 caracteres")
                Label_Asignacion_res.configure(text="No se pudo obtener la asignacion a los caracteres")
                Label_msj_6_res.configure(text="no se pudo obtener el mensaje en base 6")
                Label_bin_6_res.configure(text="no se pudo obtener el mensaje en binario")
                Label_redondeo_6_res.configure(text="no se pudo obtener el numero que permitio el redondeo")
                a=1
            else:
                for i in range(len(Trama)):
                    if(Trama[i]=="a" or Trama[i]=="b" or Trama[i]=="c" or Trama[i]=="d" or Trama[i]=="e" or Trama[i]=="f"):
                        a=0
                    else:
                        a=1
                if(a==1):
                    Label_texto6.configure(text="Su trama no posee los caracteres del alfabeto")
                    Label_Asignacion_res.configure(text="No se pudo obtener la asignacion a los caracteres")
                    Label_msj_6_res.configure(text="no se pudo obtener el mensaje en base 6")
                    Label_bin_6_res.configure(text="no se pudo obtener el mensaje en binario")
                    Label_redondeo_6_res.configure(text="no se pudo obtener el numero que permitio el redondeo")
                else:
                    Label_texto6.configure(text="Su trama si es valida para la codificacion")

                    patron = r'(\w)'
                    Trama = re.sub(patron, r'\1 ', Mensaje_base_6.get())
                    Trama = Mensaje_base_6.get().lower()
                    Dicc_Base6={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5}
                    d="0."
                    e=""
                    for i in range(Len6):
                        if (Trama[i]=='a'):
                            b=Dicc_Base6['a']
                            c= str(b)
                        if (Trama[i]=='b'):
                            b=Dicc_Base6['b']
                            c= str(b)
                        if (Trama[i]=='c'):
                            b=Dicc_Base6['c']
                            c= str(b)
                        if (Trama[i]=='d'):
                            b=Dicc_Base6['d']
                            c= str(b)
                        if (Trama[i]=='e'):
                            b=Dicc_Base6['e']
                            c= str(b)
                        if (Trama[i]=='f'):
                            b=Dicc_Base6['f']
                            c= str(b)
                        e= e+ c
                    d=d+e
                    Label_Asignacion_res.configure(text=d)
                    Lista_Asig=list(e)
                    SumDec=float(0)
                    Longitud=len(e)
                    for i in range(Longitud):
                        SumDec = SumDec + (int(Lista_Asig[i])*pow(6,-(i+1)))
                    Label_msj_6_res.configure(text=SumDec)
                    Decimal=SumDec 
                    Multiplicacion=0
                    Entero=0
                    Validacion=0
                    Numform=0
                    Potencia=0
                    d="0."
                    ResBin=""
                    cont=0
                    Resp=0
                    bin_base_6=0
                    int_base_6=0
                    resp_base_6=0
                    Res_Bin_6=0
                    aproximacion=0
                    suma=0
                    longitud=len(str(e))-1
                    while cont <= len(str(Decimal)):
                        Potencia=Potencia-1
                        Multiplicacion=Decimal*2
                        Entero=int(Multiplicacion)
                        Decimal=Multiplicacion-Entero
                        Validacion=pow(2,Potencia)
                        Numform=Entero*Validacion
                        Resp= Resp + Numform
                        resp_base_6=Resp
                        if Entero==1:
                            prueba=""
                            for i in range(longitud):
                                bin_base_6=resp_base_6*6
                                int_base_6=int(bin_base_6)
                                resp_base_6= bin_base_6-int_base_6
                                prueba = prueba + str(int_base_6)
                        ResBin= ResBin + str(Entero)
                        cont= cont+1
                    d= d + ResBin  
                    Label_bin_6_res.configure(text=d)
                    Label_redondeo_6_res.configure(text=bin_base_6)
                print(ResBin)
                jamin(ResBin)            

    Boton_cod_6=Button(Ventana_base_6, text="Codificacion",width=20,command=lambda : boton_6())
    Boton_cod_6.grid(row=5,column=1)
            
def base_7():
    Ventana_base_7=Toplevel()
    Mensaje_base_7=StringVar()
    TituloVentana_base_7=Label(Ventana_base_7, text="Base 7", bd=10, fg='black', font=("sans",16))
    TituloVentana_base_7.grid(row=0, column=1,padx=20)
    Label_base7=Label(Ventana_base_7, text="Su Alfabeto para base 7 sera: ",bd=10, fg='black', font=("sans",12))
    Label_base7.grid(row=1,column=1)
    Label_Alfabeto7=Label(Ventana_base_7, text="a b c d e f g ",bd=10, fg='black', bg="cyan", font=("sans",12))
    Label_Alfabeto7.grid(row=2,column=1)
    Label_texto7=Label(Ventana_base_7, text="Digite la trama entre 7 y 12 caracteres")
    Label_texto7.grid(row=3,column=1)
    Trama7=Entry(Ventana_base_7,textvariable=Mensaje_base_7, width=50)
    Trama7.grid(row=4,column=1,padx=10,pady=10)
    Label_Asignacion=Label(Ventana_base_7, text=" El mensaje en base 6 es ")
    Label_Asignacion.grid(row=6,column=1,padx=20,pady=20)
    Label_Asignacion_res=Label(Ventana_base_7, text="")
    Label_Asignacion_res.grid(row=7,column=1)
    Label_msj_7=Label(Ventana_base_7, text="el mensaje en decimal es: ")
    Label_msj_7.grid(row=8,column=1,padx=20,pady=20)
    Label_msj_7_res=Label(Ventana_base_7, text="")
    Label_msj_7_res.grid(row=9,column=1)
    Label_bin_7=Label(Ventana_base_7, text="Su mensaje en binario es :")
    Label_bin_7.grid(row=10,column=1,padx=20,pady=20)
    Label_bin_7_res=Label(Ventana_base_7, text="")
    Label_bin_7_res.grid(row=11,column=1)
    Label_redondeo_7=Label(Ventana_base_7, text="El numero que permitio el redondeo es :")
    Label_redondeo_7.grid(row=12,column=1,padx=20,pady=20)
    Label_redondeo_7_res=Label(Ventana_base_7, text="")
    Label_redondeo_7_res.grid(row=13,column=1)
    def boton_7():
        Trama=Mensaje_base_7.get()
        Len7=len(Trama)
        if (Len7<7):
            Label_texto7.configure(text="Su trama es menor de 7 caracteres")
            Label_Asignacion_res.configure(text="No se pudo obtener la asignacion a los caracteres")
            Label_msj_7_res.configure(text="no se pudo obtener el mensaje en base 7")
            Label_bin_7_res.configure(text="no se pudo obtener el mensaje en binario")
            Label_redondeo_7_res.configure(text="no se pudo obtener el numero que permitio el redondeo")
            a=1
        else:
            if(Len7>12):
                Label_texto7.configure(text="Su trama es mayor de 12 caracteres")
                Label_Asignacion_res.configure(text="No se pudo obtener la asignacion a los caracteres")
                Label_msj_7_res.configure(text="no se pudo obtener el mensaje en base 6")
                Label_bin_7_res.configure(text="no se pudo obtener el mensaje en binario")
                Label_redondeo_7_res.configure(text="no se pudo obtener el numero que permitio el redondeo")
                a=1
            else:
                for i in range(len(Trama)):
                    if(Trama[i]=="a" or Trama[i]=="b" or Trama[i]=="c" or Trama[i]=="d" or Trama[i]=="e" or Trama[i]=="f" or Trama[i]=="g"):
                        a=0
                    else:
                        a=1
                if(a==1):
                    Label_texto7.configure(text="Su trama no posee los caracteres del alfabeto")
                    Label_Asignacion_res.configure(text="No se pudo obtener la asignacion a los caracteres")
                    Label_msj_7_res.configure(text="no se pudo obtener el mensaje en base 6")
                    Label_bin_7_res.configure(text="no se pudo obtener el mensaje en binario")
                    Label_redondeo_7_res.configure(text="no se pudo obtener el numero que permitio el redondeo")
                else:
                    Label_texto7.configure(text="Su trama si es valida para la codificacion")

                    patron = r'(\w)'
                    Trama = re.sub(patron, r'\1 ', Mensaje_base_7.get())
                    Trama = Mensaje_base_7.get().lower()
                    Dicc_Base7={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6}
                    d="0."
                    e=""
                    for i in range(Len7):
                        if (Trama[i]=='a'):
                            b=Dicc_Base7['a']
                            c= str(b)
                        if (Trama[i]=='b'):
                            b=Dicc_Base7['b']
                            c= str(b)
                        if (Trama[i]=='c'):
                            b=Dicc_Base7['c']
                            c= str(b)
                        if (Trama[i]=='d'):
                            b=Dicc_Base7['d']
                            c= str(b)
                        if (Trama[i]=='e'):
                            b=Dicc_Base7['e']
                            c= str(b)
                        if (Trama[i]=='f'):
                            b=Dicc_Base7['f']
                            c= str(b)
                        if (Trama[i]=='g'):
                            b=Dicc_Base7['g']
                            c=str(b)
                        e= e+ c
                    d=d+e
                    Label_Asignacion_res.configure(text=d)
                    Lista_Asig=list(e)
                    SumDec=float(0)
                    Longitud=len(e)
                    for i in range(Longitud):
                        SumDec = SumDec + (int(Lista_Asig[i])*pow(7,-(i+1)))
                    Label_msj_7_res.configure(text=SumDec)
                    Decimal=SumDec 
                    Multiplicacion=0
                    Entero=0
                    Validacion=0
                    Numform=0
                    Potencia=0
                    d="0."
                    ResBin=""
                    cont=0
                    Resp=0
                    bin_base_7=0
                    int_base_7=0
                    resp_base_7=0
                    Res_Bin_7=0
                    aproximacion=0
                    suma=0
                    longitud=len(str(e))-1
                    while cont <= len(str(Decimal)):
                        Potencia=Potencia-1
                        Multiplicacion=Decimal*2
                        Entero=int(Multiplicacion)
                        Decimal=Multiplicacion-Entero
                        Validacion=pow(2,Potencia)
                        Numform=Entero*Validacion
                        Resp= Resp + Numform
                        resp_base_7=Resp
                        if Entero==1:
                            prueba=""
                            for i in range(longitud):
                                bin_base_7=resp_base_7*7
                                int_base_7=int(bin_base_7)
                                resp_base_7= bin_base_7-int_base_7
                                prueba = prueba + str(int_base_7)
                        ResBin= ResBin + str(Entero)
                        cont= cont+1
                    d= d + ResBin  
                    Label_bin_7_res.configure(text=d)
                    Label_redondeo_7_res.configure(text=bin_base_7)
                    jamin(ResBin)  


    Boton_cod_7=Button(Ventana_base_7, text="Codificacion",width=20,command=lambda : boton_7())
    Boton_cod_7.grid(row=5,column=1)

def base_8():
    Ventana_base_8=Toplevel()
    Mensaje_base_8=StringVar()
    TituloVentana_base_8=Label(Ventana_base_8, text="Base 8", bd=10, fg='black', font=("sans",16))
    TituloVentana_base_8.grid(row=0, column=1,padx=20)
    Label_base8=Label(Ventana_base_8, text="Su Alfabeto para base 8 sera: ",bd=10, fg='black', font=("sans",12))
    Label_base8.grid(row=1,column=1)
    Label_Alfabeto8=Label(Ventana_base_8, text="a b c d e f g h ",bd=10, fg='black', bg="cyan", font=("sans",12))
    Label_Alfabeto8.grid(row=2,column=1)
    Label_texto8=Label(Ventana_base_8, text="Digite la trama entre 7 y 12 caracteres")
    Label_texto8.grid(row=3,column=1)
    Trama8=Entry(Ventana_base_8,textvariable=Mensaje_base_8, width=50)
    Trama8.grid(row=4,column=1,padx=10,pady=10)
    Label_Asignacion=Label(Ventana_base_8, text=" El mensaje en base 8 es ")
    Label_Asignacion.grid(row=6,column=1,padx=20,pady=20)
    Label_Asignacion_res=Label(Ventana_base_8, text="")
    Label_Asignacion_res.grid(row=7,column=1)
    Label_msj_8=Label(Ventana_base_8, text="el mensaje en decimal es: ")
    Label_msj_8.grid(row=8,column=1,padx=20,pady=20)
    Label_msj_8_res=Label(Ventana_base_8, text="")
    Label_msj_8_res.grid(row=9,column=1)
    Label_bin_8=Label(Ventana_base_8, text="Su mensaje en binario es :")
    Label_bin_8.grid(row=10,column=1,padx=20,pady=20)
    Label_bin_8_res=Label(Ventana_base_8, text="")
    Label_bin_8_res.grid(row=11,column=1)
    Label_redondeo_8=Label(Ventana_base_8, text="El numero que permitio el redondeo es :")
    Label_redondeo_8.grid(row=12,column=1,padx=20,pady=20)
    Label_redondeo_8_res=Label(Ventana_base_8, text="")
    Label_redondeo_8_res.grid(row=13,column=1)
    def boton_8():
        Trama=Mensaje_base_8.get()
        Len8=len(Trama)
        if (Len8<7):
            Label_texto8.configure(text="Su trama es menor de 7 caracteres")
            Label_Asignacion_res.configure(text="No se pudo obtener la asignacion a los caracteres")
            Label_msj_8_res.configure(text="no se pudo obtener el mensaje en base 8")
            Label_bin_8_res.configure(text="no se pudo obtener el mensaje en binario")
            Label_redondeo_8_res.configure(text="no se pudo obtener el numero que permitio el redondeo")
            a=1
        else:
            if(Len8>12):
                Label_texto8.configure(text="Su trama es mayor de 12 caracteres")
                Label_Asignacion_res.configure(text="No se pudo obtener la asignacion a los caracteres")
                Label_msj_8_res.configure(text="no se pudo obtener el mensaje en base 8")
                Label_bin_8_res.configure(text="no se pudo obtener el mensaje en binario")
                Label_redondeo_8_res.configure(text="no se pudo obtener el numero que permitio el redondeo")
                a=1
            else:
                for i in range(len(Trama)):
                    if(Trama[i]=="a" or Trama[i]=="b" or Trama[i]=="c" or Trama[i]=="d" or Trama[i]=="e" or Trama[i]=="f" or Trama[i]=="g" or Trama[i]=="h"):
                        a=0
                    else:
                        a=1
                if(a==1):
                    Label_texto8.configure(text="Su trama no posee los caracteres del alfabeto")
                    Label_Asignacion_res.configure(text="No se pudo obtener la asignacion a los caracteres")
                    Label_msj_8_res.configure(text="no se pudo obtener el mensaje en base 8")
                    Label_bin_8_res.configure(text="no se pudo obtener el mensaje en binario")
                    Label_redondeo_8_res.configure(text="no se pudo obtener el numero que permitio el redondeo")
                else:
                    Label_texto8.configure(text="Su trama si es valida para la codificacion")

                    patron = r'(\w)'
                    Trama = re.sub(patron, r'\1 ', Mensaje_base_8.get())
                    Trama = Mensaje_base_8.get().lower()
                    Dicc_Base8={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
                    d="0."
                    e=""
                    for i in range(Len8):
                        if (Trama[i]=='a'):
                            b=Dicc_Base8['a']
                            c= str(b)
                        if (Trama[i]=='b'):
                            b=Dicc_Base8['b']
                            c= str(b)
                        if (Trama[i]=='c'):
                            b=Dicc_Base8['c']
                            c= str(b)
                        if (Trama[i]=='d'):
                            b=Dicc_Base8['d']
                            c= str(b)
                        if (Trama[i]=='e'):
                            b=Dicc_Base8['e']
                            c= str(b)
                        if (Trama[i]=='f'):
                            b=Dicc_Base8['f']
                            c= str(b)
                        if (Trama[i]=='g'):
                            b=Dicc_Base8['g']
                            c=str(b)
                        if (Trama[i]=='h'):
                            b=Dicc_Base8['h']
                            c=str(b)
                        e= e+ c
                    d=d+e
                    Label_Asignacion_res.configure(text=d)
                    Lista_Asig=list(e)
                    SumDec=float(0)
                    Longitud=len(e)
                    for i in range(Longitud):
                        SumDec = SumDec + (int(Lista_Asig[i])*pow(8,-(i+1)))
                    Label_msj_8_res.configure(text=SumDec)
                    Decimal=SumDec 
                    Multiplicacion=0
                    Entero=0
                    Validacion=0
                    Numform=0
                    Potencia=0
                    d="0."
                    ResBin=""
                    cont=0
                    Resp=0
                    bin_base_8=0
                    int_base_8=0
                    resp_base_8=0
                    Res_Bin_8=0
                    aproximacion=0
                    suma=0
                    longitud=len(str(e))-1
                    while cont <= len(str(Decimal)):
                        Potencia=Potencia-1
                        Multiplicacion=Decimal*2
                        Entero=int(Multiplicacion)
                        Decimal=Multiplicacion-Entero
                        Validacion=pow(2,Potencia)
                        Numform=Entero*Validacion
                        Resp= Resp + Numform
                        resp_base_8=Resp
                        if Entero==1:
                            prueba=""
                            for i in range(longitud):
                                bin_base_8=resp_base_8*8
                                int_base_8=int(bin_base_8)
                                resp_base_8= bin_base_8-int_base_8
                                prueba = prueba + str(int_base_8)
                        ResBin= ResBin + str(Entero)
                        cont= cont+1
                    d= d + ResBin  
                    Label_bin_8_res.configure(text=d)
                    Label_redondeo_8_res.configure(text=bin_base_8)
                print(ResBin)
                jamin(ResBin)  
             


    Boton_cod_8=Button(Ventana_base_8, text="Codificacion",width=20,command=lambda : boton_8())
    Boton_cod_8.grid(row=5,column=1)


Boton_base6=Button(Ventana_principal, text="Base 6", width=20,command=lambda : base_6())
Boton_base6.grid(row=2, column=0,padx=20,pady=20)
Boton_base7=Button(Ventana_principal, text="Base 7", width=20,command=lambda : base_7())
Boton_base7.grid(row=2, column=1,padx=20,pady=20)
Boton_base8=Button(Ventana_principal, text="Base 8", width=20,command=lambda : base_8())
Boton_base8.grid(row=2, column=2,padx=20,pady=20)
Ventana_principal.mainloop()