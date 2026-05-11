# Exemple d'Operacions amb Tuples en Python
# ==========================================

# Les tuples són col·leccions ordenades i immutables d'elements.

# 1. Crear tuples
print("=== Crear tuples ===")
tupla_buida = ()
tupla_un_element = (42,)  # La coma és necessària per un sol element!
coordenades = (10, 20)
colors = ("vermell", "verd", "blau")
mixta = (1, "text", 3.14, True)
sense_parentesis = 1, 2, 3, 4  # També és una tupla

print(f"Tupla buida: {tupla_buida}")
print(f"Tupla d'un element: {tupla_un_element}")
print(f"Coordenades: {coordenades}")
print(f"Colors: {colors}")
print(f"Mixta: {mixta}")
print(f"Sense parèntesis: {sense_parentesis}, tipus: {type(sense_parentesis)}")

# ATENCIÓ: Sense la coma, no és una tupla
no_es_tupla = (42)
print(f"\n(42) sense coma: {no_es_tupla}, tipus: {type(no_es_tupla)}")

# 2. Accedir a elements
print("\n=== Accedir a elements ===")
dies = ("dilluns", "dimarts", "dimecres", "dijous", "divendres")
print(f"Tupla: {dies}")

print(f"Primer element [0]: {dies[0]}")
print(f"Tercer element [2]: {dies[2]}")
print(f"Últim element [-1]: {dies[-1]}")
print(f"Penúltim element [-2]: {dies[-2]}")

# 3. Slicing amb tuples
print("\n=== Slicing amb tuples ===")
nums = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"Tupla original: {nums}")

print(f"nums[2:5]: {nums[2:5]}")
print(f"nums[:4]: {nums[:4]}")
print(f"nums[6:]: {nums[6:]}")
print(f"nums[::2]: {nums[::2]}")
print(f"nums[::-1]: {nums[::-1]}")

# 4. Immutabilitat de les tuples
print("\n=== Immutabilitat ===")
punt = (5, 10)
print(f"Punt original: {punt}")

# Això donaria error:
# punt[0] = 15  # TypeError: 'tuple' object does not support item assignment

# Podem crear una nova tupla basada en l'antiga
nou_punt = (15,) + punt[1:]
print(f"Nou punt (modificant el primer valor): {nou_punt}")

# O convertir a llista, modificar i tornar a tupla
llista_temp = list(punt)
llista_temp[0] = 20
punt_modificat = tuple(llista_temp)
print(f"Punt modificat via llista: {punt_modificat}")

# 5. Operadors amb tuples
print("\n=== Operadors amb tuples ===")
a = (1, 2, 3)
b = (4, 5, 6)

print(f"a = {a}")
print(f"b = {b}")
print(f"a + b (concatenació): {a + b}")
print(f"a * 3 (repetició): {a * 3}")
print(f"2 in a: {2 in a}")
print(f"10 not in a: {10 not in a}")
print(f"len(a): {len(a)}")

# 6. Mètodes de tuples
print("\n=== Mètodes de tuples ===")
lletres = ('a', 'b', 'c', 'b', 'd', 'b')
print(f"Tupla: {lletres}")

print(f"count('b'): {lletres.count('b')}")
print(f"index('c'): {lletres.index('c')}")
print(f"index('b', 2): {lletres.index('b', 2)}")  # Busca des de l'índex 2

# 7. Desempaquetat (unpacking) de tuples
print("\n=== Desempaquetat de tuples ===")
coordenada = (100, 200, 50)

# Desempaquetat bàsic
x, y, z = coordenada
print(f"Coordenada: {coordenada}")
print(f"x = {x}, y = {y}, z = {z}")

# Desempaquetat amb * (starred expression)
primer, *resta = (1, 2, 3, 4, 5)
print(f"\nprimer, *resta = (1, 2, 3, 4, 5)")
print(f"primer = {primer}, resta = {resta}")

*inici, ultim = (1, 2, 3, 4, 5)
print(f"\n*inici, ultim = (1, 2, 3, 4, 5)")
print(f"inici = {inici}, ultim = {ultim}")

primer, *mig, ultim = (1, 2, 3, 4, 5)
print(f"\nprimer, *mig, ultim = (1, 2, 3, 4, 5)")
print(f"primer = {primer}, mig = {mig}, ultim = {ultim}")

# 8. Intercanvi de valors
print("\n=== Intercanvi de valors ===")
a = 10
b = 20
print(f"Abans: a = {a}, b = {b}")

a, b = b, a  # Utilitza tuples internament
print(f"Després de a, b = b, a: a = {a}, b = {b}")

# 9. Tuples en bucles
print("\n=== Tuples en bucles ===")
persones = (
    ("Anna", 25),
    ("Pere", 30),
    ("Maria", 28)
)

print("Desempaquetat en for:")
for nom, edat in persones:
    print(f"  {nom} té {edat} anys")

# 10. Funcions amb tuples
print("\n=== Funcions amb tuples ===")
notes = (7.5, 8.2, 6.0, 9.1, 8.5)
print(f"Notes: {notes}")

print(f"min(notes): {min(notes)}")
print(f"max(notes): {max(notes)}")
print(f"sum(notes): {sum(notes)}")
print(f"sorted(notes): {sorted(notes)}")  # Retorna una llista!
print(f"tuple(sorted(notes)): {tuple(sorted(notes))}")

# 11. Tuples com a claus de diccionari
print("\n=== Tuples com a claus de diccionari ===")
# Les tuples són hashables, per tant poden ser claus
mapa = {
    (0, 0): "Origen",
    (1, 0): "Dreta",
    (0, 1): "Amunt",
    (-1, 0): "Esquerra",
    (0, -1): "Avall"
}

posicio = (1, 0)
print(f"Posició {posicio}: {mapa[posicio]}")

# Les llistes NO poden ser claus
# mapa = {[1, 2]: "error"}  # TypeError: unhashable type: 'list'

# 12. Comparació de tuples
print("\n=== Comparació de tuples ===")
t1 = (1, 2, 3)
t2 = (1, 2, 4)
t3 = (1, 2, 3)

print(f"t1 = {t1}, t2 = {t2}, t3 = {t3}")
print(f"t1 == t3: {t1 == t3}")
print(f"t1 < t2: {t1 < t2}")  # Compara element a element
print(f"t1 != t2: {t1 != t2}")

# 13. Conversions
print("\n=== Conversions ===")
llista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)
text = "hola"

print(f"Llista a tupla: {tuple(llista)}")
print(f"Tupla a llista: {list(tupla)}")
print(f"String a tupla: {tuple(text)}")

# 14. Exemple pràctic: Coordenades i distàncies
print("\n=== Exemple pràctic: Coordenades ===")
import math

def distancia(punt1, punt2):
    """Calcula la distància euclidiana entre dos punts."""
    x1, y1 = punt1
    x2, y2 = punt2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

punt_a = (0, 0)
punt_b = (3, 4)
punt_c = (6, 8)

print(f"Punt A: {punt_a}")
print(f"Punt B: {punt_b}")
print(f"Punt C: {punt_c}")
print(f"Distància A-B: {distancia(punt_a, punt_b)}")
print(f"Distància B-C: {distancia(punt_b, punt_c)}")
print(f"Distància A-C: {distancia(punt_a, punt_c)}")
