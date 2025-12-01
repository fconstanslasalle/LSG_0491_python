# Operacions amb Tuples en Python 📦

## Descripció

Aquest exemple demostra les **operacions bàsiques** amb tuples en Python. Les tuples són col·leccions ordenades i **immutables** d'elements.

## Contingut de l'Exemple

El fitxer `operacions_tuples.py` inclou els següents conceptes:

### 1. Crear Tuples

```python
tupla_buida = ()
tupla_un = (42,)        # ⚠️ Coma necessària!
coordenades = (10, 20)
colors = ("vermell", "verd", "blau")
sense_parentesis = 1, 2, 3  # També és tupla
```

⚠️ **Atenció**: Per crear una tupla d'un sol element, cal la coma!
```python
no_tupla = (42)   # És un int
tupla = (42,)     # És una tupla
```

### 2. Indexació i Slicing

Com les llistes, les tuples suporten indexació i slicing.

```python
dies = ("dl", "dm", "dc", "dj", "dv")
dies[0]      # 'dl'
dies[-1]     # 'dv'
dies[1:4]    # ('dm', 'dc', 'dj')
dies[::-1]   # ('dv', 'dj', 'dc', 'dm', 'dl')
```

### 3. Immutabilitat

Les tuples no es poden modificar després de crear-les.

```python
punt = (5, 10)
punt[0] = 15  # ❌ TypeError!

# Alternativa: crear nova tupla
nou_punt = (15,) + punt[1:]  # (15, 10)
```

### 4. Operadors

| Operador | Descripció | Exemple |
|----------|------------|---------|
| `+` | Concatenació | `(1,2) + (3,4)` → `(1,2,3,4)` |
| `*` | Repetició | `(1,2) * 2` → `(1,2,1,2)` |
| `in` | Pertinença | `2 in (1,2,3)` → `True` |
| `len()` | Longitud | `len((1,2,3))` → `3` |

### 5. Mètodes de Tuples

Les tuples només tenen 2 mètodes:

| Mètode | Descripció |
|--------|------------|
| `count(x)` | Compta ocurrències de x |
| `index(x)` | Retorna l'índex de x |

```python
t = ('a', 'b', 'c', 'b')
t.count('b')    # 2
t.index('c')    # 2
```

### 6. Desempaquetat (Unpacking)

```python
# Bàsic
x, y, z = (1, 2, 3)

# Amb *
primer, *resta = (1, 2, 3, 4, 5)
# primer = 1, resta = [2, 3, 4, 5]

*inici, ultim = (1, 2, 3, 4, 5)
# inici = [1, 2, 3, 4], ultim = 5
```

### 7. Intercanvi de Valors

```python
a, b = 10, 20
a, b = b, a  # Ara a=20, b=10
```

### 8. Tuples com a Claus de Diccionari

Les tuples són hashables i poden ser claus.

```python
mapa = {
    (0, 0): "Origen",
    (1, 0): "Dreta"
}
```

## Tuples vs Llistes

| Característica | Tuple | Llista |
|----------------|-------|--------|
| Sintaxi | `()` | `[]` |
| Mutable | No | Sí |
| Mètodes | 2 | Molts |
| Velocitat | Més ràpid | Més lent |
| Hashable | Sí | No |
| Memòria | Menys | Més |

## Quan Usar Tuples?

- **Dades que no canvien**: coordenades, colors RGB
- **Claus de diccionari**: només les tuples serveixen
- **Retornar múltiples valors**: `return (x, y, z)`
- **Desempaquetat**: `for nom, edat in persones:`
- **Rendiment**: les tuples són més eficients

## Com Executar

```bash
python operacions_tuples.py
```

## Sortida Esperada

```
=== Crear tuples ===
Tupla buida: ()
Tupla d'un element: (42,)
Coordenades: (10, 20)
...
```

## Bones Pràctiques

- Utilitza tuples per a dades que no han de canviar.
- Recorda la coma en tuples d'un sol element.
- Aprofita el desempaquetat per fer el codi més llegible.
- Considera tuples per a retornar múltiples valors de funcions.
