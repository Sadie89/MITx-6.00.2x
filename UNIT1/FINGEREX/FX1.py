# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 14:34:14 2020

@author: ghaff
"""

# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if int(i//2**j) % 2 == 1:
                combo.append(items[j])
        yield combo      
   
def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    N = len(items)
    for i in range(3**N):
        combo1 = []
        combo2 = []
        for j in range(N):
            print("i=", i, "j=", j, "int(i//3**j) % 3=", int(i//3**j) % 3)
            if int(i//3**j) % 3 == 1:
                combo1.append(items[j])
            elif int(i//3**j) % 3 == 2:
                combo2.append(items[j])
        yield combo1, combo2
        
items = [1,2,3]

# powerSet_Gen = yieldAllCombos(items) 

# z = 0
# for i in powerSet_Gen:
#     z += 1
#     print (i)
    
# print(z)

powerSet_Gen = powerSet(items)
z = 0
for i in powerSet_Gen:
    z += 1
    print(i)
print(z)


