import sys

integer_obj = 123456
string_obj = "Hello, world!"
list_obj = [i for i in range(1000)]
dict_obj = {i: i+1 for i in range(1000)}

print(f"Uso de memória do inteiro: {sys.getsizeof(integer_obj)} bytes")
print(f"Uso de memória da string: {sys.getsizeof(string_obj)} bytes")
print(f"Uso de memória da lista: {sys.getsizeof(list_obj)} bytes")
print(f"Uso de memória do dicionário: {sys.getsizeof(dict_obj)} bytes")
