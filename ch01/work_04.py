S = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can"

words = S.split(' ')
result = {}

for i, word in enumerate(words):
  
  if i in [0, 4, 5, 6, 7, 8, 14, 15, 18]:
    result[i] = word[0]
  else:
    result[i] = word[0:2]
    
print(result)