# Exemple d'Usos Avançats de Tuples en Python
# ============================================

# Les tuples tenen molts usos avançats i pràctics en Python.

# 1. Named Tuples - Tuples amb noms
print("=== Named Tuples ===")
from collections import namedtuple

# Definir una named tuple
Punt = namedtuple('Punt', ['x', 'y'])
Color = namedtuple('Color', 'vermell verd blau')  # També amb string

# Crear instàncies
p1 = Punt(10, 20)
p2 = Punt(x=5, y=15)  # Amb arguments nomenats
vermell = Color(255, 0, 0)

print(f"Punt p1: {p1}")
print(f"Accedir per índex: p1[0] = {p1[0]}")
print(f"Accedir per nom: p1.x = {p1.x}, p1.y = {p1.y}")
print(f"\nColor vermell: {vermell}")
print(f"vermell.vermell = {vermell.vermell}")

# Mètodes de named tuple
print(f"\np1._fields: {p1._fields}")
print(f"p1._asdict(): {p1._asdict()}")

# 2. Funcions que retornen múltiples valors
print("\n=== Funcions amb múltiples retorns ===")

def estadistiques(numeros):
    """Retorna múltiples estadístiques d'una llista de nombres."""
    if not numeros:
        return (0, 0, 0, 0)
    
    minim = min(numeros)
    maxim = max(numeros)
    suma = sum(numeros)
    mitjana = suma / len(numeros)
    
    return (minim, maxim, suma, mitjana)

dades = [4, 7, 2, 9, 1, 8, 3]
minim, maxim, suma, mitjana = estadistiques(dades)

print(f"Dades: {dades}")
print(f"Mínim: {minim}")
print(f"Màxim: {maxim}")
print(f"Suma: {suma}")
print(f"Mitjana: {mitjana:.2f}")

# Amb named tuple per més claredat
Estadistiques = namedtuple('Estadistiques', ['minim', 'maxim', 'suma', 'mitjana'])

def estadistiques_named(numeros):
    if not numeros:
        return Estadistiques(0, 0, 0, 0)
    return Estadistiques(
        minim=min(numeros),
        maxim=max(numeros),
        suma=sum(numeros),
        mitjana=sum(numeros) / len(numeros)
    )

stats = estadistiques_named(dades)
print(f"\nAmb named tuple: {stats}")
print(f"stats.mitjana: {stats.mitjana:.2f}")

# 3. Tuples en estructures de dades
print("\n=== Tuples en estructures de dades ===")

# Llista de tuples (registres)
estudiants = [
    ("Anna", "Garcia", 22, 8.5),
    ("Pere", "López", 21, 7.2),
    ("Maria", "Martínez", 23, 9.1)
]

print("Llista d'estudiants:")
for nom, cognom, edat, nota in estudiants:
    print(f"  {nom} {cognom}, {edat} anys, nota: {nota}")

# Ordenar per diferents camps
print("\nOrdenat per nota (descendent):")
per_nota = sorted(estudiants, key=lambda x: x[3], reverse=True)
for e in per_nota:
    print(f"  {e[0]} {e[1]}: {e[3]}")

# 4. Enumerate retorna tuples
print("\n=== Enumerate amb tuples ===")
fruites = ["poma", "plàtan", "taronja"]

print("Resultat d'enumerate:")
for element in enumerate(fruites):
    print(f"  {element} (tipus: {type(element).__name__})")

print("\nDesempaquetat:")
for i, fruita in enumerate(fruites, start=1):
    print(f"  {i}. {fruita}")

# 5. Zip retorna tuples
print("\n=== Zip amb tuples ===")
noms = ["Anna", "Pere", "Maria"]
edats = [25, 30, 28]
ciutats = ["Barcelona", "Madrid", "València"]

print("Resultat de zip:")
combinat = list(zip(noms, edats, ciutats))
for element in combinat:
    print(f"  {element}")

# Descomprimir amb zip
noms2, edats2, ciutats2 = zip(*combinat)
print(f"\nDescomprimit - noms: {noms2}")

# 6. Tuples com a arguments de funció
print("\n=== Tuples com a arguments ===")

def sumar_tot(*args):
    """Accepta un nombre variable d'arguments com a tupla."""
    print(f"  args = {args} (tipus: {type(args).__name__})")
    return sum(args)

resultat = sumar_tot(1, 2, 3, 4, 5)
print(f"  Suma: {resultat}")

# Desempaquetar tupla com a arguments
def crear_punt(x, y, z):
    return f"Punt({x}, {y}, {z})"

coordenades = (10, 20, 30)
print(f"\nCoordenades: {coordenades}")
print(f"crear_punt(*coordenades): {crear_punt(*coordenades)}")

# 7. Comparació lexicogràfica
print("\n=== Comparació de tuples ===")

# Les tuples es comparen element per element
t1 = (1, 2, 3)
t2 = (1, 2, 4)
t3 = (1, 3, 1)
t4 = (2, 0, 0)

print(f"t1 = {t1}, t2 = {t2}, t3 = {t3}, t4 = {t4}")
print(f"t1 < t2: {t1 < t2}")  # True (3 < 4)
print(f"t1 < t3: {t1 < t3}")  # True (2 < 3)
print(f"t1 < t4: {t1 < t4}")  # True (1 < 2)

# Útil per ordenar per múltiples criteris
persones = [
    ("Garcia", "Anna", 25),
    ("López", "Pere", 30),
    ("Garcia", "Joan", 22),
    ("López", "Maria", 28)
]

print("\nPersones ordenades per cognom, després per nom:")
for p in sorted(persones):
    print(f"  {p[0]}, {p[1]} ({p[2]} anys)")

# 8. Tuples immutables amb elements mutables
print("\n=== Tuples amb elements mutables ===")

# Una tupla pot contenir elements mutables (com llistes)
t = ([1, 2], [3, 4])
print(f"Tupla amb llistes: {t}")

# Podem modificar les llistes internes!
t[0].append(3)
print(f"Després de t[0].append(3): {t}")

# Però no podem canviar la referència
# t[0] = [5, 6]  # TypeError

# 9. Patró: Retorn d'estat i valor
print("\n=== Patró: Retorn d'estat i valor ===")

def dividir(a, b):
    """Retorna (èxit, resultat/error)"""
    if b == 0:
        return (False, "Error: divisió per zero")
    return (True, a / b)

casos = [(10, 2), (5, 0), (15, 3)]
for a, b in casos:
    exit, resultat = dividir(a, b)
    if exit:
        print(f"  {a} / {b} = {resultat}")
    else:
        print(f"  {a} / {b}: {resultat}")

# 10. Exemple pràctic: Inventari de productes
print("\n=== Exemple pràctic: Inventari ===")

Producte = namedtuple('Producte', ['id', 'nom', 'preu', 'estoc'])

inventari = [
    Producte(1, "Ordinador", 800.00, 15),
    Producte(2, "Teclat", 50.00, 45),
    Producte(3, "Ratolí", 25.00, 60),
    Producte(4, "Monitor", 300.00, 20),
    Producte(5, "Auriculars", 75.00, 30)
]

print("Inventari:")
print("-" * 50)
print(f"{'ID':>4} {'Producte':<15} {'Preu':>10} {'Estoc':>8} {'Valor':>10}")
print("-" * 50)

valor_total = 0
for p in inventari:
    valor = p.preu * p.estoc
    valor_total += valor
    print(f"{p.id:>4} {p.nom:<15} {p.preu:>10.2f}€ {p.estoc:>8} {valor:>10.2f}€")

print("-" * 50)
print(f"{'TOTAL':>30} {valor_total:>22.2f}€")

# Productes amb estoc baix (menys de 25 unitats)
print("\n⚠️ Productes amb estoc baix:")
for p in inventari:
    if p.estoc < 25:
        print(f"  - {p.nom}: {p.estoc} unitats")

# Producte més car
mes_car = max(inventari, key=lambda p: p.preu)
print(f"\n💰 Producte més car: {mes_car.nom} ({mes_car.preu}€)")
