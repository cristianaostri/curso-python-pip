import matplotlib.pyplot as pylot

def generate_bar_chart(name, labels, values):
  fig, ax = pylot.subplots()
  ax.bar(labels, values)
  pylot.savefig(f'./imgs/{name}.png')
  pylot.close

def generate_pie_chart(labels, values):
  fig, ax = pylot.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  pylot.savefig('pie.png')
  pylot.close

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  # generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)