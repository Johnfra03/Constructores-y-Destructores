class Zapateria:
    def __init__(self, nombre):
        """
        Inicializa la zapatería con el nombre.
        """
        self.nombre = nombre  # Nombre de la zapatería
        self.zapatos_en_stock = {}  # Inventario de zapatos
        print(f"Bienvenido a la zapatería {self.nombre}.")

    def agregar_zapato(self, modelo, cantidad, precio):
        """
        Agrega zapatos al inventario.
        """
        if modelo in self.zapatos_en_stock:
            self.zapatos_en_stock[modelo]['cantidad'] += cantidad  # Aumenta la cantidad
        else:
            self.zapatos_en_stock[modelo] = {'cantidad': cantidad, 'precio': precio}  # Nuevo modelo
        print(f"{cantidad} pares de {modelo} agregados.")

    def vender_zapato(self, modelo, cantidad):
        """
        Vende zapatos y reduce el stock.
        """
        if modelo in self.zapatos_en_stock and self.zapatos_en_stock[modelo]['cantidad'] >= cantidad:
            self.zapatos_en_stock[modelo]['cantidad'] -= cantidad  # Reduce el stock
            total = cantidad * self.zapatos_en_stock[modelo]['precio']  # Calcula el total
            print(f"Vendidos {cantidad} pares de {modelo}. Total: ${total}.")
        else:
            print(f"No hay suficientes {modelo} en stock.")

    def mostrar_stock(self):
        """
        Muestra el inventario de zapatos.
        """
        if self.zapatos_en_stock:
            print("Inventario de zapatos:")
            for modelo, datos in self.zapatos_en_stock.items():
                print(f"{modelo}: {datos['cantidad']} pares, ${datos['precio']} por par.")
        else:
            print("El inventario está vacío.")

    def __del__(self):
        """
        Mensaje cuando la zapatería cierra.
        """
        print(f"La zapatería {self.nombre} ha cerrado.")

# Crear y usar un objeto de la clase Zapateria
zapateria = Zapateria("Zapatos Fashion")  # Crear zapatería con nuevo nombre
zapateria.agregar_zapato("Sandalias de verano", 50, 25)  # Agregar sandalias
zapateria.agregar_zapato("Botas de lluvia", 40, 70)  # Agregar botas
zapateria.agregar_zapato("Zapatillas deportivas", 60, 45)  # Agregar zapatillas
zapateria.mostrar_stock()  # Mostrar inventario

zapateria.vender_zapato("Botas de lluvia", 10)  # Vender 10 pares de botas
zapateria.vender_zapato("Sandalias de verano", 5)  # Vender 5 pares de sandalias
zapateria.mostrar_stock()  # Mostrar inventario después de la venta

# Destruir el objeto para invocar el destructor
del zapateria
