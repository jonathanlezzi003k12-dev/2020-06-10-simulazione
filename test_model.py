from model.model import Model as md
costruttore=md()
costruttore.getAttori()
#print(costruttore.getNodi())
#la crazione del grafo funziona bene
print(costruttore.returnArchi())
costruttore.loadgraph()
#print(costruttore.returnArchi())
print(costruttore.attoriGrafo())


