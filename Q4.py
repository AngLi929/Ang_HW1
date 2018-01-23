yours=["Yale","MIT","Berkeley"]
mine=["Columbia","NYU","Harvard"]
ours1=mine+yours
ours2=[]
ours2.append(mine)
ours2.append(yours)
print(ours1)
print(ours2)
#Difference:
#ours1 is a list containing 6 elements and each element is a school name.
#ours2 is a list containing 2 elements and each element is a list having three school names

yours[1]="BU"
print(ours1)
print(ours2)
#Since "+" operator just concatenates all elements in two lists but "append" appends the object(here is a list) on the right-hand side instead of taking its elements.
#The + operation adds the  elements to the original list. The "append" operation inserts the list (or any object) into the end of the original list, which results in a reference to self in that spot (hence the infinite recursion).
#The append-method however does literally what you ask: append the object on the right-hand side that you give it (the list or any other object), instead of taking its elements.

