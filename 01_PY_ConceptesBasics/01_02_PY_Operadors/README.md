# Operadors en Python ➗

## Descripció

Aquest exemple demostra els diferents tipus d'**operadors** disponibles en Python. Els operadors són símbols especials que realitzen operacions sobre variables i valors.

## Contingut de l'Exemple

El fitxer `operadors.py` inclou els següents tipus d'operadors:

### 1. Operadors Aritmètics

S'utilitzen per realitzar operacions matemàtiques bàsiques.

| Operador | Descripció | Exemple |
|----------|------------|---------|
| `+` | Suma | `a + b` |
| `-` | Resta | `a - b` |
| `*` | Multiplicació | `a * b` |
| `/` | Divisió | `a / b` |
| `//` | Divisió entera | `a // b` |
| `%` | Mòdul (residu) | `a % b` |
| `**` | Exponenciació | `a ** b` |

```python
a = 15
b = 4
print(a + b)   # 19
print(a / b)   # 3.75
print(a // b)  # 3
print(a % b)   # 3
print(a ** b)  # 50625
```

### 2. Operadors de Comparació

S'utilitzen per comparar dos valors i retornen un valor booleà (`True` o `False`).

| Operador | Descripció | Exemple |
|----------|------------|---------|
| `==` | Igual | `x == y` |
| `!=` | No igual | `x != y` |
| `>` | Més gran que | `x > y` |
| `<` | Més petit que | `x < y` |
| `>=` | Més gran o igual | `x >= y` |
| `<=` | Més petit o igual | `x <= y` |

```python
x = 10
y = 20
print(x == y)  # False
print(x < y)   # True
```

### 3. Operadors Lògics

S'utilitzen per combinar condicions.

| Operador | Descripció | Exemple |
|----------|------------|---------|
| `and` | Retorna True si ambdues condicions són certes | `a and b` |
| `or` | Retorna True si almenys una condició és certa | `a or b` |
| `not` | Inverteix el valor booleà | `not a` |

```python
veritat = True
fals = False
print(veritat and fals)  # False
print(veritat or fals)   # True
print(not veritat)       # False
```

### 4. Operadors d'Assignació

S'utilitzen per assignar valors a variables, sovint combinats amb operacions.

| Operador | Equivalent | Exemple |
|----------|------------|---------|
| `=` | Assigna valor | `x = 5` |
| `+=` | `x = x + valor` | `x += 3` |
| `-=` | `x = x - valor` | `x -= 3` |
| `*=` | `x = x * valor` | `x *= 3` |
| `/=` | `x = x / valor` | `x /= 3` |
| `//=` | `x = x // valor` | `x //= 3` |
| `%=` | `x = x % valor` | `x %= 3` |
| `**=` | `x = x ** valor` | `x **= 3` |

```python
num = 10
num += 5   # num ara és 15
num *= 2   # num ara és 30
```

### 5. Operadors d'Identitat

S'utilitzen per comparar si dos objectes són el mateix objecte en memòria.

| Operador | Descripció |
|----------|------------|
| `is` | Retorna True si ambdós són el mateix objecte |
| `is not` | Retorna True si no són el mateix objecte |

```python
llista1 = [1, 2, 3]
llista2 = [1, 2, 3]
llista3 = llista1

print(llista1 is llista2)   # False (diferents objectes)
print(llista1 is llista3)   # True (mateixa referència)
print(llista1 == llista2)   # True (mateix contingut)
```

### 6. Operadors de Pertinença

S'utilitzen per comprovar si un valor existeix dins d'una seqüència.

| Operador | Descripció |
|----------|------------|
| `in` | Retorna True si el valor existeix a la seqüència |
| `not in` | Retorna True si el valor no existeix a la seqüència |

```python
fruites = ["poma", "plàtan", "taronja"]
print("poma" in fruites)      # True
print("cirera" not in fruites) # True
```

### 7. Precedència d'Operadors

La precedència determina l'ordre en què s'avaluen les operacions:

1. `()` Parèntesis
2. `**` Exponenciació
3. `*`, `/`, `//`, `%` Multiplicació, divisió
4. `+`, `-` Suma, resta
5. Operadors de comparació
6. Operadors lògics

```python
resultat1 = 10 + 5 * 2      # = 20 (multiplicació primer)
resultat2 = (10 + 5) * 2    # = 30 (parèntesis primer)
```

## Com Executar

1. Obre una terminal
2. Navega fins al directori d'aquest exemple
3. Executa el fitxer amb Python:

```bash
python operadors.py
```

## Sortida Esperada

```
=== Operadors Aritmètics ===
a = 15, b = 4
Suma (a + b): 19
Resta (a - b): 11
Multiplicació (a * b): 60
Divisió (a / b): 3.75
Divisió entera (a // b): 3
Mòdul/Residu (a % b): 3
Exponenciació (a ** b): 50625

=== Operadors de Comparació ===
x = 10, y = 20
Igual (x == y): False
No igual (x != y): True
Més gran que (x > y): False
Més petit que (x < y): True
Més gran o igual (x >= y): False
Més petit o igual (x <= y): True

=== Operadors Lògics ===
veritat = True, fals = False
AND (veritat and fals): False
OR (veritat or fals): True
NOT (not veritat): False
NOT (not fals): True

Edat: 25, Té carnet: True
Pot conduir (edat >= 18 and te_carnet): True

=== Operadors d'Assignació ===
Valor inicial: num = 10
Després de num += 5: 15
Després de num -= 3: 12
Després de num *= 2: 24
Després de num /= 4: 6.0
Després de num //= 2: 3.0

valor = 17, després de valor %= 5: 2
base = 2, després de base **= 3: 8

=== Operadors d'Identitat ===
llista1 = [1, 2, 3]
llista2 = [1, 2, 3]
llista3 = llista1 (mateixa referència)
llista1 is llista2: False
llista1 is llista3: True
llista1 == llista2: True
llista1 is not llista2: True

=== Operadors de Pertinença ===
fruites = ['poma', 'plàtan', 'taronja']
'poma' in fruites: True
'cirera' in fruites: False
'cirera' not in fruites: True

text = 'Hola món'
'món' in text: True
'adéu' in text: False

=== Precedència d'Operadors ===
10 + 5 * 2 = 20
(10 + 5) * 2 = 30
2 + 3 * 4 ** 2 / 8 - 1 = 7.0
```

## Consells Importants

- Utilitza **parèntesis** per fer el codi més llegible i evitar errors de precedència.
- Els operadors `is` i `==` són diferents: `is` compara identitat (si són el mateix objecte), `==` compara igualtat (si tenen el mateix valor).
- Els operadors d'assignació combinats (`+=`, `-=`, etc.) fan el codi més concís.
