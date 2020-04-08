S = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

S = S.strip(',')
S = S.strip('.')
words = S.split(' ')
words_len = [len(word) for word in words]
print(words_len)