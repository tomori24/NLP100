from collections import defaultdict
import matplotlib.pyplot as plt
import japanize_matplotlib

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

  result = defaultdict(int)
  
  for line in data:
    result[line['base']] += 1

  plt.hist(result.values(), bins=100)
  plt.show()
