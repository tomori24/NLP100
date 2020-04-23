from collections import defaultdict
import matplotlib.pyplot as plt
import japanize_matplotlib

def parse(data):
  result = []

  for block in data:
    if block == '':
      continue
    lines = []
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
      
      lines.append(line_dict)
    result.append(lines)
  return result

def extract(block):
  return [b['base'] for b in block]

if __name__ == "__main__":
  filepath = 'data/neko.txt.mecab'

  with open(filepath, mode='rt') as f:
    data = f.read().split('EOS\n')
    
  data = parse(data)
  words = [extract(b) for b in data]
  words = list(filter(lambda x: '猫' in x, words))
  
  result = defaultdict(int)
  for word in words:
    for w in word:
      if w != '猫':
        result[w] += 1
    
  result = sorted(result.items(), key=lambda x: x[1], reverse=True)
  
  x, y = [], []
  for key, value in result[:10]:
    x.append(key)
    y.append(value)

  # print(result[:10].value)
  plt.bar(x=x, height=y)
  plt.show()