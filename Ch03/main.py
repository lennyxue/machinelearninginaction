import trees as t

data_set, labels = t.createDataSet()
data_set[0][-1] = 'test'
# entropy more bigger, mix of classes more higher
print(t.calcShannonEnt(data_set))
print(t.calcShannonEnt([[1,0,'yes'], [1,1,'no']]))
