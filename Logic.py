# Shortcuts, any AND expression with a false is False
# any OR expression with a true is true

# Not
not False 	True
not True 	False

#Or
True or False 	True
True or True 	True
False or True 	True
False or False 	False

#And
AND 	True?
True and False 	False
True and True 	True
False and True 	False
False and False 	False

#NOT OR
not (True or False) 	False
not (True or True) 	False
not (False or True) 	False
not (False or False) 	True
NOT AND 	True?
not (True and False) 	True
not (True and True) 	False
not (False and True) 	True
not (False and False) 	True

#others
!= 	True?
1 != 0 	True
1 != 1 	False
0 != 1 	True
0 != 0 	False
== 	True?
1 == 0 	False
1 == 1 	True
0 == 1 	False
0 == 0 	True
