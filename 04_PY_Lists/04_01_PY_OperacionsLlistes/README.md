# Operacions amb Llistes en Python 📋

## Descripció

Aquest exemple demostra les **operacions bàsiques** amb llistes en Python. Les llistes són col·leccions ordenades i mutables que poden contenir elements de qualsevol tipus.

## Contingut de l'Exemple

El fitxer `operacions_llistes.py` inclou els següents conceptes:

### 1. Crear Llistes

```python
llista_buida = []
nombres = [1, 2, 3, 4, 5]
fruites = ["poma", "plàtan", "taronja"]
mixta = [1, "text", 3.14, True]
llista_range = list(range(1, 6))
```

### 2. Indexació

| Índex | Descripció | Exemple |
|-------|------------|---------|
| `[0]` | Primer element | `llista[0]` |
| `[n]` | Element n+1 | `llista[2]` → tercer |
| `[-1]` | Últim element | `llista[-1]` |
| `[-n]` | n-èsim des del final | `llista[-2]` |

```python
lletres = ['a', 'b', 'c', 'd', 'e']
print(lletres[0])   # 'a'
print(lletres[-1])  # 'e'
```

### 3. Slicing (Tallar Llistes)

| Sintaxi | Descripció |
|---------|------------|
| `[start:end]` | De start a end-1 |
| `[:end]` | Des del principi |
| `[start:]` | Fins al final |
| `[::step]` | Cada step elements |
| `[::-1]` | Invertir llista |

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums[2:5]    # [2, 3, 4]
nums[:4]     # [0, 1, 2, 3]
nums[::2]    # [0, 2, 4, 6, 8]
nums[::-1]   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

### 4. Modificar Elements

```python
colors = ["vermell", "verd", "blau"]
colors[1] = "groc"          # Modificar un element
colors[0:2] = ["a", "b"]    # Modificar múltiples
```

### 5. Afegir Elements

| Mètode | Descripció |
|--------|------------|
| `append(x)` | Afegeix x al final |
| `insert(i, x)` | Insereix x a l'índex i |
| `extend(llista)` | Afegeix múltiples elements |
| `+` | Concatena llistes |

### 6. Eliminar Elements

| Mètode | Descripció |
|--------|------------|
| `pop()` | Elimina i retorna l'últim |
| `pop(i)` | Elimina i retorna element i |
| `remove(x)` | Elimina la primera ocurrència de x |
| `del llista[i]` | Elimina l'element i |
| `clear()` | Elimina tots els elements |

### 7. Operadors

```python
a = [1, 2, 3]
b = [4, 5, 6]

a + b          # [1, 2, 3, 4, 5, 6]
a * 2          # [1, 2, 3, 1, 2, 3]
2 in a         # True
len(a)         # 3
```

### 8. Funcions amb Llistes Numèriques

```python
notes = [7.5, 8.2, 6.0, 9.1]

min(notes)              # 6.0
max(notes)              # 9.1
sum(notes)              # 30.8
sorted(notes)           # [6.0, 7.5, 8.2, 9.1]
sum(notes) / len(notes) # 7.7 (mitjana)
```

### 9. Copiar Llistes

```python
# ❌ Referència (NO és còpia)
referencia = original

# ✓ Còpies independents
copia1 = original.copy()
copia2 = list(original)
copia3 = original[:]
```

### 10. Llistes Niuades (Matrius)

```python
matriu = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matriu[1][2]  # 6
```

## Com Executar

```bash
python operacions_llistes.py
```

## Sortida Esperada

```
=== Crear llistes ===
Llista buida: []
Nombres: [1, 2, 3, 4, 5]
Fruites: ['poma', 'plàtan', 'taronja']
...
```

## Resum Visual

```
Llista:  ['a', 'b', 'c', 'd', 'e']
Índexs:    0    1    2    3    4
Negatius: -5   -4   -3   -2   -1
```

## Bones Pràctiques

- Utilitza noms descriptius per a les llistes.
- Utilitza `copy()` quan necessitis una còpia independent.
- Comprova si la llista està buida amb `if llista:` o `if not llista:`.
- Evita modificar una llista mentre la iteres.
