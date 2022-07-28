#Codificacion aritmetica de Daniel Ballesteros y Kevin Niño
from collections import Counter
from tkinter import Entry, Image, Label, LabelFrame, Tk,Text,Button,StringVar,PhotoImage,Canvas,Toplevel,Frame
import math
import re
import operator

Ventana_principal=Tk()
Ventana_principal.title("Codigo Aritmetico")
Texto=StringVar()
Probabilidad_a=StringVar()
Probabilidad_b=StringVar()
Probabilidad_c=StringVar()
Probabilidad_d=StringVar()
Probabilidad_e=StringVar()
label=Label(Ventana_principal, text="Ingrese la trama mayor que 5 digitos y  menor que 10 caracteres usando solo a,b,c,d,e:")
label.grid(row=0, column=0,)
Pantalla=Entry(Ventana_principal, textvariable=Texto, width=50)
Pantalla.grid(row=1, column=0)
probabilidades=Label(Ventana_principal, text=" Las probabilidades no pueden sumar mas de 1.")
probabilidades.grid(row=2, column=0)
Labela=Label(Ventana_principal, text=" Introduzca la probabilidad de a : ")
Labela.grid(row=3, column=0)
Entry_a=Entry(Ventana_principal, textvariable=Probabilidad_a, width=10)
Entry_a.grid(row=3, column=1)
Labelb=Label(Ventana_principal, text=" Introduzca la probabilidad de b: ")
Labelb.grid(row=4, column=0)
Entryb=Entry(Ventana_principal, textvariable=Probabilidad_b, width=10)
Entryb.grid(row=4, column=1)
Labelc=Label(Ventana_principal, text=" Introduzca la probabilidad de c : ")
Labelc.grid(row=5, column=0)
Entryc=Entry(Ventana_principal, textvariable=Probabilidad_c, width=10)
Entryc.grid(row=5, column=1)
Labeld=Label(Ventana_principal, text=" Introduzca la probabilidad de d: ")
Labeld.grid(row=6, column=0)
Entryd=Entry(Ventana_principal, textvariable=Probabilidad_d, width=10)
Entryd.grid(row=6, column=1)
Labele=Label(Ventana_principal, text=" Introduzca la probabilidad de e : ")
Labele.grid(row=7, column=0)
Entrye=Entry(Ventana_principal, textvariable=Probabilidad_e, width=10)
Entrye.grid(row=7, column=1)
Pantalla2=Label(Ventana_principal)
Pantalla2.grid(row=8, column=1) 
labelmin=Label(Ventana_principal, text=" Codificacion Limites Minimos ", bg="red")
labelmin.grid(row=10,column=0,pady=10)
labelmin_respuesta=Label(Ventana_principal, text=" ")
labelmin_respuesta.grid(row=11,column=0)
labelmax=Label(Ventana_principal, text=" Codificacion Limites Maximos ", bg="red")
labelmax.grid(row=13,column=0,pady=10)
labelmax_respuesta=Label(Ventana_principal, text=" ")
labelmax_respuesta.grid(row=14,column=0)
LabelDecodificacion=Label(Ventana_principal, text=" Decodificacion ",bg="red")
LabelDecodificacion.grid(row=16,column=0)
labeldecodificacion_respuesta=Label(Ventana_principal, text=" ")
labeldecodificacion_respuesta.grid(row=18,column=0)
LabelBinario=Label(Ventana_principal, text=" Redondeo Binario ",bg="red")
LabelBinario.grid(row=20,column=0)
LabelBinario_respuesta=Label(Ventana_principal, text="")
LabelBinario_respuesta.grid(row=21,column=0)

#Se crea la funcion que va a suceder al momento de oprimir el boton la cual contiene la mayor parte del codigo
def click_boton():
    i=1
    x=0
    Trama=Texto.get()
    len1=len(Trama)
    if(len1<5):
        label.configure(text="Su Trama es de menos de 5 caracteres")
        labeldecodificacion_respuesta.configure(text=" No se pudieron obtener los valores de la decodificacion ")
        labelmin_respuesta.configure(text=" No se pudieron obtener los valores minimos ")
        labelmax_respuesta.configure(text=" No se pudieron obtener los valores maximos ")
        LabelBinario_respuesta.configure(text= "No se puede obtener el valor binario ")
        labelmin.configure(bg="red")
        labelmax.configure(bg="red")
        LabelDecodificacion.configure(bg="red")
        LabelBinario.configure(bg="red")
        c=1
    else:
        if(len1>10):
                label.configure(text="Su Trama es de más de 10 caracteres")
                labeldecodificacion_respuesta.configure(text=" No se pudieron obtener los valores de la decodificacion ")
                labelmin_respuesta.configure(text=" No se pudieron obtener los valores minimos ")
                labelmax_respuesta.configure(text=" No se pudieron obtener los valores maximos ")
                LabelBinario_respuesta.configure(text= "No se puede obtener el valor binario ")
                labelmin.configure(bg="red")
                labelmax.configure(bg="red")
                LabelDecodificacion.configure(bg="red")
                LabelBinario.configure(bg="red")
                c=1
        else:
            for i in range(len(Trama)):
                if(Trama[i]=="a" or Trama[i]=="b" or Trama[i]=="c" or Trama[i]=="d" or Trama[i]=="e"):            
                    c=0
                else:
                    c=1
            if (c==1):
                label.configure(text="Su palabra no posee los caracteres indicados  ")
                labeldecodificacion_respuesta.configure(text=" No se pudieron obtener los valores de la decodificacion ")
                labelmin_respuesta.configure(text=" No se pudieron obtener los valores minimos ")
                labelmax_respuesta.configure(text=" No se pudieron obtener los valores maximos ")
                LabelBinario_respuesta.configure(text= "No se puede obtener el valor binario ")
                labelmin.configure(bg="red")
                labelmax.configure(bg="red")
                LabelDecodificacion.configure(bg="red")
                LabelBinario.configure(bg="red")
            else:
                label.configure(text="Su palabra si posee los caracteres indicados  ")

                #Se cambian las letras a minusculas y se quitan los espacios
                palabra=Texto.get()
                Trama=palabra
                patron = r'(\w)'
                palabra = re.sub(patron, r'\1 ', palabra)
                palabra = palabra.lower() 
                listaPalabras = palabra.split()

                frecuenciaPalabra = []

                for i in listaPalabras:
                    frecuenciaPalabra.append(listaPalabras.count(i))   
                ProbabilidadLabela=("Probabilidad de a :  ",Probabilidad_a.get())
                ProbabilidadLabelb=("Probabilidad de b  :  ",Probabilidad_b.get())
                ProbabilidadLabelc=("Probabilidad de c  :  ",Probabilidad_c.get())
                ProbabilidadLabeld=("Probabilidad de d  :  ",Probabilidad_d.get())
                ProbabilidadLabele=("Probabilidad de e  :  ",Probabilidad_e.get())

                Labela.configure(text=ProbabilidadLabela)
                Labelb.configure(text=ProbabilidadLabelb)
                Labelc.configure(text=ProbabilidadLabelc)
                Labeld.configure(text=ProbabilidadLabeld)  
                Labele.configure(text=ProbabilidadLabele)
                    
                P_a=float(Probabilidad_a.get())
                P_b=float(Probabilidad_b.get())
                P_c=float(Probabilidad_c.get())
                P_d=float(Probabilidad_d.get())
                P_e=float(Probabilidad_e.get())
                
                P_TOTAL=P_a+P_b+P_c+P_d+P_e
                if(P_TOTAL!=1):
                    probabilidades.configure(text="la suma de las probabilidades no es de 1")
                    i=1
                else:
                    probabilidades.configure(text="la suma de las probabilidades si es de 1")
                    i=0
                if(i==0):
                    Minimos=[0,P_a,P_a+P_b,P_a+P_b+P_c,P_a+P_b+P_c+P_d]
                    Maximos=[P_a,P_a+P_b,P_a+P_b+P_c,P_a+P_b+P_c+P_d,P_a+P_b+P_c+P_d+P_e]
                    AMinimo=0
                    AMaximo=1
                    Min2=0
                    Max2=0
                    #Se crean las listas

                    CodificacionMin=list()
                    CodificacionMax=list()
                    ValoresMinimos=list()
                    ValoresMaximos=list()
                    lim=1

                    for i in range(len(listaPalabras)):               
                        if(listaPalabras[i]=="a"):
                            Max2=Max2+P_a
                            Min2=Max2-P_a
                        if(listaPalabras[i]=="b"):
                            Max2=Max2+P_b
                            Min2=Max2-P_b
                        if(listaPalabras[i]=="c"): 
                            Max2=Max2+P_c
                            Min2=Max2-P_c
                        if(listaPalabras[i]=="d"):
                            Max2=Max2+P_d
                            Min2=Max2-P_d
                        if(listaPalabras[i]=="e"):   
                            Max2=Max2+P_e 
                            Min2=Max2-P_e        
                        CodificacionMin.append("Minimo "+str(lim)+"")
                        CodificacionMax.append("Maximo "+str(lim)+"")
                        lim=lim+1
                    #aca recide la creacion de los limites inferiores y superiores nuevos
                        Inferior=AMinimo+((AMaximo-AMinimo)*Min2)
                        Superior=AMinimo+((AMaximo-AMinimo)*Max2)
                        AMinimo=Inferior
                        AMaximo=Superior
                        if(Superior==1):
                            i=10
                        ValoresMinimos.append(Inferior)
                        ValoresMaximos.append(Superior)
                        CodificacionMin.append(Inferior)
                        CodificacionMax.append(Superior)
                        
                    #Decodificacion
                    Minimos_decodificacion=ValoresMinimos[-1]
                    Maximos_decodificacion=ValoresMaximos[-1]
                    Decodificacion_inicial=list()
                    Decodificacion_final=list()
                    Decodificacion_inicial.append("A"+str(x))
                    Decodificacion_final.append("A"+str(x))        
                    Decodificacion_inicial.append(Minimos_decodificacion)        
                    Decodificacion_final.append(Minimos_decodificacion)
                    x=1     
                    min_1=0
                    min_2=P_a
                    min_3=P_a+P_b
                    min_4=P_a+P_b+P_c
                    min_5=P_a+P_b+P_c+P_d
                    min_6=P_a+P_b+P_c+P_d+P_e  

                    for i in range(len(Trama)):
                        count=0
                        count2=0            
                        for n in range(len(Maximos)):
                            if (min_2 >= Minimos_decodificacion) and (count==0):
                                Limite = min_2
                                count=count+1
                            if (min_3 >= Minimos_decodificacion) and (count==0):
                                Limite = min_3
                                count=count+1
                            if (min_4 >= Minimos_decodificacion) and (count==0):
                                Limite = min_4
                                count=count+1 
                            if (min_5 >= Minimos_decodificacion) and (count==0):
                                Limite = min_5
                                count=count+1
                            if (min_6 >= Minimos_decodificacion) and (count==0):
                                Limite = min_6
                                count=count+1

                        for n in range(len(Minimos)):
                            if (min_1 >= Minimos_decodificacion) and (count2==0):
                                Limite2=min_1
                                count2=count2+1
                            if (min_2 >= Minimos_decodificacion) and (count2==0):
                                Limite2 = min_1
                                count2=count2+1
                            if (min_3 >= Minimos_decodificacion) and (count2==0):
                                Limite2 = min_2
                                count2=count2+1
                            if (min_4 >= Minimos_decodificacion) and (count2==0):
                                Limite2 = min_3
                                count2=count2+1
                            if (min_5 >= Minimos_decodificacion) and (count2==0):
                                Limite2 = min_4
                                count2=count2+1
                            if (min_6 >= Minimos_decodificacion) and (count2==0):
                                Limite2 = min_5
                                count2=count2+1
                        Decodificacion_inicial.append("Inicial"+str(x))
                        Decodificacion_final.append("Codigo "+str(x))
                        a=(Maximos_decodificacion-Limite2)/(Limite-Limite2)
                        Maximos_decodificacion=a      
                        Minimos_decodificacion=Maximos_decodificacion
                        x=x+1
                        Decodificacion_inicial.append(a)
                        Decodificacion_final.append(a)  
                    Decodificacion_final.pop(-1) 
                    Decodificacion_final.pop(-1)
                    #REDONDEO BINARIO 
                    Decimal=Decodificacion_final[1]
                    ValBin=Decimal-int(Decimal)
                    Multiplicacion=0
                    Entero=0
                    Validacion=0
                    Potencia=-1
                    ResBin=list()
                    cont=0
                    Resp=0
                    while cont <= len(str(ValBin)):
                        Potencia=Potencia-1
                        Multiplicacion=Decimal*2
                        Entero=int(Multiplicacion)
                        Decimal=Multiplicacion-Entero
                        Validacion=pow(2,Potencia)
                        NumeroFormadoDecimal=Validacion*Entero
                        Resp=Resp+NumeroFormadoDecimal
                        cont=cont+1
                        ResBin.append(Entero)

                    labelmin_respuesta.configure(text=CodificacionMin)    
                    labelmax_respuesta.configure(text=CodificacionMax)  
                    labeldecodificacion_respuesta.configure(text=Decodificacion_final)
                    LabelBinario_respuesta.configure(text=ResBin)
                    labelmin.configure(bg="green")
                    labelmax.configure(bg="green")
                    LabelDecodificacion.configure(bg="green")
                    LabelBinario.configure(bg="green")
                else:
                    labeldecodificacion_respuesta.configure(text=" No se pudieron obtener los valores de la decodificacion ")
                    labelmin_respuesta.configure(text=" No se pudieron obtener los valores minimos ")
                    labelmax_respuesta.configure(text=" No se pudieron obtener los valores maximos ")
                    LabelBinario_respuesta.configure(text= "No se puede obtener el valor binario ")
                    labelmin.configure(bg="red")
                    labelmax.configure(bg="red")
                    LabelDecodificacion.configure(bg="red")
                    LabelBinario.configure(bg="red")
                print(ResBin)
                totalstr=""
                for i in range(0, len(ResBin)):
                    totalstr=totalstr+str(ResBin[i])
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

Boton1=Button(Ventana_principal, text="codificacion", width=20, command=lambda : click_boton())
Boton1.grid(row=9, column=0)
Ventana_principal.mainloop()