def cipher(s):
  for c in s:
    if c.islower():
      c = chr(219 - ord(c))  
    print(c, end='')
    
cipher('I have a pen.')