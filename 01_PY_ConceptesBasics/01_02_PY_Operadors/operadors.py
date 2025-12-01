# Exemple d'Operadors en Python
# ==============================

# Els operadors són símbols especials que realitzen operacions sobre variables i valors.

# 1. Operadors Aritmètics
print("=== Operadors Aritmètics ===")
a = 15
b = 4

print(f"a = {a}, b = {b}")
print(f"Suma (a + b): {a + b}")          # 19
print(f"Resta (a - b): {a - b}")         # 11
print(f"Multiplicació (a * b): {a * b}") # 60
print(f"Divisió (a / b): {a / b}")       # 3.75
print(f"Divisió entera (a // b): {a // b}")  # 3
print(f"Mòdul/Residu (a % b): {a % b}")  # 3
print(f"Exponenciació (a ** b): {a ** b}")   # 50625 (15^4)

# 2. Operadors de Comparació
print("\n=== Operadors de Comparació ===")
x = 10
y = 20

print(f"x = {x}, y = {y}")
print(f"Igual (x == y): {x == y}")               # False
print(f"No igual (x != y): {x != y}")            # True
print(f"Més gran que (x > y): {x > y}")          # False
print(f"Més petit que (x < y): {x < y}")         # True
print(f"Més gran o igual (x >= y): {x >= y}")    # False
print(f"Més petit o igual (x <= y): {x <= y}")   # True

# 3. Operadors Lògics
print("\n=== Operadors Lògics ===")
veritat = True
fals = False

print(f"veritat = {veritat}, fals = {fals}")
print(f"AND (veritat and fals): {veritat and fals}")   # False
print(f"OR (veritat or fals): {veritat or fals}")      # True
print(f"NOT (not veritat): {not veritat}")             # False
print(f"NOT (not fals): {not fals}")                   # True

# Exemple pràctic amb operadors lògics
edat = 25
te_carnet = True
pot_conduir = edat >= 18 and te_carnet
print(f"\nEdat: {edat}, Té carnet: {te_carnet}")
print(f"Pot conduir (edat >= 18 and te_carnet): {pot_conduir}")

# 4. Operadors d'Assignació
print("\n=== Operadors d'Assignació ===")
num = 10
print(f"Valor inicial: num = {num}")

num += 5    # Equivalent a: num = num + 5
print(f"Després de num += 5: {num}")

num -= 3    # Equivalent a: num = num - 3
print(f"Després de num -= 3: {num}")

num *= 2    # Equivalent a: num = num * 2
print(f"Després de num *= 2: {num}")

num /= 4    # Equivalent a: num = num / 4
print(f"Després de num /= 4: {num}")

num //= 2   # Equivalent a: num = num // 2
print(f"Després de num //= 2: {num}")

valor = 17
valor %= 5  # Equivalent a: valor = valor % 5
print(f"\nvalor = 17, després de valor %= 5: {valor}")

base = 2
base **= 3  # Equivalent a: base = base ** 3
print(f"base = 2, després de base **= 3: {base}")

# 5. Operadors d'Identitat
print("\n=== Operadors d'Identitat ===")
llista1 = [1, 2, 3]
llista2 = [1, 2, 3]
llista3 = llista1

print(f"llista1 = {llista1}")
print(f"llista2 = {llista2}")
print(f"llista3 = llista1 (mateixa referència)")

print(f"llista1 is llista2: {llista1 is llista2}")   # False (diferents objectes)
print(f"llista1 is llista3: {llista1 is llista3}")   # True (mateixa referència)
print(f"llista1 == llista2: {llista1 == llista2}")   # True (mateix contingut)
print(f"llista1 is not llista2: {llista1 is not llista2}")   # True

# 6. Operadors de Pertinença
print("\n=== Operadors de Pertinença ===")
fruites = ["poma", "plàtan", "taronja"]
text = "Hola món"

print(f"fruites = {fruites}")
print(f"'poma' in fruites: {'poma' in fruites}")         # True
print(f"'cirera' in fruites: {'cirera' in fruites}")     # False
print(f"'cirera' not in fruites: {'cirera' not in fruites}")   # True

print(f"\ntext = '{text}'")
print(f"'món' in text: {'món' in text}")                 # True
print(f"'adéu' in text: {'adéu' in text}")               # False

# 7. Precedència d'Operadors
print("\n=== Precedència d'Operadors ===")
resultat1 = 10 + 5 * 2       # Multiplicació primer
resultat2 = (10 + 5) * 2     # Parèntesis primer

print(f"10 + 5 * 2 = {resultat1}")   # 20 (no 30)
print(f"(10 + 5) * 2 = {resultat2}") # 30

# Exemple més complex
resultat3 = 2 + 3 * 4 ** 2 / 8 - 1
print(f"2 + 3 * 4 ** 2 / 8 - 1 = {resultat3}")
# Explicació: 4**2=16, 3*16=48, 48/8=6, 2+6-1=7
