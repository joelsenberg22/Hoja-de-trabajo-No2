# Nodo del árbol
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

# Prioridad de operadores
def prioridad(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

# Infija → Postfija
def infija_a_postfija(exp):
    pila = []
    salida = []
    numero = ""

    for c in exp:
        if c.isdigit():
            numero += c
        else:
            if numero:
                salida.append(numero)
                numero = ""
            if c in "+-*/":
                while pila and prioridad(pila[-1]) >= prioridad(c):
                    salida.append(pila.pop())
                pila.append(c)
            elif c == '(':
                pila.append(c)
            elif c == ')':
                while pila and pila[-1] != '(':
                    salida.append(pila.pop())
                pila.pop()

    if numero:
        salida.append(numero)

    while pila:
        salida.append(pila.pop())

    return salida

# Construir árbol
def construir_arbol(postfija):
    pila = []

    for token in postfija:
        if token not in "+-*/":
            pila.append(Nodo(token))
        else:
            nodo = Nodo(token)
            nodo.der = pila.pop()
            nodo.izq = pila.pop()
            pila.append(nodo)

    return pila[0]

# Imprimir árbol de forma gráfica en consola
def imprimir_arbol(nodo, nivel=0, prefijo="Root: "):
    if nodo is not None:
        print(" " * (nivel * 4) + prefijo + nodo.valor)
        if nodo.izq or nodo.der:
            imprimir_arbol(nodo.izq, nivel + 1, "L--- ")
            imprimir_arbol(nodo.der, nivel + 1, "R--- ")

# ------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------

expresion = input("Ingresa la expresión aritmética: ")

postfija = infija_a_postfija(expresion)
arbol = construir_arbol(postfija)

print("\nÁRBOL DE EXPRESIÓN:\n")
imprimir_arbol(arbol)