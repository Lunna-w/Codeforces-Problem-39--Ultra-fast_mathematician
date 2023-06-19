n = input()
m = input()

final = ""

for i in range(len(n)):  
    if n[i] != m[i]:
        final += '1'
    else:
        final += '0'

print(final)