# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class MedioTransporte:
    def __init__(self, nombre, carga, precio):
        self.nombre = nombre
        self.carga = carga
        self.precio = precio

    def __eq__(self, other):
        if not isinstance(other, MedioTransporte):
            # don't attempt to compare against unrelated types
            return NotImplemented
        estado = 0
        if self.carga > other:
            estado = 1
        elif self.carga < other:
            estado = -1
        return estado

    def __str__(self):
        return self.nombre + ': \n Capacidad de carga: ' + str(self.carga) + '\n Costo de uso: ' + str(self.precio)

class Producto:
    def __init__(self, nombre, puntos):
        self.nombre = nombre
        self.puntos = puntos

    def __str__(self):
        return self.nombre + ': \n Espacio que ocupa: ' + str(self.puntos)

class Municipio:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return self.nombre + ': \n Precio de entrega: ' + str(self.precio)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    carro = MedioTransporte("Carro", 10, 40)
    camion = MedioTransporte("Camión", 45, 20)
    medios_trannsporte = [camion, carro]
    aceite = Producto("Aceite", 1)
    huevos = Producto("Carton de huevos", 2.5)
    pallet = Producto("Pallet de agua", 11)
    moto = Producto("Moto", 12)
    frio = Producto("Frio", 15)
    productos = [aceite, huevos, pallet, moto, frio]
    cerro = Municipio('Cerro', 5)
    cotorro = Municipio('Cotorro', 10)
    municipios = [cerro, cotorro]
    pedido = []
    while True:
        cont_transporte = 0
        cont_productos = 0
        cont_municipios = 0
        print("***** MEDIOS DE TRASNPORTE *****")
        for medio_transporte in medios_trannsporte:
            cont_transporte = cont_transporte + 1
            print(str(cont_transporte) + ' - ' + str(medio_transporte))

        print("________________________________")
        print("***** PRODUCTOS *****")
        for producto in productos:
            cont_productos = cont_productos + 1
            print(str(cont_productos) + ' - ' + str(producto))
        print("________________________________")
        print("***** MUNICIPIOS *****")
        for municipio in municipios:
            cont_municipios = cont_municipios + 1
            print(str(cont_municipios) + ' - ' + str(municipio))
        print("________________________________")
        print("***** CARRITO *****")
        for componente in pedido:
            print(str(componente) + '\n')
        print("________________________________")
        if input("TERMINO SU COMPRA? Y/N -> ").lower() == "Y".lower():
            municipio = municipios[int(input("SELECCIONE EL NUMERO DEL MUNICIPIO DE ENTREGA -> "))]
            total_puntos = 0
            for componente in pedido:
                total_puntos = total_puntos + componente.puntos
            total_viejo = total_puntos
            posicion = 0
            usados = []
            cargas = []
            for item in medios_trannsporte:
                cargas.append(item.carga)
            for denomination in cargas:
                count, total_puntos = divmod(total_puntos, denomination)
                if count:
                    for item in medios_trannsporte:
                        if item.carga == denomination:
                            for i in range(int(count)):
                                usados.append(item)
            if total_puntos > 0:
                usados.append(medios_trannsporte[len(medios_trannsporte)-1])
            print("TOTAL A CARGAR: " + str(total_viejo))
            total = 0
            for item in usados:
                total += item.precio
                print(item)
            total+=municipio.precio
            print("PRECIO DE ENVIO " + str(total))
            break
        producto = int(input("SELECCIONE EL NUMERO DEL PRODUCTO A COMPRAR -> "))
        cant = int(input("SELECCIONE LA CANTIDAD QUE DESEA DE " + productos[producto-1].nombre + " -> "))
        for i in range(cant):
            pedido.append(productos[producto-1])





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
