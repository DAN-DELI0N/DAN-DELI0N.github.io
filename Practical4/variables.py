>>> a=40
>>> b=36
>>> c=30
>>> d=a-b
>>> e=b-c

>>> if d>e :
...     print("first training regime is better")
    elif d==e :
        print("They have a same effect ")
... else :
...     print("second training regime is better")
... 
...     
second training regime is better

>>> X=True
>>> Y=False
>>> if X or Y is True and X and Y is False :
...     print("W=True")
... else :
...     print("W=False")
...
...
W=True   # X      Y        W
          True    True     False
          True    False    True
          False   True     True
          False   False    False
          
