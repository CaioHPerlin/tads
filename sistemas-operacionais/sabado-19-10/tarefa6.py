import sys
import array

list_obj = [i for i in range(1000)]
array_obj = array.array('i', list_obj)

print(f"Uso de memória da lista: {sys.getsizeof(list_obj)} bytes")
print(f"Uso de memória do array: {sys.getsizeof(array_obj)} bytes")