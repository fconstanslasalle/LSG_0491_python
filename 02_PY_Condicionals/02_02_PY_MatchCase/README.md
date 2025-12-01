# Match-Case en Python 🎯

## Descripció

Aquest exemple demostra com utilitzar l'estructura **match-case** introduïda a Python 3.10. Aquesta estructura permet comparar un valor amb múltiples patrons de forma elegant i potent.

## Contingut de l'Exemple

El fitxer `match_case.py` inclou els següents conceptes:

### 1. Match-case Bàsic

Compara un valor amb múltiples casos possibles.

```python
dia = 3
match dia:
    case 1:
        nom_dia = "Dilluns"
    case 2:
        nom_dia = "Dimarts"
    case _:
        nom_dia = "Dia no vàlid"
```

### 2. Match-case amb Múltiples Valors (OR)

Permet agrupar diversos valors en un sol cas utilitzant `|`.

```python
mes = 7
match mes:
    case 1 | 2 | 12:
        estacio = "Hivern"
    case 6 | 7 | 8:
        estacio = "Estiu"
```

### 3. Match-case amb Tuples

Permet desestructurar tuples i capturar els seus valors.

```python
punt = (0, 5)
match punt:
    case (0, 0):
        posicio = "Origen"
    case (0, y):
        posicio = f"A l'eix Y, y={y}"
    case (x, y):
        posicio = f"Coordenades ({x}, {y})"
```

### 4. Match-case amb Llistes

Útil per processar comandes o arguments.

```python
comanda = ["comprar", "pa", "3"]
match comanda:
    case ["comprar", producte]:
        print(f"Comprarem 1 {producte}")
    case ["comprar", producte, quantitat]:
        print(f"Comprarem {quantitat} de {producte}")
```

### 5. Match-case amb Guardes

Afegeix condicions addicionals als patrons amb `if`.

```python
nota = 7.5
match nota:
    case n if n >= 9:
        resultat = "Excel·lent"
    case n if n >= 7:
        resultat = "Notable"
    case n if n >= 5:
        resultat = "Aprovat"
```

### 6. Match-case amb Diccionaris

Permet fer coincidència parcial amb diccionaris.

```python
usuari = {"nom": "Anna", "rol": "admin", "actiu": True}
match usuari:
    case {"rol": "admin", "actiu": True}:
        print("Benvingut administrador!")
```

### 7. Match-case amb Classes

Permet desestructurar objectes de classes.

```python
match figura:
    case Cercle(centre, radi):
        print(f"Cercle amb radi {radi}")
    case Rectangle(punt1, punt2):
        print("Rectangle")
```

## El Patró Wildcard (_)

El patró `_` actua com a cas per defecte, captura qualsevol valor que no hagi coincidit amb els patrons anteriors.

```python
match valor:
    case 1:
        print("Un")
    case 2:
        print("Dos")
    case _:
        print("Altres")
```

## Com Executar

1. Obre una terminal
2. Navega fins al directori d'aquest exemple
3. Executa el fitxer amb Python (requereix Python 3.10 o superior):

```bash
python match_case.py
```

## Sortida Esperada

```
=== Match-case bàsic ===
El dia 3 és: Dimecres

=== Match-case amb múltiples valors ===
El mes 7 correspon a l'estació: Estiu

=== Match-case amb cadenes ===
Color: vermell
El color és càlid i intens.

=== Match-case amb tuples ===
Punt: (0, 5)
Posició: A l'eix Y, coordenada y=5

=== Match-case amb llistes ===
Comprarem 3 unitats de pa

=== Match-case amb guardes ===
Nota: 7.5
Resultat: Notable

=== Match-case amb diccionaris ===
Benvingut/da administrador/a!

=== Match-case amb classes ===
És un cercle amb radi 5

=== Exemple pràctic: Processador de comandes ===
Comanda: 'crear fitxer document.txt'
  → Creant fitxer amb nom 'document.txt'
...
```

## Avantatges del Match-Case

| Característica | Benefici |
|----------------|----------|
| Llegibilitat | Codi més clar que múltiples if-elif |
| Desestructuració | Permet extreure valors de tuples, llistes i objectes |
| Guardes | Afegeix condicions addicionals als patrons |
| Exhaustivitat | El patró `_` assegura que tots els casos es gestionen |

## Requisits

- **Python 3.10 o superior** és necessari per utilitzar match-case.

## Comparació amb if-elif-else

```python
# Amb if-elif-else
if dia == 1:
    nom = "Dilluns"
elif dia == 2:
    nom = "Dimarts"
else:
    nom = "Altres"

# Amb match-case
match dia:
    case 1:
        nom = "Dilluns"
    case 2:
        nom = "Dimarts"
    case _:
        nom = "Altres"
```

## Bones Pràctiques

- Utilitza `_` sempre com a últim cas per capturar valors inesperats.
- Aprofita la desestructuració per simplificar el codi.
- Utilitza guardes (`if`) quan necessitis condicions addicionals.
- Match-case és especialment útil per processar comandes o parsers.
