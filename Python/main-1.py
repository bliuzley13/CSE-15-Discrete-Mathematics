from logic import TruthTable
#input part with the function
myTable = TruthTable(['p', 'q'], ['p or q'])
myTable2 = TruthTable(['p', 'q'], ['p or q', 'p and q'])
#prints out the tables in latex form
myTable.latex()
myTable2.latex()
#prints out the tables
myTable.display()
myTable2.display()