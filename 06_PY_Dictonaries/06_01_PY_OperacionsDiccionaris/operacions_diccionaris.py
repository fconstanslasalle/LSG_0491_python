# Exemple d'Operacions amb Diccionaris en Python
# ================================================

# Els diccionaris són col·leccions de parells clau-valor.

# 1. Crear diccionaris
print("=== Crear diccionaris ===")
dic_buit = {}
dic_buit2 = dict()

persona = {
    "nom": "Anna",
    "edat": 25,
    "ciutat": "Barcelona"
}

notes = dict(matematiques=8.5, fisica=7.2, quimica=9.0)
des_de_llista = dict([("a", 1), ("b", 2), ("c", 3)])
des_de_zip = dict(zip(["x", "y", "z"], [10, 20, 30]))

print(f"Diccionari buit: {dic_buit}")
print(f"Persona: {persona}")
print(f"Notes: {notes}")
print(f"Des de llista de tuples: {des_de_llista}")
print(f"Des de zip: {des_de_zip}")

# 2. Accedir a valors
print("\n=== Accedir a valors ===")
estudiant = {
    "nom": "Pere",
    "edat": 22,
    "carrera": "Informàtica",
    "any_inici": 2021
}

print(f"Diccionari: {estudiant}")
print(f"Accés amb []: estudiant['nom'] = {estudiant['nom']}")
print(f"Accés amb get(): estudiant.get('edat') = {estudiant.get('edat')}")

# Diferència entre [] i get()
# estudiant['nota']  # KeyError si no existeix
print(f"estudiant.get('nota'): {estudiant.get('nota')}")  # Retorna None
print(f"estudiant.get('nota', 0): {estudiant.get('nota', 0)}")  # Retorna 0

# 3. Modificar i afegir elements
print("\n=== Modificar i afegir elements ===")
cotxe = {
    "marca": "Toyota",
    "model": "Corolla",
    "any": 2020
}
print(f"Original: {cotxe}")

# Modificar valor existent
cotxe["any"] = 2022
print(f"Després de modificar 'any': {cotxe}")

# Afegir nova clau-valor
cotxe["color"] = "vermell"
print(f"Després d'afegir 'color': {cotxe}")

# Afegir múltiples amb update()
cotxe.update({"km": 15000, "combustible": "híbrid"})
print(f"Després d'update(): {cotxe}")

# 4. Eliminar elements
print("\n=== Eliminar elements ===")
fruites = {
    "poma": 5,
    "plàtan": 3,
    "taronja": 8,
    "maduixa": 12
}
print(f"Original: {fruites}")

# del - elimina per clau
del fruites["plàtan"]
print(f"Després de del fruites['plàtan']: {fruites}")

# pop() - elimina i retorna el valor
quantitat = fruites.pop("taronja")
print(f"Després de pop('taronja'): {fruites} (valor eliminat: {quantitat})")

# pop() amb valor per defecte si no existeix
quantitat = fruites.pop("kiwi", 0)
print(f"pop('kiwi', 0): {quantitat} (no existia)")

# popitem() - elimina i retorna l'últim element (Python 3.7+)
item = fruites.popitem()
print(f"Després de popitem(): {fruites} (item eliminat: {item})")

# clear() - elimina tots
copia = {"a": 1, "b": 2}
copia.clear()
print(f"Després de clear(): {copia}")

# 5. Comprovar existència de claus
print("\n=== Comprovar existència ===")
config = {
    "idioma": "català",
    "tema": "fosc",
    "notificacions": True
}
print(f"Config: {config}")

print(f"'idioma' in config: {'idioma' in config}")
print(f"'volum' in config: {'volum' in config}")
print(f"'fosc' in config.values(): {'fosc' in config.values()}")

# 6. Iterar sobre diccionaris
print("\n=== Iterar sobre diccionaris ===")
temperatures = {
    "Barcelona": 22,
    "Madrid": 28,
    "València": 25,
    "Sevilla": 32
}

print("Iterar sobre claus:")
for ciutat in temperatures:
    print(f"  {ciutat}")

print("\nIterar sobre valors:")
for temp in temperatures.values():
    print(f"  {temp}°C")

print("\nIterar sobre claus i valors:")
for ciutat, temp in temperatures.items():
    print(f"  {ciutat}: {temp}°C")

# 7. Diccionaris niuats
print("\n=== Diccionaris niuats ===")
empresa = {
    "nom": "TechCorp",
    "empleats": {
        "desenvolupament": 15,
        "disseny": 8,
        "marketing": 5
    },
    "oficines": ["Barcelona", "Madrid"],
    "activa": True
}

print(f"Empresa: {empresa['nom']}")
print(f"Empleats de desenvolupament: {empresa['empleats']['desenvolupament']}")
print(f"Primera oficina: {empresa['oficines'][0]}")

# Afegir a diccionari niuat
empresa["empleats"]["vendes"] = 10
print(f"Empleats actualitzats: {empresa['empleats']}")

# 8. Comprensions de diccionaris
print("\n=== Comprensions de diccionaris ===")

# Quadrats dels nombres
quadrats = {x: x**2 for x in range(1, 6)}
print(f"Quadrats: {quadrats}")

# Filtrar elements
notes_original = {"Anna": 8.5, "Pere": 4.5, "Maria": 9.0, "Joan": 5.5}
aprovats = {nom: nota for nom, nota in notes_original.items() if nota >= 5}
print(f"Aprovats: {aprovats}")

# Invertir clau-valor
original = {"a": 1, "b": 2, "c": 3}
invertit = {v: k for k, v in original.items()}
print(f"Invertit: {invertit}")

# 9. Operadors amb diccionaris
print("\n=== Operadors amb diccionaris ===")
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}

print(f"a = {a}")
print(f"b = {b}")

# Fusionar (Python 3.9+)
fusionat = a | b
print(f"a | b: {fusionat}")

# Fusionar amb update
c = a.copy()
c.update(b)
print(f"a.copy() + update(b): {c}")

# Desempaquetar
fusionat2 = {**a, **b}
print(f"{{**a, **b}}: {fusionat2}")

# 10. Funcions útils
print("\n=== Funcions útils ===")
preus = {"pa": 1.5, "llet": 1.2, "ous": 2.5, "formatge": 4.0}
print(f"Preus: {preus}")

print(f"len(preus): {len(preus)}")
print(f"min(preus): {min(preus)}")  # Clau mínima
print(f"max(preus.values()): {max(preus.values())}")  # Valor màxim

# Clau amb valor màxim
mes_car = max(preus, key=preus.get)
print(f"Producte més car: {mes_car} ({preus[mes_car]}€)")

# 11. Exemple pràctic: Comptador de paraules
print("\n=== Exemple pràctic: Comptador de paraules ===")
text = "el gat i el gos juguen amb el ratolí i el gat guanya"
paraules = text.split()

comptador = {}
for paraula in paraules:
    comptador[paraula] = comptador.get(paraula, 0) + 1

print(f"Text: '{text}'")
print("Freqüència de paraules:")
for paraula, freq in sorted(comptador.items(), key=lambda x: x[1], reverse=True):
    print(f"  '{paraula}': {freq}")

# 12. Exemple pràctic: Registre d'usuaris
print("\n=== Exemple pràctic: Registre d'usuaris ===")
usuaris = {}

def registrar(usuari_id, nom, email):
    usuaris[usuari_id] = {
        "nom": nom,
        "email": email,
        "actiu": True
    }

registrar(1, "Anna Garcia", "anna@email.com")
registrar(2, "Pere López", "pere@email.com")
registrar(3, "Maria Martínez", "maria@email.com")

print("Usuaris registrats:")
for uid, info in usuaris.items():
    print(f"  ID {uid}: {info['nom']} ({info['email']})")
