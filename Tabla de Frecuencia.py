import matplotlib.pyplot as plt
from matplotlib import style
from itertools import repeat
from tabulate import tabulate

# Para tablas con frecuencia ya definida
def F_determined():
    # Codigo igual a F_undetermined, lo unico diferente es la frecuencia la cual se determina con input()
    class sort:
        def __init__(self):
            # Frequency limits
            self.Flist = []
            self.f1L = None
            self.f2L = None
            self.f3L = None
            self.f4L = None
            self.f5L = None
            self.f6L = None
            self.f7L = None
            self.f8L = None
            self.f9L = None
            self.f10L = None

            # Frequency
            self.Flst = []
            self.f1 = None
            self.f2 = None
            self.f3 = None
            self.f4 = None
            self.f5 = None
            self.f6 = None
            self.f7 = None
            self.f8 = None
            self.f9 = None
            self.f10 = None
            self.fTotal = None

            # Limit
            self.quantity = []
            self.limit = None
            self.number = 0
            self.amplitud = None
            self.amount = None
            self.a = None

            # Punto Medio
            self.PMLst = []
            self.PM1 = ""
            self.PM2 = ""
            self.PM3 = ""
            self.PM4 = ""
            self.PM5 = ""
            self.PM6 = ""
            self.PM7 = ""
            self.PM8 = ""
            self.PM9 = ""
            self.PM10 = ""

            # Punto Medio * Frequencia
            self.PMFLst = []
            self.PMF1 = ""
            self.PMF2 = ""
            self.PMF3 = ""
            self.PMF4 = ""
            self.PMF5 = ""
            self.PMF6 = ""
            self.PMF7 = ""
            self.PMF8 = ""
            self.PMF9 = ""
            self.PMF10 = ""
            self.PMFTotal = ""

            # Frecuencia Acumulada
            self.faLst = []
            self.fa1 = ""
            self.fa2 = ""
            self.fa3 = ""
            self.fa4 = ""
            self.fa5 = ""
            self.fa6 = ""
            self.fa7 = ""
            self.fa8 = ""
            self.fa9 = ""
            self.fa10 = ""

            # Frecuencia Relativa
            self.frLst = []
            self.fr1 = ""
            self.fr2 = ""
            self.fr3 = ""
            self.fr4 = ""
            self.fr5 = ""
            self.fr6 = ""
            self.fr7 = ""
            self.fr8 = ""
            self.fr9 = ""
            self.fr10 = ""

            # Frecuencia relativa porcentual
            self.frPLst = []
            self.frP1 = ""
            self.frP2 = ""
            self.frP3 = ""
            self.frP4 = ""
            self.frP5 = ""
            self.frP6 = ""
            self.frP7 = ""
            self.frP8 = ""
            self.frP9 = ""
            self.frP10 = ""

            #clases
            self.claseLst = []
            self.clase1 = ""
            self.clase2 = ""
            self.clase3 = ""
            self.clase4 = ""
            self.clase5 = ""
            self.clase6 = ""
            self.clase7 = ""
            self.clase8 = ""
            self.clase9 = ""
            self.clase10 = ""

        def limits(self):
            self.a = int(input("Cuantas clases vas a usar?"))
            self.f1L = int(input("Escribe el minimo:"))
            self.amplitud = int(input("Escribe la amplitud:"))

            for i in range(1, self.a + 2):
                self.Flist.append(eval("self." + "f" + str(i) + "L"))

            for i in range(1, self.a + 1):
                self.Flist[i] = self.Flist[i-1] + self.amplitud

            for i in range(1, self.a + 1):
                self.claseLst.append(eval("self." + "clase" + str(i)))

            for i in range(self.a):
                self.claseLst[i] = self.Flist[i], self.Flist[i + 1]

        def Frecuencia(self):
            for i in range(1,self.a + 1):
                self.Flst.append(eval("self." + "f" + str(i)))
            for i in range(self.a):
                self.Flst[i] = int(input("Determina la frecuencia" + " " + str(i + 1) + ":"))

        def PuntoMedio(self):
            for i in range(1, self.a + 1):
                self.PMLst.append(eval("self." + "PM" + str(x)))
            for i in range(self.a):
                self.PMLst[i] = (self.Flist[i] + self.Flist[i + 1])/2

        def PMF(self):
            for i in range(1, self.a + 1):
                self.PMFLst.append(eval("self." + "PMF" + str(x)))
            for i in range(self.a):
                self.PMFLst[i] = self.Flst[i] * self.PMLst[i]

        def Fa(self):
            for i in range(1, self.a + 1):
                self.faLst.append(eval("self." + "fa" + str(x)))
            self.faLst[0] = self.Flst[0]
            for i in range(1,self.a):
                self.faLst[i] = self.faLst[i-1] + self.Flst[i]

        def Total(self):
            self.fTotal = max(self.faLst)
            self.PMFTotal = sum(self.PMFLst)

        def FrecuenciaRelativa(self):
            for i in range(1, self.a + 1):
                self.frLst.append(eval("self." + "fr" + str(i)))
                self.frPLst.append(eval("self." + "frP" + str(i)))
            for i in range(self.a):
                self.frLst[i] = self.Flst[i] / self.fTotal
                self.frPLst[i] = self.frLst[i] * 100

        def runall(self):
            self.limits()
            self.Frecuencia()
            self.PuntoMedio()
            self.PMF()
            self.Fa()
            self.Total()
            self.FrecuenciaRelativa()

    main = sort()
    main.runall()

    MediaA = main.PMFTotal / main.fTotal

    class mediana:
        def __init__(self):
            self.Mnumber = ""
            self.result = ""

        def Mediana(self):
            self.Mnumber = main.fTotal / 2

            if 0 <= self.Mnumber <= main.faLst[0]:
                self.result = main.PMLst[0]
            else:
                for i in range(main.a - 1):
                    if main.faLst[i] <= self.Mnumber <= main.faLst[i + 1]:
                        self.result = main.PMLst[i + 1]

    class moda:
        def __init__(self):
            self.ModaLst = []
            self.PMLst = []
            self.fHighest = ""
            self.result = ""
            self.result2 = None
            self.MoreThanOne = False
            self.x = ""

        def fTop(self):
            for i in range(main.a):
                self.ModaLst.append(main.Flst[i])
                self.PMLst.append(main.PMLst[i])

            self.fHighest = max(self.ModaLst)

            for i in range(main.a):
                if self.fHighest == self.ModaLst[i]:
                    self.result = self.PMLst[i]
                    del self.PMLst[i]
                    break

            self.ModaLst.remove(max(self.ModaLst))

            for i in range(main.a - 1):
                if self.fHighest == self.ModaLst[i]:
                    self.result2 = self.PMLst[i]
                    self.MoreThanOne = True
                    break

    mediana = mediana()
    mediana.Mediana()
    moda = moda()
    moda.fTop()

    def draw():
        info = {'Class': main.claseLst,
                'Frecuencia': main.Flst,
                'Punto Medio': main.PMLst,
                'PM * F': main.PMFLst,
                'Frecuencia Acumulada': main.faLst,
                'Fr': main.frLst,
                'Fr%': main.frPLst
                }

        print(tabulate(info, headers='keys', tablefmt='fancy_grid'))

        print("Frecuencia Total:", main.fTotal, "  ", "PM * F Total:", main.PMFTotal)
        print("Media Aritmetica:", MediaA)
        print("Mediana:", mediana.result)
        print("Moda:", moda.result)
        if moda.MoreThanOne:
            print("Moda2:", moda.result2)

    draw()

    def Histogram():
        data = []
        for i in range(main.a):
            data.extend(repeat(main.PMLst[i], main.Flst[i]))

        style.use("ggplot")
        bins = main.Flist
        plt.hist(data, bins=bins, edgecolor="black")
        plt.ylabel("Frecuencia")
        plt.xlabel("Intervalos")
        plt.title("Histograma")
        plt.show()

    Histogram()

# Para números que deben ser puestos en una tabla y sacar toda la demás data
def F_undetermined():
    class sort:
        def __init__(self):
            #Definir todas las variables
            # Frequency limits
            self.Flist = []
            self.f1L = None
            self.f2L = None
            self.f3L = None
            self.f4L = None
            self.f5L = None
            self.f6L = None
            self.f7L = None
            self.f8L = None
            self.f9L = None
            self.f10L = None

            # Intervalos
            self.intervaloLst = []
            self.intervalo1 = []
            self.intervalo2 = []
            self.intervalo3 = []
            self.intervalo4 = []
            self.intervalo5 = []
            self.intervalo6 = []
            self.intervalo7 = []
            self.intervalo8 = []
            self.intervalo9 = []
            self.intervalo10 = []

            # Frequency
            self.Flst = []
            self.f1 = None
            self.f2 = None
            self.f3 = None
            self.f4 = None
            self.f5 = None
            self.f6 = None
            self.f7 = None
            self.f8 = None
            self.f9 = None
            self.f10 = None
            self.fTotal = None

            # Limit
            self.quantity = []
            self.limit = None
            self.number = 0
            self.amplitud = None
            self.amount = None
            self.a = None

            # Punto Medio
            self.PMLst = []
            self.PM1 = ""
            self.PM2 = ""
            self.PM3 = ""
            self.PM4 = ""
            self.PM5 = ""
            self.PM6 = ""
            self.PM7 = ""
            self.PM8 = ""
            self.PM9 = ""
            self.PM10 = ""

            # Punto Medio * Frequencia
            self.PMFLst = []
            self.PMF1 = ""
            self.PMF2 = ""
            self.PMF3 = ""
            self.PMF4 = ""
            self.PMF5 = ""
            self.PMF6 = ""
            self.PMF7 = ""
            self.PMF8 = ""
            self.PMF9 = ""
            self.PMF10 = ""
            self.PMFTotal = ""

            # Frecuencia Acumulada
            self.faLst = []
            self.fa1 = ""
            self.fa2 = ""
            self.fa3 = ""
            self.fa4 = ""
            self.fa5 = ""
            self.fa6 = ""
            self.fa7 = ""
            self.fa8 = ""
            self.fa9 = ""
            self.fa10 = ""

            # Frecuencia Relativa
            self.frLst = []
            self.fr1 = ""
            self.fr2 = ""
            self.fr3 = ""
            self.fr4 = ""
            self.fr5 = ""
            self.fr6 = ""
            self.fr7 = ""
            self.fr8 = ""
            self.fr9 = ""
            self.fr10 = ""

            # Frecuencia relativa porcentual
            self.frPLst = []
            self.frP1 = ""
            self.frP2 = ""
            self.frP3 = ""
            self.frP4 = ""
            self.frP5 = ""
            self.frP6 = ""
            self.frP7 = ""
            self.frP8 = ""
            self.frP9 = ""
            self.frP10 = ""

            # clases
            self.claseLst = []
            self.clase1 = ""
            self.clase2 = ""
            self.clase3 = ""
            self.clase4 = ""
            self.clase5 = ""
            self.clase6 = ""
            self.clase7 = ""
            self.clase8 = ""
            self.clase9 = ""
            self.clase10 = ""

        def limits(self):
            # Preguntar data necesaria
            self.a = int(input("Cuantas clases vas a usar?"))
            self.f1L = int(input("Escribe el minimo:"))
            self.amplitud = int(input("Escribe la amplitud:"))
            self.limit = int(input("Cuantos numeros vas a insertar?:"))
            print("Agrega tus números")

            # Crear lista de limites de clase y definir sus respectivos valores

            for i in range(1, self.a + 2):
                self.Flist.append(eval("self." + "f" + str(i) + "L"))

            for i in range(1, self.a + 1):
                self.Flist[i] = self.Flist[i-1] + self.amplitud

            # Crear lista de clases y agregarle sus limites

            for i in range(1, self.a + 1):
                self.claseLst.append(eval("self." + "clase" + str(i)))

            for i in range(self.a):
                self.claseLst[i] = self.Flist[i], self.Flist[i + 1]

        def sorting(self):

            #Crear lista de listas para intervalos y clasificar la data dada y agregarla a su respectivo intervalo
            for i in range(1,self.a + 1):
                self.intervaloLst.append(eval("self." + "intervalo" + str(i)))

            for i in range(self.limit):
                self.number = int(input(">"))
                self.quantity.append(self.number)
                for s in range(self.a):
                    if self.Flist[s] <= self.quantity[i] < self.Flist[s + 1]:
                        self.intervaloLst[s].append(self.quantity[i])

        def Frecuencia(self):
            # Contar la longitud de las listas de intervalos y definir la frecuencia con esta data.
            for i in range(1,self.a + 1):
                self.Flst.append(eval("self." + "f" + str(i)))
            for i in range(self.a):
                self.Flst[i] = len(self.intervaloLst[i])

        def PuntoMedio(self):
            # Definir el punto medio de cada clase
            for i in range(1, self.a + 1):
                self.PMLst.append(eval("self." + "PM" + str(x)))
            for i in range(self.a):
                self.PMLst[i] = (self.Flist[i] + self.Flist[i + 1])/2

        def PMF(self):
            # Multiplicar PM por Frecuencia y definir PMF
            for i in range(1, self.a + 1):
                self.PMFLst.append(eval("self." + "PMF" + str(x)))
            for i in range(self.a):
                self.PMFLst[i] = self.Flst[i] * self.PMLst[i]

        def Fa(self):
            # Sumar las frecuencias de cada clase para definir la frecuencia acumulada
            for i in range(1, self.a + 1):
                self.faLst.append(eval("self." + "fa" + str(x)))
            self.faLst[0] = self.Flst[0]
            for i in range(1,self.a):
                self.faLst[i] = self.faLst[i-1] + self.Flst[i]

        def Total(self):
            # Sacar el total de la frecuencia y del PMF
            self.fTotal = max(self.faLst)
            self.PMFTotal = sum(self.PMFLst)

        def FrecuenciaRelativa(self):
            # Sacar la frecuencia relativa y la frecuencia relativa porcentual
            for i in range(1, self.a + 1):
                self.frLst.append(eval("self." + "fr" + str(i)))
                self.frPLst.append(eval("self." + "frP" + str(i)))
            for i in range(self.a):
                self.frLst[i] = self.Flst[i] / self.fTotal
                self.frPLst[i] = self.frLst[i] * 100

        def runall(self):
            self.limits()
            self.sorting()
            self.Frecuencia()
            self.PuntoMedio()
            self.PMF()
            self.Fa()
            self.Total()
            self.FrecuenciaRelativa()

    main = sort()
    main.runall()

    # Sacar Media Aritmetica
    MediaA = main.PMFTotal / main.fTotal

    class mediana:
        # Sacar la mitad de la F total y clasificarla segun la F acumulada
        def __init__(self):
            self.Mnumber = ""
            self.result = ""

        def Mediana(self):
            self.Mnumber = main.fTotal / 2

            if 0 <= self.Mnumber <= main.faLst[0]:
                self.result = main.PMLst[0]
            else:
                for i in range(main.a - 1):
                    if main.faLst[i] <= self.Mnumber <= main.faLst[i + 1]:
                        self.result = main.PMLst[i + 1]

    class moda:
        def __init__(self):
            self.ModaLst = []
            self.PMLst = []
            self.fHighest = ""
            self.result = ""
            self.result2 = None
            self.MoreThanOne = False
            self.x = ""

        def fTop(self):
            # Crear listas iguales a F y PM para ser modificadas
            for i in range(main.a):
                self.ModaLst.append(main.Flst[i])
                self.PMLst.append(main.PMLst[i])

            #Sacar la frecuencia maxima y su respectivo PM sera el resultado
            self.fHighest = max(self.ModaLst)

            for i in range(main.a):
                if self.fHighest == self.ModaLst[i]:
                    self.result = self.PMLst[i]
                    del self.PMLst[i]
                    break

            #Eliminamos los datos anteriores de las listas y volvemos a sacar la moda
            self.ModaLst.remove(max(self.ModaLst))

            # Si el la misma frecuencia se vuelve a encontrar en la lista, definimos una segunda moda, de otro modo,
            # solo queda definida la primera

            for i in range(main.a - 1):
                if self.fHighest == self.ModaLst[i]:
                    self.result2 = self.PMLst[i]
                    self.MoreThanOne = True
                    break

    mediana = mediana()
    mediana.Mediana()
    moda = moda()
    moda.fTop()

    def draw():
        # Creamos un diccionario con las "keys" como el titulo, y la respectiva data en una lista como "values", para
        # ser dibujadas en una tabla por la funcion "tabulate"
        info = {'Class': main.claseLst,
                'Frecuencia': main.Flst,
                'Punto Medio': main.PMLst,
                'PM * F': main.PMFLst,
                'Frecuencia Acumulada': main.faLst,
                'Fr': main.frLst,
                'Fr%': main.frPLst
                }

        print(tabulate(info, headers='keys', tablefmt='fancy_grid'))

        # Imprimimos la demas data que no fue dibujada en la tabla
        print("Frecuencia Total:", main.fTotal, "  ", "PM * F Total:", main.PMFTotal)
        print("Media Aritmetica:", MediaA)
        print("Mediana:", mediana.result)
        print("Moda:", moda.result)
        if moda.MoreThanOne:
            print("Moda2:", moda.result2)

    draw()

    def Histogram():
        # Usamos la biblioteca de Matplotlib para dibujar un histograma
        # Creamos la lista "Data" y por clase, le agregamos el punto medio las veces que determine la frecuencia.

        data = []
        for i in range(main.a):
            data.extend(repeat(main.PMLst[i], main.Flst[i]))

        style.use("ggplot")

        # Definimos que las barras tengan los mismos límites que las clases
        bins = main.Flist

        plt.hist(data, bins=bins, edgecolor="black")
        plt.ylabel("Frecuencia")
        plt.xlabel("Intervalos")
        plt.title("Histograma")
        plt.show()

    Histogram()

# Para números que no necesitan ser puestos en una tabla
def NoChart():
    class sort:
        def __init__(self):
            # Sorting
            self.data = []
            self.dataAmount = []
            self.minimo = ""
            self.maximo = ""
            self.x = ""
            self.y = 0
            self.z = 0

            # Media
            self.media = ""

            # Mediana
            self.m = 0
            self.a = 0
            self.b = 0
            self.mediana = ""

            # Moda
            self.moda = ""
            self.moda2 = ""
            self.n = False
            self.dictionary = {}
            self.max_key = ""
            self.rev_dict = {}
            self.result = []
            self.max_key2 = ""
            self.res = ""

        def sortList(self):
            global x
            # Pedimos data necesaria y pedimos lo números
            self.y = int(input("Cuantos números agregaras?"))
            print("Agrega tu data")

            while self.z < self.y:
                x = int(input(">"))
                self.data.append(x)
                self.z += 1

            # Ordenamos los números en la lista de menor a mayor
            self.data = sorted(self.data, reverse=False)

        def Min_Max(self):
            # Definimos el número minimo y máximo de la lista
            self.minimo = min(self.data)
            self.maximo = max(self.data)

        def Media(self):
            # Sacamos la media aritmetica usando "Total/cantidad de números"
            self.media = sum(self.data) / len(self.data)

        def Mediana(self):
            # Definimos si el numero es par o impar, si es impar, sumamos los 2 números centrales y los dividimos
            if (self.y % 2) == 1:
                self.m = self.y // 2
                self.mediana = self.data[self.m]

            if (self.y % 2) == 0:
                self.m = self.y // 2
                self.a = self.data[self.m - 1]
                self.b = self.data[self.m]
                self.mediana = (self.a + self.b) / 2

        def Moda(self):

            # Creamos un diccionario que determine cuantas veces se repite un número
            self.dictionary = {item: self.data.count(item) for item in self.data}

            # Determinamos cual es el número mas repetido y creamos otro diccionario que contenga esta valor
            self.max_key = max(self.dictionary, key=self.dictionary.get)
            self.rev_dict = {}

            # Le agregamos a rev.dict los números que se repiten
            for key, value in self.dictionary.items():
                self.rev_dict.setdefault(value, set()).add(key)

            # Definimos el resultado del número mas repetido
            self.result = [key for key, values in self.rev_dict.items() if len(values) > 1]
            self.res = len(list(set(list(main.dictionary.values())))) == 1

            # Si no hay ningun número repetido, no definimos moda
            if self.res == True:
                self.moda = None
                self.moda2 = None

            # Revisamos por una segunda moda
            elif self.dictionary[self.max_key] in self.result:
                self.n = True
                del self.dictionary[self.max_key]
                self.max_key2 = max(self.dictionary, key=self.dictionary.get)
                self.moda = self.max_key
                self.moda2 = self.max_key2

            # Si no se cumplen ninguna de estas condiciones, solo definimos una moda
            else:
                self.moda = self.max_key

        def runAll(self):
            self.sortList()
            self.Min_Max()
            self.Media()
            self.Mediana()
            self.Moda()

    main = sort()
    main.runAll()

    # Imprimimos toda la data
    def draw():
        print("Lista Ordenada:", main.data)
        print("Minimo:", main.minimo, "", "Maximo:", main.maximo)
        print("Media:", main.media)
        print("Mediana:", main.mediana)
        print("Moda:", main.moda)
        if main.n is True:
            print("Moda2:", main.moda2)

    draw()  # Par


while True:

    # Preguntamos cual codigo quiere correr segun el ejercicio
    print("Ordenar números(1), ya esta designada la frecuencia(2), o no hay tabla(3)?")
    x = int(input("Tu respuesta debe ser un número:"))

    if x == 1:
        F_undetermined()
        break
    if x == 2:
        F_determined()
        break

    if x == 3:
        NoChart()
        break
