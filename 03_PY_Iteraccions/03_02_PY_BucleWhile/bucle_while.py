# Exemple de Bucle While en Python
# =================================

# El bucle while repeteix un bloc de codi mentre una condició sigui certa.

# 1. Bucle while bàsic
print("=== Bucle while bàsic ===")
comptador = 1

while comptador <= 5:
    print(f"Comptador: {comptador}")
    comptador += 1

print(f"Fi del bucle. Comptador final: {comptador}")

# 2. Bucle while amb condició booleana
print("\n=== Bucle while amb condició booleana ===")
continuar = True
intents = 0

while continuar:
    intents += 1
    print(f"Intent {intents}")
    if intents >= 3:
        continuar = False

print("Bucle finalitzat després de 3 intents")

# 3. Bucle while amb entrada d'usuari (simulat)
print("\n=== Bucle while amb entrada (simulat) ===")
respostes = ["no", "no", "sí"]  # Simulem les respostes
index = 0

while index < len(respostes):
    resposta = respostes[index]
    print(f"Vols sortir? Resposta: {resposta}")
    if resposta.lower() in ["sí", "si", "s"]:
        print("Sortint del programa...")
        break
    index += 1
else:
    print("S'han acabat les respostes simulades")

# 4. Bucle while amb break
print("\n=== Bucle while amb break ===")
num = 0

while True:  # Bucle infinit
    num += 1
    print(f"Nombre: {num}")
    if num >= 5:
        print("Hem arribat a 5, sortint!")
        break

# 5. Bucle while amb continue
print("\n=== Bucle while amb continue ===")
i = 0

print("Mostrant només nombres parells del 1 al 10:")
while i < 10:
    i += 1
    if i % 2 != 0:  # Si és senar, saltem
        continue
    print(f"  {i}")

# 6. Bucle while amb else
print("\n=== Bucle while amb else ===")
n = 1

# L'else s'executa si el while acaba normalment (sense break)
while n <= 5:
    print(f"  n = {n}")
    n += 1
else:
    print("El bucle ha acabat normalment")

# Exemple amb break (l'else no s'executa)
print("\nAmb break:")
m = 1
while m <= 5:
    print(f"  m = {m}")
    if m == 3:
        print("  Sortint amb break")
        break
    m += 1
else:
    print("Això no es mostrarà perquè hem fet break")

# 7. Compte enrere
print("\n=== Compte enrere ===")
segons = 5

while segons > 0:
    print(f"  {segons}...")
    segons -= 1

print("  🚀 Enlairament!")

# 8. Cerca d'elements
print("\n=== Cerca d'elements ===")
llista = [4, 7, 2, 9, 1, 8, 5]
objectiu = 9
index = 0
trobat = False

while index < len(llista):
    if llista[index] == objectiu:
        trobat = True
        break
    index += 1

if trobat:
    print(f"Element {objectiu} trobat a l'índex {index}")
else:
    print(f"Element {objectiu} no trobat")

# 9. Validació de dades (simulat)
print("\n=== Validació de dades ===")
contrasenyes_provades = ["123", "abc", "password123"]
contrasenya_correcta = "password123"
intent = 0

while intent < len(contrasenyes_provades):
    prova = contrasenyes_provades[intent]
    print(f"Intent {intent + 1}: Prova amb '{prova}'")
    
    if prova == contrasenya_correcta:
        print("  ✓ Contrasenya correcta!")
        break
    else:
        print("  ✗ Contrasenya incorrecta")
    
    intent += 1
else:
    print("S'han esgotat tots els intents")

# 10. Bucle while amb múltiples condicions
print("\n=== Bucle while amb múltiples condicions ===")
punts = 0
vides = 3
nivell = 1

while vides > 0 and nivell <= 3:
    print(f"Nivell {nivell}: {punts} punts, {vides} vides")
    punts += 100
    if nivell == 2:  # Simulem perdre una vida
        vides -= 1
        print("  → Has perdut una vida!")
    nivell += 1

print(f"Joc acabat: {punts} punts, {vides} vides restants")

# 11. Exemple pràctic: Menú interactiu (simulat)
print("\n=== Exemple pràctic: Menú interactiu ===")
opcions_seleccionades = [1, 2, 3, 4]  # Simulem les opcions seleccionades
index_opcio = 0
saldo = 1000

while index_opcio < len(opcions_seleccionades):
    print("\n--- MENÚ ---")
    print("1. Consultar saldo")
    print("2. Ingressar diners")
    print("3. Retirar diners")
    print("4. Sortir")
    
    opcio = opcions_seleccionades[index_opcio]
    print(f"Opció seleccionada: {opcio}")
    
    if opcio == 1:
        print(f"El teu saldo és: {saldo}€")
    elif opcio == 2:
        quantitat = 200  # Simulat
        saldo += quantitat
        print(f"Has ingressat {quantitat}€. Nou saldo: {saldo}€")
    elif opcio == 3:
        quantitat = 100  # Simulat
        if quantitat <= saldo:
            saldo -= quantitat
            print(f"Has retirat {quantitat}€. Nou saldo: {saldo}€")
        else:
            print("Saldo insuficient")
    elif opcio == 4:
        print("Gràcies per utilitzar el servei!")
        break
    else:
        print("Opció no vàlida")
    
    index_opcio += 1

# 12. Algorisme: Trobar el màxim comú divisor (MCD)
print("\n=== Algorisme: MCD (Euclides) ===")

def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1, num2 = 48, 18
resultat = mcd(num1, num2)
print(f"El MCD de {num1} i {num2} és: {resultat}")

# 13. Generador de Fibonacci
print("\n=== Seqüència de Fibonacci ===")
a, b = 0, 1
print("Primers 10 nombres de Fibonacci:")
comptador = 0

while comptador < 10:
    print(f"  {a}")
    a, b = b, a + b
    comptador += 1
