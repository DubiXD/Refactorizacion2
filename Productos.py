'''
Se plantea desarrollar un programa que permita la gestión de una empresa agroalimentaria que trabaja con tres tipos de productos:
•	Productos frescos
•	Productos refrigerados
•	Productos congelados 
•	Todos los productos llevan esta información común: fecha de caducidad y número de lote. A su vez, cada tipo de producto lleva alguna información específica.
•	Los productos frescos deben llevar la fecha de envasado y el país de origen.
•	Los productos refrigerados deben llevar el código del organismo de supervisión alimentaria.
•	Los productos congelados deben llevar la temperatura de congelación recomendada.
Realiza un menú que pregunte qué tipo de producto se quiere crear y guárdalos en listas independientes
'''
class Productos():
    def __init__(self, fecha_caducidad, numero_lote, peso, medida):
        self.fecha_caducidad = fecha_caducidad
        self.numero_lote = numero_lote
        self.peso = float(peso)
        self.medida = medida

    def calcular_coste_envio(self):
        return self.peso * 3

    def __str__(self):
        return f"Caducidad: {self.fecha_caducidad}, Lote: {self.numero_lote}, Peso: {self.peso}, Medida: {self.medida}"
    
class Frescos(Productos):
    def __init__(self, fecha_caducidad, numero_lote, peso, medida, fecha_envasado, pais_origen):
        super().__init__(fecha_caducidad, numero_lote, peso, medida)
        self.fecha_envasado = fecha_envasado
        self.pais_origen = pais_origen
        
    def __str__(self):
        return super().__str__() + f"Envasado: {self.fecha_envasado}, Pais: {self.pais_origen}"
        
class Refrigerados(Productos):
    def __init__(self,fecha_caducidad, numero_lote, peso, medida, codigo_organismo):
        super().__init__(fecha_caducidad, numero_lote, peso, medida)
        self.codigo_organismo = codigo_organismo
        
    def calcular_coste_envio(self):
        return super().calcular_coste_envio() + 2

    def __str__(self):
        return super().__str__() + f"Codigo de organismo: {self.codigo_organismo}"

class Congelados(Productos):
    def __init__(self, fecha_caducidad, numero_lote, peso, medida, temperatura_congelacion):
        super().__init__(fecha_caducidad, numero_lote, peso, medida)
        self.temperatura_congelacion = temperatura_congelacion

    def calcular_coste_envio(self):
        return super().calcular_coste_envio() + 5

    def __str__(self):
        return super().__str__() + f"Temperatura recomendada: {self.temperatura_congelacion}"

productos = []        
#productos_frescos = []
#productos_refrigerados = []
#productos_congelados = []

def datosGenerales():
    fecha_caducidad = input("Fecha de caducidad: ")
    numero_lote = input("Numero de lote: ")
    peso = input("Peso: ")
    return fecha_caducidad, numero_lote, peso

def main():
    while True:
        print("\nGestión de Productos Agroalimentarios")
        print("1. Agregar Producto Fresco")
        print("2. Agregar Producto Refrigerado")
        print("3. Agregar Producto Congelado")
        print("4. Mostrar Productos")
        print("5. Salir")
        pregunta = input("Seleccione una opción: ")

        if pregunta == "1":
            fecha_caducidad = input("Fecha de caducidad: ")
            numero_lote = input("Número de lote: ")
            peso = input("Peso: ")
            medida = input("Medida: ")
            fecha_envasado = input("Fecha de envasado: ")
            pais_origen = input("País de origen: ")
            productos.append(Frescos(fecha_caducidad, numero_lote, peso, medida, fecha_envasado, pais_origen))
            print("Producto fresco agregado.")

        elif pregunta == "2":
            fecha_caducidad = input("Fecha de caducidad: ")
            numero_lote = input("Número de lote: ")
            peso = input("Peso: ")
            medida = input("Medida: ")
            codigo_supervision = input("Código de supervisión alimentaria: ")
            productos.append(Refrigerados(fecha_caducidad, numero_lote, peso, medida, codigo_supervision))
            print("Producto refrigerado agregado.")

        elif pregunta == "3":
            fecha_caducidad = input("Fecha de caducidad: ")
            numero_lote = input("Número de lote: ")
            peso = input("Peso: ")
            medida = input("Medida: ")
            temp_congelacion = input("Temperatura de congelación recomendada: ")
            productos.append(Congelados(fecha_caducidad, numero_lote, peso, medida, temp_congelacion))
            print("Producto congelado agregado.")

        elif pregunta == "4":
            print("Productos Frescos:")
            Frescos
            print("Productos Refrigerados:")
            Refrigerados
            print("Productos Congelados:")
            Congelados
        
        elif pregunta == "5":
            print("Se acabo")
            break

        else:
            print("Escribe algo válido")
main()
