def n_gram(s, n=1):
  return [s[i:i+n] for i in range(len(s) - n + 1)]

S1 = "paraparaparadise"
S2 = "paragraph"

x = set(n_gram(S1, n=2))
y = set(n_gram(S2, n=2))

print(x | y)
print(x & y)
print(x - y)

print('se' in x)
print('se' in y)
