class Persona:

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def hablar(self):
        print(f"Hola soy {self.nombre} y estoy hablando")
    
    def __str__(self):
        return f"Hola soy {self.nombre} me gusta usar ase y clavar apus"