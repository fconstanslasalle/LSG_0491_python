# Exemple de Bucle For en Python
# ===============================

# El bucle for s'utilitza per iterar sobre seqüències (llistes, tuples, strings, etc.)

# 1. Bucle for amb llista
print("=== Bucle for amb llista ===")
fruites = ["poma", "plàtan", "taronja", "maduixa"]

for fruita in fruites:
    print(f"Fruita: {fruita}")

# 2. Bucle for amb range()
print("\n=== Bucle for amb range() ===")

# range(n) genera nombres de 0 a n-1
print("range(5):")
for i in range(5):
    print(f"  {i}")

# range(inici, fi) genera nombres de inici a fi-1
print("\nrange(2, 7):")
for i in range(2, 7):
    print(f"  {i}")

# range(inici, fi, pas) genera nombres amb un salt determinat
print("\nrange(0, 10, 2) - Nombres parells:")
for i in range(0, 10, 2):
    print(f"  {i}")

print("\nrange(10, 0, -1) - Compte enrere:")
for i in range(10, 0, -1):
    print(f"  {i}")

# 3. Bucle for amb strings
print("\n=== Bucle for amb strings ===")
paraula = "Python"

print(f"Lletres de '{paraula}':")
for lletra in paraula:
    print(f"  {lletra}")

# 4. Bucle for amb enumerate()
print("\n=== Bucle for amb enumerate() ===")
colors = ["vermell", "verd", "blau", "groc"]

for index, color in enumerate(colors):
    print(f"Color {index}: {color}")

# Començant des d'un altre índex
print("\nAmb índex començant des de 1:")
for index, color in enumerate(colors, start=1):
    print(f"Color {index}: {color}")

# 5. Bucle for amb zip()
print("\n=== Bucle for amb zip() ===")
noms = ["Anna", "Pere", "Maria"]
edats = [25, 30, 28]
ciutats = ["Barcelona", "Madrid", "València"]

print("Iterant amb zip():")
for nom, edat, ciutat in zip(noms, edats, ciutats):
    print(f"  {nom} té {edat} anys i viu a {ciutat}")

# 6. Bucle for amb diccionaris
print("\n=== Bucle for amb diccionaris ===")
estudiant = {
    "nom": "Joan",
    "edat": 22,
    "carrera": "Informàtica",
    "nota_mitjana": 7.5
}

# Iterant sobre claus
print("Claus:")
for clau in estudiant:
    print(f"  {clau}")

# Iterant sobre valors
print("\nValors:")
for valor in estudiant.values():
    print(f"  {valor}")

# Iterant sobre claus i valors
print("\nClaus i valors:")
for clau, valor in estudiant.items():
    print(f"  {clau}: {valor}")

# 7. Bucle for amb break i continue
print("\n=== Bucle for amb break i continue ===")

# break - surt del bucle
print("Exemple amb break (sortir quan trobem 'c'):")
for lletra in "abcdef":
    if lletra == 'c':
        print("  Hem trobat 'c', sortint del bucle!")
        break
    print(f"  {lletra}")

# continue - salta a la següent iteració
print("\nExemple amb continue (saltar nombres parells):")
for num in range(1, 11):
    if num % 2 == 0:
        continue
    print(f"  {num}")

# 8. Bucle for amb else
print("\n=== Bucle for amb else ===")

# L'else s'executa si el bucle acaba sense break
nombres = [1, 3, 5, 7, 9]

print("Buscant un nombre parell:")
for num in nombres:
    if num % 2 == 0:
        print(f"  Nombre parell trobat: {num}")
        break
else:
    print("  No s'ha trobat cap nombre parell")

# 9. Bucles niuats
print("\n=== Bucles niuats ===")

print("Taula de multiplicar del 1 al 3:")
for i in range(1, 4):
    print(f"\nTaula del {i}:")
    for j in range(1, 11):
        print(f"  {i} x {j} = {i * j}")

# 10. List comprehension
print("\n=== List comprehension ===")

# Forma tradicional
quadrats_tradicional = []
for x in range(1, 6):
    quadrats_tradicional.append(x ** 2)
print(f"Quadrats (tradicional): {quadrats_tradicional}")

# Amb list comprehension
quadrats = [x ** 2 for x in range(1, 6)]
print(f"Quadrats (comprehension): {quadrats}")

# Amb condició
parells = [x for x in range(1, 11) if x % 2 == 0]
print(f"Nombres parells: {parells}")

# Comprehension amb transformació
noms_majuscules = [nom.upper() for nom in noms]
print(f"Noms en majúscules: {noms_majuscules}")

# 11. Exemple pràctic: Processar dades
print("\n=== Exemple pràctic: Processar dades ===")

vendes = [
    {"producte": "Ordinador", "quantitat": 5, "preu": 800},
    {"producte": "Teclat", "quantitat": 20, "preu": 50},
    {"producte": "Ratolí", "quantitat": 15, "preu": 25},
    {"producte": "Monitor", "quantitat": 8, "preu": 300}
]

total_general = 0
print("Resum de vendes:")
print("-" * 40)

for venda in vendes:
    total = venda["quantitat"] * venda["preu"]
    total_general += total
    print(f"{venda['producte']:15} | {venda['quantitat']:3} units | {total:>8}€")

print("-" * 40)
print(f"{'TOTAL':15} | {'':>8} | {total_general:>8}€")
