# Operacions amb Diccionaris en Python 📖

## Descripció

Aquest exemple demostra les **operacions bàsiques** amb diccionaris en Python. Els diccionaris són col·leccions de parells clau-valor, mutables i ordenades (des de Python 3.7+).

## Contingut de l'Exemple

### 1. Crear Diccionaris

```python
# Amb claus
persona = {"nom": "Anna", "edat": 25}

# Amb constructor
notes = dict(mat=8.5, fis=7.2)

# Des de llista de tuples
d = dict([("a", 1), ("b", 2)])

# Des de zip
d = dict(zip(["x", "y"], [1, 2]))
```

### 2. Accedir a Valors

| Mètode | Si no existeix |
|--------|----------------|
| `dict[clau]` | KeyError |
| `dict.get(clau)` | None |
| `dict.get(clau, default)` | default |

```python
persona = {"nom": "Anna", "edat": 25}
persona["nom"]           # "Anna"
persona.get("ciutat")    # None
persona.get("ciutat", "Desconeguda")  # "Desconeguda"
```

### 3. Modificar i Afegir

```python
persona = {"nom": "Anna"}

# Modificar
persona["nom"] = "Pere"

# Afegir
persona["edat"] = 30

# Afegir múltiples
persona.update({"ciutat": "BCN", "actiu": True})
```

### 4. Eliminar Elements

| Mètode | Descripció |
|--------|------------|
| `del dict[clau]` | Elimina per clau |
| `dict.pop(clau)` | Elimina i retorna valor |
| `dict.popitem()` | Elimina últim element |
| `dict.clear()` | Elimina tot |

### 5. Comprovar Existència

```python
config = {"idioma": "ca", "tema": "fosc"}

"idioma" in config          # True
"volum" in config           # False
"fosc" in config.values()   # True
```

### 6. Iterar

```python
d = {"a": 1, "b": 2}

# Sobre claus
for clau in d:
    print(clau)

# Sobre valors
for valor in d.values():
    print(valor)

# Sobre ambdós
for clau, valor in d.items():
    print(f"{clau}: {valor}")
```

### 7. Diccionaris Niuats

```python
empresa = {
    "nom": "Tech",
    "empleats": {
        "dev": 15,
        "disseny": 8
    }
}
empresa["empleats"]["dev"]  # 15
```

### 8. Comprensions

```python
# Bàsic
quadrats = {x: x**2 for x in range(5)}

# Amb condició
aprovats = {n: nota for n, nota in notes.items() if nota >= 5}

# Invertir
invertit = {v: k for k, v in d.items()}
```

### 9. Fusionar Diccionaris

```python
a = {"x": 1}
b = {"y": 2}

# Python 3.9+
c = a | b

# Alternatives
c = {**a, **b}
a.update(b)
```

## Claus de Diccionari

Les claus han de ser **hashables**:
- ✓ Strings, números, tuples
- ✗ Llistes, diccionaris, sets

## Com Executar

```bash
python operacions_diccionaris.py
```

## Sortida Esperada

```
=== Crear diccionaris ===
Diccionari buit: {}
Persona: {'nom': 'Anna', 'edat': 25, 'ciutat': 'Barcelona'}
...
```

## Bones Pràctiques

- Utilitza `get()` per evitar KeyError.
- Prefereix comprensions per crear diccionaris.
- Utilitza `in` per comprovar existència.
- Considera `defaultdict` per a comptadors.
