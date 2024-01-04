from logic import TruthTable
#part of the function that is built to run
myTable = TruthTable(['a', 'b'], ['a and -b'])
myTable2 = TruthTable(['a', 'b', 'c'], ['(a and b)','-c','(a and b) or -c'])
#result that prints out in the end
myTable.display();
myTable2.display();