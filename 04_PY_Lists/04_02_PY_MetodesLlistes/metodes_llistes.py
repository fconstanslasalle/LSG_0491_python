# Exemple de Mètodes de Llistes en Python
# ========================================

# Les llistes tenen molts mètodes incorporats per manipular-les.

# 1. Mètode append() - Afegir element al final
print("=== Mètode append() ===")
compres = ["llet", "pa"]
print(f"Original: {compres}")

compres.append("ous")
print(f"Després d'append('ous'): {compres}")

compres.append(["fruita", "verdura"])  # Afegeix la llista com un element
print(f"Després d'append(['fruita', 'verdura']): {compres}")

# 2. Mètode extend() - Afegir múltiples elements
print("\n=== Mètode extend() ===")
nums = [1, 2, 3]
print(f"Original: {nums}")

nums.extend([4, 5, 6])
print(f"Després d'extend([4, 5, 6]): {nums}")

# extend també funciona amb altres iterables
nums.extend(range(7, 10))
print(f"Després d'extend(range(7, 10)): {nums}")

# 3. Mètode insert() - Inserir en posició específica
print("\n=== Mètode insert() ===")
dies = ["dilluns", "dimecres", "dijous"]
print(f"Original: {dies}")

dies.insert(1, "dimarts")
print(f"Després d'insert(1, 'dimarts'): {dies}")

dies.insert(0, "diumenge")
print(f"Després d'insert(0, 'diumenge'): {dies}")

# 4. Mètode remove() - Eliminar per valor
print("\n=== Mètode remove() ===")
lletres = ['a', 'b', 'c', 'b', 'd']
print(f"Original: {lletres}")

lletres.remove('b')  # Elimina només la primera ocurrència
print(f"Després de remove('b'): {lletres}")

# 5. Mètode pop() - Eliminar per índex i retornar
print("\n=== Mètode pop() ===")
pila = [1, 2, 3, 4, 5]
print(f"Original: {pila}")

ultim = pila.pop()
print(f"Després de pop(): {pila} (element extret: {ultim})")

segon = pila.pop(1)
print(f"Després de pop(1): {pila} (element extret: {segon})")

# 6. Mètode clear() - Eliminar tots els elements
print("\n=== Mètode clear() ===")
temporal = [1, 2, 3, 4, 5]
print(f"Original: {temporal}")

temporal.clear()
print(f"Després de clear(): {temporal}")

# 7. Mètode index() - Trobar posició d'un element
print("\n=== Mètode index() ===")
fruites = ["poma", "plàtan", "taronja", "maduixa", "plàtan"]
print(f"Llista: {fruites}")

pos = fruites.index("taronja")
print(f"index('taronja'): {pos}")

# Buscar des d'una posició específica
pos2 = fruites.index("plàtan", 2)  # Busca després de l'índex 2
print(f"index('plàtan', 2): {pos2}")

# 8. Mètode count() - Comptar ocurrències
print("\n=== Mètode count() ===")
valors = [1, 2, 2, 3, 2, 4, 2, 5]
print(f"Llista: {valors}")

quants = valors.count(2)
print(f"count(2): {quants}")

text_llista = list("mississippi")
print(f"\nLletres de 'mississippi': {text_llista}")
print(f"Quantes 's': {text_llista.count('s')}")
print(f"Quantes 'i': {text_llista.count('i')}")
print(f"Quantes 'p': {text_llista.count('p')}")

# 9. Mètode sort() - Ordenar la llista (modifica l'original)
print("\n=== Mètode sort() ===")
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(f"Original: {numeros}")

numeros.sort()
print(f"Després de sort(): {numeros}")

numeros.sort(reverse=True)
print(f"Després de sort(reverse=True): {numeros}")

# Ordenar strings
noms = ["Pere", "anna", "Maria", "joan"]
print(f"\nNoms original: {noms}")

noms.sort()
print(f"Després de sort(): {noms}")

noms.sort(key=str.lower)  # Ordenar ignorant majúscules/minúscules
print(f"Després de sort(key=str.lower): {noms}")

# Ordenar per longitud
paraules = ["elefant", "gat", "llop", "formiga"]
print(f"\nParaules: {paraules}")

paraules.sort(key=len)
print(f"Ordenat per longitud: {paraules}")

# 10. Mètode reverse() - Invertir la llista
print("\n=== Mètode reverse() ===")
seqüencia = [1, 2, 3, 4, 5]
print(f"Original: {seqüencia}")

seqüencia.reverse()
print(f"Després de reverse(): {seqüencia}")

# 11. Mètode copy() - Crear còpia
print("\n=== Mètode copy() ===")
original = [1, 2, 3, 4, 5]
copia = original.copy()

copia.append(6)
print(f"Original: {original}")
print(f"Còpia: {copia}")

# 12. Comparació sort() vs sorted()
print("\n=== sort() vs sorted() ===")
dades = [5, 2, 8, 1, 9]
print(f"Dades original: {dades}")

# sorted() retorna una nova llista, no modifica l'original
ordenada = sorted(dades)
print(f"sorted(dades): {ordenada}")
print(f"Dades després de sorted(): {dades}")

# sort() modifica la llista original
dades.sort()
print(f"Dades després de sort(): {dades}")

# 13. Exemple pràctic: Gestió de tasques
print("\n=== Exemple pràctic: Gestió de tasques ===")

tasques = []

# Afegir tasques
tasques.append({"id": 1, "nom": "Comprar pa", "prioritat": 2})
tasques.append({"id": 2, "nom": "Estudiar Python", "prioritat": 1})
tasques.append({"id": 3, "nom": "Fer esport", "prioritat": 3})
tasques.append({"id": 4, "nom": "Llegir llibre", "prioritat": 2})

print("Tasques afegides:")
for t in tasques:
    print(f"  {t['id']}. {t['nom']} (prioritat: {t['prioritat']})")

# Ordenar per prioritat
tasques.sort(key=lambda x: x['prioritat'])
print("\nTasques ordenades per prioritat:")
for t in tasques:
    print(f"  {t['id']}. {t['nom']} (prioritat: {t['prioritat']})")

# Eliminar tasca completada
tasques_id2 = [t for t in tasques if t['id'] == 2]
if tasques_id2:
    tasques.remove(tasques_id2[0])
    print(f"\nTasca 2 completada i eliminada")

print("\nTasques restants:")
for t in tasques:
    print(f"  {t['id']}. {t['nom']}")

# 14. Exemple pràctic: Puntuacions de jugadors
print("\n=== Exemple pràctic: Puntuacions ===")

puntuacions = [
    {"nom": "Anna", "punts": 850},
    {"nom": "Pere", "punts": 920},
    {"nom": "Maria", "punts": 780},
    {"nom": "Joan", "punts": 950},
    {"nom": "Laia", "punts": 890}
]

# Ordenar per puntuació (descendent)
puntuacions.sort(key=lambda x: x['punts'], reverse=True)

print("Taula de classificació:")
print("-" * 25)
for i, jugador in enumerate(puntuacions, 1):
    medalla = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else "  "
    print(f"{medalla} {i}. {jugador['nom']:10} {jugador['punts']} pts")

# Mitjana de puntuacions
mitjana = sum(j['punts'] for j in puntuacions) / len(puntuacions)
print(f"\nMitjana de puntuació: {mitjana:.1f}")

# Comptar jugadors per sobre de la mitjana
per_sobre = len([j for j in puntuacions if j['punts'] > mitjana])
print(f"Jugadors per sobre la mitjana: {per_sobre}")
