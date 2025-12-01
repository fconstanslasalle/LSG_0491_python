# Bucle While en Python 🔁

## Descripció

Aquest exemple demostra com utilitzar el **bucle while** en Python. El bucle while repeteix un bloc de codi mentre una condició sigui certa.

## Contingut de l'Exemple

El fitxer `bucle_while.py` inclou els següents conceptes:

### 1. Bucle while Bàsic

Repeteix mentre la condició sigui certa.

```python
comptador = 1
while comptador <= 5:
    print(comptador)
    comptador += 1
```

⚠️ **Important**: Assegura't d'actualitzar la variable de control per evitar bucles infinits!

### 2. Bucle while amb break

`break` permet sortir del bucle abans que la condició sigui falsa.

```python
while True:  # Bucle infinit
    entrada = input("Escriu 'sortir' per acabar: ")
    if entrada == "sortir":
        break
```

### 3. Bucle while amb continue

`continue` salta a la següent iteració sense executar la resta del bloc.

```python
i = 0
while i < 10:
    i += 1
    if i % 2 != 0:
        continue
    print(i)  # Només mostra parells
```

### 4. Bucle while amb else

El bloc `else` s'executa quan la condició esdevé falsa (no si fem `break`).

```python
n = 1
while n <= 3:
    print(n)
    n += 1
else:
    print("Bucle acabat normalment")
```

### 5. Bucle while amb Múltiples Condicions

Es poden combinar condicions amb `and`, `or`.

```python
vides = 3
nivell = 1
while vides > 0 and nivell <= 10:
    # codi del joc
    nivell += 1
```

### 6. Patró: Menú Interactiu

```python
while True:
    print("1. Opció A")
    print("2. Opció B")
    print("3. Sortir")
    opcio = input("Tria: ")
    
    if opcio == "1":
        print("Has triat A")
    elif opcio == "2":
        print("Has triat B")
    elif opcio == "3":
        break
```

### 7. Algorismes Clàssics

#### MCD (Algorisme d'Euclides)

```python
def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

#### Fibonacci

```python
a, b = 0, 1
while a < 100:
    print(a)
    a, b = b, a + b
```

## Com Executar

1. Obre una terminal
2. Navega fins al directori d'aquest exemple
3. Executa el fitxer amb Python:

```bash
python bucle_while.py
```

## Sortida Esperada

```
=== Bucle while bàsic ===
Comptador: 1
Comptador: 2
Comptador: 3
Comptador: 4
Comptador: 5
Fi del bucle. Comptador final: 6

=== Bucle while amb condició booleana ===
Intent 1
Intent 2
Intent 3
Bucle finalitzat després de 3 intents
...
```

## Comparació: while vs for

| Aspecte | while | for |
|---------|-------|-----|
| Quan usar | Condició desconeguda | Iteració sobre seqüència |
| Exemple | Esperar entrada | Recórrer llista |
| Risc bucle infinit | Alt | Baix |
| Variable control | Manual | Automàtic |

## ⚠️ Evitar Bucles Infinits

Un bucle infinit es produeix quan la condició mai és falsa:

```python
# ❌ MAL - Bucle infinit!
i = 0
while i < 5:
    print(i)
    # Falta: i += 1

# ✓ BÉ
i = 0
while i < 5:
    print(i)
    i += 1
```

## Patrons Comuns

### Validació d'Entrada

```python
while True:
    entrada = input("Número positiu: ")
    if entrada.isdigit() and int(entrada) > 0:
        break
    print("Entrada no vàlida")
```

### Cerca amb Sentinella

```python
llista = [4, 7, 2, 9, 1]
objectiu = 9
i = 0
trobat = False

while i < len(llista) and not trobat:
    if llista[i] == objectiu:
        trobat = True
    else:
        i += 1
```

### Compte Enrere

```python
segons = 10
while segons > 0:
    print(segons)
    segons -= 1
print("🚀 Enlairament!")
```

## Bones Pràctiques

- Assegura't que la condició eventualment serà falsa.
- Utilitza `break` amb moderació.
- Considera usar `for` si coneixes el nombre d'iteracions.
- Inicialitza les variables de control abans del bucle.
- Documenta bucles complexos amb comentaris.
