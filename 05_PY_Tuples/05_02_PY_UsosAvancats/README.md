# Usos Avançats de Tuples en Python 🚀

## Descripció

Aquest exemple demostra els **usos avançats** de les tuples en Python, incloent `namedtuple`, patrons de disseny i casos d'ús pràctics.

## Contingut de l'Exemple

### 1. Named Tuples

Les `namedtuple` proporcionen tuples amb camps nomenats.

```python
from collections import namedtuple

Punt = namedtuple('Punt', ['x', 'y'])
p = Punt(10, 20)

print(p.x)      # 10
print(p[0])     # 10 (també per índex)
print(p._fields)    # ('x', 'y')
print(p._asdict())  # {'x': 10, 'y': 20}
```

### 2. Funcions amb Múltiples Retorns

```python
def estadistiques(nums):
    return (min(nums), max(nums), sum(nums))

minim, maxim, suma = estadistiques([1, 2, 3, 4, 5])
```

### 3. Enumerate i Zip

Ambdues funcions retornen tuples:

```python
# enumerate
for i, valor in enumerate(['a', 'b', 'c']):
    print(f"{i}: {valor}")

# zip
noms = ['Anna', 'Pere']
edats = [25, 30]
for nom, edat in zip(noms, edats):
    print(f"{nom}: {edat}")
```

### 4. Descomprimir amb *

```python
# Desempaquetar com arguments
def crear_punt(x, y, z):
    return f"({x}, {y}, {z})"

coords = (10, 20, 30)
crear_punt(*coords)  # crear_punt(10, 20, 30)

# Descomprimir zip
combinat = [('a', 1), ('b', 2)]
lletres, nums = zip(*combinat)
# lletres = ('a', 'b'), nums = (1, 2)
```

### 5. *args com a Tupla

```python
def suma(*args):
    # args és una tupla
    return sum(args)

suma(1, 2, 3, 4, 5)  # 15
```

### 6. Comparació Lexicogràfica

Les tuples es comparen element per element:

```python
(1, 2, 3) < (1, 2, 4)  # True
(1, 3) < (2, 0)        # True (primer element)

# Útil per ordenar per múltiples criteris
persones = [('Garcia', 'Anna'), ('López', 'Pere')]
sorted(persones)  # Ordena per cognom, després nom
```

### 7. Patró: Retorn d'Estat i Valor

```python
def dividir(a, b):
    if b == 0:
        return (False, "Error: divisió per zero")
    return (True, a / b)

ok, resultat = dividir(10, 2)
if ok:
    print(resultat)
```

## Quan Usar Named Tuples?

| Situació | Usar |
|----------|------|
| Dades simples amb camps fixes | ✓ Named Tuple |
| Necessites mètodes | Classe |
| Dades mutables | Classe o dataclass |
| Compatibilitat amb tuple | ✓ Named Tuple |

## Avantatges de Named Tuples

1. **Llegibilitat**: `punt.x` vs `punt[0]`
2. **Immutabilitat**: Més segures
3. **Memòria**: Més eficients que diccionaris
4. **Compatibilitat**: Funcionen com tuples normals

## Com Executar

```bash
python usos_avancats_tuples.py
```

## Sortida Esperada

```
=== Named Tuples ===
Punt p1: Punt(x=10, y=20)
Accedir per índex: p1[0] = 10
Accedir per nom: p1.x = 10, p1.y = 20
...
```

## Comparació: Tuple vs Named Tuple vs Dict vs Dataclass

```python
# Tupla normal
persona = ("Anna", 25, "Barcelona")
print(persona[0])  # Poc clar

# Named tuple
Persona = namedtuple('Persona', ['nom', 'edat', 'ciutat'])
persona = Persona("Anna", 25, "Barcelona")
print(persona.nom)  # Més clar

# Diccionari
persona = {"nom": "Anna", "edat": 25, "ciutat": "Barcelona"}
print(persona["nom"])  # Mutable

# Dataclass (Python 3.7+)
from dataclasses import dataclass

@dataclass
class Persona:
    nom: str
    edat: int
    ciutat: str

persona = Persona("Anna", 25, "Barcelona")
print(persona.nom)  # Mutable per defecte
```

## Bones Pràctiques

- Usa `namedtuple` per a estructures de dades simples.
- Aprofita el desempaquetat per fer el codi més llegible.
- Considera `dataclass` si necessites mutabilitat.
- Les tuples són ideals per a retornar múltiples valors.
