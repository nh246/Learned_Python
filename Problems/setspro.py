#display unique numbers


s = set()
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  

print(s)

# length of s after these operations?
s = set()
s.add(20)
s.add(20.0)
s.add('20') 
# The leanth will be 2 beacuse python dosen't considers int and float as diferent it sees as same 
print(len(s))