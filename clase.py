class Resistencia:
    def __init__(self, valor):
        if valor <= 0:
            raise ValueError("El valor de la resistencia debe ser mayor a cero.")
        self.valor = valor


class Circuito:
    def __init__(self, resistencias):
        self.resistencias = resistencias


class CircuitoSerie(Circuito):
    def calcular(self):
        return sum(r.valor for r in self.resistencias)


class CircuitoParalelo(Circuito):
    def calcular(self):
        inversa_total = sum(1 / r.valor for r in self.resistencias)
        return 1 / inversa_total if inversa_total != 0 else float('inf')


print("--- Cálculo de Resistencia Total ---")
tipo = input("Tipo de circuito (serie/paralelo): ").lower()

try:
    n = int(input("¿Cuántas resistencias vas a ingresar?: "))
    resistencias = []

    for i in range(n):
        valor = float(input(f"Ingrese el valor de la resistencia {i+1} (ohmios): "))
        resistencias.append(Resistencia(valor))

    if tipo == "serie":
        circuito = CircuitoSerie(resistencias)
    elif tipo == "paralelo":
        circuito = CircuitoParalelo(resistencias)
    else:
        raise ValueError("Tipo de circuito no válido. Usa 'serie' o 'paralelo'.")

    print(f"La resistencia total es: {circuito.calcular()} Ω")

except ValueError as e:
    print(f"Error: {e}")
