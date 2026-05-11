# Exemple de Mètodes de Diccionaris en Python
# =============================================

# Els diccionaris tenen molts mètodes útils incorporats.

# 1. Mètode keys() - Obtenir claus
print("=== Mètode keys() ===")
persona = {
    "nom": "Anna",
    "edat": 25,
    "ciutat": "Barcelona",
    "professio": "Enginyera"
}

claus = persona.keys()
print(f"Diccionari: {persona}")
print(f"keys(): {claus}")
print(f"Tipus: {type(claus)}")
print(f"Com a llista: {list(claus)}")

# keys() és una vista dinàmica
persona["email"] = "anna@email.com"
print(f"Després d'afegir 'email', keys(): {list(claus)}")

# 2. Mètode values() - Obtenir valors
print("\n=== Mètode values() ===")
preus = {"pa": 1.5, "llet": 1.2, "ous": 2.5}
print(f"Diccionari: {preus}")

valors = preus.values()
print(f"values(): {valors}")
print(f"Suma de valors: {sum(valors)}")

# 3. Mètode items() - Obtenir parells clau-valor
print("\n=== Mètode items() ===")
notes = {"Anna": 8.5, "Pere": 7.2, "Maria": 9.0}
print(f"Diccionari: {notes}")

items = notes.items()
print(f"items(): {items}")

# Molt útil per iterar
print("Iteració amb items():")
for nom, nota in items:
    print(f"  {nom}: {nota}")

# 4. Mètode get() - Obtenir amb valor per defecte
print("\n=== Mètode get() ===")
config = {"idioma": "català", "tema": "fosc"}
print(f"Config: {config}")

print(f"get('idioma'): {config.get('idioma')}")
print(f"get('volum'): {config.get('volum')}")  # None
print(f"get('volum', 50): {config.get('volum', 50)}")  # 50

# 5. Mètode setdefault() - Obtenir o establir per defecte
print("\n=== Mètode setdefault() ===")
usuari = {"nom": "Pere", "edat": 30}
print(f"Original: {usuari}")

# Si la clau existeix, retorna el valor existent
edat = usuari.setdefault("edat", 0)
print(f"setdefault('edat', 0): {edat}")
print(f"Diccionari: {usuari}")

# Si la clau no existeix, l'afegeix amb el valor per defecte
ciutat = usuari.setdefault("ciutat", "Desconeguda")
print(f"setdefault('ciutat', 'Desconeguda'): {ciutat}")
print(f"Diccionari: {usuari}")

# 6. Mètode update() - Actualitzar amb altre diccionari
print("\n=== Mètode update() ===")
original = {"a": 1, "b": 2}
print(f"Original: {original}")

# Amb diccionari
original.update({"b": 20, "c": 3})
print(f"Després d'update({{'b': 20, 'c': 3}}): {original}")

# Amb arguments nomenats
original.update(d=4, e=5)
print(f"Després d'update(d=4, e=5): {original}")

# Amb llista de tuples
original.update([("f", 6), ("g", 7)])
print(f"Després d'update([('f', 6), ('g', 7)]): {original}")

# 7. Mètode pop() - Eliminar i retornar
print("\n=== Mètode pop() ===")
fruites = {"poma": 5, "plàtan": 3, "taronja": 8}
print(f"Original: {fruites}")

quantitat = fruites.pop("plàtan")
print(f"pop('plàtan'): {quantitat}")
print(f"Diccionari: {fruites}")

# Amb valor per defecte si no existeix
quantitat = fruites.pop("kiwi", 0)
print(f"pop('kiwi', 0): {quantitat}")

# 8. Mètode popitem() - Eliminar últim element
print("\n=== Mètode popitem() ===")
lletres = {"a": 1, "b": 2, "c": 3}
print(f"Original: {lletres}")

item = lletres.popitem()
print(f"popitem(): {item}")
print(f"Diccionari: {lletres}")

# 9. Mètode clear() - Eliminar tot
print("\n=== Mètode clear() ===")
temporal = {"x": 1, "y": 2}
print(f"Original: {temporal}")

temporal.clear()
print(f"Després de clear(): {temporal}")

# 10. Mètode copy() - Còpia superficial
print("\n=== Mètode copy() ===")
original = {"nom": "Anna", "notes": [8, 9, 7]}
copia = original.copy()

print(f"Original: {original}")
print(f"Còpia: {copia}")

copia["nom"] = "Pere"
print(f"Després de modificar còpia['nom']:")
print(f"  Original: {original}")
print(f"  Còpia: {copia}")

# ATENCIÓ: còpia superficial no copia objectes niuats
copia["notes"].append(10)
print(f"\nDesprés d'afegir a còpia['notes']:")
print(f"  Original: {original}")  # També afectat!
print(f"  Còpia: {copia}")

# Per còpia profunda, usa copy.deepcopy()
import copy
original2 = {"nom": "Anna", "notes": [8, 9, 7]}
copia_profunda = copy.deepcopy(original2)
copia_profunda["notes"].append(10)
print(f"\nAmb deepcopy:")
print(f"  Original: {original2}")
print(f"  Còpia profunda: {copia_profunda}")

# 11. Mètode fromkeys() - Crear amb claus i valor per defecte
print("\n=== Mètode fromkeys() ===")
claus = ["nom", "edat", "ciutat"]

# Valor per defecte: None
dic1 = dict.fromkeys(claus)
print(f"fromkeys({claus}): {dic1}")

# Valor per defecte específic
dic2 = dict.fromkeys(claus, "Desconegut")
print(f"fromkeys({claus}, 'Desconegut'): {dic2}")

# Amb range
comptadors = dict.fromkeys(range(5), 0)
print(f"fromkeys(range(5), 0): {comptadors}")

# 12. Exemple pràctic: Gestió d'inventari
print("\n=== Exemple pràctic: Gestió d'inventari ===")

inventari = {}

def afegir_producte(nom, quantitat, preu):
    if nom in inventari:
        inventari[nom]["quantitat"] += quantitat
    else:
        inventari[nom] = {"quantitat": quantitat, "preu": preu}

def vendre(nom, quantitat):
    if nom not in inventari:
        return f"Error: {nom} no existeix"
    if inventari[nom]["quantitat"] < quantitat:
        return f"Error: estoc insuficient de {nom}"
    
    inventari[nom]["quantitat"] -= quantitat
    ingressos = quantitat * inventari[nom]["preu"]
    return f"Venda: {quantitat}x {nom} = {ingressos}€"

def mostrar_inventari():
    print("\nInventari actual:")
    print("-" * 45)
    print(f"{'Producte':<15} {'Quantitat':>10} {'Preu':>10} {'Valor':>10}")
    print("-" * 45)
    
    valor_total = 0
    for nom, info in inventari.items():
        valor = info["quantitat"] * info["preu"]
        valor_total += valor
        print(f"{nom:<15} {info['quantitat']:>10} {info['preu']:>10.2f}€ {valor:>10.2f}€")
    
    print("-" * 45)
    print(f"{'TOTAL':<15} {'':<10} {'':<10} {valor_total:>10.2f}€")

# Operacions
afegir_producte("Ordinador", 10, 800)
afegir_producte("Teclat", 25, 50)
afegir_producte("Ratolí", 30, 25)
mostrar_inventari()

print(vendre("Ordinador", 3))
print(vendre("Teclat", 5))
print(vendre("Monitor", 1))  # No existeix
mostrar_inventari()

# 13. Exemple pràctic: Memòria cau (cache)
print("\n=== Exemple pràctic: Memòria cau ===")

cache = {}

def calcular_amb_cache(n):
    """Calcula el factorial amb memòria cau."""
    if n in cache:
        print(f"  {n}! des de cache")
        return cache[n]
    
    if n <= 1:
        resultat = 1
    else:
        resultat = n * calcular_amb_cache(n - 1)
    
    cache[n] = resultat
    return resultat

print("Primers càlculs:")
for i in [5, 3, 7]:
    print(f"  {i}! = {calcular_amb_cache(i)}")

print("\nSegons càlculs (des de cache):")
for i in [5, 3, 7]:
    print(f"  {i}! = {calcular_amb_cache(i)}")

print(f"\nContingut del cache: {cache}")
