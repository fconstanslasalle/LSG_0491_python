# Mètodes de Llistes en Python 🛠️

## Descripció

Aquest exemple demostra els **mètodes incorporats** de les llistes en Python. Aquests mètodes permeten manipular llistes de forma eficient.

## Contingut de l'Exemple

El fitxer `metodes_llistes.py` inclou els següents mètodes:

### Mètodes per Afegir Elements

| Mètode | Descripció | Exemple |
|--------|------------|---------|
| `append(x)` | Afegeix x al final | `llista.append(5)` |
| `extend(iter)` | Afegeix múltiples elements | `llista.extend([1,2])` |
| `insert(i, x)` | Insereix x a l'índex i | `llista.insert(0, 'a')` |

```python
llista = [1, 2, 3]
llista.append(4)          # [1, 2, 3, 4]
llista.extend([5, 6])     # [1, 2, 3, 4, 5, 6]
llista.insert(0, 0)       # [0, 1, 2, 3, 4, 5, 6]
```

### Mètodes per Eliminar Elements

| Mètode | Descripció | Retorna |
|--------|------------|---------|
| `remove(x)` | Elimina primera ocurrència de x | - |
| `pop()` | Elimina i retorna l'últim | Element |
| `pop(i)` | Elimina i retorna element a i | Element |
| `clear()` | Elimina tots els elements | - |

```python
llista = [1, 2, 3, 2, 4]
llista.remove(2)    # [1, 3, 2, 4]
x = llista.pop()    # [1, 3, 2], x = 4
llista.clear()      # []
```

### Mètodes de Cerca

| Mètode | Descripció |
|--------|------------|
| `index(x)` | Retorna l'índex de x |
| `index(x, start)` | Busca des de start |
| `count(x)` | Compta ocurrències de x |

```python
llista = ['a', 'b', 'c', 'b']
llista.index('b')      # 1
llista.index('b', 2)   # 3
llista.count('b')      # 2
```

### Mètodes d'Ordenació

| Mètode | Descripció |
|--------|------------|
| `sort()` | Ordena la llista (ascendent) |
| `sort(reverse=True)` | Ordena descendent |
| `sort(key=func)` | Ordena segons funció |
| `reverse()` | Inverteix l'ordre |

```python
nums = [3, 1, 4, 1, 5]
nums.sort()                # [1, 1, 3, 4, 5]
nums.sort(reverse=True)    # [5, 4, 3, 1, 1]
nums.reverse()             # [1, 1, 3, 4, 5]

# Ordenar per criteri personalitzat
noms = ["Pere", "anna", "Joan"]
noms.sort(key=str.lower)   # ['anna', 'Joan', 'Pere']
```

### Mètode copy()

Crea una còpia superficial de la llista.

```python
original = [1, 2, 3]
copia = original.copy()
copia.append(4)
# original = [1, 2, 3]
# copia = [1, 2, 3, 4]
```

## sort() vs sorted()

| | `sort()` | `sorted()` |
|---|----------|------------|
| Tipus | Mètode | Funció |
| Modifica original | Sí | No |
| Retorna | None | Nova llista |

```python
nums = [3, 1, 4]

# sort() modifica l'original
nums.sort()
print(nums)  # [1, 3, 4]

# sorted() retorna nova llista
nums = [3, 1, 4]
nova = sorted(nums)
print(nums)  # [3, 1, 4]
print(nova)  # [1, 3, 4]
```

## Ordenació amb key

El paràmetre `key` permet ordenar per criteris personalitzats.

```python
# Per longitud
paraules = ["elefant", "gat", "llop"]
paraules.sort(key=len)  # ["gat", "llop", "elefant"]

# Per un atribut
persones = [
    {"nom": "Anna", "edat": 30},
    {"nom": "Pere", "edat": 25}
]
persones.sort(key=lambda x: x['edat'])
```

## Com Executar

```bash
python metodes_llistes.py
```

## Sortida Esperada

```
=== Mètode append() ===
Original: ['llet', 'pa']
Després d'append('ous'): ['llet', 'pa', 'ous']
...
```

## Taula Resum de Mètodes

| Mètode | Modifica? | Retorna |
|--------|-----------|---------|
| `append(x)` | Sí | None |
| `extend(iter)` | Sí | None |
| `insert(i, x)` | Sí | None |
| `remove(x)` | Sí | None |
| `pop()` | Sí | Element |
| `clear()` | Sí | None |
| `index(x)` | No | Índex |
| `count(x)` | No | Nombre |
| `sort()` | Sí | None |
| `reverse()` | Sí | None |
| `copy()` | No | Nova llista |

## Bones Pràctiques

- Utilitza `append()` per afegir un element, `extend()` per afegir múltiples.
- Utilitza `sorted()` si vols conservar l'original.
- El mètode `index()` llança `ValueError` si l'element no existeix - verifica primer amb `in`.
- Per cerques freqüents, considera usar un `set` o `dict` en lloc d'una llista.
