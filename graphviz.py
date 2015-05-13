import pygraphviz as pgv
import sys

name = 'MDDFT.dot'
if len(sys.argv) > 1:
    name = str(sys.argv[1]) 

D=pgv.AGraph(name)
D.layout('dot') # layout with dot
name = name[:-4]
D.draw(name+'.png') # draw png
print("Wrote "+name+".png")

