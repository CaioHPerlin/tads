words = input().split()

biggest = words[0]
for word in words:
    if len(word) > len(biggest):
        biggest = word

print(biggest)