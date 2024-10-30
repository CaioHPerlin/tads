# 1 - Crie um código que:
#     • Crie variáveis diferentes apontando para o mesmo objeto.
#     • Exiba o id() do objeto em diferentes momentos, para observar se ele é o mesmo.
#     • Remova referências e observe se o Garbage Collector libera a memória.
import gc
gc.set_debug(gc.DEBUG_STATS)

objeto = []
print('obj', id(objeto))
a = objeto
print('a', id(a))
b = objeto
print('b', id(b))
c = objeto
print('c', id(c))
