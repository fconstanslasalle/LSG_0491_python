# Exemple d'Operacions amb Llistes en Python
# ============================================

# Les llistes són col·leccions ordenades i mutables d'elements.

# 1. Crear llistes
print("=== Crear llistes ===")
llista_buida = []
nombres = [1, 2, 3, 4, 5]
fruites = ["poma", "plàtan", "taronja"]
mixta = [1, "text", 3.14, True, None]
llista_range = list(range(1, 6))

print(f"Llista buida: {llista_buida}")
print(f"Nombres: {nombres}")
print(f"Fruites: {fruites}")
print(f"Mixta: {mixta}")
print(f"Des de range: {llista_range}")

# 2. Accedir a elements (indexació)
print("\n=== Accedir a elements ===")
lletres = ['a', 'b', 'c', 'd', 'e']

print(f"Llista: {lletres}")
print(f"Primer element [0]: {lletres[0]}")
print(f"Tercer element [2]: {lletres[2]}")
print(f"Últim element [-1]: {lletres[-1]}")
print(f"Penúltim element [-2]: {lletres[-2]}")

# 3. Slicing (tallar llistes)
print("\n=== Slicing ===")
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"Llista original: {nums}")
print(f"nums[2:5]: {nums[2:5]}")         # Elements 2, 3, 4
print(f"nums[:4]: {nums[:4]}")           # Des del principi fins 3
print(f"nums[6:]: {nums[6:]}")           # Des de 6 fins al final
print(f"nums[::2]: {nums[::2]}")         # Cada 2 elements
print(f"nums[1::2]: {nums[1::2]}")       # Senars per índex
print(f"nums[::-1]: {nums[::-1]}")       # Invertir la llista
print(f"nums[-3:]: {nums[-3:]}")         # Últims 3 elements
print(f"nums[2:8:2]: {nums[2:8:2]}")     # De 2 a 7, cada 2

# 4. Modificar elements
print("\n=== Modificar elements ===")
colors = ["vermell", "verd", "blau"]
print(f"Original: {colors}")

colors[1] = "groc"
print(f"Després de colors[1] = 'groc': {colors}")

colors[0:2] = ["negre", "blanc"]
print(f"Després de colors[0:2] = ['negre', 'blanc']: {colors}")

# 5. Afegir elements
print("\n=== Afegir elements ===")
animals = ["gat", "gos"]
print(f"Original: {animals}")

animals.append("conill")
print(f"Després d'append('conill'): {animals}")

animals.insert(1, "ocell")
print(f"Després d'insert(1, 'ocell'): {animals}")

animals.extend(["peix", "tortuga"])
print(f"Després d'extend(['peix', 'tortuga']): {animals}")

# També podem usar + per concatenar
nous_animals = animals + ["hamster"]
print(f"Concatenació amb +: {nous_animals}")

# 6. Eliminar elements
print("\n=== Eliminar elements ===")
llenguatges = ["Python", "Java", "C++", "JavaScript", "Go", "Rust"]
print(f"Original: {llenguatges}")

eliminat = llenguatges.pop()
print(f"Després de pop(): {llenguatges} (eliminat: {eliminat})")

eliminat = llenguatges.pop(1)
print(f"Després de pop(1): {llenguatges} (eliminat: {eliminat})")

llenguatges.remove("Go")
print(f"Després de remove('Go'): {llenguatges}")

del llenguatges[0]
print(f"Després de del llenguatges[0]: {llenguatges}")

# Clear - eliminar tots
llista_temp = [1, 2, 3]
llista_temp.clear()
print(f"Després de clear(): {llista_temp}")

# 7. Operadors amb llistes
print("\n=== Operadors amb llistes ===")
a = [1, 2, 3]
b = [4, 5, 6]

print(f"a = {a}")
print(f"b = {b}")
print(f"a + b = {a + b}")            # Concatenació
print(f"a * 3 = {a * 3}")            # Repetició
print(f"2 in a: {2 in a}")           # Pertinença
print(f"10 not in a: {10 not in a}") # No pertinença
print(f"len(a): {len(a)}")           # Longitud

# 8. Funcions amb llistes numèriques
print("\n=== Funcions amb llistes numèriques ===")
notes = [7.5, 8.2, 6.0, 9.1, 7.8, 8.5]
print(f"Notes: {notes}")

print(f"min(notes): {min(notes)}")
print(f"max(notes): {max(notes)}")
print(f"sum(notes): {sum(notes)}")
print(f"Mitjana: {sum(notes) / len(notes):.2f}")
print(f"sorted(notes): {sorted(notes)}")
print(f"sorted(notes, reverse=True): {sorted(notes, reverse=True)}")

# 9. Copiar llistes
print("\n=== Copiar llistes ===")
original = [1, 2, 3, 4, 5]

# Atenció: assignació NO crea còpia
referencia = original
referencia.append(6)
print(f"Original després d'afegir a referència: {original}")  # Afectat!

# Formes de crear còpies independents
copia1 = original.copy()
copia2 = list(original)
copia3 = original[:]

copia1.append(7)
print(f"Original: {original}")
print(f"Còpia (modificada): {copia1}")

# 10. Llistes niuades (matrius)
print("\n=== Llistes niuades (matrius) ===")
matriu = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriu:")
for fila in matriu:
    print(f"  {fila}")

print(f"\nElement [1][2]: {matriu[1][2]}")  # 6
print(f"Primera fila: {matriu[0]}")
print(f"Diagonal: {matriu[0][0]}, {matriu[1][1]}, {matriu[2][2]}")

# 11. Exemple pràctic: Gestió de notes
print("\n=== Exemple pràctic: Gestió de notes ===")
estudiants = [
    ["Anna", [7.5, 8.0, 9.0]],
    ["Pere", [6.0, 7.0, 5.5]],
    ["Maria", [8.5, 9.0, 8.0]]
]

print("Informe de notes:")
print("-" * 35)
for nom, notes in estudiants:
    mitjana = sum(notes) / len(notes)
    aprovat = "✓" if mitjana >= 5 else "✗"
    print(f"{nom:10} | Notes: {notes} | Mitjana: {mitjana:.2f} {aprovat}")
