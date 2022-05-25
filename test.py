import graphviz
import os
os.environ["PATH"] += os.pathsep + 'C:\Users\HP\AppData\Local\Programs\Python\Python310\Lib\site-packages\graphviz'

if os.path.exists('projectparseTree.gv.pdf'): #C:\\Users\\Seif Eldin Sameh\\PycharmProjects\\pythonProject5\\
    os.remove('projectparseTree.gv.pdf') #C:\\Users\\Seif Eldin Sameh\\PycharmProjects\\pythonProject5\\
    os.remove('projectparseTree.gv') #C:\\Users\\Seif Eldin Sameh\\PycharmProjects\\pythonProject5\\

dot = graphviz.Digraph('The Round Table',filename= 'projectparseTree.gv')
dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')

dot.edge('B', 'L', label='my_label')
dot.view()