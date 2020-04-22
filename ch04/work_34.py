def parse(data):
  result = []

  for block in data:
    if block == '':
      continue
    for line in block.split('\n'):
      if line == '':
        continue
      (surface, attr) = line.split('\t')
      attr = attr.split(',')
      line_dict = {
        'surface': surface,
        'base': attr[6],
        'pos': attr[0],
        'pos1': attr[1]
      }
      
      result.append(line_dict)
  return result


if __name__ == "__main__":
  filepath = 'data/neko.txt.mecab'

  with open(filepath, mode='rt') as f:
    data = f.read().split('EOS\n')
    
  data = parse(data)
  
  temp = []
  result = []
  
  for i in range(len(data)):
    if data[i]['pos'] == '名詞':
      temp.append(data[i]['surface'])
    elif len(temp) > 1:
      result.append(''.join(temp))
      temp = []
    else:
      temp = []
      
  print(*result[:10], sep='\n')
