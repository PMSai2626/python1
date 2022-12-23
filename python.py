            python  coding Interview series - 1

#1. access the both key and values uing item() from dict

details = {"name":"Sai kumar", "age":24, "qualification": "Graduation"}
for i,j in details.items():
    print(i,j)

#output
#name sai kumar
#age 24
#qualification Graduation

#2. python program using to calculate the length
#method-1
name = "sai kumar"
length_of_name = len(name)
print(length_of_name)

#output
#9

#methos-2
name = "sai kumar"
count = 0
for i in name:
    count += 1
print(count)
    
#output
#9


#3. python fun that accepts a string and calculate the number of upper and lower latters

def string(s):
    d = {"Upper case":0, "Lower case":0}
    for i in s:
        if i.isupper():
            d["Upper case"]+=1
        
        elif i.islower():
            d["Lower case"]+=1
        
        else:
            pass
    print("Upper case Letters",d["Upper case"])
    print("Lower case Letters",d["Lower case"])
name = string("My Name is sai Kumar i learning dull Stack Developement")
print(name)

#output
#Upper case Letters 5
#Lower case Letters 41 


#4. check if the first and last number of a list is the same

number = [55,23,95,84,55]
first = number[0]
Last= number[-1]
if first == Last:
    print(True)
else:
    print(False)
 
 #output
 #True  
 
 
 
 #5. python program to check if a key is already present in dictionary
 
my_dict = {1: "A", 2:"B", 3:"C"}
if 2 in my_dict:
     print("the key is present")
else:
    print("the key is not present")
 
 #output
 #the key is present
 