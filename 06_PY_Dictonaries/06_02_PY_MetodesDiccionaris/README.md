# Mètodes de Diccionaris en Python 🔧

## Descripció

Aquest exemple demostra els **mètodes incorporats** dels diccionaris en Python. Aquests mètodes permeten manipular diccionaris de forma eficient.

## Contingut de l'Exemple

### Mètodes d'Accés

| Mètode | Descripció | Retorna |
|--------|------------|---------|
| `keys()` | Obté totes les claus | Vista de claus |
| `values()` | Obté tots els valors | Vista de valors |
| `items()` | Obté parells clau-valor | Vista de tuples |
| `get(k)` | Obté valor de clau k | Valor o None |
| `get(k, d)` | Obté valor o d si no existeix | Valor o d |

```python
d = {"a": 1, "b": 2}
d.keys()        # dict_keys(['a', 'b'])
d.values()      # dict_values([1, 2])
d.items()       # dict_items([('a', 1), ('b', 2)])
d.get("c", 0)   # 0
```

### Mètode setdefault()

Retorna el valor si existeix, o estableix i retorna el valor per defecte.

```python
d = {"a": 1}
d.setdefault("a", 10)  # 1 (existeix)
d.setdefault("b", 10)  # 10 (no existeix, s'afegeix)
# d = {"a": 1, "b": 10}
```

### Mètode update()

Actualitza amb altre diccionari o iterable.

```python
d = {"a": 1}

# Amb diccionari
d.update({"b": 2, "c": 3})

# Amb arguments nomenats
d.update(d=4, e=5)

# Amb llista de tuples
d.update([("f", 6)])
```

### Mètodes d'Eliminació

| Mètode | Descripció |
|--------|------------|
| `pop(k)` | Elimina i retorna valor de k |
| `pop(k, d)` | Com pop, però retorna d si k no existeix |
| `popitem()` | Elimina i retorna últim parrell |
| `clear()` | Elimina tots els elements |

```python
d = {"a": 1, "b": 2, "c": 3}
d.pop("a")        # 1, d = {"b": 2, "c": 3}
d.popitem()       # ("c", 3), d = {"b": 2}
d.clear()         # d = {}
```

### Mètode copy()

Crea una còpia superficial.

```python
original = {"a": 1, "llista": [1, 2]}
copia = original.copy()

# ⚠️ Objectes niuats es comparteixen!
copia["llista"].append(3)  # Afecta original!

# Per còpia profunda:
import copy
copia_profunda = copy.deepcopy(original)
```

### Mètode fromkeys()

Crea diccionari amb claus i valor per defecte.

```python
# Valor None per defecte
d = dict.fromkeys(["a", "b", "c"])
# {"a": None, "b": None, "c": None}

# Valor específic
d = dict.fromkeys(["x", "y"], 0)
# {"x": 0, "y": 0}
```

## Vistes Dinàmiques

`keys()`, `values()` i `items()` retornen vistes que s'actualitzen automàticament.

```python
d = {"a": 1}
claus = d.keys()
d["b"] = 2
print(claus)  # dict_keys(['a', 'b'])
```

## Taula Resum de Mètodes

| Mètode | Modifica? | Retorna |
|--------|-----------|---------|
| `keys()` | No | Vista de claus |
| `values()` | No | Vista de valors |
| `items()` | No | Vista de tuples |
| `get(k)` | No | Valor o None |
| `setdefault(k, d)` | Pot ser | Valor |
| `update(d)` | Sí | None |
| `pop(k)` | Sí | Valor |
| `popitem()` | Sí | Tupla |
| `clear()` | Sí | None |
| `copy()` | No | Nou dict |
| `fromkeys(k)` | - | Nou dict |

## Com Executar

```bash
python metodes_diccionaris.py
```

## Sortida Esperada

```
=== Mètode keys() ===
Diccionari: {'nom': 'Anna', 'edat': 25, 'ciutat': 'Barcelona', 'professio': 'Enginyera'}
keys(): dict_keys(['nom', 'edat', 'ciutat', 'professio'])
...
```

## Patrons Comuns

### Comptador

```python
comptador = {}
for element in llista:
    comptador[element] = comptador.get(element, 0) + 1
```

### Agrupar

```python
grups = {}
for element in llista:
    clau = element["categoria"]
    grups.setdefault(clau, []).append(element)
```

### Cache

```python
cache = {}
def calcular(n):
    if n not in cache:
        cache[n] = operacio_costosa(n)
    return cache[n]
```

## Bones Pràctiques

- Utilitza `get()` per evitar KeyError.
- Utilitza `setdefault()` per a diccionaris amb valors llista.
- Recorda que `copy()` és superficial.
- Les vistes (`keys()`, `values()`, `items()`) són eficients en memòria.
