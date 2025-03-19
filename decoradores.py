# Decorador para validar que el texto no esté vacío
def validar_texto(func):
    def wrapper(self, valor):
        if not valor.strip():
            raise ValueError("El valor no puede estar vacío")
        func(self, valor)
    return wrapper

# Clase base
class Persona:
    def __init__(self, nombre, cedula, telefono):
        self._nombre = nombre
        self._cedula = cedula
        self._telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @validar_texto
    def nombre(self, valor):
        self._nombre = valor

    @property
    def cedula(self):
        return self._cedula

    @property
    def telefono(self):
        return self._telefono

    @validar_texto
    def telefono(self, valor):
        self._telefono = valor

    def mostrar_datos(self):
        return f"Nombre: {self._nombre}, Cédula: {self._cedula}, Teléfono: {self._telefono}"

# Clase Empleado (hereda de Persona)
class Empleado(Persona):
    def __init__(self, nombre, cedula, telefono, cargo, salario):
        super().__init__(nombre, cedula, telefono)
        self._cargo = cargo
        self._salario = salario

    @property
    def cargo(self):
        return self._cargo

    @validar_texto
    def cargo(self, valor):
        self._cargo = valor

    @property
    def salario(self):
        return self._salario

    def mostrar_datos(self):
        datos = super().mostrar_datos()
        return f"{datos}, Cargo: {self._cargo}, Salario: {self._salario}"

# Clase Dirección
class Direccion:
    def __init__(self, direccion, ciudad):
        self._direccion = direccion
        self._ciudad = ciudad

    @property
    def direccion(self):
        return self._direccion

    @validar_texto
    def direccion(self, valor):
        self._direccion = valor

    @property
    def ciudad(self):
        return self._ciudad

    @validar_texto
    def ciudad(self, valor):
        self._ciudad = valor

    def mostrar_direccion(self):
        return f"Dirección: {self._direccion}, Ciudad: {self._ciudad}"

# Herencia múltiple: Usuario hereda de Empleado y Dirección
class Usuario(Empleado, Direccion):
    def __init__(self, nombre, cedula, telefono, cargo, salario, direccion, ciudad):
        Empleado.__init__(self, nombre, cedula, telefono, cargo, salario)
        Direccion.__init__(self, direccion, ciudad)

    # Polimorfismo: sobreescribo mostrar_datos
    def mostrar_datos(self):
        datos_empleado = Empleado.mostrar_datos(self)
        datos_direccion = Direccion.mostrar_direccion(self)
        return f"{datos_empleado}, {datos_direccion}"

# Clase para manejar el listado de usuarios
class SistemaUsuarios:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print("Usuario agregado exitosamente.")

    def listar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
        for usuario in self.usuarios:
            print(usuario.mostrar_datos())

    def buscar_usuario(self, cedula):
        for usuario in self.usuarios:
            if usuario.cedula == cedula:
                return usuario
        return None

    def editar_usuario(self, cedula):
        usuario = self.buscar_usuario(cedula)
        if usuario:
            print("Usuario encontrado:")
            print(usuario.mostrar_datos())
            print("Ingrese nuevos datos (deje vacío si no desea cambiar):")
            nuevo_nombre = input("Nuevo nombre: ")
            if nuevo_nombre:
                usuario.nombre = nuevo_nombre
            nuevo_telefono = input("Nuevo teléfono: ")
            if nuevo_telefono:
                usuario.telefono = nuevo_telefono
            nuevo_cargo = input("Nuevo cargo: ")
            if nuevo_cargo:
                usuario.cargo = nuevo_cargo
            nuevo_direccion = input("Nueva dirección: ")
            if nuevo_direccion:
                usuario.direccion = nuevo_direccion
            nueva_ciudad = input("Nueva ciudad: ")
            if nueva_ciudad:
                usuario.ciudad = nueva_ciudad
            print("Usuario editado exitosamente.")
        else:
            print("Usuario no encontrado.")

# Programa principal
def menu():
    sistema = SistemaUsuarios()
    while True:
        print("\n--- Sistema de Usuarios - Empresa de Servicios Generales ---")
        print("1. Agregar usuario")
        print("2. Listar usuarios")
        print("3. Consultar usuario por cédula")
        print("4. Editar usuario")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                nombre = input("Nombre: ")
                cedula = input("Cédula: ")
                telefono = input("Teléfono: ")
                cargo = input("Cargo: ")
                salario = float(input("Salario: "))
                direccion = input("Dirección: ")
                ciudad = input("Ciudad: ")
                usuario = Usuario(nombre, cedula, telefono, cargo, salario, direccion, ciudad)
                sistema.agregar_usuario(usuario)
            except Exception as e:
                print(f"Error: {e}")
        elif opcion == "2":
            sistema.listar_usuarios()
        elif opcion == "3":
            cedula = input("Ingrese la cédula a consultar: ")
            usuario = sistema.buscar_usuario(cedula)
            if usuario:
                print(usuario.mostrar_datos())
            else:
                print("Usuario no encontrado.")
        elif opcion == "4":
            cedula = input("Ingrese la cédula del usuario a editar: ")
            sistema.editar_usuario(cedula)
        elif opcion == "5":
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    menu()
