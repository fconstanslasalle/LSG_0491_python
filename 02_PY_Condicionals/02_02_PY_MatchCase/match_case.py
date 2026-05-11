# Exemple de Match-Case en Python
# ================================

# Match-case és una estructura de control introduïda a Python 3.10
# que permet comparar un valor amb múltiples patrons.

# 1. Match-case bàsic
print("=== Match-case bàsic ===")
dia = 3

match dia:
    case 1:
        nom_dia = "Dilluns"
    case 2:
        nom_dia = "Dimarts"
    case 3:
        nom_dia = "Dimecres"
    case 4:
        nom_dia = "Dijous"
    case 5:
        nom_dia = "Divendres"
    case 6:
        nom_dia = "Dissabte"
    case 7:
        nom_dia = "Diumenge"
    case _:
        nom_dia = "Dia no vàlid"

print(f"El dia {dia} és: {nom_dia}")

# 2. Match-case amb múltiples valors (OR)
print("\n=== Match-case amb múltiples valors ===")
mes = 7

match mes:
    case 1 | 2 | 12:
        estacio = "Hivern"
    case 3 | 4 | 5:
        estacio = "Primavera"
    case 6 | 7 | 8:
        estacio = "Estiu"
    case 9 | 10 | 11:
        estacio = "Tardor"
    case _:
        estacio = "Mes no vàlid"

print(f"El mes {mes} correspon a l'estació: {estacio}")

# 3. Match-case amb cadenes de text
print("\n=== Match-case amb cadenes ===")
color = "vermell"

match color.lower():
    case "vermell" | "red":
        missatge = "El color és càlid i intens."
    case "blau" | "blue":
        missatge = "El color és fred i tranquil."
    case "verd" | "green":
        missatge = "El color és natural i relaxant."
    case "groc" | "yellow":
        missatge = "El color és brillant i alegre."
    case _:
        missatge = "Color no reconegut."

print(f"Color: {color}")
print(missatge)

# 4. Match-case amb tuples
print("\n=== Match-case amb tuples ===")
punt = (0, 5)

match punt:
    case (0, 0):
        posicio = "Origen"
    case (0, y):
        posicio = f"A l'eix Y, coordenada y={y}"
    case (x, 0):
        posicio = f"A l'eix X, coordenada x={x}"
    case (x, y):
        posicio = f"Al pla, coordenades ({x}, {y})"

print(f"Punt: {punt}")
print(f"Posició: {posicio}")

# 5. Match-case amb llistes
print("\n=== Match-case amb llistes ===")
comanda = ["comprar", "pa", "3"]

match comanda:
    case ["ajuda"]:
        print("Comandes disponibles: comprar, vendre, sortir")
    case ["comprar", producte]:
        print(f"Comprarem 1 unitat de {producte}")
    case ["comprar", producte, quantitat]:
        print(f"Comprarem {quantitat} unitats de {producte}")
    case ["vendre", producte, preu]:
        print(f"Vendrem {producte} a {preu}€")
    case ["sortir"]:
        print("Sortint del programa...")
    case _:
        print("Comanda no reconeguda")

# 6. Match-case amb guardes (condicions addicionals)
print("\n=== Match-case amb guardes ===")
nota = 7.5

match nota:
    case n if n >= 9:
        resultat = "Excel·lent"
    case n if n >= 7:
        resultat = "Notable"
    case n if n >= 5:
        resultat = "Aprovat"
    case n if n >= 0:
        resultat = "Suspès"
    case _:
        resultat = "Nota no vàlida"

print(f"Nota: {nota}")
print(f"Resultat: {resultat}")

# 7. Match-case amb diccionaris
print("\n=== Match-case amb diccionaris ===")
usuari = {"nom": "Anna", "rol": "admin", "actiu": True}

match usuari:
    case {"rol": "admin", "actiu": True}:
        print(f"Benvingut/da administrador/a!")
    case {"rol": "admin", "actiu": False}:
        print("Compte d'administrador desactivat.")
    case {"rol": "usuari", "actiu": True}:
        print("Benvingut/da usuari/a!")
    case {"rol": "usuari", "actiu": False}:
        print("Compte d'usuari desactivat.")
    case _:
        print("Rol desconegut.")

# 8. Match-case amb classes
print("\n=== Match-case amb classes ===")

class Punt:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Cercle:
    __match_args__ = ('centre', 'radi')
    def __init__(self, centre, radi):
        self.centre = centre
        self.radi = radi

class Rectangle:
    __match_args__ = ('punt1', 'punt2')
    def __init__(self, punt1, punt2):
        self.punt1 = punt1
        self.punt2 = punt2

figura = Cercle(Punt(0, 0), 5)

match figura:
    case Punt(x, y):
        print(f"És un punt a ({x}, {y})")
    case Cercle(centre, radi):
        print(f"És un cercle amb radi {radi}")
    case Rectangle(punt1, punt2):
        print(f"És un rectangle")
    case _:
        print("Figura no reconeguda")

# 9. Exemple pràctic: Processador de comandes
print("\n=== Exemple pràctic: Processador de comandes ===")

def processar_comanda(accio):
    match accio.split():
        case ["crear", tipus, nom]:
            return f"Creant {tipus} amb nom '{nom}'"
        case ["eliminar", nom]:
            return f"Eliminant '{nom}'"
        case ["llistar"]:
            return "Mostrant tots els elements"
        case ["llistar", tipus]:
            return f"Mostrant elements de tipus '{tipus}'"
        case ["ajuda" | "help"]:
            return "Comandes: crear <tipus> <nom>, eliminar <nom>, llistar [tipus]"
        case _:
            return "Comanda no reconeguda. Escriu 'ajuda' per veure les opcions."

comandes = [
    "crear fitxer document.txt",
    "eliminar document.txt",
    "llistar",
    "llistar carpetes",
    "ajuda",
    "comanda_invalida"
]

for cmd in comandes:
    print(f"Comanda: '{cmd}'")
    print(f"  → {processar_comanda(cmd)}")
