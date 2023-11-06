#d=dict.fromkeys(['name','age','sex','height','weight','foot size'])
d={'name':'Ivan','age':42,'sex':'male','height':182,'weight':70,'foot size':42}
print(d['name'],d['age'],d['sex'],d['height'],d['weight'],d['foot size'])
d.update({'foot size':47})
d.pop('age')
print(d)