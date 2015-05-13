import pygraphviz as pgv

D=pgv.AGraph('MDDFT.dot')
D.layout('dot') # layout with dot 
D.draw('MDDFT.png') # draw png
print("Wrote MDDFT.png")

