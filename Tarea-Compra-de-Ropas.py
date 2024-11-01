class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self.nombre= nombre
        self.precio= precio
        self.cantidad=cantidad
        
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Precio: {self.precio}, Stock: {self.cantidad}")
    
class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla=talla
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")
        
class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla=talla
        
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")

class Inventario:
    def __init__(self):
        self.prendas= []
        
    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)
        
    def mostrar_inventario(self):
        for prenda in self.prendas:
            prenda.mostrar_info()
    
camisa = RopaHombre("Camisa de Hombre", 25.00, 50, "M")
pantalon = RopaHombre("Pantalon de Hombre", 30.00, 30, "S")
chaqueta = RopaHombre("Chaqueta de Hombre", 55.00, 20, "G")
falda = RopaMujer("Falda de Mujer", 28.00, 15, "S")
blusa = RopaMujer("Blusa de Mujer", 22.00, 40, "G")
vestido = RopaMujer("Vestido de mujer", 45.00, 10, "S")
zapatosH = RopaHombre("Zapatos de hombre", 60.00, 25, "43")
zapatosM = RopaMujer("Zapatos de mujer", 50.00, 20, "38")

inventario = Inventario()
inventario.agregar_prenda(camisa)
inventario.agregar_prenda(falda)
inventario.agregar_prenda(zapatosH)
inventario.agregar_prenda(blusa)

inventario.mostrar_inventario()
