import random

S = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

words = S.split(' ')
result = []
for word in words:
  if len(word) > 4:
    word = word[0] + ''.join(random.sample(word[1:-1], len(word) - 2)) + word[-1]
    
  result.append(word)
  
print(' '.join(result))