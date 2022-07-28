#Codificacion Huffman de Daniel Ballesteros Y Kevin Niño
from tkinter import Entry, Image, Label, LabelFrame, Tk,Text,Button,StringVar,PhotoImage,Canvas,Toplevel,Frame
from time import sleep
from tkinter.constants import INSERT
import math
import operator

ventana_principal=Tk()
trama=StringVar()
ventana_principal.title('Codigo Shannon fano')
label=Label(text='ingrese una trama palindroma para el codigo shannon fanon sin espacios: ')
label.grid(row=0,column=1,columnspan=5,padx=20,pady=2,)
pantalla=Entry(ventana_principal,textvariable=trama, state='normal',width=40,background='white',foreground='black')
pantalla.grid(row=1,column=1,columnspan=5,padx=20,pady=20)
texto=trama.get()

#Se crea la funcion que va a suceder al momento de oprimir el boton la cual contiene la mayor parte del codigo
def click_boton():
    #se verifica que la trama sea menor de 25 digitos
    if len(trama.get())>25:
        label3=Label(text='digite una trama menor de 25 digitos')
        label3.grid(row=3,column=5,columnspan=5,padx=20,pady=2)
    else:
        #se verifica que la trama sea una palabrapalindroma
        if str(trama.get())!=str(trama.get())[::-1]:
            label3=Label(text='digite una palabra palindroma')
            label3.grid(row=2,column=5,columnspan=5,padx=20,pady=2)
        else: 
            #se crea la funcion la cual va a crear el diccionario que va a contener el codigo shannon fano   
            def contenedor(trama):
                caracteres=list(trama)
                diccionario={}
                for caracter in range(len(caracteres)):
                    diccionario[trama[caracter]]=0
                return diccionario
            #Se crea la funcion que realiza el ordenamiento generando tambien las frecuencias de cada letra
            def ordenamiento(trama):
                caracteres=list(trama)
                diccionario={}
                for posicion in range(len(caracteres)):
                    repeticiones=0
                    for caracter in range(len(caracteres)):
                        if caracteres[posicion] == caracteres[caracter]:
                            repeticiones=repeticiones+1
                        else:
                            repeticiones=repeticiones
                    diccionario[caracteres[posicion]]=repeticiones
                diccionario=sorted(diccionario.items(),key=operator.itemgetter(1), reverse=True)
                #se crean los label con las frecuencias
                cartel3=Label(text='FRECUENCIAS')
                cartel3.grid(row=5,column=1,columnspan=5,padx=20,pady=2)
                cartel4=Label(text=diccionario)
                cartel4.grid(row=6,column=1,columnspan=5,padx=20,pady=2)
                return diccionario
            #se crea la funcion la cual va a contener el diccionario con la codificacion shannon
            def Shanon_codigo(contenido):
                for i in contenido:
                    contenido[i]=str(list(contenido[i])[1:len(list(contenido))])
                return contenido

            def codificacion (mitad,contenedor,frecuencia):
                digito=0
                if len(frecuencia)>1:
                    for key in dict(frecuencia):
                        contenedor[key]=(str(contenedor[key])+str(digito))
                        if key == mitad:
                            digito=1
                return contenedor

            #se crea la funcion en la cual se va a buscar la mitad de la trama en el diccionario      
            def encontrar_mitad(a_dict):
                frecuencia=dict(a_dict)
                Mitad=(sum(frecuencia.values())/2)
                suma=0
                suma_anterior=0
                last_key=0
                i=1
                for key in frecuencia:
                    suma_anterior=suma
                    suma=suma+frecuencia[key]
                    if(suma >= Mitad):

                        if abs(suma_anterior-Mitad) < abs(suma-Mitad):
                            return last_key
                        else:
                            return key

                    last_key=key
                    i=i+1
            #se crea la funcion que va a actualizar el diccionario con las mitades de la funcion anterior
            def Shannon_mitades(frecuencia,mitad):
                diccionario1={}
                diccionario2={}
                dictionary=dict(frecuencia)
                a=0
                for i in range(len(dictionary)):
                    if str(list(dictionary.items())[i][0])==str(mitad):
                        a=i
                diccionario1=dict(list(dictionary.items())[0:a+1])
                diccionario2=dict(list(dictionary.items())[a+1:len(dictionary)])
                return [diccionario1,diccionario2]

                
            frecuencia=ordenamiento(trama.get())
            Shannon_Fanon=[dict(frecuencia)]
            contenido=contenedor(trama.get())
            frecuencia_dict=dict(frecuencia)
            #se crea el diccionario probabilidad, el cual se ira actualizando con respecto al diccionario de frecuencias
            probabilidad={}
            for i in str(trama.get()):
                probabilidad[i] = frecuencia_dict[i]/float(len(trama.get()))
            #print(probabilidad)
    
        #Se crea la ecuacion para la entropia
            entropia=0
            for i in probabilidad:
                entropia= entropia + (-1*(probabilidad[i])*math.log2(probabilidad[i]))
            
            i=0
            #se hacen los llamados de las funciones mientras que el diccionario ordenado sea menor al tamaño de la trama
            while len(Shannon_Fanon) < (len(trama.get())):
                Shannon_Fanon[i]=sorted(Shannon_Fanon[i].items(),key=operator.itemgetter(1), reverse=True)
                diccionario_mitad=encontrar_mitad(Shannon_Fanon[i])
                contenido=codificacion(diccionario_mitad,contenido,Shannon_Fanon[i])
                shannon_mitad=Shannon_mitades(Shannon_Fanon[i],diccionario_mitad)
                Shannon_Fanon.append(dict(shannon_mitad[0]))
                Shannon_Fanon.append(dict(shannon_mitad[1]))
                i=i+1
            #se crea la variable cod la cual va a contener el codigo shannon fanon con la variable contenido la cual contiene la codificacion
            cod=Shanon_codigo(contenido)
            #Se crea las ecuaciones para longitud promedio y eficiencia,tasa de compresion
            longitudp=0
            for i in probabilidad:
                    longitudp=longitudp+(probabilidad[i]*len(cod[i]))

            eficiencia=entropia/longitudp

            cou=len(set(trama.get()))

            tasa=(math.log(cou,2)/longitudp)
            
            longitudes_minimas={}
            for i in probabilidad:
                longitudes_minimas[i]=(-1*math.log2(probabilidad[i]))
            #print(longitudes_minimas)

            #Se crean los label con los valores que van a ser mostrados en la interfaz
            cartel=Label(text='Codificacion Shannon fanon')
            cartel.grid(row=3,column=1,columnspan=5,padx=20,pady=2)
            cartel2=Label(text=cod)
            cartel2.grid(row=4,column=1,columnspan=5,padx=20,pady=2)
            cartel5=Label(text='PROBABILIDADES')
            cartel5.grid(row=7,column=1,columnspan=5,padx=20,pady=2)
            cartel6=Label(text=probabilidad)
            cartel6.grid(row=8,column=1,columnspan=5,padx=20,pady=2)
            cartel7=Label(text='ENTROPIA')
            cartel7.grid(row=9,column=1,columnspan=5,padx=20,pady=2)
            cartel8=Label(text=entropia)
            cartel8.grid(row=10,column=1,columnspan=5,padx=20,pady=2)
            cartel11=Label(text='LONGITUD PROMEDIO')
            cartel11.grid(row=13,column=1,columnspan=5,padx=20,pady=2)
            cartel12=Label(text=longitudp)
            cartel12.grid(row=14,column=1,columnspan=5,padx=20,pady=2)
            cartel13=Label(text='EFICIENCIA')
            cartel13.grid(row=15,column=1,columnspan=5,padx=20,pady=2)
            cartel14=Label(text=eficiencia)
            cartel14.grid(row=16,column=1,columnspan=5,padx=20,pady=2)
            cartel15=Label(text='TASA DE COMPRESION')
            cartel15.grid(row=17,column=1,columnspan=5,padx=20,pady=2)
            cartel16=Label(text=tasa)
            cartel16.grid(row=18,column=1,columnspan=5,padx=20,pady=2)
            cartel17=Label(text='Longitudes minimas')
            cartel17.grid(row=19,column=1,columnspan=5,padx=20,pady=2)
            cartel18=Label(text=longitudes_minimas)
            cartel18.grid(row=20,column=1,columnspan=5,padx=20,pady=2)
            tramafinal=list(map(cod.get,frecuencia_dict))
            print(tramafinal)
            totalstr=""
            for i in range(0, len(tramafinal)):
                totalstr=totalstr+tramafinal[i][2]
                totalstr=totalstr+tramafinal[i][7]
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
            print ("xd")
            
            
boton1=Button(ventana_principal, text='codificacion',width=9,height=1,command=click_boton)
boton1.grid(row=2,column=1,columnspan=5,padx=20,pady=1)
ventana_principal.mainloop()
