num = [1,2,3,3,2,1]

numcopy = num.copy()
numcopy.reverse()

if numcopy == num.copy():
    print("palindrome")
else:
    print("not palindrome")    



listt=['a','b','c','d']
copylistt=listt.copy()  # copylistt is variable name and listt.copy() is a copy method which returns a copy of listt
copylistt.reverse()
if copylistt==listt.copy():
    print("palinde")  
else:
    print("not palinde")