# Exemple de Condicionals If-Else en Python
# ==========================================

# Les estructures condicionals permeten executar codi diferent segons es compleixin certes condicions.

# 1. Estructura if simple
print("=== Estructura if simple ===")
edat = 20

if edat >= 18:
    print(f"Amb {edat} anys, ets major d'edat.")

# 2. Estructura if-else
print("\n=== Estructura if-else ===")
nota = 4.5

if nota >= 5:
    print(f"Has aprovat amb un {nota}!")
else:
    print(f"Has suspès amb un {nota}. Has d'estudiar més.")

# 3. Estructura if-elif-else
print("\n=== Estructura if-elif-else ===")
puntuacio = 85

if puntuacio >= 90:
    qualificacio = "Excel·lent"
elif puntuacio >= 80:
    qualificacio = "Notable"
elif puntuacio >= 70:
    qualificacio = "Bé"
elif puntuacio >= 60:
    qualificacio = "Suficient"
else:
    qualificacio = "Insuficient"

print(f"Amb una puntuació de {puntuacio}, la qualificació és: {qualificacio}")

# 4. Condicionals amb operadors lògics
print("\n=== Condicionals amb operadors lògics ===")
te_carnet = True
anys_experiencia = 2

# Operador AND
if te_carnet and anys_experiencia >= 1:
    print("Pots conduir sol.")
else:
    print("No pots conduir sol.")

# Operador OR
es_cap_de_setmana = True
es_festiu = False

if es_cap_de_setmana or es_festiu:
    print("Avui és dia de descans!")
else:
    print("Avui és dia de feina.")

# Operador NOT
esta_plovent = False

if not esta_plovent:
    print("Podem sortir a passejar!")
else:
    print("Millor quedar-se a casa.")

# 5. Condicionals niuats (nested)
print("\n=== Condicionals niuats ===")
usuari_valid = True
contrasenya_correcta = True
es_admin = False

if usuari_valid:
    if contrasenya_correcta:
        if es_admin:
            print("Benvingut, administrador!")
        else:
            print("Benvingut, usuari!")
    else:
        print("Contrasenya incorrecta.")
else:
    print("Usuari no vàlid.")

# 6. Operador ternari (condicional en una línia)
print("\n=== Operador ternari ===")
temperatura = 25
estat = "Fa calor" if temperatura > 20 else "Fa fred"
print(f"Amb {temperatura}°C: {estat}")

# Exemple més complex
edat = 17
tipus_entrada = "juvenil" if edat < 18 else "adult" if edat < 65 else "jubilat"
print(f"Amb {edat} anys, l'entrada és de tipus: {tipus_entrada}")

# 7. Comprovació de valors buits o None
print("\n=== Comprovació de valors buits ===")
nom = ""
llista = []
valor = None

if nom:
    print(f"El nom és: {nom}")
else:
    print("El nom està buit.")

if llista:
    print(f"La llista té elements: {llista}")
else:
    print("La llista està buida.")

if valor is None:
    print("El valor és None.")
else:
    print(f"El valor és: {valor}")

# 8. Comparació de cadenes
print("\n=== Comparació de cadenes ===")
resposta = "sí"

if resposta.lower() in ["sí", "si", "s", "yes", "y"]:
    print("Has respost afirmativament.")
elif resposta.lower() in ["no", "n"]:
    print("Has respost negativament.")
else:
    print("Resposta no reconeguda.")

# 9. Exemple pràctic: Calculadora de descomptes
print("\n=== Calculadora de descomptes ===")
preu_original = 100
es_soci = True
quantitat = 5

if es_soci:
    descompte = 0.20  # 20% de descompte per socis
elif quantitat >= 10:
    descompte = 0.15  # 15% per compres grans
elif quantitat >= 5:
    descompte = 0.10  # 10% per compres mitjanes
else:
    descompte = 0     # Sense descompte

preu_final = preu_original * (1 - descompte) * quantitat
print(f"Preu original: {preu_original}€")
print(f"Quantitat: {quantitat}")
print(f"Descompte aplicat: {descompte * 100}%")
print(f"Preu final: {preu_final}€")
