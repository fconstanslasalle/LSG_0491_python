# Condicionals If-Else en Python 🔀

## Descripció

Aquest exemple demostra com utilitzar les **estructures condicionals** en Python. Les condicionals permeten executar blocs de codi diferents segons si es compleixen certes condicions.

## Contingut de l'Exemple

El fitxer `condicionals.py` inclou els següents conceptes:

### 1. Estructura if simple

S'executa un bloc de codi només si la condició és certa.

```python
edat = 20
if edat >= 18:
    print("Ets major d'edat.")
```

### 2. Estructura if-else

S'executa un bloc o l'altre segons si la condició és certa o falsa.

```python
nota = 4.5
if nota >= 5:
    print("Has aprovat!")
else:
    print("Has suspès.")
```

### 3. Estructura if-elif-else

Permet avaluar múltiples condicions.

```python
puntuacio = 85
if puntuacio >= 90:
    qualificacio = "Excel·lent"
elif puntuacio >= 80:
    qualificacio = "Notable"
elif puntuacio >= 70:
    qualificacio = "Bé"
else:
    qualificacio = "Insuficient"
```

### 4. Condicionals amb Operadors Lògics

| Operador | Descripció | Exemple |
|----------|------------|---------|
| `and` | Cert si ambdues condicions són certes | `a and b` |
| `or` | Cert si almenys una condició és certa | `a or b` |
| `not` | Inverteix el valor booleà | `not a` |

```python
if te_carnet and anys_experiencia >= 1:
    print("Pots conduir sol.")
```

### 5. Condicionals Niuats

Condicionals dins d'altres condicionals per crear lògica més complexa.

```python
if usuari_valid:
    if contrasenya_correcta:
        print("Benvingut!")
```

### 6. Operador Ternari

Permet escriure condicionals simples en una sola línia.

```python
estat = "Fa calor" if temperatura > 20 else "Fa fred"
```

### 7. Comprovació de Valors Buits

Python considera alguns valors com "falsos":
- `""` (cadena buida)
- `[]` (llista buida)
- `None`
- `0`
- `False`

```python
if nom:
    print(f"El nom és: {nom}")
else:
    print("El nom està buit.")
```

## Com Executar

1. Obre una terminal
2. Navega fins al directori d'aquest exemple
3. Executa el fitxer amb Python:

```bash
python condicionals.py
```

## Sortida Esperada

```
=== Estructura if simple ===
Amb 20 anys, ets major d'edat.

=== Estructura if-else ===
Has suspès amb un 4.5. Has d'estudiar més.

=== Estructura if-elif-else ===
Amb una puntuació de 85, la qualificació és: Notable

=== Condicionals amb operadors lògics ===
Pots conduir sol.
Avui és dia de descans!
Podem sortir a passejar!

=== Condicionals niuats ===
Benvingut, usuari!

=== Operador ternari ===
Amb 25°C: Fa calor
Amb 17 anys, l'entrada és de tipus: juvenil

=== Comprovació de valors buits ===
El nom està buit.
La llista està buida.
El valor és None.

=== Comparació de cadenes ===
Has respost afirmativament.

=== Calculadora de descomptes ===
Preu original: 100€
Quantitat: 5
Descompte aplicat: 20.0%
Preu final: 400.0€
```

## Bones Pràctiques

- Utilitza `elif` en lloc de múltiples `if` quan les condicions són mútuament excloents.
- Evita condicionals massa niuats per millorar la llegibilitat.
- L'operador ternari és útil per a condicions simples, però no abuseu-ne per a lògica complexa.
