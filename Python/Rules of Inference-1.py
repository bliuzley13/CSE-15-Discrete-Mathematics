from logic import TruthTable

#Modus Ponens ((p → q) ∧ p) → q
myTable = TruthTable(['p', 'q'], ['(p -> q)','((p -> q) and p)','((p -> q) and p) -> q'])
myTable.display();

#Modus Tollens (¬q ∧(p →q)) →¬p
myTable2 = TruthTable(['p', 'q'], ['-q','(p -> q)','(-q and (p -> q))','-p','(-q and (p -> q)) -> -p'])
myTable2.display();

#Hypothetical Syllogism ((p → q) ∧ (q → r)) → (p → r)
myTable3 = TruthTable(['p', 'q', 'r'], ['(p -> q)','(q -> r)','((p -> q) and (q -> r))','(p -> r)','((p -> q) and (q -> r)) -> (p -> r)'])
myTable3.display();

#Disjunctive Syllogism ((p ∨ q) ∧ ¬p) →q
myTable4 = TruthTable(['p', 'q'], ['(p or q)','-p','((p or q) and -p)','((p or q) and -p) -> q'])
myTable4.display();

#Addition p -> (p ∨ q)
myTable5 = TruthTable(['p', 'q'], ['(p or q)','p -> (p or q)'])
myTable5.display();

#Simplification (p ∧ q) → p
myTable6 = TruthTable(['p', 'q'], ['(p and q)', '(p and q) -> p'])
myTable6.display();

#Conjuction ((p) ∧ (q)) → (p ∧ q)
myTable7 = TruthTable(['p', 'q'], ['(p) and (q)','((p) and (q))','(p and q)','((p) and (q)) -> (p and q)'])
myTable7.display();

#Resolution ((p ∨ q) ∧ (¬p ∨ r)) →(q ∨r)
myTable8 = TruthTable(['p', 'q', 'r'], ['(p or q)','(-p or r)','(p or q) and (-p or r)','(q or r)','((p or q) and (-p or r)) -> (q or r)'])
myTable8.display();