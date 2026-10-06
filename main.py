from pyscript import document, display

A = {'burger', 'fries'}
B = {'burger', 'fries', 'coke', 'pie'}

#Using set operators
display((A<= B), target="output1")  #subset
display ((A < B), target="output1") #proper subset
display((B >= A), target="output1") #superset
display ((B > A), target="output1") #proper superset

#using set methods
display(A.issubset(B), target="output1") #subset
display(A.issuperset(B), target="output1") #superset