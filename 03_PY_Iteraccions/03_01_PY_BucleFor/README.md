# Bucle For en Python 🔄

## Descripció

Aquest exemple demostra com utilitzar el **bucle for** en Python. El bucle for s'utilitza per iterar sobre seqüències (llistes, tuples, strings, diccionaris, etc.) o sobre rangs de nombres.

## Contingut de l'Exemple

El fitxer `bucle_for.py` inclou els següents conceptes:

### 1. Bucle for Bàsic

Itera sobre cada element d'una seqüència.

```python
fruites = ["poma", "plàtan", "taronja"]
for fruita in fruites:
    print(fruita)
```

### 2. Bucle for amb range()

La funció `range()` genera una seqüència de nombres.

| Sintaxi | Descripció | Exemple |
|---------|------------|---------|
| `range(n)` | 0 a n-1 | `range(5)` → 0,1,2,3,4 |
| `range(inici, fi)` | inici a fi-1 | `range(2,7)` → 2,3,4,5,6 |
| `range(inici, fi, pas)` | amb salt | `range(0,10,2)` → 0,2,4,6,8 |

```python
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
```

### 3. Bucle for amb enumerate()

Obté l'índex i el valor alhora.

```python
colors = ["vermell", "verd", "blau"]
for index, color in enumerate(colors):
    print(f"{index}: {color}")
```

### 4. Bucle for amb zip()

Itera sobre múltiples seqüències simultàniament.

```python
noms = ["Anna", "Pere"]
edats = [25, 30]
for nom, edat in zip(noms, edats):
    print(f"{nom}: {edat} anys")
```

### 5. Bucle for amb Diccionaris

```python
persona = {"nom": "Anna", "edat": 25}

# Iterar claus
for clau in persona:
    print(clau)

# Iterar valors
for valor in persona.values():
    print(valor)

# Iterar claus i valors
for clau, valor in persona.items():
    print(f"{clau}: {valor}")
```

### 6. Control del Bucle: break i continue

| Instrucció | Descripció |
|------------|------------|
| `break` | Surt completament del bucle |
| `continue` | Salta a la següent iteració |

```python
# break
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# continue
for i in range(5):
    if i == 2:
        continue
    print(i)  # 0, 1, 3, 4
```

### 7. Bucle for amb else

El bloc `else` s'executa si el bucle acaba normalment (sense `break`).

```python
for n in [1, 3, 5]:
    if n % 2 == 0:
        print("Parell trobat!")
        break
else:
    print("No hi ha parells")
```

### 8. Bucles Niuats

Bucles dins d'altres bucles.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
```

### 9. List Comprehension

Forma concisa de crear llistes amb bucles.

```python
# Tradicional
quadrats = []
for x in range(5):
    quadrats.append(x**2)

# List comprehension
quadrats = [x**2 for x in range(5)]

# Amb condició
parells = [x for x in range(10) if x % 2 == 0]
```

## Com Executar

1. Obre una terminal
2. Navega fins al directori d'aquest exemple
3. Executa el fitxer amb Python:

```bash
python bucle_for.py
```

## Sortida Esperada

```
=== Bucle for amb llista ===
Fruita: poma
Fruita: plàtan
Fruita: taronja
Fruita: maduixa

=== Bucle for amb range() ===
range(5):
  0
  1
  2
  3
  4
...
```

## Comparació: for vs while

| Característica | for | while |
|----------------|-----|-------|
| Ús principal | Iterar sobre seqüències | Repetir mentre condició sigui certa |
| Nombre d'iteracions | Conegut | Pot ser desconegut |
| Risc de bucle infinit | Baix | Alt si no es controla |

## Bones Pràctiques

- Utilitza `for` quan saps el nombre d'iteracions o quan iteres sobre una seqüència.
- Utilitza `enumerate()` en lloc d'un comptador manual.
- Utilitza `zip()` per iterar sobre múltiples llistes.
- Considera list comprehension per a operacions simples.
- Evita modificar la llista mentre la iteres.
