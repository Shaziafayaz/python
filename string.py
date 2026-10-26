
string1 ="shazia"
stirng2 ="Fayaz"
print(string1 +" "+stirng2)



print(len(string1))
len2 = len(stirng2)
print(len2)
print(len(string1) + len(stirng2))


#indexing
str1 = "lets learn python"
print(str1[6])

ch = str1[0]
print(ch)
print(str1[4:17])
print(str1[1:len(str1)]) # prints from index 1 to end of string

  #negative indexing
print(str1[-10:-1])


#string functions
str2 = "i am studying python"
print(str2.endswith("hon"))
print(str2.capitalize())
print(str2) # prints old string 
#str2 = print(str2.capitalize()) # prints new string
print(str2.replace('y','r')) 
print(str2.find("python"))
print(str2.count('i'))