from collections import defaultdict

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
  
  result = defaultdict(int)
  
  for line in data:
    result[line['base']] += 1
    
  result = sorted(result.items(), key=lambda x: x[1], reverse=True)
  print(result)