def n_gram(s, n=1):
  return [s[i:i+n] for i in range(len(s) - n + 1)]

S = 'I am an NLPer'
words = S.split(' ')
print(n_gram(S, n=2))

print(n_gram(words, n=2))