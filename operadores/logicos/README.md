# Operadores Lógicos em Python

Os operadores lógicos são usados para combinar expressões booleanas, retornando `True` ou `False` com base nas condições avaliadas.

## Principais Operadores:

| Operador  | Descrição                                  | Exemplo        |
|-----------|------------------------------------------|----------------|
| `and`     | Retorna `True` se ambas as condições forem verdadeiras | `True and False → False` |
| `or`      | Retorna `True` se pelo menos uma das condições for verdadeira | `True or False → True` |
| `not`     | Inverte o valor booleano da expressão | `not True → False` |

### Exemplo de uso:
```python
a = True
b = False

resultado_and = a and b  # False
resultado_or = a or b    # True
resultado_not = not a    # False

print(resultado_and, resultado_or, resultado_not)
