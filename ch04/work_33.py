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
  result = []
  for i in range(1, len(data) - 1):
    if data[i-1]['pos'] == '名詞' and data[i+1]['pos'] == '名詞' and data[i]['base'] == 'の':
      result.append(data[i-1]['surface'] + data[i]['surface'] + data[i+1]['surface'])
  
  print(*result[:10], sep='\n')
