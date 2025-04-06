# Ejercicio: Sistema de Gestión de Empleados de una Empresa

# Objetivo:
# Crear un sistema simple para gestionar diferentes tipos de empleados en una empresa.
# Deberás aplicar herencia para modelar distintos roles, usar super() para inicializar atributos
# comunes, implementar un classmethod para llevar un registro global y usar polimorfismo para manejar
# acciones comunes de formas específicas. También necesitarás bucles para procesar una colección de
# empleados.

class Empleado():

    lista_instancias = []

    def __init__(self, nombre : str, id_empleado, salario_base : float):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.salario_base = salario_base
        Empleado.lista_instancias.append(self)
        
    def calcular_salario_mensual(self):
        return self.salario_base

    def mostrar_detalle(self):
        print(f'El empleado se llama : {self.nombre} y su id de este empleado es: {self.id_empleado}')
        return

    @classmethod
    def obtener_numero_total_empleados(cls):
        return len(cls.lista_instancias)

class Gerente(Empleado):

    def __init__(self, nombre_gerente, id_gerente, salario_gerente, bono_gestion : float):
        super().__init__(nombre_gerente, id_gerente, salario_gerente)
        self.bono_gestion = bono_gestion

    def calcular_salario_mensual(self):
        return super().calcular_salario_mensual() + self.bono_gestion

    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f'{self.nombre} es gerente. Su bono por ser gerente de esta empresa es de: {self.bono_gestion}')

class Desarrollador(Empleado):
    
    def __init__(self, nombre_development, id_development, salario_development, lenguaje_principal: str, horas_extra = 0):
        super().__init__(nombre_development, id_development, salario_development)
        self.lenguaje_principal = lenguaje_principal
        self.tarifa_hora_extra = 75
        self.horas_extras = horas_extra
        
    def asignar_horas_extra(self, horas):
        self.horas_extras = horas
        return self.horas_extras

    def calcular_salario_mensual(self):
        herencia = super().calcular_salario_mensual()
        return herencia + (self.horas_extras * self.tarifa_hora_extra)

    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f'{self.nombre} es desarrollador y su lenguaje principal es python. Horas extras acumuladas {self.horas_extras}')

class Becario(Empleado):

    def __init__(self, nombre_becario, id_becario, salario_becario, duracion_pasantia_meses : int, universidad : str):
        super().__init__(nombre_becario, id_becario, salario_becario)
        self.duracion_pasantia_meses = duracion_pasantia_meses
        self.universidad = universidad

    def calcular_salario_mensual(self):
        return super().calcular_salario_mensual()
        
    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f'{self.nombre} es un Becario o pasante, el es de la universidad {self.universidad}, el está durante {self.duracion_pasantia_meses} meses.')

def main():
    Juan = Empleado('Juan', 412097840, 2000.00)
    Lupita = Empleado('Lupita', 412000840, 1000.00)

    Miguel_Angel = Desarrollador('Miguel Ángel Gutiérrez Rojas', 320275986, 70000.00, 'Python')
    Joshua = Desarrollador('Joshua', 9823741290, 70000.00, 'Python')

    MiBecario = Becario('Daniel', 4987129920, 900.00, 6, 'Universidad Nacional Autonoma de México')
    Mi2doBecario = Becario('Jose', 4798231490, 900.00, 6, 'Universidad Nacional Autonoma de México')

    MiGerente = Gerente('Claudia', 92074102, 3000.00, 500.00)
    Mi2doGerente = Gerente('Julieta', 9739471290, 3000.00, 500.00)

    costo_total_nomina_mensual = 0
    nomina_empleados = [Juan, Lupita,Miguel_Angel, Joshua, MiBecario, Mi2doBecario, MiGerente, Mi2doGerente]

    Miguel_Angel.asignar_horas_extra(6)
    for nomina_empleado in nomina_empleados:
        print('--------------------------------------')
        nomina_empleado.mostrar_detalle()
        costo = nomina_empleado.calcular_salario_mensual()
        costo_total_nomina_mensual += costo
        print('--------------------------------------')
    
    print(Miguel_Angel.calcular_salario_mensual())
    print(f'costo total de la nomina: {costo_total_nomina_mensual}')
    print('personas laborano dentro de la empresa:', Empleado.obtener_numero_total_empleados())


if __name__ == '__main__':
    main()