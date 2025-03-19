class Usuario:
    def __init__(self, nombre, apellido, cedula, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.telefono = telefono
        
    def mostrar_datos(self):
            return f"Nombre: {self.nombre} {self.apellido}, Cedula: {self.cedula} Telefono: {self.telefono}"
        
    def editar_datos(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
            
class Contrato:
    def __init__(self, fecha_inicio, salario):
        self.fecha_inicio = fecha_inicio
        self.salario = salario
        
        
    def mostrar_contrato(self):
        return "Fecha de inicio: {self.fecha_inicio}, Salario {self.salario}"
    

    def editar_contrato(self, fecha_inicio, salario):
        self.fecha_inicio = fecha_inicio
        self.salario = salario
    
class Empleado(Usuario, Contrato):
    def __init__(self, nombre, apellido, cedula, telefono, cargo, fecha_inicio, salario):
        Usuario.__init__(self, nombre, apellido, cedula, telefono)
        Contrato.__init__(self,fecha_inicio, salario)
        self.cargo = cargo
        
    def mostrar_datos(self):
        return f"Empleado: {Usuario.mostrar_datos(self)}, Cargo: {self.cargo}, {self.mostrar_contrato()}"
    
    def editar_empleado(self,  nombre, apellido, cedula, telefono, cargo, fecha_inicio, salario ):
        self.editar_datos(nombre, apellido, telefono)
        self.cargo = cargo
        self.editar_contrato(fecha_inicio, salario)
        
        
class Cliente(Usuario):
    def __init__(self, nombre, apellido, cedula, telefono, direccion):
        super().__init__(nombre, apellido, cedula, telefono)
        self.direccion = direccion

    def mostrar_datos(self):
        return f"Cliente - {super().mostrar_datos()}, Direccin: {self.direccion}"
    
    def editar_cliente(self, nombre, apellido, cedula, telefono, direccion):
        self.editar_datos(nombre, apellido,telefono)
        self.direccion = direccion

class ListaUsuario:
    def __init__(self):
        self.usuarios = []
        
    def agregar_usuraio(self, usuario):
        self.usuarios.append(usuario)
    
    def mostrar_todos(self):
        for usuario in self.usuarios:
            print(usuario.mostrar_datos())


    def buscar_usurio(self, cedula):
        for unsuario in self.usuarios:
            if unsuario.cedula == cedula:
                return unsuario
        return None
        
    def editar_usuario(self, cedula):
        usuario = self.buscar_usurio(cedula)
        if usuario:
            if isinstance(usuario, Empleado):
                print("Editando empleado")
                nombre = input("Nuevo nombre:")
                apellido = input("Nuevo apellido:")
                telefono = input("Nuevo telefono:")
                cargo = input("Nuevo cargo:")
                fecha_inicio = input("Nuevo fecha de inicio:")
                salario = input("Nuevo salario:")
                usuario.editar_empleado(nombre, apellido, telefono, cargo, fecha_inicio, salario)
            elif isinstance(usuario, Cliente):
                print("Editando cliente")
                nombre = input("Nuevo nombre:")
                apellido = input("Nuevo apellido:")
                telefono = input("Nuevo telefono:")
                direccion = input("Nuevo direccion:")
                usuario.editar_cliente(nombre, apellido, telefono, direccion)
            print("Usuario editado conexito")
        else:
            print("Usuario no encontrado")
                
lista = ListaUsuario()

while True:
    print("\nOpciones")
    print("1. Agregar Empleado")
    print("2. Agregar Clinete")
    print("3. Mostrar todos los usuarios")
    print("4. Editar un usurio por cedula")
    print("5. Salir")
    
    opcion = input(" Seleccione una opcion ")
    

    if opcion == "1":
        nombre = input(" Nombre: ")               
        apellido = input(" Apellido: ")               
        cedula = input(" Cedula: ")               
        telefono = input(" Telefono: ")               
        cargo = input(" Cargo: ")               
        fecha_inicio = input(" Fecha de inicio: ")               
        salario = input(" Nombre: ")               
        empleado = Empleado(nombre, apellido, cedula, telefono, cargo, fecha_inicio, salario)       
        lista.agregar_usuraio(empleado)
        
    elif opcion == "2":
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        cedula = input("Cédula: ")
        telefono = input("Teléfono: ")
        direccion = input("Dirección: ")
        cliente = Cliente(nombre, apellido, cedula, telefono, direccion)
        lista.agregar_usuario(cliente)
        
    elif opcion == "3":
        print("\n Listado de usuario ingresado: ")
        lista.mostrar_todos()
        
    elif opcion == "4":
        cedula = input("Ingrese la cedula del usurio")
        lista.editar_usuario(cedula)
        
    elif opcion == "5":
        print("Saliendo del programa ")
        break
    else:
        print("Opcion no balida")
               

        