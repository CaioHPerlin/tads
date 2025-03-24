def criarFila():
    fila = []
    return fila

def vazia(fila):
    return len(fila) == 0

def verificarPrimeiro(fila):
    if (vazia(fila)):
        return "fila vazia!"
    return fila[0]

def enfileirar(fila, item):
    fila.append(item)
    print(item, "enfileirado")

def desenfileirar(fila):
    if (vazia(fila)):
        print("fila vazia!")
    print(fila.pop(0), "desenfileirado")

    