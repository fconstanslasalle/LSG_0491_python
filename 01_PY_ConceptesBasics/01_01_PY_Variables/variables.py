# Exemple de Variables i Tipus de Dades en Python
# =================================================

# Les variables són contenidors per emmagatzemar valors de dades.
# Python és de tipatge dinàmic, no cal declarar el tipus de variable explícitament.

# 1. Variables de tipus String (cadena de text)
nom = "Anna"
cognom = "Garcia"
ciutat = "Barcelona"

print("=== Variables de tipus String ===")
print(f"Nom: {nom}")
print(f"Cognom: {cognom}")
print(f"Ciutat: {ciutat}")
print(f"Tipus de 'nom': {type(nom)}")

# 2. Variables de tipus Integer (enter)
edat = 25
any_naixement = 1999
quantitat = -50

print("\n=== Variables de tipus Integer ===")
print(f"Edat: {edat}")
print(f"Any de naixement: {any_naixement}")
print(f"Quantitat: {quantitat}")
print(f"Tipus de 'edat': {type(edat)}")

# 3. Variables de tipus Float (nombre decimal)
altura = 1.75
pes = 68.5
temperatura = -3.2

print("\n=== Variables de tipus Float ===")
print(f"Altura: {altura} metres")
print(f"Pes: {pes} kg")
print(f"Temperatura: {temperatura}°C")
print(f"Tipus de 'altura': {type(altura)}")

# 4. Variables de tipus Boolean (booleà)
es_estudiant = True
te_carnet_conduir = False
major_edat = edat >= 18

print("\n=== Variables de tipus Boolean ===")
print(f"És estudiant: {es_estudiant}")
print(f"Té carnet de conduir: {te_carnet_conduir}")
print(f"És major d'edat: {major_edat}")
print(f"Tipus de 'es_estudiant': {type(es_estudiant)}")

# 5. Conversió de tipus (Type Casting)
print("\n=== Conversió de tipus ===")
numero_text = "42"
numero_enter = int(numero_text)  # Convertir string a int
print(f"'{numero_text}' convertit a enter: {numero_enter}")
print(f"Tipus original: {type(numero_text)}, Tipus convertit: {type(numero_enter)}")

decimal_enter = float(25)  # Convertir int a float
print(f"25 convertit a float: {decimal_enter}")

text_numero = str(3.14)  # Convertir float a string
print(f"3.14 convertit a string: '{text_numero}'")

# 6. Concatenació de strings
print("\n=== Concatenació de strings ===")
nom_complet = nom + " " + cognom
print(f"Nom complet: {nom_complet}")
salutacio = f"Hola, em dic {nom} i tinc {edat} anys."
print(salutacio)

# 7. Variables múltiples en una línia
print("\n=== Variables múltiples ===")
x, y, z = 10, 20, 30
print(f"x = {x}, y = {y}, z = {z}")

a = b = c = 100
print(f"a = {a}, b = {b}, c = {c}")
