# Variables i Tipus de Dades en Python 📦

## Descripció

Aquest exemple demostra com treballar amb **variables** i els diferents **tipus de dades** bàsics en Python. Les variables són contenidors que emmagatzemen valors de dades i Python utilitza tipatge dinàmic, la qual cosa significa que no cal declarar el tipus de variable explícitament.

## Contingut de l'Exemple

El fitxer `variables.py` inclou els següents conceptes:

### 1. Variables de tipus String (str)
Les cadenes de text s'utilitzen per emmagatzemar text. Es defineixen entre cometes simples `'...'` o dobles `"..."`.

```python
nom = "Anna"
cognom = "Garcia"
ciutat = "Barcelona"
```

### 2. Variables de tipus Integer (int)
Els enters són nombres sencers, positius o negatius, sense decimals.

```python
edat = 25
any_naixement = 1999
quantitat = -50
```

### 3. Variables de tipus Float (float)
Els floats són nombres amb decimals, positius o negatius.

```python
altura = 1.75
pes = 68.5
temperatura = -3.2
```

### 4. Variables de tipus Boolean (bool)
Els booleans representen valors de veritat: `True` (veritat) o `False` (fals).

```python
es_estudiant = True
te_carnet_conduir = False
major_edat = edat >= 18
```

### 5. Conversió de Tipus (Type Casting)
Python permet convertir entre diferents tipus de dades:

- `int()` - Converteix a enter
- `float()` - Converteix a decimal
- `str()` - Converteix a cadena de text

```python
numero_text = "42"
numero_enter = int(numero_text)  # Convertir string a int
```

### 6. Concatenació de Strings
Es poden unir cadenes de text amb l'operador `+` o utilitzant f-strings.

```python
nom_complet = nom + " " + cognom
salutacio = f"Hola, em dic {nom} i tinc {edat} anys."
```

### 7. Variables Múltiples
Python permet assignar múltiples variables en una sola línia.

```python
x, y, z = 10, 20, 30
a = b = c = 100
```

## Com Executar

1. Obre una terminal
2. Navega fins al directori d'aquest exemple
3. Executa el fitxer amb Python:

```bash
python variables.py
```

## Sortida Esperada

```
=== Variables de tipus String ===
Nom: Anna
Cognom: Garcia
Ciutat: Barcelona
Tipus de 'nom': <class 'str'>

=== Variables de tipus Integer ===
Edat: 25
Any de naixement: 1999
Quantitat: -50
Tipus de 'edat': <class 'int'>

=== Variables de tipus Float ===
Altura: 1.75 metres
Pes: 68.5 kg
Temperatura: -3.2°C
Tipus de 'altura': <class 'float'>

=== Variables de tipus Boolean ===
És estudiant: True
Té carnet de conduir: False
És major d'edat: True
Tipus de 'es_estudiant': <class 'bool'>

=== Conversió de tipus ===
'42' convertit a enter: 42
Tipus original: <class 'str'>, Tipus convertit: <class 'int'>
25 convertit a float: 25.0
3.14 convertit a string: '3.14'

=== Concatenació de strings ===
Nom complet: Anna Garcia
Hola, em dic Anna i tinc 25 anys.

=== Variables múltiples ===
x = 10, y = 20, z = 30
a = 100, b = 100, c = 100
```

## Funció `type()`

La funció `type()` s'utilitza per obtenir el tipus d'una variable:

```python
print(type(nom))  # <class 'str'>
print(type(edat)) # <class 'int'>
```

## Resum de Tipus de Dades Bàsics

| Tipus | Descripció | Exemple |
|-------|------------|---------|
| `str` | Cadena de text | `"Hola"` |
| `int` | Nombre enter | `42` |
| `float` | Nombre decimal | `3.14` |
| `bool` | Valor booleà | `True` / `False` |
