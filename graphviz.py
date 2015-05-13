import pygraphviz as pgv
import sys

name = 'MDDFT'
if len(sys.argv) > 1:
    name = str(sys.argv[1]) 

D=pgv.AGraph(name+'.dot')
D.layout('dot') # layout with dot 
D.draw(name+'.png') # draw png
print("Wrote "+name+".png")

