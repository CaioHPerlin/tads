

integer = 1
string = 'hey'
c = [1, 2, 3, 4, 5]

print(id(integer))
print(id(string))
print(id(c))

# =======================================

d = c
print(f'C e D compartilham o mesmo endereço de memória? {id(c) == id(d)}')
print(f'C = {id(c)}')
print(f'D = {id(d)}')

# =======================================
import gc

gc.set_debug(gc.DEBUG_LEAK)

class ex:
    pass

object_list = []

for _ in range(9999):
    example_obj = ex()
    object_list.append(example_obj)

print('Objetos criados')
del object_list

print('Objetos deletados, coletando lixo')
gc.collect()

gc.set_debug(gc.DEBUG_COLLECTABLE)

class block:
    def __init__(self, next):
        self.next: next

b1 = block()